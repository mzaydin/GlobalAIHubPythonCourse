word = str(input("kelime girin : "))

for i in range(len(word)):
    temp = str(input("tahmin edilen harf girin : "))
    if temp in word:
        print("buldun")