def g(f):
    def h():
        print("f")
        f()
        print("k")
    return (h)

def ddd():
    print('0. Exit')


ddd = (g(ddd))









