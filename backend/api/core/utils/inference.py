import requests

from typing import List

from core.setting import config
from schemas.recommend import RecommendCreate

def request_recommendation(userid: int, history_list: List[int], playtime: int) -> List[RecommendCreate]:
    user_history_data = {"userid": userid, "gameid_list": history_list, "playtime_forever": playtime}

    response = requests.post(config.infer.url, json=user_history_data)
    rec_list = response.json()["products"][0]["gameid_list"]
    # TODO delete user's recommend table and insert new rec_list
    new_rec_list = [RecommendCreate(userid=userid,gameid=gid) for gid in rec_list]
    return new_rec_list