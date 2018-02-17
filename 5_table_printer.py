def printTable(lists):
    colWidths = [0] * len(lists)
    # for i, v in enumerate(colWidths):
    #     colWidths[i] = len(max(lists[i], key=len)) + 1
    # print(colWidths)
    colWidths = [len(max(i, key=len))+1 for i in lists]
    # print(colWidths)
    for i in range(len(lists[0])):
        print(lists[0][i].rjust(colWidths[0]) + lists[1][i].rjust(colWidths[1]) + lists[2][i].rjust(colWidths[2]))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)