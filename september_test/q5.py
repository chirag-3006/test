python = 0
database = 0
programming = 0
entered = False

while True:

    print("1. enter student marks")
    print("2. display average marks")
    print("3. display highest marks")
    print("4. display lowest marks")
    print("5. display result")
    print("6. exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            python = int(input("enter Python marks: "))
            database = int(input("enter Database marks: "))
            programming = int(input("enter Programming marks: "))

            entered = True
            print("Marks entered successfully!")

        case 2:
            if entered:
                average = (python + database + programming) / 3
                print("Average marks:", average)
            else:
                print("Please enter marks first!")

        case 3:
            if entered:
                highest = python

                if database > highest:
                    highest = database

                if programming > highest:
                    highest = programming

                print("Highest marks:", highest)
            else:
                print("Please enter marks first!")

        case 4:
            if entered:
                lowest = python

                if database < lowest:
                    lowest = database

                if programming < lowest:
                    lowest = programming

                print("Lowest marks:", lowest)
            else:
                print("Please enter marks first!")

        case 5:
            if entered:
                percentage = (python + database + programming) / 3

                if python >= 40 and database >= 40 and programming >= 40 and percentage >= 50:
                    print("result: PASS")
                else:
                    print("result: FAIL")

                print("percentage:", percentage)

            else:
                print("please enter marks first!")

        case 6:
            print("program exited")
            break

        case _:
            print("invalid choice")