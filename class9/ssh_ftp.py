import paramiko

transport = paramiko.Transport(("192.168.50.11", 22))
transport.connect(username="root", password="passwd")

sftp = paramiko.SFTPClient.from_transport(transport)
# 将multipro.py 上传至服务器 /tmp/test.py

sftp.put("D:\\multipro.py", "/tmp/test.py")

# 将remove_path  下载到本地 local_path
sftp.get("remove_path", "local_path")

transport.close()