
import platform
import subprocess
from subprocess import check_output, CalledProcessError, STDOUT

packages = ['ansible','docker','molecule']
version={'ansible':'2.10.4','docker':'19.03.5','molecule:'2.4'}

apt_update='apt get update'
apt_update='apt list --installed'
yum_update='yum update'
yum_list='yum list installed'
yum_install='yum install -y'
apt_install='apt install -y '


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
        subprocess.call(apt_update)
    elif family == redhat or centos:
        subprocess.call(yum_update)

update_cache(family)

def install_tools()
    if family == redhat or centos:
        subprocess.call(yum_update)
        if package in check_output(yum_list).split("\n"):
            print(package+ "is alrealy installed")
        else:
            install(package)
install_tools()

def install_command():
    if family == redhat or centos:
        

          



def get_requirements():
    



def 
    
    


    