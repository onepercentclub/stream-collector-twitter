try:
    from secrets import *
except ImportError:
    import sys
    sys.exit('secrets.py settings file not found. Please run `prepare.sh` to create one.')


STREAM_SERVER = "http://localhost:8080"


