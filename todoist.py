#!/usr/bin/env python
# encoding:utf8

import todoist
import requests
import json
import re
import argparse

import config
from printHandler import printList, printError


def getProjectID(button):
    if button == 1:
        project = getProjectInfo(config.projects["id1"])
        tasks = getTasks(config.projects["id1"])

        printList(config.projects["id1"], project, tasks)

    elif button == 2:
        project = getProjectInfo(config.projects["id2"])
        tasks = getTasks(config.projects["id2"])

        printList(config.projects["id2"], project, tasks)

    elif button == 3:
        project = getProjectInfo(config.projects["id3"])
        tasks = getTasks(config.projects["id3"])

        printList(config.projects["id3"], project, tasks)


def getProjectInfo(project_id):
    response = requests.get(config.todoist["project_endpoint"] + project_id)
    if response.status_code == 200:
        res_dict = response.json()

        return res_dict.name
    else:
        print("Error code: ")
        print(response.status_code)
        printError(response.status_code)


def getTasks(project_id):
    response = requests.get(
        config.todoist["tasks_endpoint"] + "project_id=" + project_id + "&filter=today"
    )
    if response.status_code == 200:
        res_dict = response.json()

        return(res_dict)
    else:
        print("Error code: ")
        print(response.status_code)
        printError(response.status_code)
