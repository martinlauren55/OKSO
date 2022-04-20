
def splitter(value):
    if len(value) == 6:
        f = value[0:2]
        s = value[2:4]
        e = value[4:6]
        res = f"{f}.{s}.{e}"
        return res
    else:
        pass


spec_file = open("1_from_exel.txt", encoding="utf-8")
spec = spec_file.read()
spec_file.close()

for row in spec.split("\n"):
    old_row = row.split("@")
    col1 = splitter(old_row[0])
    old_row[0] = col1
    line = ""
    for r in old_row:
        line = line + "#" + str(r)
    print(line)
    with open("2_specialty_dots.txt", "ab+")as f:
        f.write(bytes(line + '\n', 'utf8'))