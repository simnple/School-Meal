import json
import requests

KEY = "YOURKEY"

SCHUL_NM = input("학교이름 > ")
MLSV_YMD = input("날짜 > ")

def get_school(KEY, SCHUL_NM):
    # 학교정보 불러오기
    url = f"https://open.neis.go.kr/hub/schoolInfo?KEY={KEY}&Type=json&SCHUL_NM={SCHUL_NM}"
    req = requests.get(url)
    j = json.loads(req.text)

    global ATPT_OFCDC_SC_CODE
    global SD_SCHUL_CODE

    ATPT_OFCDC_SC_CODE = j["schoolInfo"][1]["row"][0]["ATPT_OFCDC_SC_CODE"]
    SD_SCHUL_CODE = j["schoolInfo"][1]["row"][0]["SD_SCHUL_CODE"]
    #print(f"{ATPT_OFCDC_SC_CODE}, {SD_SCHUL_CODE}")

def get_meal(KEY, ATPT_OFCDC_SC_CODE, SD_SCHUL_CODE, MLSV_YMD):
    # 학교급식 불러오기
    r = requests.get(url=f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&MLSV_YMD={MLSV_YMD}")

    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={KEY}&Type=json&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&MLSV_YMD={MLSV_YMD}"

    req = requests.get(url)
    j = json.loads(req.text)

    meal = j["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
    result = meal.replace("<br/>","\n")

    print(result)

get_school(KEY, SCHUL_NM)
get_meal(KEY, ATPT_OFCDC_SC_CODE, SD_SCHUL_CODE, MLSV_YMD)