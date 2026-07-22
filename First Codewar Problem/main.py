attempts = []
ans = []
while True:
    a = input("First digit: ")
    b = input("Second digit: ")
    c = input("Third digit: ")
    d = input("Fourth digit: ")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    anse = ""
    if a == b and b == c and c == d:
        anse = "YES"
    else:
        anse = "NO"
    final = len(attempts) + 1
    attempts.append(final)
    ans.append(anse)
    choice = input("More? y/n: ")

    if choice == "y":
        continue
    elif choice == "Y":
        continue
    else:
        break
print("A.==========B.")
for i, e in zip(attempts, ans):
    print(f"{i}.          {e}.")
