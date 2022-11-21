import paramiko
import sys
def get_user_password(path):

    lines = open(path).readlines()
    ips = False
    
    for line in lines:
        if not ips:
            if "user" in line:
                x_list = line.replace(" ","").replace("\n","").split("=")
                print(x_list)
                user = x_list[1]
            if "pass" in line:
                x_list = line.replace(" ","").replace("\n","").split("=")
                print(x_list)
                password = x_list[1]
            else:
                pass
    print(user, password)
    return user, password


def ssh_login(host, user, passwd):

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host=host, username=user, password=passwd)

    
    ssh_in, ssh_out, ssh_err = ssh.exec_command('ss -ltn')
    print(ssh_in, ssh_out, ssh_err)


user, password = get_user_password('ips.txt')
host = '192.168.13.1'

ssh_login(host, user, password)

sys.exit()