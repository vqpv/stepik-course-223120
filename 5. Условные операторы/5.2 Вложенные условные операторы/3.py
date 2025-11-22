y, m, d = input().split("-")

new_m = ""

if m == "01":
    new_m = "января"
elif m == "02":
    new_m = "февраля"
elif m == "03":
    new_m = "марта"
elif m == "04":
    new_m = "апреля"
elif m == "05":
    new_m = "мая"
elif m == "06":
    new_m = "июня"
elif m == "07":
    new_m = "июля"
elif m == "08":
    new_m = "августа"
elif m == "09":
    new_m = "сентября"
elif m == "10":
    new_m = "октября"
elif m == "11":
    new_m = "ноября"
elif m == "12":
    new_m = "декабря"

print("{} {} {}".format(d, new_m, y))
