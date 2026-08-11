import csv
import json
import bs4
import requests


def scrape_tech_news():
    url = "https://news.ycombinator.com/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
    }

    try:
        print(f"⏳ Fetching web content from {url}...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        headlines = []

        title_tags = soup.select(".titleline > a")

        for idx, tag in enumerate(title_tags[:15], start=1):
            title = tag.get_text()
            link = tag.get("href")
            headlines.append({"id": idx, "title": title, "link": link})

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching website data: {e}")
        return []


def save_to_json(data, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"💾 Saved {len(data)} headlines to '{filename}'")


def save_to_csv(data, filename="news.csv"):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"📄 Exported {len(data)} headlines to '{filename}'")


def main():
    print("=" * 50)
    print("🕸️  AUTOMATED WEB SCRAPER & DATA EXTRACTOR 🕸️")
    print("=" * 50)

    headlines = scrape_tech_news()

    if headlines:
        print("\n📰 TOP TRENDING TECH HEADLINES:")
        print("-" * 50)
        for item in headlines:
            print(f"{item['id']}. {item['title']}")
            print(f"   🔗 {item['link']}\n")

        save_to_json(headlines)
        save_to_csv(headlines)
        print("\n✅ Scraping & Data Export Completed Successfully!")
    else:
        print("❌ No data scraped.")


if __name__ == "__main__":
    main()