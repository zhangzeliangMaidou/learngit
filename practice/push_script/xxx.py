#!/usr/bin/env python
# -*- utf-8 -*-

import os
import time

from xml.dom.minidom import parse
import xml.dom.minidom

project_name_git_command_dict = {}
project_name_path_dict = {}

def get_project_name():
    f = open("untitled.txt", "r")
    lines = f.readlines()
    for line in lines:
        project_name = ""
        if "com:29418" in line:
            project_name = [name for name in line.split("com:29418")][1]
            if "revision" in project_name:
                project_name = project_name.split(" revision")[0]
            if "\n" in project_name:
                project_name = project_name[:-1]
            if '"' in project_name:
                project_name = project_name[:-1]
            if "HEAD" in project_name:
                project_name = project_name.split(" HEAD")[0]
            project_name_git_command_dict[project_name[1:]] = line
    f.close()

def read_manifest_file():
    dom = xml.dom.minidom.parse("manifest.xml")
    root = dom.documentElement
    project_list = root.getElementsByTagName("project")
    for project in project_list:
        name = ""
        path = ""
        if project.hasAttribute("name"):
            name = project.getAttribute("name")
            if project.hasAttribute("path"):
                path = project.getAttribute("path")
            else:
                path = name
        project_name_path_dict[name] = path

def push_file(path,command):
    os.chdir(path)
    result = os.popen(command)
    while True:
        line = result.read()
        if "XXXX" in line:
            break
count = 0
def main():
    global count
    get_project_name()
    read_manifest_file()
    project_name_path_dict_name_list = project_name_path_dict.keys()
    for name in project_name_git_command_dict.keys():
        if name in project_name_path_dict_name_list:
            path = project_name_path_dict.get(name)
            push_file(path,project_name_git_command_dict.get(name))
            count += 1

if __name__ == "__main__":
    main()
    print(count)









