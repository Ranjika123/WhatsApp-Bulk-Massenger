from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Config
login_time = 100                 # Time for login (in seconds)
new_msg_time = 5                # TTime for a new message (in seconds)
send_msg_time = 5               # Time for sending a message (in seconds)
country_code = 7               # Set your country code
action_time = 2                 # Set time for button click action
image_path = None        # Absolute path to you image




def send_whatsapp_message(driver, country_code, phone_number, message, image_path=None):
    link = f'https://web.whatsapp.com/send/?phone={country_code}{phone_number}'
    driver.get(link)
    
    # Wait until the chat input field is present
    chat_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._2_1wd')))
    
    # Enter the message
    chat_input.send_keys(message)
    chat_input.send_keys(Keys.ENTER)

    # Add logic for attaching image if needed

    time.sleep(send_msg_time)

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Encode Message Text
with open('message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()


# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        send_whatsapp_message(driver, country_code, num, msg, image_path)

# Quit the driver
driver.quit()
