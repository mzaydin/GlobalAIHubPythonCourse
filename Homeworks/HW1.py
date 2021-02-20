# 3x3 matrise asal sayı atama

#Question 1 ; Day 2
matris = [[0,0,0],[0,0,0],[0,0,0]]
x = -1
for sayi in range(2,100):
    for i in range(2,sayi-1):
        if sayi%i !=0 & sayi != i:
            x += 1
            if x<3: # 0 1 2
                matris[0][x] = sayi
            elif 2<x<6: # 3 4 5
                matris[1][x-3] = sayi
            elif 5<x<9: # 6 7 8
                matris[2][x-6] = sayi
            else:
                break
        break
print(matris)
