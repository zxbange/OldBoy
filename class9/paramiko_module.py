import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不再know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname="192.168.50.11", port=22, username="root",
            password="passwd")

# 执行命令
stdin, stdout, stderr = ssh.exec_command("df")

# 获取结果
# result = stdout.read()
res, err = stdout.read(), stderr.read()
result = res if res else stderr
print(result.decode())

ssh.close()