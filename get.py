
import json
import time

import requests


def getAll(gu):
    link=""
    headers = gu
    payload=None
    jsonl=[]
    endid=0
    with open("hide.txt","r") as f:
        link=f.read()
    while True:
        response0 = requests.request("GET", link+str(endid), headers=headers, data=payload)
        rjson=json.loads(response0.content)
        for i in rjson["data"]["list"]:
            jsonl.append(i)
        endid=jsonl[-1]["id"]
        time.sleep(0.01)
        if rjson["data"]["list"]==[]:
            break
        
    with open("./角色活动.json","w",encoding="utf-8") as f:
        f.write(json.dumps(jsonl))

    jsonl=[]
    endid=0
    while True:
        response0 = requests.request("GET", link+str(endid), headers=headers, data=payload)
        rjson=json.loads(response0.content)
        for i in rjson["data"]["list"]:
            jsonl.append(i)
        endid=jsonl[-1]["id"]
        time.sleep(0.01)
        if rjson["data"]["list"]==[]:
            break
        
    with open("./常驻.json","w",encoding="utf-8") as f:
        f.write(json.dumps(jsonl))

    jsonl=[]
    endid=0
    while True:
        response0 = requests.request("GET", link+str(endid), headers=headers, data=payload)
        rjson=json.loads(response0.content)
        for i in rjson["data"]["list"]:
            jsonl.append(i)
        endid=jsonl[-1]["id"]
        time.sleep(0.01)
        if rjson["data"]["list"]==[]:
            break
        
    with open("./光锥.json","w",encoding="utf-8") as f:
        f.write(json.dumps(jsonl))