def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            if orderalpha(i) not in anagrams.keys():
                anagrams[orderalpha(i)] = [i]                
            else:
                anagrams[orderalpha(i)].append(i)
        return anagrams.values()
        
def orderalpha(str):
    return ''.join(sorted(str))
