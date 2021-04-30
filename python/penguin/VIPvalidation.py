#/usr/bin/python

import sys
import socket,ssl
argumentList= sys.argv
outlist = []
dictionary = {}
class validate:
    def __init__(self,argumentList):
       self.argumentList = argumentList    #Using the argument list get the cert details
    for target_url in argumentList[1:]:
        cert = ssl.get_server_certificate((target_url, 443))
        ctx = ssl.create_default_context()
        socks = socket.socket()
        sock = ctx.wrap_socket(socks, server_hostname=target_url)
        sock.connect((target_url, 443))
        cert = sock.getpeercert()
	outlist.append(cert)

#Convert will convert the 'subjectAltName' which is dict of tuples with duplicate values..
    def Convert(self,tup, di):
        for a, b in tup:
            di.setdefault(a, []).append(b)
        return di


    def display(self,outlist):
        for certs in outlist:
            print(' \n')
            print("SAN Entries: {}".format(self.Convert(certs['subjectAltName'],dictionary)))
            print("notBefore: {}".format(str(certs['notBefore'])))
            print("notAfter: {}".format(str(certs['notAfter'])))
            print("serialNumber: {}".format(certs['serialNumber']))
	    dictionary.clear()
    
        

validate = validate(argumentList)
validate.display(outlist)


        
        
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
        




