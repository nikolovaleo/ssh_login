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

#username, password = get_user_password("ips.txt")

def ssh_login():

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('tty.sdf.org', username=username, password=password)


    host = "tty.sdf.org"
    username = "nikolov"
    password = "mHfYoQEg5iyStw"


    ssh(host, cmd, user, password, timeout=30, bg_run=False)
    ssh_in, ssh_out, ssh_err = ssh.exec_command('ss -ltn')
    print(ssh_in, ssh_out, ssh_err)

ssh_login()

sys.exit()