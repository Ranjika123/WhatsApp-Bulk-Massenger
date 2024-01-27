from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import quote
import os

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Ranjika Nethpriya   ***")
print("*****           www.github.com/Ranjika123            ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

# Read the message from the file
with open("message.txt", "r", encoding="utf8") as f:
    message = f.read()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message + style.RESET)

# Read phone numbers from the file
numbers = []
with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f if line.strip()]

total_number = len(numbers)
print(style.RED + f'We found {total_number} numbers in the file' + style.RESET)
delay = 30

# Initialize ChromeDriver using WebDriver Manager
driver = webdriver.Chrome()

print('Once your browser opens up, sign in to web WhatsApp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

for idx, number in enumerate(numbers):
    number = number.strip()
    if not number:
        continue

    print(style.YELLOW + f'{idx + 1}/{total_number} => Sending message to {number}.' + style.RESET)
    
    try:
        url = f'https://web.whatsapp.com/send?phone={number}&text={quote(message)}'
        sent = False

        for i in range(3):
            if not sent:
                driver.get(url)
                
                try:
                    click_btn = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer are connected to the internet.")
                    print("If there is an alert, please dismiss it." + style.RESET)
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(3)
                    print(style.GREEN + f'Message sent to: {number}' + style.RESET)
    except Exception as e:
        print(style.RED + f'Failed to send message to {number}: {e}' + style.RESET)

# Close the browser
driver.quit()
