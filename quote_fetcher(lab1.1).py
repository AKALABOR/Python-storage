import requests

url = "https://favqs.com/api/qotd"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    quote = data["quote"]["body"]
    author = data["quote"]["author"]

    print(f'"{quote}" - {author}')

    with open("quote.txt", "w", encoding="utf-8") as file:
        file.write(f'"{quote}" - {author}')

except requests.exceptions.RequestException as e:
    print("Помилка під час отримання цитати:", e)
