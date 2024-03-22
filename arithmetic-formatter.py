def arithmetic_arranger(problems, show_answers=False):

    firstNums = []
    secNums = []
    dashes = []
    sums = []
    operatorPlus = ' + '
    operatorMinus = ' - '

    for i in problems:
        if operatorPlus in i:
            i = i.split(operatorPlus)
            if not i[0].isnumeric() or not i[-1].isnumeric():
                return 'Error: Numbers must only contain digits.'
            if len(i[0]) >= len(i[-1]):
                y = 2
            elif len(i[0]) > 4 or len(i[-1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                y = len(i[-1]) - len(i[0]) + 2
            firstNums.append(y*' ' + i[0])
            if len(i[0]) <= len(i[-1]):
                x = 1
            elif len(i[0]) > 4 or len(i[-1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                x = len(i[0]) - len(i[-1]) + 1
            secNums.append('+' + x*' ' + i[-1])
            if firstNums[-1] == secNums[-1]:
                dashes.append((len(firstNums[-1]))*'-')
            elif firstNums[-1] > secNums[-1]:
                dashes.append((len(firstNums[-1]))*'-')
            else:
                dashes.append((len(secNums[-1]))*'-')
            sumItem = str(int(i[0])+int(i[-1]))
            z = len(dashes[-1]) - len(sumItem)
            sums.append(z*' ' + sumItem)
        elif operatorMinus in i:
            i = i.split(operatorMinus)
            if len(i[0]) >= len(i[-1]):
                y = 2
            elif len(i[0]) > 4 or len(i[-1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                y = len(i[-1]) - len(i[0]) + 2
            firstNums.append(y*' ' + i[0])
            if len(i[0]) <= len(i[-1]):
                x = 1
            elif len(i[0]) > 4 or len(i[-1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                x = len(i[0]) - len(i[-1]) + 1
            secNums.append('-' + x*' ' + i[-1])
            if firstNums[-1] == secNums[-1]:
                dashes.append((len(firstNums[-1]))*'-')
            elif firstNums[-1] > secNums[-1]:
                dashes.append((len(firstNums[-1]))*'-')
            else:
                dashes.append((len(secNums[-1]))*'-')
            sumItem = str(int(i[0])-int(i[-1]))
            z = len(dashes[-1]) - len(sumItem)
            sums.append(z*' ' + sumItem)
        else:
            return "Error: Operator must be '+' or '-'."
    
    for i in range(len(problems)):
        firstNums[i] += '    '
        secNums[i] += '    '
        dashes[i] += '    '
        sums[i] += '    '
    firstNums[-1] = firstNums[-1].rstrip()
    secNums[-1] = secNums[-1].rstrip()
    dashes[-1] = dashes[-1].rstrip()
    sums[-1] = sums[-1].rstrip()

    firstLine = ''.join(firstNums)
    secondLine = ''.join(secNums)
    thirdLine = ''.join(dashes)
    fourthLine = ''.join(sums)

    if len(problems) > 5:
        return 'Error: Too many problems.'

    if show_answers:
        problems = firstLine + '\n' + secondLine + '\n' + thirdLine + '\n' + fourthLine
    else:
        problems = firstLine + '\n' + secondLine + '\n' + thirdLine

    return problems

p = ('12 + 56', '1111 + 9999')
print(arithmetic_arranger(p, True))