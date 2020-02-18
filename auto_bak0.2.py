import telnet2
t=telnet2.telnet()
ip = '192.168.0.211'
t.login(ip, username='admin',password='sanyou',p=23,timeout=5)
output1=t.execute('dis th')
print(output1)
output2=t.execute('dis cu')
print(output2)
t.close()