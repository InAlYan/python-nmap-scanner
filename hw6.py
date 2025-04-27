# Написать программу на Python, которая будет проводить сканирование с использованием nmap.
import time

import nmap
from _socket import gethostname, gethostbyname

begin_time = time.time()
now = time.ctime(int(begin_time))
print(f'Время начала: {str(now)}')

sc = nmap.PortScanner()

host_name = gethostname()
ip_address = gethostbyname(host_name)

print(f'Запущено на {host_name} с ip {ip_address}')
print('===========================================')

# Сканировать чужие сети незаконно, поэтому
scanning_ip = ip_address
scanning_net = scanning_ip + '/24'

scan_result = sc.scan(scanning_net)

for item in scan_result['scan']:
    print(f'{item} : {scan_result["scan"][item]["status"]["state"]} : {scan_result["scan"][item]["vendor"]}')
    if scan_result["scan"][item]["status"]["state"] == 'up':
        print('\tпорты:')
        if "tcp" in scan_result["scan"][item]:
            for port in scan_result["scan"][item]["tcp"]:
                print(f'\t{port} : {scan_result["scan"][item]["tcp"][port]["state"]}')

end_time = time.time()
now = time.ctime(int(end_time))
print(f'Время окончания: {str(now)}')

elapsed_time = end_time - begin_time
print(f"Прошло {elapsed_time:.2f} секунд.")


# ВЫВОД:
# Время начала: Sun Apr 27 06:48:20 2025
# Запущено на HomeServ10 с ip 192.168.88.253
# ===========================================
# 192.168.88.1 : up : {'XX:XX:XX:XX:XX:XX': 'Routerboard.com'}
# 	порты:
# 	21 : open
# 	22 : open
# 	23 : open
# 	53 : open
# 	80 : open
# 	2000 : open
# 	8291 : open
# 192.168.88.247 : up : {'XX:XX:XX:XX:XX:XX': 'ASUSTek Computer'}
# 	порты:
# 	135 : open
# 	139 : open
# 	445 : open
# 	554 : open
# 	2869 : open
# 	3389 : open
# 	10243 : open
# 	49152 : open
# 	49153 : open
# 	49154 : open
# 	49155 : open
# 	49163 : open
# 192.168.88.248 : up : {}
# 	порты:
# 192.168.88.252 : up : {'XX:XX:XX:XX:XX:5XX': 'Giga-byte Technology'}
# 	порты:
# 	135 : open
# 	139 : open
# 	445 : open
# 	5357 : open
# 	49152 : open
# 	49153 : open
# 	49154 : open
# 	49155 : open
# 	49161 : open
# 192.168.88.253 : up : {}
# 	порты:
# 	80 : open
# 	135 : open
# 	139 : open
# 	445 : open
# 	902 : open
# 	912 : open
# 	2179 : open
# 	3306 : open
# 	6002 : open
# 	6881 : open
# 	7001 : open
# 	7002 : open
# 	7070 : open
# 	8000 : open
# Время окончания: Sun Apr 27 07:06:09 2025
# Прошло 1069.86 секунд.
