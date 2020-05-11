import subprocess
import sys
from datetime import datetime
import socket
argumentList = sys.argv
def validate(argumentList):
    str='openssl s_client -connect :443  </dev/null 2>&1 | openssl x509 -noout -issuer -dates -serial -subject'
    j= [ ]
    liste = [ ]
    for k in argumentList[1:]:
        addr1 = socket.gethostbyaddr(k)
    for k in argumentList[1:]:
        j.append(str[:26]+k+str[26:])
    for i in j:
        process = subprocess.check_output(i,shell=True).splitlines()
        for n in process:
            delta= datetime.strptime(process[2][-24:],'%b %d %H:%M:%S %Y %Z') - datetime.strptime(process[1][-24:],'%b %d %H:%M:%S %Y %Z')
        print "\033[1;32;40m"+socket.gethostbyaddr(i[25:-75])[0],"VIP will expire in",delta.days,"Days"+"\033[1;32;40m"
        print (process[0])
        print (process[3])
        print (process[4])
        print
        

validate(argumentList)