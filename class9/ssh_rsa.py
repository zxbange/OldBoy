import paramiko

private_key = paramiko.RSAKey.from_private_key("id_rsa")  # 填入私钥文件名

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="192.168.50.11", port=22, username="root", pkey=private_key)

stdin, stdout, stderr = ssh.exec_command("df")

result = stdout.read()

print(result.decode())

ssh.close()

#  上传下载文件

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('192.168.50.11', 22))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()