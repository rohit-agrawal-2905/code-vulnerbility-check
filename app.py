import requests

def get_greeting():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        return "Hello, GitHub!"
    else:
        return "Failed to connect."

if __name__ == "__main__":
    print(get_greeting())

