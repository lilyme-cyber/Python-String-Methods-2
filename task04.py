day = input("Hafta kunini kiriting: ")
hour = input("Soatni kiriting: ")

template = "Bugun {day} kuni, dars soat {hour} da!"

result = template.format(day=day, hour=hour)

print("Natija: ", result)