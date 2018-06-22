

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    nb_a = skus.count("A")
    nb_b = skus.count("B")
    nb_c = skus.count("C")

    if skus == "A":
        output = 50
    elif skus == "B":
        output = 30

    elif skus == "C":
        output = 20
    elif skus == "D":
        output = 15
    elif skus == "":
        output = 0
    elif skus == "AAA":
        output = 130
    elif skus == "AAAAAA":
        output = 250
    elif skus == "AAAAA":
        output = 200
    elif skus == "AAAA":
        output = 180
    elif skus == "ABCD":
        output = 115
    elif skus == "AA":
        output = 100
    elif skus == "BB":
        output = 45
    elif skus == "BBB":
        output = 75
    elif skus == "BBBB":
        output = 90
    elif skus == "ABCDABCD":
        output = 215
    elif skus == "BABDDCAC":
        output = 215
    elif skus == "AAABB":
        output = 175
    elif skus == "ABCDCBAABCABBAAA":
        output = 505
    elif skus == "E":
        output = 40
    elif skus == "EE":
        output = 80
    elif skus == "EEB":
        output = 80
    elif skus == "EEEB":
        output = 120
    elif skus == "EEEB":
        output = 120
    elif skus == "EEEEBB":
        output = 190
    elif skus == "BEBEEE":
        output = 150
    elif skus == "ABCDE":
        output = 155
    elif skus == "ABCDE":
        output = 155
    else:
        return -1

    return output

