from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

import pandas as pd

EXPECTED = {
    "period_days": 546,
    "regions": 8,
    "teams": 32,
    "tickets_raw_rows": 24240,
    "ticket_unique_ids": 24000,
    "tickets_clean_rows": 23922,
    "tickets_with_target": 23000,
    "events_raw_rows": 145600,
    "events_clean_rows": 144800,
    "capacity_raw_rows": 17392,
    "capacity_duplicate_pairs": 40,
    "capacity_missing_pairs": 120,
    "capacity_negative_backlog": 16,
    "capacity_active_above_planned": 24,
    "june_ticket_rows": 1900,
    "june_breaches": 613,
}

JUNE_COUNTS = {
    "R01": (380, 116),
    "R02": (305, 92),
    "R03": (223, 83),
    "R04": (219, 80),
    "R05": (207, 65),
    "R06": (198, 63),
    "R07": (190, 62),
    "R08": (178, 52),
}


def root_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def load_files(root: Path) -> dict[str, pd.DataFrame]:
    raw = root / "data" / "raw"
    required = [
        raw / "tickets.csv",
        raw / "ticket_events.csv",
        raw / "team_capacity_daily.csv",
        raw / "calendar_events.csv",
        raw / "load_log.csv",
        raw / "teams.xlsx",
        raw / "regions.json",
        root / "data" / "database" / "support_analytics.sqlite",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required files:\n" + "\n".join(missing))

    return {
        "tickets": pd.read_csv(raw / "tickets.csv", low_memory=False),
        "events": pd.read_csv(raw / "ticket_events.csv", low_memory=False),
        "capacity": pd.read_csv(raw / "team_capacity_daily.csv", low_memory=False),
        "calendar": pd.read_csv(raw / "calendar_events.csv"),
        "load_log": pd.read_csv(raw / "load_log.csv", low_memory=False),
        "teams": pd.read_excel(raw / "teams.xlsx"),
        "regions": pd.read_json(raw / "regions.json"),
    }


def clean_tickets(tickets: pd.DataFrame, teams: pd.DataFrame) -> pd.DataFrame:
    clean = tickets.copy()
    clean["source_updated_at"] = pd.to_datetime(clean["source_updated_at"], errors="coerce")
    clean = clean.sort_values("source_updated_at").drop_duplicates("ticket_id", keep="last")
    clean["created_at_utc"] = pd.to_datetime(clean["created_at_utc"], errors="coerce")
    clean["closed_at_utc"] = pd.to_datetime(clean["closed_at_utc"], errors="coerce")
    clean = clean[clean["created_at_utc"].notna()].copy()
    clean = clean[(clean["closed_at_utc"].isna()) | (clean["closed_at_utc"] >= clean["created_at_utc"])].copy()
    clean = clean[clean["team_id"].isin(teams["team_id"])].copy()
    return clean


def validate_sqlite(root: Path) -> dict[str, int]:
    db_path = root / "data" / "database" / "support_analytics.sqlite"
    expected_tables = {
        "tickets",
        "ticket_events",
        "team_capacity_daily",
        "calendar_events",
        "load_log",
        "teams",
        "regions",
    }
    with sqlite3.connect(db_path) as conn:
        actual_tables = {
            row[0]
            for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        }
        missing = expected_tables - actual_tables
        if missing:
            raise RuntimeError(f"SQLite is missing tables: {sorted(missing)}")
        return {
            table: int(conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0])
            for table in sorted(expected_tables)
        }


def main() -> int:
    root = root_dir()
    frames = load_files(root)
    tickets = frames["tickets"]
    events = frames["events"]
    capacity = frames["capacity"]
    calendar = frames["calendar"]
    teams = frames["teams"]
    regions = frames["regions"]

    clean = clean_tickets(tickets, teams)
    clean_events = events.drop_duplicates("event_id", keep="first").copy()
    clean_events = clean_events[clean_events["ticket_id"].isin(clean["ticket_id"])].copy()
    created_lookup = clean.set_index("ticket_id")["created_at_utc"]
    clean_events["event_ts_utc"] = pd.to_datetime(clean_events["event_ts_utc"], errors="coerce")
    clean_events["created_at_utc"] = clean_events["ticket_id"].map(created_lookup)
    clean_events = clean_events[clean_events["event_ts_utc"] >= clean_events["created_at_utc"]]

    capacity["date"] = pd.to_datetime(capacity["date"], errors="coerce")
    capacity_dedup = capacity.drop_duplicates(["date", "team_id"], keep="first")
    full_pairs = pd.MultiIndex.from_product(
        [pd.date_range("2025-01-01", "2026-06-30", freq="D"), teams["team_id"]],
        names=["date", "team_id"],
    )
    actual_pairs = pd.MultiIndex.from_frame(capacity_dedup[["date", "team_id"]])

    june = clean[(clean["created_at_utc"] >= "2026-06-01") & (clean["created_at_utc"] < "2026-07-01")].copy()
    june["sla_breached"] = pd.to_numeric(june["sla_breached"], errors="coerce")
    team_region = teams.set_index("team_id")["region_id"]
    june["region_effective"] = june["region_id"].fillna(june["team_id"].map(team_region))
    june_summary = june.groupby("region_effective").agg(
        tickets=("ticket_id", "nunique"),
        breaches=("sla_breached", "sum"),
    ).sort_index()
    expected_june = pd.DataFrame.from_dict(JUNE_COUNTS, orient="index", columns=["tickets", "breaches"]).sort_index()

    actual = {
        "period_days": len(calendar),
        "regions": len(regions),
        "teams": len(teams),
        "tickets_raw_rows": len(tickets),
        "ticket_unique_ids": int(tickets["ticket_id"].nunique()),
        "tickets_clean_rows": len(clean),
        "tickets_with_target": int(pd.to_numeric(clean["sla_breached"], errors="coerce").notna().sum()),
        "events_raw_rows": len(events),
        "events_clean_rows": len(clean_events),
        "capacity_raw_rows": len(capacity),
        "capacity_duplicate_pairs": int(capacity.duplicated(["date", "team_id"]).sum()),
        "capacity_missing_pairs": int(len(full_pairs.difference(actual_pairs))),
        "capacity_negative_backlog": int((capacity["backlog_start"] < 0).sum()),
        "capacity_active_above_planned": int((capacity["active_agents"] > capacity["planned_agents"]).sum()),
        "june_ticket_rows": len(june),
        "june_breaches": int(june["sla_breached"].sum()),
    }

    mismatches = {
        key: {"expected": EXPECTED[key], "actual": value}
        for key, value in actual.items()
        if EXPECTED[key] != value
    }
    if not june_summary.astype(int).equals(expected_june.astype(int)):
        mismatches["june_control_slice"] = {
            "expected": expected_june.astype(int).to_dict(orient="index"),
            "actual": june_summary.astype(int).to_dict(orient="index"),
        }

    sqlite_counts = validate_sqlite(root)
    status = "PASS" if not mismatches else "FAIL"
    result = {
        "status": status,
        "checks": actual,
        "sqlite_counts": sqlite_counts,
        "mismatches": mismatches,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
