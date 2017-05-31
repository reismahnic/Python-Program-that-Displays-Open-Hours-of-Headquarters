import datetime
import time
import pytz

from datetime import datetime, timedelta
from pytz import timezone

pacificUS = timezone('US/Pacific')
portland_time = datetime.now(pacificUS)
print "The current time in Portland is:"
print portland_time.strftime('%H-%M')

if(int(portland_time.strftime('%H')) > 9 and int(portland_time.strftime('%H')) < 21):
    print "The branch is open."
else:
    print "The branch is closed."

easternUS = timezone('US/Eastern')
newYork_time = datetime.now(easternUS)
print "The current time in New York is:"
print newYork_time.strftime('%H-%M')

if(int(newYork_time.strftime('%H')) > 9 and int(newYork_time.strftime('%H')) < 21):
    print "The branch is open."
else:
    print "The branch is closed."

pacificEU = timezone('Europe/London')
london_time = datetime.now(pacificEU)
print "The current time in London is:"
print london_time.strftime('%H-%M')

if(int(london_time.strftime('%H')) > 9 and int(london_time.strftime('%H')) < 21):
    print "The branch is open."
else:
    print "The branch is closed."

