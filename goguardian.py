import requests
import sys

API_URL = "https://panther.goguardian.com/api/v1/ext/fullurl/categories"
AUTH_KEY = "ccd522cc-ba45-4554-b0d8-567ebc8c38a3"
category_map = {
    3: "Games",
    7: "Porn",
    13: "Games",
    15: "Drugs",
    17: "Social Media",
    20: "Adult",
    22: "Proxys",
    23: "Illegal",
    26: "Search Engines",
    42: "Time Wasting",
    45: "Entertainment",
    58: "Education Games",
    81: "Education",
    130: "No category",
}

def categorize(url):
    headers = {"Authorization": AUTH_KEY}
    params = {"url": url}
    try:
        res = requests.get(API_URL, headers=headers, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()
        categories = []
        for cat in data['categories'][0]['cats']:
            categories.append(category_map[cat] if cat in category_map else cat)
        return categories
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    result = categorize(domain)
    print(result)
