import sys
import logging
from locust.main import main

# Suppress noisy Locust startup logs to keep your branding clean
logging.getLogger("locust").setLevel(logging.WARNING)

print(r"""
  _    _          _             _     _   _ _____ _____ 
 | |  | |        | |           | |   | | | |_   _|  __ \
 | |  | |___   __| | __ _ _ __ | |_  | |_| | | | | |__) |
 | |  | / _ \ / _` |/ _` | '_ \| __| |  _  | | | |  ___/ 
 | |__| |  __/ (_| | (_| | | | | |_  | | | |_| |_| |     
  \____/ \___|\__,_|\__,_|_| |_|\__| \_| |_/_____|_|   .!.  
                                                         
  [ HTTP PERFORMANCE TESTER ]
======================================================
""")
print('[+] Initializing testing engine...')
print('[+] Starting web interface on port 8089...\n')

# This injects the arguments directly into Locust and holds the process open
sys.argv = ['locust', '-f', 'locustfile.py']
main()