import GetMeal

School_Name = input("학교이름 > ")
Area_Code, School_Code = GetMeal.get_school(School_Name)

Date = input("날짜 > ")
result = GetMeal.get_meal(Area_Code, School_Code, Date)

print(result)
input()