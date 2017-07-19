from security.zap_scanner import Scanner
from accounts import Accounts

scanner = Scanner()
scanner.run('http://' + Accounts.ZAP_API_IP, Accounts.ZAP_API_KEY)