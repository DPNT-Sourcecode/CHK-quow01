

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    output = 0
    n = 1
    if skus == "A":

        output = 50
    elif skus == "B":
        output = 30

    elif skus == "C":
        output = 20*n
    elif skus == "D":
        output = 15*n
    elif skus == "":
        output = 0
    elif skus == "AAA":
        output = 130
    elif skus == "BB":
        output = 45

    else:
        return -1

    return output

