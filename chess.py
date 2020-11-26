def main():
    numbers = [str(i) for i in range(1, 9)]
    print("Hello. You need to enter indexes k, l, m, n for 2 chess squares. Be careful: numbers must be between 1 to 8 inclusively.")
    k = input("Enter value k: ")
    l = input("Enter value l: ")
    m = input("Enter value m: ")
    n = input("Enter value n: ")
    if k in numbers and l in numbers and m in numbers and n in numbers:
        k, l, m, n = map(int, (k, l, m, n))
    else:
        print("Some of the values are incorrect! Let's try again \n")
        main()


if __name__ == '__main__':
    main()