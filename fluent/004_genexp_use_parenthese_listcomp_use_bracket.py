def main():
    symbols = 'AabcdefBC'
    captial_char = tuple(ord(symbol) for symbol in symbols if ord(symbol) < 97)
    print(captial_char)

if __name__ == '__main__':
    main()
