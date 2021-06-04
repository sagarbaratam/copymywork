import os,sys
import subprocess
l = os.environ['HOME']+'/git/'

def getimmediatesubdirs(l):
    return [name for name in os.listdir(l) if os.path.isdir(os.path.join(l,name))]

m = getimmediatesubdirs(l)

def vpnstatus():
    return subprocess.check_output("/opt/cisco/anyconnect/bin/vpn state|grep state", shell=True)

def gitpull(m):
    if b'state: Connected' not in vpnstatus():
        sys.exit("Please connect to VPN")
    else:
        for i in m:
         os.chdir(l+i)
         proc = subprocess.Popen(["git", "pull"],stdout=subprocess.PIPE)
         os.chdir(l)
         print(i,proc.stdout.read())

gitpull(m)

