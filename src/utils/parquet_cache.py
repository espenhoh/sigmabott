from pathlib import Path
from datetime import datetime, timezone, timedelta
import pandas as pd

def read_parquet_cache(path, max_age_hours=None):
    """
    Leser en Parquet-fil hvis den finnes og er fersk nok.

    Args:
        path (Path | str): sti til fil
        max_age_hours (float | None): maks alder i timer før nedlasting kreves

    Returns:
        DataFrame | None  (None hvis ingen gyldig cache)
    """
    path = Path(path)
    if not path.exists():
        return None

    df = pd.read_parquet(path)
    meta = df.attrs or {}
    last_fetch = meta.get("last_fetch")

    if max_age_hours and last_fetch:
        age = datetime.now(datetime.timezone.utc) - datetime.fromisoformat(last_fetch)
        if age > timedelta(hours=max_age_hours):
            return None
    return df


def write_parquet_cache(df, path: Path, **meta):
    """
    Skriver DataFrame til Parquet med metadata.

    Eksempel:
        write_parquet_cache(df, "data/BTC-USD_1h.parquet", symbols="BTC-USD", interval="1h")
    """
    path = path.with_suffix('.parquet')
    print(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df = df.copy()
    meta["last_fetch"] = datetime.now(timezone.utc).isoformat()
    for k, v in meta.items():
        df.attrs[k] = v

    df.to_parquet(path, index=True)
    print(f"💾 Lagret {path.name} ({len(df)} rader)")
