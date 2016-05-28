def main():
    symbols = 'AbaaaBCccd'
    captial_char = [ord(s) for s in symbols if ord(s) < 97]
    print(captial_char)

    captial_char = list(filter(lambda c: c < 97, map(ord, symbols)))
    print(captial_char)

if __name__ == '__main__':
    main()
