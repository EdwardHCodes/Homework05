# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:25:32 2020

@author: Edward
"""


import requests
import json

def gitHub_API(user_Name):
    response = requests.get("https://api.github.com/users/"+user_Name+"/repos")

    response = response.json()

    if len(response) == 0:
        print("No Repos")
        return False

    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = repoResponse.json()
        print("Repo: "+ repo['name'] + " \nNumber Of commits: " + str(len(repoResponse)))

    return True
if __name__ == "__main__":
    user_Input = input("Enter GitHub ID/Username: ")
    gitHub_API(user_Input)