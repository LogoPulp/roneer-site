import json
import time
import re
import concurrent.futures
import requests

WIDGETS = {
    "all_time": "https://www.donationalerts.com/widget/instream-stats?id=2437375&token=yGN6M9ZbvUBBHFGsWmyR",
    "year": "https://www.donationalerts.com/widget/instream-stats?id=2437376&token=yGN6M9ZbvUBBHFGsWmyR",
    "month": "https://www.donationalerts.com/widget/instream-stats?id=2437377&token=yGN6M9ZbvUBBHFGsWmyR",
    "stream": "https://www.donationalerts.com/widget/instream-stats?id=2437378&token=yGN6M9ZbvUBBHFGsWmyR"
}

OUTPUT_FILE = "assets/donors.json"

def fetch_widget_data(key, url):
    print(f"⏳ [{key}] Загрузка данных...")

    match = re.search(r'id=(\d+)&token=([^&]+)', url)
    if not match:
        print(f"❌ [{key}] Ошибка парсинга URL")
        return key, []

    widget_id = match.group(1)
    token = match.group(2)

    api_url = f"https://www.donationalerts.com/api/getisswidgetdata?widget_id={widget_id}&token={token}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    donors = []

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()

        text = response.text.strip('()')
        data = json.loads(text)

        items = data.get("data")
        if not items:
            items = []

        for item in items:
            name = str(item.get("username", "")).strip()
            amount_str = str(item.get("amount", "")).strip()
            currency = str(item.get("currency", "")).strip()

            if name:
                clean_amount = re.sub(r'[^0-9]', '', amount_str.split(',')[0].split('.')[0])
                is_gold = clean_amount and int(clean_amount) >= 1000

                amount_formatted = f"{amount_str} {currency}".strip()

                donors.append({
                    "name": name,
                    "amount": amount_formatted,
                    "type": "gold" if is_gold else "normal"
                })

        print(f"✅ [{key}] Итог: {len(donors)} записей")
        return key, donors

    except Exception as e:
        print(f"❌ [{key}] Ошибка HTTP/Парсинга: {e}")
        return key, []

def main():
    print("🚀 Запуск сборщика донатов RONEER_ (через API)...")
    print("=" * 50)
    start_time = time.time()

    final_data = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url = {executor.submit(fetch_widget_data, key, url): key for key, url in WIDGETS.items()}
        for future in concurrent.futures.as_completed(future_to_url):
            key, data = future.result()
            final_data[key] = data

    total_donors = sum(len(v) for v in final_data.values())

    if total_donors == 0:
        print("\n" + "=" * 50)
        print("ℹ️  Список донатеров пуст.")
        print("=" * 50)

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(final_data, f, ensure_ascii=False, indent=2)

        elapsed = time.time() - start_time
        print(f"\n💾 Готово за {elapsed:.2f} сек! Файл: {OUTPUT_FILE}")
        print(f"📊 Всего записей: {total_donors}")

    except Exception as e:
        print(f"🔥 Ошибка сохранения: {e}")

if __name__ == "__main__":
    main()
