import paramiko
from os import os.system as call 
from logs import logger

class ssh:
    def scp_upload(self,localfile,remoteserver,destinationfile):
        logger().log("Uploading {} to {} at {} ".format(localfile,remoteserver,destinationfile))
        call('scp "%s" "%s:%s"' % (localfile,remoteserver,destinationfile))
        return

    def scp_download(self,remoteserver,destinationfile,localfile):
        logger().log("Downloading {} to {} at {} ".format(destinationfile,remoteserver,localfile))
        call('scp "%s:%s" "%s"' % (remoteserver,destinationfile,localfile))
        return
    
    def run_commad(self,server_hostname,command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_hostname, username=os.environ['SSHUSER'], key_filename=os.environ['SSHKEY'])
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.readlines()

    def get_jmphst_tunnel():



ssh = ssh()

#usage
#scp.scp_upload("paramikosshcheck.py","ptl11jmphst03.bby","/home/a1455121/sample.py")


        

        





#ssh = paramiko.SSHClient()

#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect('ptl12ugcapp102-m.bby', username='a1455121', key_filename='/Users/a1455121/.ssh/id_rsa-cert.pub')

#stdin, stdout, stderr = ssh.exec_command('ls')
#print (stdout.readlines())
#ssh.close()

