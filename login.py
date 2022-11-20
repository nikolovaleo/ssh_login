import paramiko
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

username = "nikolov"
password = "mHfYoQEg5iyStw"
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('tty.sdf.org', username=username, password=password)
