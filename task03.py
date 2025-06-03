file = input("")
file_type = input("")

template = "Fayl: {file}.{file_type}"

result = template.format(file=file, file_type=file_type)

print("Natija: ", result)
