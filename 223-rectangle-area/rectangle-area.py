class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:

        # Area of rectangle A
        area1 = (ax2 - ax1) * (ay2 - ay1)

        # Area of rectangle B
        area2 = (bx2 - bx1) * (by2 - by1)

        # Width and height of the overlapping region
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

        # Total area without counting overlap twice
        return area1 + area2 - (overlap_width * overlap_height)