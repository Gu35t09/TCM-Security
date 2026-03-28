# Importing is important
import  sys # System function and parameters
print(sys.version)

import datetime
# if we do this to get the time we'll need to do 
print(datetime.datetime.now())

from datetime import datetime # with this we can do as follow
print(datetime.now())

from datetime import datetime as dt # using an alias
print(dt.now())
