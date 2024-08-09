# log-ic

Keep tabs on your internet outages (and give your ISP a hard time!)

## Overview

Ever been frustrated by a choppy, unreliable internet connection, especially during the weekends? This small project was born out of that same agony. With your ISP always insisting that there's "nothing wrong," **log-ic** helps you track exactly when your internet decides to take a nap and for how long.

**log-ic** works by performing regular socket tests, pinging a list of DNS servers to check if you're online or not. If it finds your internet is down, it'll log the outage, including a timestamp and any relevant error messages, into a neat little SQLite database file. When your connection comes back, it'll log that too!

### Fair warning

This script actively pings servers, so if you overdo it, you might accidentally annoy the servers you're testing against—possibly getting yourself temporarily banned. Use responsibly!

## Features

- **Manual Outage Logging:** Quickly log an outage when you notice your connection is down.
- **Continuous Monitoring:** Automatically test and log your connection status every ~30 seconds.
- **Readable Logs:** Easily view and format your logs to share with your ISP when you demand that sweet refund.

## Usage

### Prerequisites

- You'll need [Python 3](https://www.python.org/downloads/ "Download Python 3") to run these scripts. If you don't have it installed yet, go grab it!

### First Run

1. Open your terminal or command prompt.
2. Navigate to the script folder.
3. Run `create_log_db.py` to set up your database (you might need to create the folder first).

### Checking Your Connection Manually

When you suspect that your internet connection is doing its disappearing act:

1. Run `log_ic_manually.py` immediately (before your connection reappears like nothing happened).
2. Keep the script running until you're back online.
3. The script logs an outage every ~30 seconds—feel free to adjust this interval in the code if you want.

#### Note:

Don't run this script too often in a short period, or you might be seen as a threat by the servers you're pinging. No one wants a DDOS ban!

### Continuous Monitoring (Set It and Forget It)

1. Start `log_ic_continuously.py` in your terminal.
2. The script will check your connection status at regular intervals and log any outages.
3. To stop it, use `Ctrl+C`, `Ctrl+Break`, or `CMD+Z`, depending on your OS and terminal.

### Viewing Your Log

Need evidence to wave in your ISP's face? Run `print_log.py` to format and view your logs in a human-readable way. Copy, paste, and hit send!

## Project Participation

Think you can make this project even better? Want to join the battle against dodgy ISPs? We'd love to have you on board! Feel free to fork the code, submit pull requests, or suggest new features and improvements. Whether you're fixing bugs, adding cool new functionalities, or just adding your own twist to the project, your contributions are welcome. Together, we can give ISPs everywhere a run for their money!

## A Note on Customization

These scripts are provided as-is under the MIT license, meaning you can use, modify, and distribute them as you like. However, to get them working just right for you, you may need to dive into the code and tweak things like database files, file paths, server lists, and timing intervals. Don’t worry—comments are sprinkled throughout the code to guide you!
