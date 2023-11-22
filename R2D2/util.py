import os
import datetime
import logging
import platform
import config
import socket
def time():
    time = datetime.datetime.now()
    return time

def start():
    print('▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▉ ▉ ▊ ▉ ▊ ▉ ▊ ▊ ▊ ▋' +
          '\n__________БОТ_ЗАГРУЗИЛСЯ_____________' +
          '\n дата загрузки : ' + str(time()))

def host_name():
    mashine_name = socket.gethostname()
    return mashine_name

def mashine_ip():
    ip_addr = socket.gethostbyname(host_name())
    return ip_addr


def verni_logo():
    print("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:::::lkXW"
          "\nWMWWNNXXXXXNNWWMMMMMWNXXKKXNWWMMMMWNXXXXXXNNWWMMWWNNXNWWMWNNXNWMMWNXNWMMMMMMMMWWNXNWWWWNNX0kxxk0KXNW"
          "\nWNOolcccccccldKWWWXOdlc:::clxKWWW0dlcc:::ccldKWXkllccdXWKxlccxXNkolcoKWMMWMMWXkoccoKW0dlccxNN0dlccdX"
          "\nWk:,;;:dxo:;;,oXNkc;,;lxdc;;,c0W0c,;;:odl;;;,dKd;;;;;dXKl,;;;kXx;,;;oKWWWMMWNx;;;;oXKl,;,:kKx:,;;;xN"
          "\nXo;;;;cdxo:;;cOXx;;;;:oxxl;;;;xXd;;;;o00o;;;;xOc,;;;;ldl;;;,l00c,;;;:loodxKN0c,;,:kNx;;;;lxl;;;;,cKW"
          "\nO:,;;;cc:;;;:oKOc,;;;cllllllodK0l;;,;;::;;:lkKd;;;;;:c:;;;;;dXk:,;;:loc;;,cOx;,;,lKKl,;;;::c:;;;;dNM"
          "\nd;;;;lOKx:,;;;xOc,;;:xKKOdddd0Nk;;;,cxkkOOKNWKl,;,,:xXk:,;,:OXo;;,;dKKd;;,cxl,;;;xXk:,;;;:dxc;;,:OWM"
          "\nc,;,;:cc:;,;;oKXkc;;;:c:;,;cxXXo,;;:kNWWMMMMWk;,;;;oXNd;,,:xXO:,;,;:cc;,;ckk:,;;oKXo,,,;lOXx;,;;dNMM"
          "\nc:::::::::cokXWWN0oc:;;:clxKWWKl:clkNWWMMMMMNx:clxOKWXd::lkXNk::::::::clxKNk::cdKWKo:clxKWXd:clxXWMM")

def write_log(string):
    try:
        logging.info('\n'+str(time())+' '+string)
    except:
        print('Ошибка записи в лог')


def write_bug(string):
    try:
        logging.warning('\n'+str(time())+' '+string)
    except:
        print('Ошибка записи в лог')

def use_cmd(command):
    resp = os.popen(command)
    return resp

def get_os():
    my_os = str(platform.system())+' '+str(platform.machine())
    return my_os

def get_processor():
    proc_name = str(os.cpu_count())+'x '+str(platform.processor())
    return proc_name

def get_os_login():
    login = str(os.getlogin())
    return login

def write_file(string, path):
    f = open(path, 'a')
    f.write(string)
    f.close()

def read_file(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

def delite_file(path):
    os.remove(path)

def dir():
    dir = os.listdir(os.getcwd())
    return dir