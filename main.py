from models.utils import (
    parsePartern,
    handelLogicalForm,
    formatDependences,
    handleQueryForm,
    searchInDb
)


def main():
    inputPath = './input/input.txt'
    with open(inputPath, 'r') as f:
        sentences = list(f)
    output_a = []
    output_b = []
    output_c = []
    output_d = []
    for s in sentences:
        s = s.strip()
        output_a.append('Sentences'.center(100, ' '))
        output_b.append('Sentences'.center(100, ' '))
        output_c.append('Sentences'.center(100, ' '))
        output_d.append('Sentences'.center(100, ' '))
        output_a.append(s)
        output_b.append(s)
        output_c.append(s)
        output_d.append(s)

        print('##############################################')
        print(s)
        parterns = parsePartern(s)
        output_a.append('tokens'.center(100, '~'))
        output_a.append(str(parterns))

        logicalForm = handelLogicalForm(parterns)
        formatLF = formatDependences(logicalForm)
        output_b.append('logical form'.center(100, '~'))
        output_b.append(str(formatLF))

        query = handleQueryForm(logicalForm)
        output_c.append('query form'.center(100, '~'))
        output_c.append(str(query))

        result = searchInDb(query)
        output_d.append('result'.center(100, '~'))
        output_d.append(str(result))
        print(result)

        output_a.append(''.center(100, '#'))
        output_b.append(''.center(100, '#'))
        output_c.append(''.center(100, '#'))
        output_d.append(''.center(100, '#'))
    with open('./output/output_a.txt', 'w') as f:
        f.write('\n'.join(output_a))
    with open('./output/output_b.txt', 'w') as f:
        f.write('\n'.join(output_b))
    with open('./output/output_c.txt', 'w') as f:
        f.write('\n'.join(output_c))
    with open('./output/output_d.txt', 'w') as f:
        f.write('\n'.join(output_d))


if __name__ == '__main__':
    main()
