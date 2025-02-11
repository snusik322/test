def file_analiz(file):
    res = {}
    with open(file, "r") as failik:
        for line_number, line in enumerate(failik,start=1):
            res[line_number] = len(line.rstrip())
    return res

a = file_analiz("test.txt")
print(f"Справочник: {a}")

print(f"Шифр: {" ".join(map(str,a.values()))}")

