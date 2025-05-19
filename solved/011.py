# Completed on Sat, 5 Sep 2020, 11:20

line1 = [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
line2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00]
line3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
line4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
line5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
line6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
line7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
line8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
line9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
line10 = [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
line11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
line12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
line13 = [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
line14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
line15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
line16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
line17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
line18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
line19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
line20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
a = []

# Ce qui suit, c'est tout ce qui est horizontal
for n in range(0, 17):
    list = line1
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line2
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line3
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line4
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line5
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line6
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line7
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line8
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line9
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line10
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line11
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line12
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line13
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line14
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line15
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line16
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line17
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line18
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line19
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))
    list = line20
    a.append(int(list[n]) * int(list[n + 1]) * int(list[n + 2]) * int(list[n + 3]))

# Ce qui suit, c'est tout ce qui est vertical
for n in range(0, 20):
    a.append(int(line1[n]) * int(line2[n]) * int(line3[n]) * int(line4[n]))
    a.append(int(line2[n]) * int(line3[n]) * int(line4[n]) * int(line5[n]))
    a.append(int(line3[n]) * int(line4[n]) * int(line5[n]) * int(line6[n]))
    a.append(int(line4[n]) * int(line5[n]) * int(line6[n]) * int(line7[n]))
    a.append(int(line5[n]) * int(line6[n]) * int(line7[n]) * int(line8[n]))
    a.append(int(line6[n]) * int(line7[n]) * int(line8[n]) * int(line9[n]))
    a.append(int(line7[n]) * int(line8[n]) * int(line9[n]) * int(line10[n]))
    a.append(int(line8[n]) * int(line9[n]) * int(line10[n]) * int(line11[n]))
    a.append(int(line9[n]) * int(line10[n]) * int(line11[n]) * int(line12[n]))
    a.append(int(line10[n]) * int(line11[n]) * int(line12[n]) * int(line13[n]))
    a.append(int(line11[n]) * int(line12[n]) * int(line13[n]) * int(line14[n]))
    a.append(int(line12[n]) * int(line13[n]) * int(line14[n]) * int(line15[n]))
    a.append(int(line13[n]) * int(line14[n]) * int(line15[n]) * int(line16[n]))
    a.append(int(line14[n]) * int(line15[n]) * int(line16[n]) * int(line17[n]))
    a.append(int(line15[n]) * int(line16[n]) * int(line17[n]) * int(line18[n]))
    a.append(int(line16[n]) * int(line17[n]) * int(line18[n]) * int(line19[n]))
    a.append(int(line17[n]) * int(line18[n]) * int(line19[n]) * int(line20[n]))

#Ce qui suit, c'est tout ce qui est diagonal (haut gauche -> bas droite)
for n in range(0, 17):
    a.append(int(line1[n]) * int(line2[n + 1]) * int(line3[n + 2]) * int(line4[n + 3]))
    a.append(int(line2[n]) * int(line3[n + 1]) * int(line4[n + 2]) * int(line5[n + 3]))
    a.append(int(line3[n]) * int(line4[n + 1]) * int(line5[n + 2]) * int(line6[n + 3]))
    a.append(int(line4[n]) * int(line5[n + 1]) * int(line6[n + 2]) * int(line7[n + 3]))
    a.append(int(line5[n]) * int(line6[n + 1]) * int(line7[n + 2]) * int(line8[n + 3]))
    a.append(int(line6[n]) * int(line7[n + 1]) * int(line8[n + 2]) * int(line9[n + 3]))
    a.append(int(line7[n]) * int(line8[n + 1]) * int(line9[n + 2]) * int(line10[n + 3]))
    a.append(int(line8[n]) * int(line9[n + 1]) * int(line10[n + 2]) * int(line11[n + 3]))
    a.append(int(line9[n]) * int(line10[n + 1]) * int(line11[n + 2]) * int(line12[n + 3]))
    a.append(int(line10[n]) * int(line11[n + 1]) * int(line12[n + 2]) * int(line13[n + 3]))
    a.append(int(line11[n]) * int(line12[n + 1]) * int(line13[n + 2]) * int(line14[n + 3]))
    a.append(int(line12[n]) * int(line13[n + 1]) * int(line14[n + 2]) * int(line15[n + 3]))
    a.append(int(line13[n]) * int(line14[n + 1]) * int(line15[n + 2]) * int(line16[n + 3]))
    a.append(int(line14[n]) * int(line15[n + 1]) * int(line16[n + 2]) * int(line17[n + 3]))
    a.append(int(line15[n]) * int(line16[n + 1]) * int(line17[n + 2]) * int(line18[n + 3]))
    a.append(int(line16[n]) * int(line17[n + 1]) * int(line18[n + 2]) * int(line19[n + 3]))
    a.append(int(line17[n]) * int(line18[n + 1]) * int(line19[n + 2]) * int(line20[n + 3]))

#Ce qui suit, c'est tout ce qui est diagonal (haut droite -> bas gauche)
for n in range(0, 17):
    a.append(int(line1[n + 3]) * int(line2[n + 2]) * int(line3[n + 1]) * int(line4[n]))
    a.append(int(line2[n + 3]) * int(line3[n + 2]) * int(line4[n + 1]) * int(line5[n]))
    a.append(int(line3[n + 3]) * int(line4[n + 2]) * int(line5[n + 1]) * int(line6[n]))
    a.append(int(line4[n + 3]) * int(line5[n + 2]) * int(line6[n + 1]) * int(line7[n]))
    a.append(int(line5[n + 3]) * int(line6[n + 2]) * int(line7[n + 1]) * int(line8[n]))
    a.append(int(line6[n + 3]) * int(line7[n + 2]) * int(line8[n + 1]) * int(line9[n]))
    a.append(int(line7[n + 3]) * int(line8[n + 2]) * int(line9[n + 1]) * int(line10[n]))
    a.append(int(line8[n + 3]) * int(line9[n + 2]) * int(line10[n + 1]) * int(line11[n]))
    a.append(int(line9[n + 3]) * int(line10[n + 2]) * int(line11[n + 1]) * int(line12[n]))
    a.append(int(line10[n + 3]) * int(line11[n + 2]) * int(line12[n + 1]) * int(line13[n]))
    a.append(int(line11[n + 3]) * int(line12[n + 2]) * int(line13[n + 1]) * int(line14[n]))
    a.append(int(line12[n + 3]) * int(line13[n + 2]) * int(line14[n + 1]) * int(line15[n]))
    a.append(int(line13[n + 3]) * int(line14[n + 2]) * int(line15[n + 1]) * int(line16[n]))
    a.append(int(line14[n + 3]) * int(line15[n + 2]) * int(line16[n + 1]) * int(line17[n]))
    a.append(int(line15[n + 3]) * int(line16[n + 2]) * int(line17[n + 1]) * int(line18[n]))
    a.append(int(line16[n + 3]) * int(line17[n + 2]) * int(line18[n + 1]) * int(line19[n]))
    a.append(int(line17[n + 3]) * int(line18[n + 2]) * int(line19[n + 1]) * int(line20[n]))

a.sort()
print(a[len(a)-1])