from pathlib import Path
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# This script regenerates the synthetic support_tickets.csv dataset.
# It uses only artificial training data and does not contain personal data.

OUTPUT = Path("data/raw/support_tickets.csv")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
start = datetime(2026, 1, 5)
num_days = 112
rows = []
channels = ["email", "chat", "phone", "web"]
priorities = ["low", "medium", "high", "critical"]
categories = ["billing", "technical", "access", "delivery", "product"]
segments = ["B2C", "SMB", "Enterprise"]
regions = ["Central", "North-West", "Volga", "Siberia", "South"]

sla_hours = {"low": 72, "medium": 48, "high": 24, "critical": 8}
channel_base = {"chat": 7.0, "email": 10.5, "phone": 8.8, "web": 9.6}
priority_multiplier = {"low": 0.75, "medium": 1.0, "high": 1.45, "critical": 2.05}
segment_effect = {"B2C": 0.8, "SMB": 1.0, "Enterprise": 1.18}

counter = 1
for d in range(num_days):
    date = start + timedelta(days=d)
    weekday = date.weekday()
    base_count = 5.2 + 0.035 * d + (2.2 if weekday == 0 else 0) + (1.2 if weekday in [1, 2] else 0) - (1.3 if weekday in [5, 6] else 0)
    daily_count = max(1, rng.poisson(max(base_count, 1.0)))
    for _ in range(daily_count):
        channel = rng.choice(channels, p=[0.34, 0.31, 0.17, 0.18])
        priority = rng.choice(priorities, p=[0.38, 0.42, 0.16, 0.04])
        category = rng.choice(categories, p=[0.25, 0.31, 0.15, 0.14, 0.15])
        segment = rng.choice(segments, p=[0.58, 0.30, 0.12])
        region = rng.choice(regions, p=[0.35, 0.18, 0.21, 0.15, 0.11])
        created = date + timedelta(hours=int(rng.integers(8, 22)), minutes=int(rng.integers(0, 60)))
        mean_hours = channel_base[channel] * priority_multiplier[priority] * segment_effect[segment]
        resolution = rng.gamma(shape=2.1, scale=mean_hours / 2.1)
        if rng.random() < 0.015:
            resolution *= rng.uniform(2.5, 4.0)
        resolution = round(float(resolution), 2)
        first_response = max(2, int(rng.normal(loc=35 if channel == "chat" else 95 if channel == "email" else 55, scale=18)))
        sla_missed = int(resolution > sla_hours[priority])
        score_mean = 4.5 - min(resolution / 48, 1.8) - 0.5 * sla_missed
        satisfaction = int(np.clip(round(rng.normal(score_mean, 0.75)), 1, 5))
        rows.append({
            "ticket_id": f"TCK-{counter:05d}",
            "created_at": created.strftime("%Y-%m-%d %H:%M:%S"),
            "channel": channel,
            "priority": priority,
            "category": category,
            "customer_segment": segment,
            "region": region,
            "resolution_hours": resolution,
            "sla_missed": sla_missed,
            "satisfaction_score": satisfaction,
            "first_response_minutes": first_response,
        })
        counter += 1

df = pd.DataFrame(rows)
issue_idx = rng.choice(df.index, size=18, replace=False)
df.loc[issue_idx[:6], "resolution_hours"] = np.nan
df.loc[issue_idx[6:9], "created_at"] = "not_a_date"
df.loc[issue_idx[9:12], "channel"] = df.loc[issue_idx[9:12], "channel"].str.upper()
df.loc[issue_idx[12:14], "resolution_hours"] = -1
if len(df) > 50:
    dup_rows = df.sample(4, random_state=42).copy()
    df = pd.concat([df, dup_rows], ignore_index=True)
space_idx = rng.choice(df.index, size=8, replace=False)
df.loc[space_idx, "category"] = df.loc[space_idx, "category"].astype(str) + " "

df.to_csv(OUTPUT, index=False, encoding="utf-8")
print(f"Saved {len(df)} rows to {OUTPUT}")
