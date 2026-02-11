import os
def run_bash_cmd(some_choice):
    """
    A function that utilizes the os library to run bash commands without the user inputting them.
    Implemented in a menu system, a user input corresponds to a bash command
    
    :param some_choice: the user's choice from the menu system
    """
    print('-' * 80, '\n')
    print(f'You entered #{some_choice}')
    match some_choice:
        case 1:
            print('The available memory is ')
            os.system('free -tmh')
            print('-' * 80, '\n')
        case 2:
            print('The current network connections include: ')
            os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
            print('-' * 80, '\n')
        case 3:
            print('Available file space is: ')
            os.system('df -h | grep \"Filesystem\|root\"')
            print('-' * 80, '\n')
    return