from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json
import time
import datetime

class TwitchPointFarmer():
    def __init__(self, authTokenCookie, chromeDriverPath, streamers, hideTheBot, logs):
        self.chromeDriverPath = chromeDriverPath
        self.authTokenCookie = authTokenCookie
        self.driver = None
        self.streamers = streamers
        self.currentStreamer = None
        self.hideTheBot = hideTheBot
        self.logs = logs

    def main(self):
        # Open chromedriver
        chromeOptions = Options()
        if hideTheBot:
            chromeOptions.add_argument("--headless")

        self.driver = webdriver.Chrome(
            executable_path = self.chromeDriverPath,
            chrome_options = chromeOptions
        )

        # Connection
        self.driver.get("https://www.twitch.tv")
        self.driver.add_cookie({
            "name": "auth-token", 
            "value": self.authTokenCookie
        })

        while True:
            # Set the current streamer
            if self.currentStreamer is None:
                self.getNextCurrentStreamer()

            # Click on the reward
            try:
                self.driver.find_element_by_css_selector("button[class='sc-fzozJi sc-fznKkj jwRWhW']").click()
                self.log("Drop collected")
            except:
                pass
            time.sleep(8)

    def getNextCurrentStreamer(self):
        for i in self.streamers:
            if self.checkIfUserIsStreaming(i):
                self.currentStreamer = i
                self.log(f"Is farming {self.currentStreamer}")
                time.sleep(8)
                try:
                    # If the live is under 18 yo
                    self.driver.find_element_by_css_selector("button[data-a-target='player-overlay-mature-accept']").click()
                    self.log("+18 overlay skipped")
                except:
                    pass
                return
        self.currentStreamer = None
        return

    def checkIfUserIsStreaming(self, user): #returns true if online, false if not
        self.driver.get(f"https://www.twitch.tv/{user}")
        self.log(f"Checking if {user} is streaming")
        time.sleep(10)
        try:
            self.driver.find_element_by_css_selector("p[data-a-target='animated-channel-viewers-count']") # Number of viewers (is streaming)
            self.log(f"{user} is streaming")
            return True
        except:
            self.log(f"{user} is not streaming")
            return False

    def log(self, content):
        if self.logs:
            print(f"[{datetime.datetime.now().strftime('%X')}] {content}")

if __name__ == '__main__':
    # Read config
    with open("config.json", "r", encoding="utf8") as f:
        config = json.load(f)
        authTokenCookie = config["authTokenCookie"]
        chromeDriverPath = config["chromeDriverPath"]
        streamers = config["streamers"]
        hideTheBot = config["hideTheBot"]
        logs = config["logs"]

    twitchPointFarmer = TwitchPointFarmer(authTokenCookie, chromeDriverPath, streamers, hideTheBot, logs)
    twitchPointFarmer.main()
