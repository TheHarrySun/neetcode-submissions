class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(smaller) - 1
        while True:
            m = l + (r - l) // 2
            m2 = half - m - 2
            
            Aleft = smaller[m] if m >= 0 else float("-infinity")
            Aright = smaller[m + 1] if m + 1 < len(smaller) else float("infinity")

            Bleft = larger[m2] if m2 >= 0 else float("-infinity")
            Bright = larger[m2 + 1] if m2 + 1 < len(larger) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1