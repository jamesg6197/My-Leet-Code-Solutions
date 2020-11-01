def convert(self, s: str, numRows: int) -> str:
        if numRows > len(s) or numRows == 1:
            return s
        mystr = ''
        numDif = 2 * numRows - 2
        for i in range(numRows):
            z = i
            mystr += s[i]
            while True:
                if i == numRows - 1:
                    i = 0
                if z + (numDif - 2*i) < len(s):
                    mystr += s[z + numDif - 2*i]
                    z += (numDif - 2*i)
                else:
                    break
                if z + 2*i < len(s) and i != 0:
                    mystr += s[z + 2*i]
                    z += 2*i
                elif i != 0:
                    break
        return mystr
