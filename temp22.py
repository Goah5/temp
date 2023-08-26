def qazwsx(uid):
    uid = str(uid)
    with open("users.txt", "r") as file:
        for f in file.readlines(1):
            if uid in f.split()[0]:
                return int(f.split()[1])
print(qazwsx(4))