import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TTACClient:
    def __init__(self):
        self.session = requests.Session()
        self.device_identifier = "a5894ad8-bd16-46f0-bf98-44e959eb735c"
        self._init_session()

    def _init_session(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://mobile.ttac.ir/")
        cookies = driver.get_cookies()
        driver.quit()

        # انتقال cookieها به requests
        for c in cookies:
            self.session.cookies.set(c["name"], c["value"])

    def check_uid(self, uid_code: str):
        url = "https://newapi.ttac.ir/irfdamobile/v1/checkuId"

        params = {
            "uidCode": uid_code,
            "latitude": 0,
            "longitude": 0,
            "device": 2,
            "deviceIdentifier": self.device_identifier,
            "Platform": 0,
            "PlatformVersion": 1,
            "VersionCode": "",
            "AppVersion": ""
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Origin": "https://mobile.ttac.ir",
            "Referer": "https://mobile.ttac.ir/"
        }

        r = self.session.get(url, params=params, headers=headers, timeout=10)

        if r.status_code == 401:
            # session منقضی شده → دوباره بساز
            self._init_session()
            r = self.session.get(url, params=params, headers=headers, timeout=10)

        r.raise_for_status()
        return r.json()
    
client = TTACClient()

data = client.check_uid("13240014003003123598")

print(data)
