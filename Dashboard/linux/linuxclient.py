import paramiko
from scp import SCPClient
import os
from pathlib import Path

qa_x_server = "lxqa3451"
prod_x_server = "lxqa5421"
prod_xyz_server = "lxqa2455"
#

dquote = '"'
shebang = "#!/bin/bash"
askpass = "/u/home/whoisthis/temp.sh"

host = prod_xyz_server

# ****

port = 22
username = "whowho"
# username = "sysplot"
password = "dösdlmfösldf"

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def connect():
    try:
        ssh.connect(host, port, username, password)
    except Exception as e:
        print("linuxclient ssh exception!")
        print(str(e))

       
def close():
    ssh.close()
        

def command_list_runner(command_list):
    command_iterator = iter(command_list)
    exit_status = 0
    while exit_status == 0:
        try: 
            command = next(command_iterator)
            stdin, stdout, stderr = ssh.exec_command(command)
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                msg = stdout.read().decode('utf-8').strip()
            else:
                print(f"Command '{command}' failed with exit status {exit_status}.")
                msg = stderr.read().decode()
                print("Error:\n", msg)
                return -1, msg
        except StopIteration:        
            return 0, msg
            # break
        except Exception as e:     
            msg = str(e)
            print(msg)
            return -99, msg    
        
def text_runner(text):
    stdin, stdout, stderr = ssh.exec_command(text)
    # Read the output
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    print("sysout:")
    print(output)
    print("syserr:")
    print(error)
    
            
def sudo_heredoc_runner(heredoc, otheruser):
    commands = f"""
echo {dquote}{shebang}{dquote} > '{askpass}'
echo 'echo {dquote}{password}{dquote}' >> '{askpass}'
chmod +x '{askpass}'
export SUDO_ASKPASS='{askpass}'
export DISPLAY=:0
sudo -A su - {otheruser} <<EOF
{heredoc}
exit
EOF
rm '{askpass}'
cd $HOME
pwd
"""
    
    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(commands)
    stdin.write(password + '\n')
    stdin.flush()
    
    # Read the output
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    print("sysout:")
    print(output)
    print("syserr:")
    print(error)
        
        
def scp_download(remote_path, local_path):
        scp = SCPClient(ssh.get_transport())
        # Download the directory recursively
        scp.get(remote_path, local_path, recursive=True)
        scp.close()


def sftp_download_transport(remote_path, local_path, filelist):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get_channel().settimeout(300)  # 5 minutes timeout
        # for file in filelist[:10]:
        for file in filelist:
            remote_file = remote_path + "/" + file
            local_file = local_path + "/" + file
            file_attr = sftp.stat(remote_file)
            print(f"Downloading: {remote_file}")
            sftp.get(remote_file, local_file, prefetch=True)
        sftp.close()
        transport.close()
    except Exception as e:
        print(f"Connection error: {str(e)}")        


def get_filtered_filelist():
    remotepath = r'/app/dominic/wilkins/somepath'
    ftype = 'prefix'
    fvalue = 'TENNIS_2024'
    command_list = []
    if ftype == "prefix":
        command_list.append(f"cd {remotedir} && ls -1 {fvalue}* ")  
    
    if ftype == "suffix":
        command_list.append(f"cd {remotedir} && ls -1 *{fvalue} ")  
        
    rc, msg = command_list_runner(command_list)
    print(f">>>{msg}<<<")
    filepath = r'C:\roger_federer\filelist.txt'
    f = open(filepath, "w+", encoding='UTF-8', newline='\n') # newline='\n' if you don't want CRLF
    f.write(str(msg) + '\n')
    f.close
    filelist = msg.splitlines()
    print(str(len(filelist)))
    last = len(filelist) - 1
    print(filelist[0])
    print(filelist[last])
    return filelist


def get_filtered_filelist_otheruser():
    connect()
    remotedir = r'/app/dominic/wilkins/somepath'
    ftype = 'prefix'
    fvalue = 'TENNIS_2024'
    otheruser = 'privilaged_user'
    heredoc = f""" 
            cd {remotedir} && ls -1 {fvalue}*
            """
    sudo_heredoc_runner(heredoc, otheruser)
    close()

def sftp_download():
    connect()
    remote_path = r'/app/dominic/wilkins/somepath'
    local_path = Path(r'C:\carlos\moya\wimbledon')
    listfile = Path(r'C:\boris\matchlist.txt')
    file = open(listfile, "r")
    filelist = file.read().split('\n')
    file.close()
    
    try:
        ssh.load_system_host_keys()
        sftp = ssh.open_sftp()
        sftp.get_channel().settimeout(300)  # 5 minutes timeout
        
        # Download each file
        # for file in filelist[:10]:
        for file in filelist:
            remote_file = remote_path + "/" + file
            local_file = local_path.joinpath(file)
            file_attr = sftp.stat(remote_file)
            print(file_attr)                
            print(f"Downloading: {remote_file}")
            # sftp.get(remote_path, local_path, prefetch=True)
            sftp.get(remote_file, local_file)
    except Exception as e:
        print(f"Connection error: {str(e)}")
    finally:
        sftp.close()


def sftp_upload():
    connect()
    inputdir = Path(r'C:\carlos\alcaraz\winners\archive\upload\files')
    remotedir = r'/u/jcferrero/temp'
    listfile = Path(r'C:\carlos\alcaraz\winners\archive\upload\uploadlist.txt')
    file = open(listfile, "r")
    filelist = file.read().split('\n')
    file.close()
    
    try:
        ssh.load_system_host_keys()
        sftp = ssh.open_sftp()
        sftp.get_channel().settimeout(300)  # 5 minutes timeout
        sftp.stat(remotedir)
        for file in filelist:
            local_file  = inputdir.joinpath(file)
            remote_file  = f"{remotedir}/{file}"
            print(f"Uploading: {local_file}")
            sftp.put(local_file, remote_file)                
    except Exception as e:
        print(f"Connection error: {str(e)}")
    finally:
        sftp.close()
    close()

def copy_or_move():
    connect()
    sourcedir = r'/u/someuser/players/'
    targetdir = r'/app/tennisdb/players/'
    heredoc = f"""
            cp {sourcedir}*.xml {targetdir}
            """
    otheruser = 'privilaged_user'        
    sudo_heredoc_runner(heredoc, otheruser)
    close()
    
def add_permission():
    connect()
    parent1 = f"/app/tennisdb"
    parent2 = f"/matches"
    parent3 = f"/done"
    files = f"/2024_clay_*.xml"
     
    heredoc = f"""
            chmod o+rx {parent1}
            chmod o+rx {parent1}{parent2}
            chmod o+rx {parent1}{parent2}
            chmod o+rx {parent1}{parent2}{parent3}
            chmod o+rx {parent1}{parent2}{parent3}{files}
            """

    text_runner(heredoc)
    # or 
    # otheruser = 'privilaged_user'                
    # sudo_heredoc_runner(heredoc, otheruser)
    close()
    
    
def remove_permission():
    heredoc = f"""
            chmod o-rwx {files}
            chmod o-x {parent3}
            chmod o-x {parent2}
            chmod o-x {parent1}
            """
    
    otheruser = 'privilaged_user'        
    sudo_heredoc_runner(heredoc, otheruser)


def see_permission():
    # Show all .txt files
    # ls -l *.txt

    # Show all files starting with 'test'
    # ls -l test*

    # Show all .jpg and .png files
    # ls -l *.{jpg,png}

    # Show all files starting with 'data' and ending in .csv
    # ls -l data*.csv
    
    # First .txt file in directory
    # ls -l *.txt | head -n1

    connect()
    parent1 = f"/app/tennisdb"
    parent2 = f"/matches"
    parent3 = f"/done"
    files = f"/2024_clay*.xml"
    
            # ls -ld {parent1}
            # ls -ld {parent1}{parent2}
            # ls -ld {parent1}{parent2}{parent3}
    heredoc = f"""
            ls -l {parent1}{parent2}{parent3}{files}
            ls -l {parent1}{parent2}{parent3}{files} | wc -l
            """
    heredoc = f"""
            grep -rl RELEASED  /app/t613vcom/send_to_kola_files/done --include=SMARTEAM_20241114* | xargs grep item
            """
    otheruser = 'privilaged_user'        
    sudo_heredoc_runner(heredoc, otheruser)
    close()

def delete_files(): 
    connect()
    remote_path = r'/app/tennisdb/temp'
    listfile = Path(r'C:\tennisdb\deletelist.txt')
    file = open(listfile, "r")
    filelist = file.read().split('\n')
    file.close()
    for file in filelist:
        remote_file  = f"{remote_path}/{file}"
        heredoc = f"""
            rm -f {remote_file}
            """
        otheruser = 'privilaged_user'        
        sudo_heredoc_runner(heredoc, otheruser)
    close()
    
    
if __name__ == "__main__":
    

    # get_filtered_filelist_otheruser()
    # sftp_upload()
    see_permission()
    # add_permission()
    # copy_or_move()
    # sftp_download()
    # delete_files()
    
    

    
#User categories
# u = owner
# g = group
# o = others
# a = all (same as ugo)

#Operators
# + = add permission
# - = remove permission
# = = set exact permission

#Examples
# chmod u+x file      # Add execute for owner
# chmod g-w file      # Remove write for group
# chmod o=r file      # Set others to read-only
# chmod a+rx file     # Add read+execute for all
# chmod ug=rw file    # Set user and group to read+write    
    