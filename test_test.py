def test():
        try:
                choice = int(input("Enter integer btwn 1-12: "))
                if not (1 <= choice <= 12):
                        print('Not in range!')
        except ValueError:
                print("Not an integer")
        else:
                print("Your choice is", choice)

test()
test()
test()
