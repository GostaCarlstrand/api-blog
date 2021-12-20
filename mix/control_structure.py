def main():
    age = 14

    if age < 20:
        print("age is less than 20")
    else:
        print("age is greater than or equal to 20")


    if age < 20:
        print("something")
    else:
        if age < 30:
            print("something else")
        else:
            print("Hej")

    if age == 20:
        print("hej")
    elif age < 20:
        print("hejdå")



    #For-loop      2 = Starting pos in range, 10 = stopping condition, 2=increament with
    for i in range(2, 10, 2):
        print(i)

    values = range(100)
    for value in values:
        if value == 55:
            break
        print(value)


    #while

    value = 0
    while value < 10:
        print(value)
        value += 1

    # Do-while loop does not exist in Python

if __name__ == "__main__":
    main()
