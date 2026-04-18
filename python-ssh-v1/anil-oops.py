import paramiko

# Replace with your VM details
hostname = ["192.168.11.101", "192.168.1.10"]  # e.g., "20.55.123.45"
port = 22
username = ["anil", "root"]       # e.g., "azureuser"
password = ["passwd", "Ubs@122628"]       # VM login password

class SSHClient:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
        

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode()

    def close(self):
        self.ssh.close()


if __name__ == "__main__":
    for i in range(len(hostname)):
        connection1 = SSHClient(hostname[i], port, username[i], password[i])
        try:
            connection1.connect()
        except Exception as e:
            print(f"Error connecting to {hostname[i]}")
            continue
        output = connection1.execute_command("uname -a")
        print(output)
        connection1.close()