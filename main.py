from balance import balance

if __name__ == '__main__':
    text = '[[{())}]'
    print(balance(text))
    text2 = '[([])((([[[]]])))]{()}'
    print(balance(text2))