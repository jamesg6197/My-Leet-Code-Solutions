def letterCombinations(self, digits: str) -> List[str]:
        phonebook = {
            '2' : list('abc'),
            '3' : list('def'),
            '4' : list('ghi'),
            '5' : list('jkl'),
            '6' : list('mno'),
            '7' : list('pqrs'),
            '8' : list('tuv'),
            '9' : list('wxyz')
        }
        if len(digits) == 1:
            return phonebook[digits]
        elif (digits) == '':
            return
        else:
            return [x + y for x in self.letterCombinations(digits[:-1]) for y in                                 self.letterCombinations(digits[-1])]
