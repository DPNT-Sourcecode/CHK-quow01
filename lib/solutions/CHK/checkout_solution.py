

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    output = 0
    n = 0
    result = {}
    for i in skus[0]:
        n +=1

        result[i] = n

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

    else:
        return -1

    return output

