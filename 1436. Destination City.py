class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap = {}
        for i in range(len(paths)):
            # key -> start , value -> destination 
            if paths[i][0] not in hashmap: 
                hashmap[paths[i][0]] = paths[i][1]
        for i in range(len(paths)): 
            if paths[i][1] not in hashmap:
                return paths[i][1]

#-------------------------------------------
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityPaths = {}
        for path in paths:
            cityPaths[path[0]] = path[1]
        
        for city in cityPaths.values():
            if city not in cityPaths:
                return city