text = input("Matnni kiriting: ")
word = input("so'zni kiriting: ")
start = int(input("Qayerdan boshlab qidirilsin: "))

result = text.find(word, start)
print("Natija: ", result)
