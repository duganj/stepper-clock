import ntplib
from datetime import datetime, timezone
import time
import pytz

c = ntplib.NTPClient()
# Provide the respective ntp server ip in below function
response = c.request('time.nist.gov', version=3)
response.offset

utctime = datetime.fromtimestamp(response.tx_time, timezone.utc)
print(utctime)

localtime = utctime.astimezone(pytz.timezone('America/Los_Angeles'))
print(localtime)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# at this point I have the time to send to the clock

# home / time setting sequence (would be nice to automate homing with a hall effect sensor or similar

# when minute ticks over, move minute hand
