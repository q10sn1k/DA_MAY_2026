from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

DUPLICATES = 500


def generate_events(rows: int, seed: int) -> pd.DataFrame:
    if rows <= DUPLICATES + 1000:
        raise ValueError("rows must be greater than 1500")
    rng = np.random.default_rng(seed)
    n_base = rows - DUPLICATES
    days = pd.date_range("2026-07-01", periods=30, freq="D")
    weights = np.ones(30, dtype=float)
    weights[days.dayofweek >= 5] *= 0.82
    weights[13] *= 1.85
    weights /= weights.sum()
    day_idx = rng.choice(np.arange(30), size=n_base, p=weights)
    seconds = rng.integers(0, 86400, size=n_base)
    times = np.datetime64("2026-07-01T00:00:00") + day_idx.astype("timedelta64[D]") + seconds.astype("timedelta64[s]")
    times = pd.to_datetime(times)

    event_types = np.array(["view", "add_to_cart", "purchase", "cancel", "support_request", "login"])
    event_type = rng.choice(event_types, size=n_base, p=[0.45, 0.18, 0.12, 0.04, 0.08, 0.13])
    regions = np.array(["Москва", "Санкт-Петербург", "Екатеринбург", "Казань", "Новосибирск", "Самара", "Ростов-на-Дону", "Нижний Новгород"], dtype=object)
    region = rng.choice(regions, size=n_base, p=[0.32, 0.15, 0.11, 0.10, 0.09, 0.08, 0.08, 0.07]).astype(object)
    device = rng.choice(np.array(["mobile", "desktop", "tablet"]), size=n_base, p=[0.60, 0.34, 0.06])
    product_num = rng.integers(1, 501, size=n_base)
    category = np.select(
        [product_num <= 120, product_num <= 230, product_num <= 340, product_num <= 430],
        ["Электроника", "Аксессуары", "Дом и офис", "Спорт"],
        default="Красота и здоровье",
    ).astype(object)
    prices = {"Электроника": 18000.0, "Аксессуары": 2500.0, "Дом и офис": 6500.0, "Спорт": 5000.0, "Красота и здоровье": 1800.0}
    base_price = np.array([prices[c] for c in category], dtype=float)
    price = np.round(base_price * rng.lognormal(0.0, 0.35, n_base), 2)
    quantity = np.where(np.isin(event_type, ["add_to_cart", "purchase"]), rng.integers(1, 5, n_base), 0)
    response_ms = rng.lognormal(np.log(220), 0.45, n_base)
    response_ms *= np.where(event_type == "support_request", 1.45, 1.0)
    response_ms *= np.where(device == "mobile", 1.10, 1.0)
    response_ms *= np.where(day_idx == 13, 1.65, 1.0)
    response_ms = np.maximum(20, np.round(response_ms)).astype(int)

    df = pd.DataFrame({
        "event_id": np.char.add("EV-", np.char.zfill(np.arange(1, n_base + 1).astype(str), 9)).astype(object),
        "event_time": times,
        "event_date": times.date,
        "user_id": np.char.add("U-", np.char.zfill(rng.integers(1, 40001, n_base).astype(str), 6)),
        "session_id": np.char.add("S-", np.char.zfill(rng.integers(1, 90001, n_base).astype(str), 7)),
        "event_type": event_type,
        "product_id": np.char.add("P-", np.char.zfill(product_num.astype(str), 4)),
        "category": category,
        "region": region,
        "device": device,
        "quantity": quantity.astype(int),
        "price": price,
        "response_ms": response_ms,
    })

    issue = rng.permutation(n_base)[:600]
    df.loc[issue[:100], "event_id"] = None
    df.loc[issue[100:300], "region"] = None
    df.loc[issue[300:400], "price"] = -np.abs(df.loc[issue[300:400], "price"])
    df.loc[issue[400:500], "quantity"] = -1
    df.loc[issue[500:600], "response_ms"] = -np.abs(df.loc[issue[500:600], "response_ms"])

    excluded = set(issue.tolist())
    candidates = np.array([i for i in range(n_base) if i not in excluded], dtype=int)
    dup_idx = rng.choice(candidates, size=DUPLICATES, replace=False)
    dup = df.iloc[dup_idx].copy()
    dup["event_time"] = pd.to_datetime(dup["event_time"]) + pd.to_timedelta(1, unit="s")
    dup["event_date"] = pd.to_datetime(dup["event_time"]).dt.date
    return pd.concat([df, dup], ignore_index=True).sample(frac=1.0, random_state=seed).reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate synthetic event data for the Big Data webinar")
    parser.add_argument("--rows", type=int, default=250000)
    parser.add_argument("--output", type=Path, default=Path("data/raw/events_lite.csv"))
    parser.add_argument("--seed", type=int, default=20260803)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df = generate_events(args.rows, args.seed)
    df.to_csv(args.output, index=False, encoding="utf-8", date_format="%Y-%m-%d %H:%M:%S")
    print(f"Created {args.output}: {len(df):,} rows, {args.output.stat().st_size / 1024**2:.2f} MB")


if __name__ == "__main__":
    main()
