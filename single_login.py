import paramiko
import sys

#sys.stdout = open('log.txt', 'w')
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

def get_dic_ips(path):
    lines = open(path).readlines()
    
    ips = False
    ip_list = []
    for line in lines:

        if "=====" in line:
            ips = True

        elif ips:
            x_list = line.replace(" ","").replace("\n","").split("\t")
            par_ordenado = [x_list[0],int(x_list[1])]
            ip_list.append(par_ordenado)
    return ip_list


def ssh_login(host, user, passwd):
    #paramiko.transport.Transport._preferred_keys += ('ssh-dss',)
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)

    if ssh.get_transport() is not None:
        print(ssh.get_transport().is_active())



    ssh_in, ssh_out, ssh_err = ssh.exec_command('en')
    print(ssh_in, ssh_out, ssh_err)


user, password = get_user_password('ips.txt')

host = "192.168.13.1"
user = "root"
password = "wdpf"


ssh_login(host, user, password)



wait = input('---------')
sys.stdout.close()
sys.exit()