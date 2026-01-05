from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import tkinter as tk
from tkinter import messagebox




options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://mobile.ttac.ir/")

wait = WebDriverWait(driver, 15)

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/barcodeUID/']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "styles_uid_button__3-wy8"))
).click()




current_price = None


def normalize_price(text):
    return int(text.replace(",", "").strip())


def extract_result():
    global current_price

    container = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "styles_container__rZSyv"))
    )

    fa_name = container.find_element(By.XPATH, ".//p[contains(text(),'نام فارسی')]/following-sibling::p").text
    en_name = container.find_element(By.XPATH, ".//p[contains(text(),'نام انگلیسی')]/following-sibling::p").text
    price_text = container.find_element(By.CLASS_NAME, "styles_date_box_text__8M_KO").text

    current_price = normalize_price(price_text)

    result = (
        f": نام فارسی\n{fa_name}\n\n"
        f": نام انگلیسی\n{en_name}\n\n"
        f": قیمت فرآورده\n{current_price:,}ریال"
    )

    return result


def go_back_and_reset():
    driver.back()

    input_field = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_text_input__WDJdn"))
    )
    input_field.clear()




def run_check(event=None):
    uid = entry.get().strip()

    if len(uid) < 38:
        messagebox.showwarning("خطا", " معتبر وارد کنید UID")
        return

    uid = uid[18:38]

    try:
        input_field = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_text_input__WDJdn"))
        )
        input_field.clear()
        input_field.send_keys(uid)

        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_button__2qa-L"))
        ).click()

        result = extract_result()
        result_label.config(text=result)

        go_back_and_reset()
        entry.delete(0, tk.END)
        divide_entry.delete(0, tk.END)
        divide_result_label.config(text="")

    except Exception as e:
        messagebox.showerror("خطا", str(e))


def divide_price(event=None):
    global current_price

    if current_price is None:
        divide_result_label.config(text="❌ هنوز قیمتی ثبت نشده")
        return

    try:
        value = int(divide_entry.get())
        if value <= 0:
            raise ValueError

        result = current_price // value
        divide_result_label.config(
            text=f": قیمت هر واحد\n {result:,}ریال  "
        )

    except ValueError:
        divide_result_label.config(text="❌ عدد معتبر وارد کنید")




root = tk.Tk()
root.title("TTAC بررسی")
root.geometry("520x700")
root.resizable(False, False)

tk.Label(
    root,
    text=": را وارد کنید UID  ",
    font=("Tahoma", 12, "bold"),
    fg="red"
).pack(pady=10)

entry = tk.Entry(root, width=55)
entry.pack()
entry.bind("<Return>", run_check)

tk.Button(
    root,
    text="UID بررسی",
    command=run_check,
    height=2,
    font=("Tahoma", 10, "bold")
    
).pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    wraplength=480,
    justify="center",
    font=("Tahoma", 13, "bold"),
    fg="blue"
)
result_label.pack(pady=15)




divider_frame = tk.Frame(root)
divider_frame.pack(pady=10)

tk.Label(
    divider_frame,
    text=": تقسیم قیمت بر تعداد",
    font=("Tahoma", 11, "bold"),
    fg="red"
).pack()

divide_entry = tk.Entry(divider_frame, width=25, justify="center")
divide_entry.pack(pady=5)
divide_entry.bind("<Return>", divide_price)

divide_result_label = tk.Label(
    divider_frame,
    text="",
    font=("Tahoma", 12, "bold"),
    fg="blue"
)
divide_result_label.pack(pady=5)




tk.Label(
    root,
    text="Made by Dr.Ghaznavi",
    font=("Tahoma", 9,"italic"),
    fg="gray"
).pack(side="bottom", pady=10)


root.mainloop()
