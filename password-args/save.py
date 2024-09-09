"""This module has function for storing 
and retrieving password
"""
PASS_FILE='passwd-file.txt'
def save_pass(service,username,password):
    """This function will save password in a .txt file

    Args:
        service (string): specific service name
        username (string): username
        password (string): password of an user
    """
    # saving in a file
    with open(PASS_FILE,mode='a',encoding='utf8') as file:
        file.write(f"{service}\t{username}\t{password}\n")

def view_pass(ser_name):
    """This function will show user,passwd

    Args:
        ser_name (string): specific service name
    """
    # retrieving contents
    with open(PASS_FILE,mode='r',encoding='utf8') as file:
        for lines in file.readlines():
            service,username,password=lines.split("\t")
            if service == ser_name:
                return (username,password)
    
    return None  #if nothing found