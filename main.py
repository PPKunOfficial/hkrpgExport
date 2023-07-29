import json
import excel,get

RuntimeData = {}
HadAvatar = []


def main():
    gu={}
    with open("gameu.json","r") as f:
        gu=json.loads(f.read())
    get.getAll(gu)
    excel.exportExcel()

main()