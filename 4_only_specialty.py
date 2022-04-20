spec_file = open("3_specialty_with_dots.txt", encoding="utf-8")
spec = spec_file.read()
spec_file.close()

for row in spec.split("\n"):
    if 'None' in row:
        pass
    else:
        print(row)
        with open("4_speci.txt", "ab+")as f:
            f.write(bytes(row + '\n', 'utf8'))