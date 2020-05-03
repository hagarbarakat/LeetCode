class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        for i in range(len(list1)):
            dic[list1[i]] = i
        result = []
        mini = sys.maxint
        s = 0
        for j in range(len(list2)):
            if  j <= mini:
                if list2[j] in dic:
                    s = j + dic[list2[j]]
                    if s < mini:
                        del result[:]
                        result.append(list2[j])
                        mini = s
                    elif s == mini:
                        result.append(list2[j])
        return result