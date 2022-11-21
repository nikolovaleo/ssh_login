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
    ssh.connect(host, username=user, password=passwd)

    
    ssh_in, ssh_out, ssh_err = ssh.exec_command('ss -ltn')
    print(ssh_in, ssh_out, ssh_err)


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





            







user, password = get_user_password('ips.txt')
ip_list = get_dic_ips('ips.txt')
print(ip_list)

for ip in ip_list:
    print(ip)
    host = ip[0]

    for i in range(0,ip[1]):
        try:
            ssh_login(host, user, password)
        except:
            pass




wait = input()
sys.exit()