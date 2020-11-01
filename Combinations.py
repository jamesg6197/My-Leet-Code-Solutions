def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def fn(start, step, tmp):
            if step == k:
                ret.append(tmp)
                return
            
            for i in range(start,n+1):
                fn(i+1,step+1,tmp+[i])
                
        fn(1,0,[])
        return ret
