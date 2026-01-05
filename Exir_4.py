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
wait = WebDriverWait(driver, 10)

driver.get("https://mobile.ttac.ir/")

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[@href='/barcodeUID/']")
)).click()

wait.until(EC.element_to_be_clickable(
    (By.CLASS_NAME, "styles_uid_button__3-wy8")
)).click()




def check_uid(uid_code):
    try:
        uid = uid_code[18:38]

        input_field = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_text_input__WDJdn"))
        )
        send_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_card_button__2qa-L"))
        )

        input_field.send_keys(uid)
        send_button.click()

        container = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "styles_date_box_text__8M_KO"))
        )
        
        
        eng_name = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "styles_box_text_ltr__qM6W9"))
        )
        
        farsi_name=wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "styles_box_text__28j4K"))
        )


        container=container.text
        container = int(container)  
        container = f"{container:,}"
        
        
        eng_name=eng_name.text
        farsi_name=farsi_name.text


        new_result= f': نام فرآورده \n {farsi_name} \n \n : نام انگلیسی \n {eng_name} \n \n : قیمت  \n {container}'
                          
       
        result_text = new_result
        
        driver.get("https://mobile.ttac.ir/barcodeUID/")

        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "styles_uid_button__3-wy8"))
        ).click()
        
        
        
        return result_text

    except Exception as e:
        return f"❌ خطا:\n{e}"




def run_check():
    uid = entry.get().strip()

    if len(uid) < 38:
        messagebox.showwarning("خطا", "UID معتبر وارد کنید")
        return

    result_label.config(text="⏳ در حال بررسی...")
    root.update()

    result = check_uid(uid)
    result_label.config(text=result)

    entry.delete(0, tk.END)
    entry.focus()


def on_close():
    driver.quit()
    root.destroy()


root = tk.Tk()
root.title("بررسی UID TTAC")
root.geometry("700x800")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text=":  را وارد کنید UID ", font=("Tahoma", 12)).pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.focus()

tk.Button(root, text="UID بررسی ", command=run_check, height=2).pack(pady=15)

result_label = tk.Label(
    root, text="", wraplength=460, justify="center", font=("Tahoma", 14)
)
result_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Made by Dr. Ghaznavi",
    font=("Tahoma", 12, "italic"),
    fg="gray"
)
footer.pack(side="bottom", pady=5)


root.mainloop()
