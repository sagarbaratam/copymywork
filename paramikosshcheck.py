import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('ptl12ugcapp102-m.bby', username='sbaratam', key_filename='/Users/a1455121/.ssh/id_rsa-cert.pub')

stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.readlines())
ssh.close()