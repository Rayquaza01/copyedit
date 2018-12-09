#!/usr/bin/env python3
import pyperclip
import os
import sys
import json
import time
import subprocess
import shlex


def readFile(file):
    with open(file, "r") as f:
        return f.read()


def writeFile(file, contents):
    with open(file, "w") as f:
        f.write(contents)


def configExists(name):
    homefile = os.path.join(os.path.expanduser("~"), name)
    if os.path.exists(name):  # if file in current folder
        return name
    elif os.path.exists(homefile):  # if file in home folder
        return homefile
    else:  # file not found
        return False


if __name__ == "__main__":
    configFile = configExists("copyedit.json")
    if not configFile:  # download config file if does not exist
        configFile = os.path.expanduser("~/copyedit.py")
        import urllib.request
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Rayquaza01/copyedit/master/copyedit.json", configFile)
        print("Downloaded sample config file to {0}".format(configFile))
    config = json.loads(configFile)
    now = time.strftime("%Y%m%d%H%M%S")  # year, month, day, hour, minutes, seconds; used for file name
    storagedir = os.path.expanduser(config["directory"])  # dir to store files in
    if not os.path.exists(storagedir):  # create dir if doesn't exist
        os.mkdir(storagedir)
    extension = input("File Extension (blank for {0}): ".format(config["default_extension"]))  # get file extension
    if extension == "":
        extension = config["default_extension"]
    file = os.path.join(storagedir, ".".join([now, extension]))
    writeFile(file, pyperclip.paste())  # create file with clipboard contents
    print("Created {0}".format(file))
    print("Opening file...")
    process = subprocess.Popen(shlex.split(config["editor"]) + [file])  # launch editor with file as argument
    process.wait()  # wait for editor to close
    pyperclip.copy(readFile(file))  # copy contents to clipboard
    print("Copied contents of {0} to clipboard".format(file))
    if config["delete_on_close"]:  # delete file if set to delete automatically
        os.remove(file)
        print("Deleted {0}".format(file))
    print("Done!")
