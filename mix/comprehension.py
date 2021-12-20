def main():
    values = [1, 2, 3, 4, 5, 6]
    new_values = []
    for value in values:
        if value % 2 == 0:
            new_values.append(values * 2)






    # List comprehension
    new_values = [value * 2 for value in values if value % 2 == 0]
    print(new_values)
    print(type(new_values))


    # Set
    new_values = {value * 2 for value in values if value % 2 == 0}
    print(new_values)
    print(type(new_values))


    new_values = {value : value * 2 for value in values if value % 2 == 0}
    print(new_values)
    print(type(new_values))

    new_values = (value * 2 for value in values if value % 2 == 0)
    print(new_values)
    print(type(new_values))



if __name__ == "__main__":
    main()
