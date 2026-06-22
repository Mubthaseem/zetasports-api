import json
import datetime
import sys

def main():
    status = sys.argv[1] if len(sys.argv) > 1 else 'fresh'
    try:
        with open('live-feed.json', 'r') as f:
            data = json.load(f)
    except Exception as e:
        # If file doesn't exist and we're marking it stale, start with empty data.
        # Otherwise, propagate the error if we expected fresh data.
        if status == 'stale':
            data = {}
        else:
            print(f"Error reading live-feed.json: {e}")
            sys.exit(1)

    data['_proxy_status'] = status
    data['_fetched_at'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    with open('live-feed.json', 'w') as f:
        json.dump(data, f, separators=(',', ':'))
    print(f"Stamped _fetched_at: {data['_fetched_at']} with status: {status}")

if __name__ == '__main__':
    main()
