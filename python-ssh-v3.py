import paramiko

class connection_class:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        
    def ip_check(func):
        def wrapper(self, command):
            try:
                self.stdin, self.stdout, self.stderr = self.ssh.exec_command("ip a | grep enp0s3 | tail -n 1 | awk '{print $2}'")
                print(f"Output of 'ip cmd ':\n{self.stdout.read().decode()}")
                if self.stderr.read():
                    print(f"Error executing 'ip cmd':\n{self.stderr.read().decode()}")
            except Exception as e:
                print(f"Failed to execute command 'ip cmd': {e}")
            print("This is inside and last part of decorator")
            result = func(self, command)
            return result
        return wrapper

    def ssh_connect(self):
        print(self.host)
        try:
            # Create an SSH client
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the host
            self.ssh.connect(hostname=self.host, username=self.username, password=self.password)
            print(f"Successfully connected to {self.host}")
        
        except Exception as e:
            print(f"Failed to connect to {self.host}: {e}")
    @ip_check
    def command_execution(self, command):
        self.user_input = input("Enter some junk: ")
        print(self.user_input)
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            print(f"Output of '{command}':\n{stdout.read().decode()}")
            self.ssh.close()
            if stderr.read():
                print(f"Error executing '{command}':\n{stderr.read().decode()}")
        except Exception as e:
            print(f"Failed to execute command '{command}': {e}") 

if __name__ == "__main__":
    conn = connection_class("192.168.1.10", "root", "Ubs@122628")
    conn.ssh_connect()
    output = conn.command_execution("uname -a")