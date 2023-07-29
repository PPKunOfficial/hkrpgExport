import json
import requests


class ssrCore:
    apis = {
        "index": "https://api-takumi-record.mihoyo.com/game_record/app/hkrpg/api/index",
    }
    class Api:
        def GetIndex(UserInformation):
            headers = UserInformation["User"]
            payload = None
            response0 = requests.request(
                "GET",
                ssrCore.apis["index"]
                + "?role_id="
                + UserInformation["uid"]
                + "&server="
                + UserInformation["server"],
                headers=headers,
                data=payload,
            )
            return json.loads(response0.content.decode("utf-8")) 
    class File:
        def ReadDataFromFile(Path):
            with open(Path, "r") as f:
                context = f.read()
            CtoJson = json.loads(context)
            return CtoJson
