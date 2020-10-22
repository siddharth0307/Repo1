from netmiko import ConnectHandler as SSH
import time

my_machine = {
    'device_type': 'linux',
    'host':   '141.137.234.229',
    'username': 'root',
    'password': 'shroot'
    }


def remote_command(conn_dict, commands=[]):
    ssh = SSH(**conn_dict)
    prompt = ssh.find_prompt()
    print(prompt, end=" ")
    output = ""
    for cmd in commands:
        # print(cmd)
        ssh.write_channel(str(cmd) + "\n")
        time.sleep(1)
        output = ssh.read_channel()
        print(output, end="")

    ssh.disconnect()


if __name__ == '__main__':
    commands = ["ssh ms-1", "ssh -i /root/.ssh/vm_private_key cloud-user@svc-1-lvsrouter", "sudo su", "pwd", "ls -lrth", "exit", "exit"]
    remote_command(my_machine, commands)