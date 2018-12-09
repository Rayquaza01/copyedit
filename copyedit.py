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


if __name__ == "__main__":
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    config = json.loads(readFile(os.path.join(cwd, "config.json")))
    now = time.strftime("%Y%m%d%H%M%S")  # year, month, day, hour, minutes, seconds; used for file name
    storagedir = os.path.expanduser(config["directory"])  # dir to store files in
    if not os.path.exists(storagedir):  # create dir if doesn't exist
        os.mkdir(storagedir)
    extension = input("File Extension (blank for {}): ".format(config["default_extension"]))  # get file extension
    if extension == "":
        extension = config["default_extension"]
    file = os.path.join(storagedir, ".".join([now, extension]))
    print("Creating {}".format(file))
    writeFile(file, pyperclip.paste())  # create file with clipboard contents
    print("Opening file...")
    process = subprocess.Popen(shlex.split(config["editor"]) + [file])  # launch editor with file as argument
    process.wait()  # wait for editor to close
    print("Copying {} to clipboard".format(file))
    pyperclip.copy(readFile(file))  # copy contents to clipboard
    if config["delete_on_close"]:  # delete file if set to delete automatically
        print("Deleting {}".format(file))
        os.remove(file)
    print("Done!")
