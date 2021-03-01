#for i in `ls -ld */ |awk '{print $10}'`; do cd $i; pwd;cd ..; done



import subprocess

def check_package_installation():
    subprocess.call('yum list installed|grep vim  >>)
