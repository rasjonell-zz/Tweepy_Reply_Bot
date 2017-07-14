# Python Basic Tweet-Replying Bot

Simple Tweet-Replying Bot Made Using Python-Tweepy Library.

## Getting Started

in secrets.py Replace the items in single quotes with your unique strings from the Twitter apps website (and keep the single quotes).

### Prerequisites

You’ll need to create a Twitter app and install the Python Tweepy library.
Also you should have your Consumer Key, Consumer Secret, Access Token, and Access Token Secret in hand before beginning this.


## Running the bot

To keep our Twitterbot program running, we’ll be using the nohup command which ignores the hangup (HUP) signal. By using nohup, output that normally appears in the terminal window will instead print to a file called nohup.out.

Ensure that you’re in your Python environment with access to the Tweepy library, and in the directory where your Python program file lives, and type the following command:

```
nohup python bot.py &
```

### What's Next

You should receive output with a number in brackets ([1] if this is the first process you’re starting) and a string of numbers:

```
[1] 21725
```

## Stopping the Bot

Once you have verified that your Twitterbot is running, use logout to close the connection to your server.
```
logout
```

## Credits

* [DigitalOcean](https://www.digitalocean.com)
