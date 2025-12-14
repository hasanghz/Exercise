from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True  # این باعث می‌شود مرورگر باز نشود
options.add_argument("--disable-gpu")  # بهینه‌سازی برای headless
options.add_argument("--window-size=1920,1080")  # تعیین اندازه صفحه

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)


#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

qr=(input())
qr="https://mobile.ttac.ir/showResult?uid="+(qr[18:38])


driver.get(qr)
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/barcodeUID/']")))
button.click()


button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "styles_uid_button__3-wy8")))
button.click()

input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_text_input__WDJdn")))



input_field.send_keys(qr)
send_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_button__2qa-L"))
)
send_button.click()



container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "styles_container__rZSyv"))
)
print(container.text)





print(driver.current_url)




driver.quit()





    
    

    
