import paramiko
import sys
import logbook
#sys.stdout = open('log.txt', 'w')

logbook.StreamHandler(paramiko).push_application()

def get_user_password(path):
    
    lines = open(path).readlines()
    ips = False
    
    for line in lines:
        if not ips:
            if "user" in line:
                x_list = line.replace(" ","").replace("\n","").split("=")
                user = x_list[1]
            if "pass" in line:
                x_list = line.replace(" ","").replace("\n","").split("=")
                password = x_list[1]
            else:
                pass
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
            try:
                par_ordenado = [x_list[0],int(x_list[1])]
            except:
                par_ordenado = [x_list[0],3]
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
print(f"\n  User, password: {user}, {password}")


ip_list = get_dic_ips('ips.txt')
print("\nip_list: ", ip_list, "\n\n-------------------------------------\n")

for ip in ip_list:
    print("[  HOST |  #Trys ]")
    print(ip)
    print('---------------------')
    host = ip[0]

    for i in range(0,ip[1]):
        try:
            print(f'[{host}]log-in try #{i+1}')
            ssh_login(host, user, password)
        except:
            pass


wait = input('\n\n-------------------------------------\n----end---Press enter to close:    ')
sys.stdout.close()
sys.exit()