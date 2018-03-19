import connexion
import six
from swagger_server.models.computer import COMPUTER  # noqa: E501
from swagger_server import util
from psutil import virtual_memory
import os, platform, subprocess, re


def get_CPU():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                CPU = re.sub(".*model name.*:", "", line, 1)
                return CPU
    return "cannot find cpuinfo"


def get_RAM():
    RAM = []
    RAM.append(str(round(virtual_memory().total/1024/1024/1024)))
    RAM.append('G')
    RAM = ''.join(RAM)
    return RAM


def get_OS():
    OS = platform.system()
    return OS 


def computer_get():  # noqa: E501
    """computer_get

    Resturns computer information of the hosting server # noqa: E501


    :rtype: COMPUTER
    """
    return COMPUTER(get_CPU(), get_RAM(), get_OS())
