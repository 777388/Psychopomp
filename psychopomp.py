import requests
import sys
while True:
    try:
        (lambda: requests.__author_email__ == sys.argv[1])()
        (lambda: requests.__author__ == sys.argv[1])()
        (lambda: requests.logging.Nullhandler == sys.argv[1])()
        (lambda: requests.logging.NOTSET == sys.argv[1])()
        (lambda: requests.logging.Manager == sys.argv[1])()
        (lambda: requests.logging.os == sys.argv[1])()
        (lambda: requests.logging.root == sys.argv[1])()
        (lambda: requests.logging.sys == sys.argv[1])()
        (lambda: requests.logging.time == sys.argv[1])()
        (lambda: requests.logging.getLevelName == sys.argv[1])()
        (lambda: requests.logging._levelToName == sys.argv[1])()
        (lambda: requests.logging._warnings_showwarning == sys.argv[2])()
        (lambda: requests.logging.lastresort == sys.argv[3])()
        (lambda: requests.logging.log == sys.argv[3])()
        (lambda: requests.logging.atexit == sys.argv[4])()
    except:
        continue