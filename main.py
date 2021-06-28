from selenium import webdriver

import json
import platform
import time

def main(authToken):
    
    # Open chromedriver
    if platform.system() == "Windows":
        driver = webdriver.Chrome("chromedriver.exe")
    else:
        driver = webdriver.Chrome()

    # Connection
    driver.get("https://www.twitch.tv")
    driver.add_cookie({
        "name": "auth-token", 
        "value": authToken
    })
    driver.get("https://www.twitch.tv/gotaga")
    
    while True:
        # Click on the reward
        try:
            driver.find_element_by_css_selector("button[class='ScCoreButton-sc-1qn4ixc-0 ScCoreButtonSuccess-sc-1qn4ixc-5 VGQNd']").click()
        except:
            pass
        time.sleep(8)
    
# time.sleep(2)
# driver.find_element_by_css_selector("input[id='login-username']").send_keys(login)
# driver.find_element_by_css_selector("button[data-a-target='passport-login-button']").click()

if __name__ == '__main__':
    # Read config
    with open("config.json", "r", encoding="utf8") as f:
        config = json.load(f)
        authToken = config["authToken"]
        
    main(authToken)