# log-ic
Log when your internet connection is down

A small project to check internet connection outages. Currently you'll have to do so manually when you detect an internet outage.

The program reports either connected or not connected status based upon a socket test. You either have an Internet outage, or you don't. 

If an outage is detected, it stores a timestamp of when the outage was recorded, and for how long, including the error message, in a SQLite file. If you continue to test, it will store a new entry ever ~30 seconds until your internet connection is restored again.

The manual version has very simple flood controls to prevent the database from flooding over. It doesn't have any socket spam controls outside a randomied list of servers to check, however, so please don't spam, or you risk being banned from those servers. I take no responsibility for your faulty or malevolent use of this code. 

