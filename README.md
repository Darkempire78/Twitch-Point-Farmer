# Twitch Point Farmer

![](https://img.shields.io/codefactor/grade/github/Darkempire78/Twitch-Point-Farmer?style=for-the-badge) ![](https://img.shields.io/github/repo-size/Darkempire78/Twitch-Point-Farmer?style=for-the-badge) ![](https://img.shields.io/badge/SOURCERY-ENABLED-green?style=for-the-badge) <a href="https://discord.com/invite/sPvJmY7mcV"><img src="https://img.shields.io/discord/831524351311609907?color=%237289DA&label=DISCORD&style=for-the-badge"></a>

Automatically collects channel points for your favorite streamers.

## Installation

* Install all dependencies : ``pip install -r requirements.txt``.
* Download [Chromedriver](https://chromedriver.chromium.org/downloads).
* Get your Twitch authentication cookie (auth-token).
* Edit `config.example.json`:

```Javascript
{
    "chromeDriverPath": "", // Set the path of the chromedriver
    "authTokenCookie": "", // Paste the content of your Twitch authentication cookie (auth-token)
    "streamers": [] // Put a list of your streamers to farm in order of preference (ex: ["streamerName1", "streamerName2", ...])
}
```

* Rename it to `config.json`.

Finally, launch the script.

## See the bot

You can see how the robot works by commenting [this line](https://github.com/Darkempire78/Twitch-Point-Farmer/blob/main/main.py#L19).

## Get your Twitch authentication cookie (auth-token).

* Go to `settings` (`advanced settings` for some browsers)
* Go to `privacy and security`
* Click on `cookies and other site data`
* Click on `set cookies and site data`
* Search for twitch.tv
* Click on the coupon and retrieve the contents of the cookie named `auth-token`

Shortcut for main browsers:

**Chrome:** `chrome://settings/cookies/detail?site=twitch.tv`

**Brave:** `brave://settings/cookies/detail?site=twitch.tv`

### Firefox

* Go to `https://www.twitch.tv/`
* Open the Dev Tools (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> or <kbd>F12</kbd>)
* Go to the Storage tab
* Click on `Cookies` then `https://www.twitch.tv`
* Copy the content of the cookie named `auth-token`

## Features

* Collect points (every 5 minutes) (+10pts)
* Recover the drops (+50pts)
* Watch serial streams (+450pts)

## Discord

Join the Discord server !

[![](https://i.imgur.com/UfyvtOL.png)](https://discord.gg/sPvJmY7mcV)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is under [GPLv3](https://github.com/Darkempire78/Raid-Protect-Discord-Bot/blob/master/LICENSE).
