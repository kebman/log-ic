# log-ic
Log when your internet connection is down

A small project to check internet connection outages, born out of the agony of a very bad, choppy and intermittent internet connection with chunks of outages coming at certain congested times (usually during weekends), and my ISP always reporting back that there's nothing wrong with the connection.

The program reports either a connected or not connected status based upon a socket test with active polling of a DNS from a list of choice servers. You either have an Internet outage, or you don't. 

If an outage is detected, it stores a timestamp of when the outage was recorded, and for how long—including the server note or error message—in an SQLite file. If you continue to test, it will store a new entry every ~30 seconds until your internet connection is restored again.

Note that all testing is currently done by actively polling a server. The manual version has only very basic flood controls to prevent the database file from becomming overfilled. The script doesn't have any socket flood controls outside a randomized list of servers to check, however, so please don't spam, or you risk being banned from those servers. I take no responsibility for your faulty or malevolent use of this code! I'm also looking for a way to test the connection passively.

A fully automated version is also available, that tests your internet connection a couple of times a minute.

## How to use

First of all, you need [Python 3](https://www.python.org/downloads/ "Download Python 3") installed to run these scripts. Once you have installed Python 3, you can open a terminal or command prompt, navigate to the folder of the script, and type something along the lines of `python name_of_script.py` in order to run the script in question. On some systems, you'll have to write `python3` instead of just `python`, depending on the architecture and if there are more than one version of Pythnon present. 

Note: You may have to edit small sections of the scripts yourself before use, such as changing file paths or file names. Let the comments guide you!

### First Run:
Run `create_log_db.py` once to create the database file. (You may have to create the folder for it too.)

### Testing Your Connection:
When you suspect an internet connection problem or outage, quickly run `log_ic_manually.py` before internet gets back on again. Keep running it until you're connected to the internet again. It should make the first database entry on the first run, and then log outages when they occurr. 
Note: It will only make a new log every ~30 seconds, but you can change this treshold to your liking in the script.
Warning: Running this script many times a second, for a prolonged period, may result in you getting banned from the servers it is pinging for attempted DDOS.

### Continuous Logging:
Start up the `log_ic_continuously.py` in your favourite terminal or cmd program. It will timestamp each test, and if an URL name is returned from the tested, you're online. If you're offline, the script will make a log entry in the SQLite database. 

To stop the script, hit either `Ctrl+C` or `Ctrl+Break` or `Ctrl+Z` or `CMD+Z` depending a bit on which terminal you're using and under which OS. 

### Print Log:
When you want to view the log, run `print_log.py`. It'll format the entries into something human readable. Then just copy it, paste it into a mail, and send to your ISP with a demand for a refund. :D
