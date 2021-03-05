listor = []
listlast = []
def palindrome(x):
    x = str(x)
    for i in x:
        listor.append(i)
    j = 1
    while (j <= len(listor)):
        listlast.append(listor[len(listor) - j])
        j+=1
    if listor == listlast:
        return True
    else:
        return False



print(palindrome(123454321))




