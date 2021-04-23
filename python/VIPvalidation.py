#/usr/bin/python

import sys
import socket,ssl
argumentList= sys.argv
dictionary = {}
class validate:
    def __init__(self,argumentList):
       self.argumentList = argumentList
    for target_url in argumentList[1:]:
        cert = ssl.get_server_certificate((target_url, 443))
        ctx = ssl.create_default_context()
        socks = socket.socket()
        sock = ctx.wrap_socket(socks, server_hostname=target_url)
        sock.connect((target_url, 443))
        certs = sock.getpeercert()
    
    def Convert(self,tup, di):
        dictionary = {}
        for a, b in tup:
            di.setdefault(a, []).append(b)
        return di


    def display(self):
        #print(self.certs)
        print("SAN Entries: {}".format(self.Convert(self.certs['subjectAltName'],dictionary)))
        print("notBefore: {}".format(str(self.certs['notBefore'])))
        print("notAfter: {}".format(str(self.certs['notAfter'])))
        print("serialNumber: {}".format(self.certs['serialNumber']))

validate = validate(argumentList)
validate.display()


        
        
## print ("subject:",dict(x[0] for x in certs['subject']))--- interesting one--
        

   
            










    #for k in argumentList[1:]:
     #   addr1 = socket.gethostbyaddr(k)
    #for k in argumentList[1:]:
    #    j.append(str[:26]+k+str[26:])
    #for i in j:
    #    process = subprocess.check_output(i,shell=True).splitlines()
    #    for n in process:
    #        delta= datetime.strptime(process[2][-24:],'%b %d %H:%M:%S %Y %Z') - datetime.strptime(process[1][-24:],'%b %d %H:%M:%S %Y %Z')
    #    print "\033[1;32;40m"+socket.gethostbyaddr(i[25:-75])[0],"VIP will expire in",delta.days,"Days"+"\033[1;32;40m"
    #    print (process[0])
    #    print (process[3])
    #    print (process[4])
    #    print
        




