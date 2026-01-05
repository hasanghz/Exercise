from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from tkinter import messagebox

# ================== راه‌اندازی Selenium ==================
options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# باز کردن سایت
driver.get("https://mobile.ttac.ir/")
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/barcodeUID/']"))).click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "styles_uid_button__3-wy8"))).click()

# ================== تابع بررسی UID ==================
def check_uid(uid_code):
    try:
        uid = uid_code[18:38]

        input_field = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_text_input__WDJdn"))
        )
        send_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_button__2qa-L"))
        )

        # پاک کردن محتوای قبلی قبل از ارسال UID جدید
        input_field.clear()
        input_field.send_keys(uid)
        send_button.click()

        container = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "styles_container__rZSyv"))
        )

        # استخراج اطلاعات موردنظر
        name_eng = container.find_element(By.XPATH, ".//p[contains(text(), 'TABLET') or contains(text(), 'mg')]").text
        name_fa = container.find_element(By.XPATH, ".//p[@class='styles_box_text__28j4K']").text
        price = container.find_element(By.XPATH, ".//p[contains(@class, 'styles_date_box_text__8M_KO')]").text

        # قالب‌بندی خروجی: عنوان و مقدار در دو خط
        result_text = f"💊 نام انگلیسی:\n{name_eng}\n\n💊 نام فارسی:\n{name_fa}\n\n💰 قیمت فراورده:\n{price}"

        # آماده شدن برای UID بعدی (پاک کردن فیلد و تمرکز دوباره)
        input_field.clear()
        input_field.click()

        return result_text

    except Exception as e:
        return f"❌ خطا:\n{e}"

# ================== GUI ==================
def run_check():
    uid = entry.get().strip()

    if len(uid) < 38:
        messagebox.showwarning("خطا", "UID معتبر وارد کنید")
        return

    result_label.config(text="⏳ در حال بررسی...")
    root.update()

    result = check_uid(uid)
    result_label.config(text=result, font=("Tahoma", 14, "bold"))

    # پاک کردن ورودی UID بعد از بررسی
    entry.delete(0, tk.END)
    entry.focus()

root = tk.Tk()
root.title("بررسی UID TTAC")
root.geometry("550x450")
root.resizable(False, False)

tk.Label(root, text="UID را وارد کنید:", font=("Tahoma", 12, "bold")).pack(pady=10)

entry = tk.Entry(root, width=50, font=("Tahoma", 12))
entry.pack(pady=5)

tk.Button(root, text="بررسی UID", command=run_check, height=2, font=("Tahoma", 12, "bold")).pack(pady=15)

result_label = tk.Label(root, text="", wraplength=500, justify="right", font=("Tahoma", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()

# ================== پایان برنامه ==================
# کروم باز است و آماده UID بعدی
