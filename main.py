from models.utils import (
    parsePartern,
    handelLogicalForm,
    printDependences,
    handleQueryForm,
    searchInDb
)


def main():
    inputPath = './input/input.txt'
    with open(inputPath, 'r') as f:
        sentences = list(f)

    for s in sentences:
        print('Sentences'.center(100, ' '))
        print(s)
        parterns = parsePartern(s)
        print('tokens'.center(100, ' '))
        print(parterns)
        print('logical form'.center(100, ' '))
        logicalForm = handelLogicalForm(parterns)
        printDependences(logicalForm)

        print('query form'.center(100, ' '))
        query = handleQueryForm(logicalForm)
        print(query)

        print('Result'.center(100, ' '))
        print(searchInDb(query))
        print(''.center(100, '#'))
        print(''.center(100, '#'))


if __name__ == '__main__':
    main()
