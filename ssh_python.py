
import paramiko

hostname = "192.168.1.101"
username = "test"
password = "abc123"

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
	stdin, stdout, stderr = client.exec_command(command)
	print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()