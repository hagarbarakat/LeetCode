class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        output = 0
        for i in range(len(boxTypes)): 
            if truckSize <= 0: 
                break
            elif truckSize >= boxTypes[i][0]: 
                output += boxTypes[i][0] * boxTypes[i][1]
            elif truckSize < boxTypes[i][0]: 
                output += truckSize * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
        return output
            