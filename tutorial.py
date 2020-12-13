def test1(text, alter):
    alter = int(alter)
    print(text, alter)

if __name__ == '__main__':

    # sample try catch similar to C++ / ABAP / C#
    # here is not catch -> is execpt

    try:
        test1("Ich bin", input('Alter eingeben: '))
    except ValueError:
        test1("Ich bin", 30)
    input('Weiter mit einer Taste ...')
