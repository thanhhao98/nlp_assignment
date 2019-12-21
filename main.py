from models.utils import (
    parsePartern,
    handelLogicalForm,
    printDependences,
    handleQueryForm,
    searchInDb
)

# with open('input.txt', 'r') as f:
#     s = f.readline()
s = [
    'Xe bus nào đến thành phố huế lúc 20:00hr ?',
    'Thời gian xe bus B3 từ Đà nẵng đến huế ?',
    'xe bus nào đi từ thành phố đà nẵng lúc 8:30 ?',
    'xe bus nào đến thành phố huế lúc 20:00hr ?',
    'xe bus nào đi từ đà nẵng đến thành phố hồ chí minh?'
]
print('Sentences'.center(100, ' '))
s = s[1]
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
