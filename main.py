import platform
import random
import re
import socket
from sys import exit

import clipboard


def junk_input():
    _ = input('按回車鍵退出:')


ip = ''
randomNums = [p for p in range(1, 10)]
random.shuffle(randomNums)
for num in randomNums:
    domain = 'cn-sh-ix-acache-0{}.acgvideo.com'.format(num)
    try:
        ip = socket.gethostbyname(domain)
    except:
        pass
        # should never ignore exceptions!!

    if ip != '' and ip != '127.0.0.1':
        print("取得IP {} = {}".format(domain, ip))
        break

if ip == '':
    print("無法取得cn-sh-ix-acache-XX.acgvideo.com的IP")
    junk_input()
    exit(1)

text = clipboard.paste()
print('已複製: ' + text)
# cn-zjhz2-wasu-acache-10.acgvideo.com/XXX?abc=123
pattern = re.compile('[a-zA-Z0-9-]+[0-1]{1}[0-9]{1}.acgvideo.com')
p = pattern.match(text.strip())
if p is None:
    print('輸入錯誤...請確定複製伺服器: 如cn-zjhz2-wasu-acache-10.acgvideo.com')
    junk_input()
    exit(0)

target = p.group(0)
prefix = re.sub('[0-1]{1}[0-9]{1}.acgvideo.com', '', target)
# print('prefix:' + prefix)
# print(platform.system())

kernel = platform.system()
etc_host = '/etc/hosts'
if kernel == 'Windows':
    etc_host = r'C:\Windows\System32\drivers\etc\hosts'

f = open(etc_host, "r+")

hosts = []
for line in f:
    hosts.append(line)

# print(hosts)

s_marker = '##bilibili hosts start\n'
e_marker = '##bilibili hosts end\n'
s_i = hosts.index(s_marker) if s_marker in hosts else -1
e_i = hosts.index(e_marker) if e_marker in hosts else -1
# print(s_i)
# print(e_i)

if s_i != -1 and e_i != -1:
    del hosts[s_i:e_i + 1]

f.seek(0)
f.truncate()

for item in hosts:
    f.write(item)

if hosts[-1] != '\n':
    f.write('\n')

f.write(s_marker)
for i in range(0, 10):
    srv = prefix + '0' + str(i) + '.acgvideo.com'
    f.write(ip + ' ' + srv + '\n')
    print('寫入伺服器: ' + srv)
for i in range(10, 21):
    srv = prefix + str(i) + '.acgvideo.com'
    f.write(ip + ' ' + srv + '\n')
    print('寫入伺服器: ' + srv)
f.write(e_marker)
f.close()

junk = input('完成! 按回車鍵退出:')
