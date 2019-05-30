def printTable(big_list):
    ans = ''
    for col in range(len(big_list[0])):
        for row in range(len(big_list)):
            ans += big_list[row][col].rjust(7)
        ans += '\n'

    print(ans)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)