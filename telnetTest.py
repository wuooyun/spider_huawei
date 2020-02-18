import telnet2
import telnetlib


ip = '192.168.0.213'
t = telnet2.telnet()

t.login(ip, username='admin',password='sanyou',p=23,timeout=5)

output1=t.execute('dis cu') 
print(output1) 
output1=t.execute('dis th') 
t.close()