from datetime import datetime, timezone

def convert_iso_to_millis(iso_timestamp):
    dt = datetime.fromisoformat(iso_timestamp.replace('Z', '+00:00'))
    return int(dt.timestamp() * 1000)
