num01 = int(input(''))
num02 = int(input(''))

temp = "{num01} + {num02} = {sum}"

result = temp.format(num01=num01,num02=num02, sum=num01 + num02)

print("Natija: ", result)


