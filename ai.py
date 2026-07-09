import requests
from bs4 import BeautifulSoup
from config import API_KEY, MODEL

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


def search_web(query):
    try:
        url = "https://html.duckduckgo.com/html/"
        r = requests.post(url, data={"q": query}, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        results = []
        for a in soup.select(".result__title a"):
            text = a.get_text(" ", strip=True)
            if text:
                results.append(text)

        if results:
            return "نتائج من الإنترنت:\n\n" + "\n".join(results[:5])

        return "لم أجد نتائج."

    except Exception as e:
        return f"خطأ أثناء البحث: {e}"


def ask_ai(message):
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": message
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, json=data, timeout=20)

        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]

        print("Gemini فشل، سيتم البحث في الإنترنت...")
        return search_web(message)

    except Exception:
        return search_web(message)