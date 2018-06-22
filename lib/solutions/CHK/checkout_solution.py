

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    output = 0
    n = 1
    if skus == "A":

        output = 130
    elif skus == "B":
        output = 45

    elif skus == "C":
        output = 20*n
    elif skus == "D":
        output = 15*n
    else:
        return -1

    return output

