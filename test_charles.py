import requests

url = "https://irc.fda.gov.ir/nfi"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "TTAC-Android"
}

data = {
    "code": "12345678901234567890"
}

r = requests.post(url, json=data, headers=headers, timeout=10)
print(r.status_code)
print(r.text)
