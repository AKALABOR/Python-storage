import requests

url = "https://api.quotable.io/random"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    quote = data["content"]
    author = data["author"]
    
    print(f'"{quote}" - {author}')

    with open("quote.txt", "w", encoding="utf-8") as file:
        file.write(f'"{quote}" - {author}')
else:
    print("Помилка отримання цитати")
