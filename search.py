import requests
from bs4 import BeautifulSoup

def search_web(query):
    try:
        url = "https://html.duckduckgo.com/html/"
        r = requests.post(url, data={"q": query}, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        results = []

        for item in soup.select(".result")[:5]:
            title = item.select_one(".result__title")
            snippet = item.select_one(".result__snippet")

            if title:
                text = title.get_text(" ", strip=True)

                if snippet:
                    text += "\n" + snippet.get_text(" ", strip=True)

                results.append(text)

        if results:
            return "\n\n".join(results)

        return "لم أجد نتائج."

    except Exception as e:
        return f"خطأ: {e}"