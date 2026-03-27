import requests
import json
import re

WIDGETS = {
    "all_time": "https://www.donationalerts.com/widget/instream-stats?id=2437375&token=yGN6M9ZbvUBBHFGsWmyR",
    "year": "https://www.donationalerts.com/widget/instream-stats?id=2437376&token=yGN6M9ZbvUBBHFGsWmyR",
    "month": "https://www.donationalerts.com/widget/instream-stats?id=2437377&token=yGN6M9ZbvUBBHFGsWmyR",
    "stream": "https://www.donationalerts.com/widget/instream-stats?id=2437378&token=yGN6M9ZbvUBBHFGsWmyR"
}

for key, url in WIDGETS.items():
    match = re.search(r'id=(\d+)&token=([^&]+)', url)
    if match:
        widget_id = match.group(1)
        token = match.group(2)
        api_url = f"https://www.donationalerts.com/api/getisswidgetdata?widget_id={widget_id}&token={token}"
        
        try:
            resp = requests.get(api_url)
            text = resp.text.strip('()')
            data = json.loads(text)
            print(f"{key}: Loaded {len(data.get('data', []))} records.")
            if len(data.get('data', [])) > 0:
                print(data['data'][0])
        except Exception as e:
            print(f"Error {key}: {e}")
