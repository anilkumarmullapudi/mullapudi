import paramiko

# Replace with your VM details
hostname = ["192.168.11.101", "192.168.1.10"]  # e.g., "20.55.123.45"
port = 22
username = ["anil", "root"]       # e.g., "azureuser"
password = ["passwd", "Ubs@122628"]       # VM login password

import paramiko
from concurrent.futures import ThreadPoolExecutor, as_completed

servers = [
    {"hostname": "192.168.11.101", "username": "anil", "password": "passwd"},
    {"hostname": "192.168.1.10", "username": "root", "password": "Ubs@122628"}
]

class SSHClient:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password
        )

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        self.ssh.close()


def run_command(server, command="uname -a"):
    connection = SSHClient(server["hostname"], 22, server["username"], server["password"])
    try:
        connection.connect()
        output, error = connection.execute_command(command)
        return server["hostname"], output, error
    except Exception as e:
        return server["hostname"], None, str(e)
    finally:
        connection.close()


if __name__ == "__main__":
    # Run commands in parallel across servers
    with ThreadPoolExecutor(max_workers=5) as executor:  # adjust workers as needed
        futures = [executor.submit(run_command, server) for server in servers]

        for future in as_completed(futures):
            hostname, output, error = future.result()
            print(f"\n--- {hostname} ---")
            if output:
                print(output)
            if error:
                print(f"Error: {error}")
