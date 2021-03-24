
import platform
import subprocess

yum_update='yum update'
y
def platform():
    if platform.dist()[0] == redhat:
       family = redhat
    elif platform.dist()[0] == ubuntu:
       family = ubuntu
    elif platform.dist()[0] == centos: 
       family = centos
    else:
        return "Unfamiliar distro"
platform()

def update_cache(family):
    if family == ubuntu:
        subprocess.call([apt, get, update])
    elif family == redhat or centos:
        subprocess.call(['yum','update','all'])

update_cache(family)

def install_tools()
    if subprocess.call(['yum','list','installed'])

def get_requirements():
    



def 
    
    


    