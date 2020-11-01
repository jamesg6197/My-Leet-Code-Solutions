def validitycheck(mylist):
    modifiedlist = [x for x in mylist if x != '.']
    if len(modifiedlist) != len(set(modifiedlist)):
        return False
    return True
def isValidSudoku(self, board: List[List[str]]) -> bool:
        good = True
        for i in board:
            if validitycheck(i) == False:
                good = False
        columns = []
        for j in range(9):
            column = []
            for k in board:
                column.append(k[j])
            columns.append(column)
        for eachcolumn in columns:
            if validitycheck(eachcolumn) == False:
                good = False
        thrbythrs = [
            columns[0][0:3] + columns[1][0:3] + columns[2][0:3],
            columns[0][3:6] + (columns[1][3:6]) + (columns[2][3:6]),
            columns[0][6:9] + (columns[1][6:9]) + (columns[2][6:9]),
            columns[3][0:3] + (columns[4][0:3]) + (columns[5][0:3]),
            columns[3][3:6] + (columns[4][3:6]) + (columns[5][3:6]),
            columns[3][6:9] + (columns[4][6:9]) + (columns[5][6:9]),
            columns[6][0:3] + (columns[7][0:3]) + (columns[8][0:3]),
            columns[6][3:6] + (columns[7][3:6]) + (columns[8][3:6]),
            columns[6][6:9] + (columns[7][6:9]) + (columns[8][6:9]) 
        ]
        for thrbythr in thrbythrs:
            if validitycheck(thrbythr) == False:
                good = False    
        return good
