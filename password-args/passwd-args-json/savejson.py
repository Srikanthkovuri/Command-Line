"""This module has function for storing 
and retrieving password
"""
import os
import json
from cryptography.fernet import Fernet

PASS_FILE = 'passwd.secret'

def load_file():
    """Loads existing records

    Returns:
        dict:loaded records from a file
    """
    with open(PASS_FILE,'r',encoding='utf16') as file:
        return json.load(file)

secret_dict=load_file()

def load_key(key_file='passwd.key'):
    """This function will load the key

    Args:
        key_file (str, optional):key file name. Defaults to 'passwd.key'.

    Returns:
        String: returns key value in binary format
    """
    return open(key_file,'rb').read()
        
def get_key(key_file='passwd.key'):
    """This function will get the key

    Args:
        key_file (str, filename): Key file name. Defaults to 'passwd.key'.
    """
    if not os.path.exists(key_file):
        key=Fernet.generate_key()
        with open(key_file,'wb') as file:
            file.write(key)
    key=load_key(key_file)
    return key

def encrypt(plain_msg):
    """This will encrypts the message

    Args:
        plain_msg (String): text
    """
    key=get_key()
    fer_obj=Fernet(key)
    cipher_byte=fer_obj.encrypt(plain_msg.encode())
    cipher_text=cipher_byte.decode('utf16')
    return cipher_text

def decrypt(cipher_msg):
    """It will decrypt the encrypted text

    Args:
        cipher_msg (string): encrypted text
    """
    key=get_key()
    fer_obj=Fernet(key)
    cipher_byte=cipher_msg.encode('utf16')
    return fer_obj.decrypt(cipher_byte).decode()

def save_pass(service,username,password):
    """This function will save password in a .txt file

    Args:
        service (string): specific service name00
        username (string): username
        password (string): password of an user
    """
    # saving in a file with encrytion in json format
    secret_dict[service]={
        'username':encrypt(username),
        'password':encrypt(password)
    }
    with open(PASS_FILE,mode='w',encoding='utf16') as file:
        json.dump(secret_dict,file,indent=4)

def view_pass(ser_name):
    """This function will show user,passwd

    Args:
        ser_name (string): specific service name
    """
    # retrieving contents from an encrypted json format file
    if ser_name not in secret_dict:
        raise ValueError("service you entered was incorrect")
    username=decrypt(secret_dict[ser_name]['username'])
    password=decrypt(secret_dict[ser_name]['password'])
    
    return (username,password)
