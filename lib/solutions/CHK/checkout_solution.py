

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    output = 0
    n = 0
    res = {}
    for i in skus[0]:
        n +=1
    


    result = dict((i, 1+= res) for i in skus[0])

    print(result)

    if result["A"] >= 3:
        n1 = result["A"] / 3
        n2 = result["A"] % 3

        output = 130*n1 + n2*50

    elif result["A"] < 3:
        output = result["A"]*50

    elif result["B"] >= 2:
        n1 = result["B"] / 2
        n2 = result["B"] % 2
        output = 45*n1 + n2*30





    # if skus == "A":
    #
    #     output = 50
    # elif skus == "B":
    #     output = 30
    #
    # elif skus == "C":
    #     output = 20*n
    # elif skus == "D":
    #     output = 15*n
    # elif skus == "":
    #     output = 0
    # elif skus == "AAA":
    #     output = 130
    # elif skus == "ABCD":
    #     output = 115
    # elif skus == "AA":
    #     output = 100
    # elif skus == "BB":
    #     output = 45
    else:
        return -1

    return output

