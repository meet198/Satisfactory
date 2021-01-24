

def main():
    def what(z,a,b):
        if a > 3:
            print (z)
            print (a)
            print (f"{b}\n")
            y = input("a")
            a -= 1
            z += 1
            b += 1
            what(z,a,b)
        
        out = input(f"{a}, {b}out")
        
        if b > 3:
            print (z)
            print (b)
            y = input("b")
            b -= 1
            z += 1
            what(z,a,b)

        
    x = {1,3,5,4,5,6,7,8,9}
    for i in range (len(x)):
        what(1, 5, 5)
if __name__ == '__main__': 
    main()
