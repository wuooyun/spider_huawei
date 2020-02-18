from telnetlib import Telnet
import time

HOST = '192.168.0.213'
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

def execute(self,cmd,new_line='\n',timeout=5,more_timeout=2):#this function executes any command and returns the output
    if cmd.strip()!='':
        self.telnet.write("{} {}".format(cmd.strip(),new_line).encode('utf-8'))#send the command
        c=self.telnet.read_until(self.prompt_end,timeout=timeout)#read data until it receive the end of the prompt after executing the command
        if b"---- More ----" in c:
            while True:
                self.telnet.write("\n".format(cmd.strip(),new_line).encode('utf-8'))
                o=self.telnet.read_until(b"---- More ----",timeout=more_timeout)
                c+=o
                if self.prompt_end in c:
                    break

tn.write(b'qu \n')
print (res)

pass


