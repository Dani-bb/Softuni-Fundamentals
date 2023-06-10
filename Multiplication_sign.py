def checker(n1,n2,n3):
    while True:
        if n1 < 0 or n2 < 0 or n3 < 0:

            if n1 < 0 and n2 < 0 and n3 != 0:
                print("positive")
                break
            if n2 < 0 and n3 < 0 and n1 != 0:
                print("positive")
                break

            if n3 < 0 and n1 < 0 and n2 != 0:
                print("positive")
                break


            if n1 == 0 or n2 == 0 or n3 == 0:
                print("zero")
                break
            else:
                print("negative")
                break


        if n1 == 0 or n2 == 0 or n3 == 0:
            print("zero")
            break
        else:
            print("positive")
            break



n1 = int(input())
n2 = int(input())
n3 = int(input())

checker(n1,n2,n3)