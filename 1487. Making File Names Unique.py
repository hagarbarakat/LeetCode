class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        result = []
        for name in names:
            if name not in used: 
                used[name] = 1
                result.append(name)
            elif name in used: 
                k = used[name] 
                new_name = name + "("+str(k)+")"
                while new_name in used: 
                    k += 1 
                    new_name = name + "("+str(k)+")"
                used[name] = k 
                used[new_name] = 1
                result.append(new_name)
        return result