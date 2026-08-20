import sys
from locust.main import main

print('=============================================')
print('     [ Vedant HTTP Performance Tester ]      ')
print('=============================================')
print('[+] Initializing testing engine...')
print('[+] Starting web interface on port 8089...\n')

# This injects the arguments directly into Locust and holds the process open
sys.argv = ['locust', '-f', 'locustfile.py']
main()
