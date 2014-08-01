try:
    from secrets import *
except ImportError:
    import sys
    sys.exit('secrets.py settings file not found. Please run `prepare.sh` to create one.')


ONEPERCENT_SERVER = "https://testing.onepercentclub.com"
ONEPERCENT_SERVER = "http://localhost:8000"
STREAM_SERVER = "http://stream.onepercentlive.com"
