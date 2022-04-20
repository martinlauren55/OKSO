# Среднее объединяем в одну кучу
# Высшее делим на Уровни

# Среднее =51, 52
# Высшее БАКАЛАВР = 62
# Высшее СПЕЦИАЛИТЕТ = 65
# Высшее МАГИСТР = 68


spec_file = open("4_speci.txt", encoding="utf-8")
spec = spec_file.read()
spec_file.close()

for row in spec.split("\n"):
    code = row.split('#')[0]
    name = row.split('#')[1]
    level = row.split('#')[2]
    if level == "51" or level == "52":
        level = "CL"
    elif level == "62":
        level = "BA"
    elif level == "68":
        level = "MA"
    elif level == "65":
        level = "SP"
    print(f"code:{code} name:{name} level_old: {row.split('#')[2]} level: {level}")
