def greet(name):
    print("Hello", name)



def create_greeting(name, end = "."):
    return f"Hello {name}{end}"


def double_values(a,b):
    a *= 2
    b *= 2
    return a,b

def many_values():
    return 10, 15, 23, 45, 67, 88, 94

def main():
    message = create_greeting("Bob")
    print(message)

    a = 10
    b = 5
    a, b = double_values(a, b)
    print(a, b)

    result = many_values()
    print(result)


if __name__ == "__main__":
    main()
