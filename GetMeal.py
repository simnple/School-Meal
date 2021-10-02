import json
import requests

global KEY
KEY = "YOUR_KEY" # 키가 없으면 실행하지 못합니다.

# 학교정보 불러오기
def get_school(School_Name):
    # 정보 요청
    url = f"https://open.neis.go.kr/hub/schoolInfo"
    params = {
        "KEY": KEY,
        "Type": "json",
        "SCHUL_NM": School_Name
    }
    req = requests.post(url, params=params)

    # 정보 처리
    j = json.loads(req.text)

    # 정보가 존재 할때
    try:
        Area_Code = j["schoolInfo"][1]["row"][0]["ATPT_OFCDC_SC_CODE"]
        School_Code = j["schoolInfo"][1]["row"][0]["SD_SCHUL_CODE"]

        return Area_Code, School_Code
    
    # 정보가 존재하지 않을때
    except:
        print(j["RESULT"]["MESSAGE"])
        input()
        exit()

# 학교정보 불러오기
def get_meal(ATPT_OFCDC_SC_CODE, SD_SCHUL_CODE, MLSV_YMD):
    # 정보 요청
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "KEY": KEY,
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": MLSV_YMD
    }
    req = requests.post(url, params=params)

    # 정보 처리
    j = json.loads(req.text)

    # 정보가 존재 할때
    try:
        meal = j["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
        result = meal.replace("<br/>","\n")

        return result
    
    # 정보가 존재하지 않을때
    except:
        print(j["RESULT"]["MESSAGE"])
        input()
        exit()
