def numOfLittersInNumeric(number):
    numWords = list()
    numWords[1] = 3; # one
    numWords[2] = 3; # two
    numWords[3] = 5; # three
    numWords[4] = 4; # four
    numWords[5] = 4; # five
    numWords[6] = 3; # six
    numWords[7] = 5; # seven
    numWords[8] = 5; # eight
    numWords[9] = 4; # nine
    numWords[10] = 3; # ten
    numWords[11] = 6; # eleven
    numWords[12] = 6; # twelve
    numWords[13] = 8; # thirteen
    numWords[14] = 8; # fourteen
    numWords[15] = 7; # fifteen
    numWords[16] = 7; # sixteen
    numWords[17] = 9; # seventeen
    numWords[18] = 8; # eighteen
    numWords[19] = 8; # nineteen
    numWords[20] = 6; # twenty
    numWords[30] = 6; # thirty
    numWords[40] = 5; # forty
    numWords[50] = 5; # fifty
    numWords[60] = 5; # sixty
    numWords[70] = 7; # seventy
    numWords[80] = 6; # eighty
    numWords[90] = 6; # ninety
    numWords[100] = 7; # hundred
    numWords[1000] = 8; # thousand
    numWords[0] = 3; # and

    for i in range(number):
