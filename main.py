

plocha = [["r", "n", "b", "q", "k", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["+", "+", "+", "+", "+", "+", "+", "+"], ["=", "%", "!", "#", "?", "!", "%", "="]]


def hrac1_vyhra():
    global plocha
    print("Hráč 1 vyhral.")
    print("Pre novú hru stlačte 1 pre vypnutie stlačte 0.")
    hra = input()
    if hra == "0":
        quit()
    elif hra == "1":
        plocha = [["r", "n", "b", "q", "k", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"],
                  ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
                  ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
                  ["+", "+", "+", "+", "+", "+", "+", "+"], ["=", "%", "!", "#", "?", "!", "%", "="]]
        hrac1()
    else:
        hrac1_vyhra()



def hrac2_vyhra():
    global plocha
    print("Hráč 2 vyhral.")
    print("Pre novú hru stlačte 1 pre vypnutie stlačte 0.")
    hra = input()
    if hra == "0":
        quit()
    elif hra == "1":
        plocha = [["r", "n", "b", "q", "k", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"],
                  ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
                  ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
                  ["+", "+", "+", "+", "+", "+", "+", "+"], ["=", "%", "!", "#", "?", "!", "%", "="]]
        hrac1()
    else:
        hrac2_vyhra()



def hracia_plocha(plocha):
    print(" ", 1, 2, 3, 4, 5, 6, 7, 8)
    print("A", plocha[0][0], plocha[0][1], plocha[0][2], plocha[0][3], plocha[0][4], plocha[0][5], plocha[0][6], plocha[0][7])
    print("B", plocha[1][0], plocha[1][1], plocha[1][2], plocha[1][3], plocha[1][4], plocha[1][5], plocha[1][6],
          plocha[1][7])
    print("C", plocha[2][0], plocha[2][1], plocha[2][2], plocha[2][3], plocha[2][4], plocha[2][5], plocha[2][6],
          plocha[2][7])
    print("D", plocha[3][0], plocha[3][1], plocha[3][2], plocha[3][3], plocha[3][4], plocha[3][5], plocha[3][6],
          plocha[3][7])
    print("E", plocha[4][0], plocha[4][1], plocha[4][2], plocha[4][3], plocha[4][4], plocha[4][5], plocha[4][6],
          plocha[4][7])
    print("F", plocha[5][0], plocha[5][1], plocha[5][2], plocha[5][3], plocha[5][4], plocha[5][5], plocha[5][6],
          plocha[5][7])
    print("G", plocha[6][0], plocha[6][1], plocha[6][2], plocha[6][3], plocha[6][4], plocha[6][5], plocha[6][6],
          plocha[6][7])
    print("H", plocha[7][0], plocha[7][1], plocha[7][2], plocha[7][3], plocha[7][4], plocha[7][5], plocha[7][6],
          plocha[7][7])


def hrac1():
    hracia_plocha(plocha)
    print("Na rade je hráč 1.")
    temp = input()
    if len(temp) != 2:
        print("Chybný ťah.")
        hrac1()
    else:
        riadok = temp[0]
        stlpec = temp[1]
        if riadok == "A" or riadok == "B" or riadok == "C" or riadok == "D" or riadok == "E" or riadok == "F" or riadok == "G" or riadok == "H":
            if stlpec == "1" or stlpec == "2" or stlpec == "3" or stlpec == "4" or stlpec == "5" or stlpec == "6" or stlpec == "7" or stlpec == "8":
                if riadok == "A":
                    y = 0
                elif riadok == "B":
                    y = 1
                elif riadok == "C":
                    y = 2
                elif riadok == "D":
                    y = 3
                elif riadok == "E":
                    y = 4
                elif riadok == "F":
                    y = 5
                elif riadok == "G":
                    y = 6
                elif riadok == "H":
                    y = 7
                if stlpec == "1":
                    x = 0
                elif stlpec == "2":
                    x = 1
                elif stlpec == "3":
                    x = 2
                elif stlpec == "4":
                    x = 3
                elif stlpec == "5":
                    x = 4
                elif stlpec == "6":
                    x = 5
                elif stlpec == "7":
                    x = 6
                elif stlpec == "8":
                    x = 7
                if plocha[y][x] == "+":
                    b_pesiak(y, x)
                elif plocha[y][x] == "=":
                    b_veza(y, x)
                elif plocha[y][x] == "?":
                    b_kral(y, x)
                elif plocha[y][x] == "%":
                    b_kon(y, x)
                elif plocha[y][x] == "!":
                    b_strelec(y, x)
                elif plocha[y][x] == "#":
                    b_kralovna(y, x)
                else:
                    print("Chybný ťah.")
                    hrac1()
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()


def b_pesiak(y, x):
    if plocha[y][x] == "+":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-":
            if x == int(x1) and (y-1) == int(y1):
                plocha[y][x] = "-"
                plocha[y1][x1] = "+"
                hrac2()
            elif x == int(x1) and (y-2) == int(y1) and y == 6:
                plocha[y][x] = "-"
                plocha[y1][x1] = "+"
                hrac2()
            else:
                print("Chybný ťah.")
                hrac1()
        elif plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":
            if (x+1) == int(x1) or (x-1) == int(x1) and (y-1) == int(y1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "+"
                hrac2()
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()




def b_veza(y, x):
    if plocha[y][x] == "=":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":
            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "="
                    hrac2()
                else:
                    for i in range(int(y1+1), y):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "="
                            hrac2()
            elif x == int(x1) and y < int(y1):
                if int(y1) == y+1:
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "="
                    hrac2()

                else:
                    for i in range(y+1, int(y1)):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "="
                            hrac2()
            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "="
                    hrac2()

                else:
                    for i in range(x1+1, x):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "="
                            hrac2()
            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "="
                    hrac2()

                else:
                    for i in range(x+1, x1):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "="
                            hrac2()

            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()


def b_kral(y, x):
    if plocha[y][x] == "?":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":

            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "?"
                    hrac2()

                else:
                    print("Chybný ťah.")
                    hrac1()

            elif x == int(x1) and y < int(y1):
                if (y+1) == int(y1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "?"
                    hrac2()

                else:
                    print("Chybný ťah.")
                    hrac1()

            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "?"
                    hrac2()

                else:
                    print("Chybný ťah.")
                    hrac1()

            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "?"
                    hrac2()

                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "?"
                hrac2()

            elif x == int(x1+1) and (y+1) == int(y1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "?"
                hrac2()

            elif (x+1) == int(x1) and (y+1) == int(y1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "?"
                hrac2()

            elif (x+1) == int(x1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "?"
                hrac2()

            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()


def b_kon(y, x):
    if plocha[y][x] == "%":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":

            if y == int(y1+1) and (x+2) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1-1) and (x+2) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1-1) and (x-2) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1+1) and (x-2) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1-2) and (x-1) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1-2) and (x+1) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1+2) and (x-1) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            elif y == int(y1+2) and (x+1) == int(x1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "%"
                hrac2()

            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()



def b_strelec(y, x):
    if plocha[y][x] == "!":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":

            if x == int(x1+7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1+6)] == "-" and plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1+1)] == "-":

                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "!"
                hrac2()
            elif x == int(x1-7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1-6)] == "-" and plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-1) and y == int(y1-1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "!"
                hrac2()
            elif x == int(x1+7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1+6)] == "-" and plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+1) and y == int(y1-1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "!"
                hrac2()
            elif x == int(x1-7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1-6)] == "-" and plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "!"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "!"
                hrac2()

            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()



def b_kralovna(y, x):
    if plocha[y][x] == "#":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac1()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "p" or plocha[y1][x1] == "r" or plocha[y1][x1] == "n" or plocha[y1][x1] == "b" or plocha[y1][x1] == "q" or plocha[y1][x1] == "k":

            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    for i in range(int(y1+1), y):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "#"
                            hrac2()
            elif x == int(x1) and y < int(y1):
                if int(y1) == y+1:
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()

                else:
                    for i in range(y+1, int(y1)):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "#"
                            hrac2()
            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()

                else:
                    for i in range(x1+1, x):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "#"
                            hrac2()
            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()

                else:
                    for i in range(x+1, x1):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac1()
                        else:
                            if plocha[y1][x1] == "k":
                                hrac1_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "#"
                            hrac2()
            elif x == int(x1+7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1+6)] == "-" and plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "#"
                hrac2()
            elif x == int(x1-7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1-6)] == "-" and plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-1) and y == int(y1-1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "#"
                hrac2()
            elif x == int(x1+7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1+6)] == "-" and plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1+1) and y == int(y1-1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "#"
                hrac2()
            elif x == int(x1-7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1-6)] == "-" and plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "k":
                        hrac1_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "#"
                    hrac2()
                else:
                    print("Chybný ťah.")
                    hrac1()
            elif x == int(x1-1) and y == int(y1+1):
                if plocha[y1][x1] == "k":
                    hrac1_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "#"
                hrac2()

            else:
                print("Chybný ťah.")
                hrac1()


        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()



def hrac2():
    hracia_plocha(plocha)
    print("Na rade je hráč 2.")
    temp = input()
    if len(temp) != 2:
        print("Chybný ťah.")
        hrac2()
    else:
        riadok = temp[0]
        stlpec = temp[1]
        if riadok == "A" or riadok == "B" or riadok == "C" or riadok == "D" or riadok == "E" or riadok == "F" or riadok == "G" or riadok == "H":
            if stlpec == "1" or stlpec == "2" or stlpec == "3" or stlpec == "4" or stlpec == "5" or stlpec == "6" or stlpec == "7" or stlpec == "8":
                if riadok == "A":
                    y = 0
                elif riadok == "B":
                    y = 1
                elif riadok == "C":
                    y = 2
                elif riadok == "D":
                    y = 3
                elif riadok == "E":
                    y = 4
                elif riadok == "F":
                    y = 5
                elif riadok == "G":
                    y = 6
                elif riadok == "H":
                    y = 7
                if stlpec == "1":
                    x = 0
                elif stlpec == "2":
                    x = 1
                elif stlpec == "3":
                    x = 2
                elif stlpec == "4":
                    x = 3
                elif stlpec == "5":
                    x = 4
                elif stlpec == "6":
                    x = 5
                elif stlpec == "7":
                    x = 6
                elif stlpec == "8":
                    x = 7
                if plocha[y][x] == "p":
                    c_pesiak(y, x)
                elif plocha[y][x] == "r":
                    c_veza(y, x)
                elif plocha[y][x] == "k":
                    c_kral(y, x)
                elif plocha[y][x] == "n":
                    c_kon(y, x)
                elif plocha[y][x] == "b":
                    b_strelec(y, x)
                elif plocha[y][x] == "q":
                    b_kralovna(y, x)
                else:
                    print("Chybný ťah.")
                    hrac2()
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()



def c_pesiak(y, x):
    if plocha[y][x] == "p":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-":
            if x == int(x1) and (y+1) == int(y1):
                plocha[y][x] = "-"
                plocha[y1][x1] = "p"
                hrac1()
            elif x == int(x1) and (y+2) == int(y1) and y == 1:
                plocha[y][x] = "-"
                plocha[y1][x1] = "p"
                hrac1()
            else:
                print("Chybný ťah.")
                hrac2()
        elif plocha[y1][x1] == "+" or plocha[y1][x1] == "%" or plocha[y1][x1] == "#" or plocha[y1][x1] == "!" or plocha[y1][x1] == "=" or plocha[y1][x1] == "?":

            if (x+1) == int(x1) and (y+1) == int(y1) or (x-1) == int(x1) and (y+1) == int(y1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "p"
                hrac1()
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()


def c_veza(y, x):
    if plocha[y][x] == "r":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "+" or plocha[y1][x1] == "=" or plocha[y1][x1] == "%" or plocha[y1][x1] == "!" or plocha[y1][x1] == "#" or plocha[y1][x1] == "?":

            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "r"
                    hrac1()
                else:
                    for i in range(int(y1+1), y):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "r"
                            hrac1()
            elif x == int(x1) and y < int(y1):
                if int(y1) == y+1:
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "r"
                    hrac1()

                else:
                    for i in range(y+1, int(y1)):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "r"
                            hrac1()
            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "r"
                    hrac1()

                else:
                    for i in range(x1+1, x):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "r"
                            hrac1()
            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "r"
                    hrac1()

                else:
                    for i in range(x+1, x1):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "r"
                            hrac1()

            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()



def c_kral(y, x):
    if plocha[y][x] == "k":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "+" or plocha[y1][x1] == "=" or plocha[y1][x1] == "%" or plocha[y1][x1] == "!" or plocha[y1][x1] == "#" or plocha[y1][x1] == "?":

            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "k"
                    hrac1()

                else:
                    print("Chybný ťah.")
                    hrac2()

            elif x == int(x1) and y < int(y1):
                if (y+1) == int(y1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "k"
                    hrac1()

                else:
                    print("Chybný ťah.")
                    hrac2()

            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "k"
                    hrac1()

                else:
                    print("Chybný ťah.")
                    hrac2()

            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "k"
                    hrac1()

                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "k"
                hrac1()

            elif x == int(x1+1) and (y+1) == int(y1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "k"
                hrac1()

            elif (x+1) == int(x1) and (y+1) == int(y1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "k"
                hrac1()

            elif (x+1) == int(x1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "k"
                hrac1()

            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()


def c_kon(y, x):
    if plocha[y][x] == "n":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "+" or plocha[y1][x1] == "=" or plocha[y1][x1] == "%" or plocha[y1][x1] == "!" or plocha[y1][x1] == "#" or plocha[y1][x1] == "?":

            if y == int(y1+1) and (x+2) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1-1) and (x+2) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1-1) and (x-2) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1+1) and (x-2) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1-2) and (x-1) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1-2) and (x+1) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1+2) and (x-1) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            elif y == int(y1+2) and (x+1) == int(x1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "n"
                hrac1()

            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()



def c_strelec(y, x):
    if plocha[y][x] == "b":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "+" or plocha[y1][x1] == "=" or plocha[y1][x1] == "%" or plocha[y1][x1] == "!" or plocha[y1][x1] == "#" or plocha[y1][x1] == "?":

            if x == int(x1+7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1+6)] == "-" and plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "b"
                hrac1()
            elif x == int(x1-7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1-6)] == "-" and plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-1) and y == int(y1-1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "b"
                hrac1()
            elif x == int(x1+7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1+6)] == "-" and plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+1) and y == int(y1-1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "b"
                hrac1()
            elif x == int(x1-7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1-6)] == "-" and plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "b"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "b"
                hrac1()

            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()


def c_kralovna(y, x):
    if plocha[y][x] == "q":
        temp1 = input()
        if len(temp1) != 2:
            print("Chybný ťah.")
            hrac2()
        riadok1 = temp1[0]
        stlpec1 = temp1[1]
        if riadok1 == "A" or riadok1 == "B" or riadok1 == "C" or riadok1 == "D" or riadok1 == "E" or riadok1 == "F" or riadok1 == "G" or riadok1 == "H":
            if stlpec1 == "1" or stlpec1 == "2" or stlpec1 == "3" or stlpec1 == "4" or stlpec1 == "5" or stlpec1 == "6" or stlpec1 == "7" or stlpec1 == "8":
                if riadok1 == "A":
                    y1 = 0
                elif riadok1 == "B":
                    y1 = 1
                elif riadok1 == "C":
                    y1 = 2
                elif riadok1 == "D":
                    y1 = 3
                elif riadok1 == "E":
                    y1 = 4
                elif riadok1 == "F":
                    y1 = 5
                elif riadok1 == "G":
                    y1 = 6
                elif riadok1 == "H":
                    y1 = 7
                if stlpec1 == "1":
                    x1 = 0
                elif stlpec1 == "2":
                    x1 = 1
                elif stlpec1 == "3":
                    x1 = 2
                elif stlpec1 == "4":
                    x1 = 3
                elif stlpec1 == "5":
                    x1 = 4
                elif stlpec1 == "6":
                    x1 = 5
                elif stlpec1 == "7":
                    x1 = 6
                elif stlpec1 == "8":
                    x1 = 7
            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
        if plocha[y1][x1] == "-" or plocha[y1][x1] == "+" or plocha[y1][x1] == "=" or plocha[y1][x1] == "%" or plocha[y1][x1] == "!" or plocha[y1][x1] == "#" or plocha[y1][x1] == "?":

            if x == int(x1) and y > int(y1):
                if y == int(y1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    for i in range(int(y1+1), y):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "q"
                            hrac1()
            elif x == int(x1) and y < int(y1):
                if int(y1) == y+1:
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()

                else:
                    for i in range(y+1, int(y1)):
                        if plocha[i][x] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "q"
                            hrac1()
            elif x > int(x1) and y == int(y1):
                if x == int(x1+1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()

                else:
                    for i in range(x1+1, x):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "q"
                            hrac1()
            elif x < int(x1) and y == int(y1):
                if (x+1) == int(x1):
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()

                else:
                    for i in range(x+1, x1):
                        if plocha[y][i] != "-":
                            print("Chybný ťah.")
                            hrac2()
                        else:
                            if plocha[y1][x1] == "?":
                                hrac2_vyhra()
                            plocha[y][x] = "-"
                            plocha[y1][x1] = "q"
                            hrac1()
            elif x == int(x1+7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1+6)] == "-" and plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1+5)] == "-" and plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1+4)] == "-" and plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1+3)] == "-" and plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1+2)] == "-" and plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "q"
                hrac1()
            elif x == int(x1-7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1-6)] == "-" and plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1-5)] == "-" and plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1-4)] == "-" and plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1-3)] == "-" and plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1-2)] == "-" and plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-1) and y == int(y1-1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "q"
                hrac1()
            elif x == int(x1+7) and y == int(y1-7):
                if plocha[int(y1-6)][int(x1+6)] == "-" and plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+6) and y == int(y1-6):
                if plocha[int(y1-5)][int(x1+5)] == "-" and plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+5) and y == int(y1-5):
                if plocha[int(y1-4)][int(x1+4)] == "-" and plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+4) and y == int(y1-4):
                if plocha[int(y1-3)][int(x1+3)] == "-" and plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+3) and y == int(y1-3):
                if plocha[int(y1-2)][int(x1+2)] == "-" and plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+2) and y == int(y1-2):
                if plocha[int(y1-1)][int(x1+1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1+1) and y == int(y1-1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "q"
                hrac1()
            elif x == int(x1-7) and y == int(y1+7):
                if plocha[int(y1+6)][int(x1-6)] == "-" and plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-6) and y == int(y1+6):
                if plocha[int(y1+5)][int(x1-5)] == "-" and plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-5) and y == int(y1+5):
                if plocha[int(y1+4)][int(x1-4)] == "-" and plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-4) and y == int(y1+4):
                if plocha[int(y1+3)][int(x1-3)] == "-" and plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-3) and y == int(y1+3):
                if plocha[int(y1+2)][int(x1-2)] == "-" and plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-2) and y == int(y1+2):
                if plocha[int(y1+1)][int(x1-1)] == "-":
                    if plocha[y1][x1] == "?":
                        hrac2_vyhra()
                    plocha[y][x] = "-"
                    plocha[y1][x1] = "q"
                    hrac1()
                else:
                    print("Chybný ťah.")
                    hrac2()
            elif x == int(x1-1) and y == int(y1+1):
                if plocha[y1][x1] == "?":
                    hrac2_vyhra()
                plocha[y][x] = "-"
                plocha[y1][x1] = "q"
                hrac1()

            else:
                print("Chybný ťah.")
                hrac2()
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()




hrac1()
