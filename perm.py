from itertools import permutations
def perm(str):
    a=permutations(str)
    for x in list(a):
    print (''.join(x))

if __name__=="__main__":
    str='SOJA'
    perm(str)
