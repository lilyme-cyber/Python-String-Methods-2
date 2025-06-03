name = input("Ismingizni kiriting: ")
age = input("Yoshingizni kiriting: ")

template = "Salom mening ismim {name} va yoshim {age} da!"

result = template.format(name=name, age=age)

print("Natija: ", result)