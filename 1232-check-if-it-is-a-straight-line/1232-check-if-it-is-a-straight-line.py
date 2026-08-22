class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2 == x1:
            for x, y in coordinates:
                if x != x1:
                    return False
            return True


        slop = (y2-y1) / (x2-x1)

        for i in range(2, len(coordinates)):
            x3,y3 = coordinates[i]

            if x3 == x1:
                return False   

            current_slop = (y3-y1) / (x3-x1)

            if current_slop != slop:
                return False

        return True                     