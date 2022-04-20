spec_file = open("2_specialty_dots.txt", encoding="utf-8")
spec = spec_file.read()
spec_file.close()

for row in spec.split("\n"):
    old_row = row[1:]
    print(old_row)
    with open("3_specialty_with_dots.txt", "ab+")as f:
        f.write(bytes(old_row + '\n', 'utf8'))