     if len(coordinates) == 2:
            return True
        x1,y1 = coordinates[0][0],coordinates[0][1]
        x2,y2 = coordinates[1][0],coordinates[1][1]
        if x2-x1 == 0:
            return False
        diff = (y2-y1)/(x2-x1)
        i = 2
        while i < len(coordinates):
            if coordinates[i][0] - coordinates[i-1][0] == 0:
                return False
            diff_ = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
            if diff_ != diff:
                return False
            i += 1
        return True