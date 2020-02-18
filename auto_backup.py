from telnetlib import Telnet
import time

HOST = '192.168.0.211'
user = 'admin'
password = 'sanyou'

tn = Telnet(HOST)

tn.read_until(b"Username:")
tn.write(user.encode('ascii')+b'\n')

tn.read_until(b'Password:')
tn.write(password.encode('ascii')+b'\n')

tn.write(b'dis cu \n')
time.sleep(2)
a = tn.read_until(b'')
print(a)
res = tn.read_very_eager()
tn.write(b'qu \n')
print (res)

pass


