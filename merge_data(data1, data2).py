## merge_data(data1, data2)

def merge_data(data1, data2):
    merged = {}

    for item in data1:
        ts = convert_iso_to_millis(item['timestamp'])
        merged[ts] = {'timestamp': ts, 'value': item['value']}

    for item in data2:
        ts = item['timestamp']
        if ts in merged:
            merged[ts]['value'] += item['value']
        else:
            merged[ts] = {'timestamp': ts, 'value': item['value']}

    # Return sorted list by timestamp
    return [merged[ts] for ts in sorted(merged)]
