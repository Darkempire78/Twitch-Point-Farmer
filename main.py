from selenium import webdriver

import json
import time
import requests

class TwitchPointFarmer():
    def __init__(self, authTokenCookie, chromeDriverPath, twitchClientID, streamers):
        self.chromeDriverPath = chromeDriverPath

        self.authTokenCookie = authTokenCookie
        self.twitchClientID = twitchClientID
        self.twitchAPIEndpoint = "https://api.twitch.tv/kraken"
        self.twitchAPIHeaders = {
            'Client-ID' : self.twitchClientID,
            'Accept' : 'application/vnd.twitchtv.v5+json',
        }

        self.driver = None

        self.streamers = streamers
        self.currentStreamer = None

    def main(self):
        # Open chromedriver
        self.driver = webdriver.Chrome(self.chromeDriverPath)

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
                self.driver.find_element_by_css_selector("button[class='ScCoreButton-sc-1qn4ixc-0 ScCoreButtonSuccess-sc-1qn4ixc-5 VGQNd']").click()
            except:
                pass
            time.sleep(8)

    def getNextCurrentStreamer(self):
        for i in self.streamers:
            if self.checkIfUserIsStreaming(i):
                self.currentStreamer = i
                # Change the url
                self.driver.get(f"https://www.twitch.tv/{self.currentStreamer}")
                time.sleep(8)
                try:
                    # If the live is under 18 yo
                    self.driver.find_element_by_css_selector("button[data-a-target='player-overlay-mature-accept']").click()
                except:
                    pass
                return
        self.currentStreamer = None
        return

    def getUserID(self, user):
        reqSession = requests.Session()
        url = f"{self.twitchAPIEndpoint}/users?login={user}"

        req = reqSession.get(url, headers=self.twitchAPIHeaders)
        jsondata = req.json()
        if len(jsondata["users"]) > 0:
            return jsondata["users"][0]["_id"]
        return None

    def checkIfUserIsStreaming(self, user): #returns true if online, false if not
        userID = self.getUserID(user)

        if userID:
            reqSession = requests.Session()
            url = f"{self.twitchAPIEndpoint}/streams/{userID}"

            try:
                req = reqSession.get(url, headers=self.twitchAPIHeaders)
                jsondata = req.json()
                if 'stream' in jsondata:
                    return jsondata['stream'] is not None
            except Exception as e:
                print('Error checking user: ', e)
                return None
        else:
            print("invalid user")
            return False

if __name__ == '__main__':
    # Read config
    with open("config.json", "r", encoding="utf8") as f:
        config = json.load(f)
        authTokenCookie = config["authTokenCookie"]
        chromeDriverPath = config["chromeDriverPath"]
        twitchClientID = config["twitchClientID"]
        streamers = config["streamers"]

    twitchPointFarmer = TwitchPointFarmer(authTokenCookie, chromeDriverPath, twitchClientID, streamers)

    twitchPointFarmer.main()