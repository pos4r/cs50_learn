def convert(x):
    x = x.replace(":)", "🙂").replace(":(", "🙁")
    return x

def main():
    y = input()
    result = convert(y)
    print(result)

main()
