from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random 

driver = webdriver.Chrome()

driver.get("https://internxt.com/temporary-email")

# Use explicit wait to ensure the cookies button is visible
wait = WebDriverWait(driver, 15)
accept_cookies_button = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".sn-b-def.sn-three-btn.sn-adj-fnt.sn-blue")
))

# Try clicking the accept cookies button
accept_cookies_button.click()

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # ascii_letters includes both lowercase and uppercase
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def close_ad():
    try:
        ad_button = driver.find_element(By.CSS_SELECTOR, ".absolute.right-0.m-7.flex.rounded-md.text-white.hover:bg-gray-1/10")
        if ad_button:
            ad_button.click()
    except:
        print("No ad found")

def inbox_content(driver, selector):
    # Find the div
    div = driver.find_element(By.CSS_SELECTOR, selector)
    # Check if it has any non-whitespace content
    return bool(div.text.strip())

for i in range(10):
    email = ""
    password = "Test1234"
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    year = random.randint(1980, 2000)
    name = generate_random_string(8)
    user_name = name + "1234"
    
    while email == "":
        close_ad()
        parent = driver.find_element(By.CSS_SELECTOR, ".flex.h-full.w-full.cursor-pointer.flex-row.items-center.justify-between.rounded-xl.bg-white.text-gray-80.shadow-sm.px-4.py-3")
        p_element = parent.find_element(By.TAG_NAME, 'p')
        p_text = p_element.text
        if "@" in p_text:
            email = p_text

    driver.execute_script("window.open('https://www.instagram.com/accounts/emailsignup/', 'new window')")

    # Switch to the new tab (Instagram)
    driver.switch_to.window(driver.window_handles[1])

    # Wait for Instagram cookie button
    cookie_element = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "._a9--._ap36._a9_0")
    ))
    
    cookie_button = driver.find_element(By.CSS_SELECTOR, "._a9--._ap36._a9_0")
    cookie_button.click()

    inputs = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".x6s0dn4.xnz67gz.x19gtwsn.x1nk0tez.x1xp9za0.x1hm1hlx.x1npaq5j.x1c83p5e.x1enjb0b.x199158v.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x9f619.x5n08af.x78zum5.x1q0g3np.xvs91rp.x1n2onr6.xh8yej3")
    ))

    index_of_input = 0
    User_data = [email,name,user_name,password]
    for input in inputs:
        label = input.find_element(By.TAG_NAME, 'label')
        input = label.find_element(By.TAG_NAME, "input")
        input.send_keys(User_data[index_of_input])
        index_of_input += 1
    time.sleep(1)

    next_buttons = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")
    ))
    next_buttons[1].click()

    selects = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "._aau-._ap32")
    ))

    index_of_select = 0
    date_data = [month,day,year]
    for select in selects:
        main_select = Select(select)
        main_select.select_by_value(str(date_data[index_of_select]))
        index_of_select += 1

    next_buttons = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")
    ))
    next_buttons[0].click()
    
    driver.switch_to.window(driver.window_handles[0])

            

    time.sleep(1000)
    driver.quit()
