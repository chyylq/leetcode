class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        move from both ends towards center
        water trapped on the side in the determined by same side from the lower of the left, right bar 
        '''
        n = len(height)
        if n==0: return 0
        ileft = 0
        bar_left = height[ileft]
        iright = n-1
        bar_right = height[iright]
        water = [0]*n
        while (ileft<iright):
            if bar_left<height[ileft]:
                bar_left=height[ileft]
            if bar_right<height[iright]:
                bar_right=height[iright]                
            if bar_left<=bar_right:
                water[ileft] = bar_left - height[ileft]
                ileft = ileft+1
            else:
                water[iright] = bar_right - height[iright]
                iright=iright-1
        return sum(water)

m = Solution()
s = [1,0,1,0,2,1,0,1,3,2,1,2,1]
print(m.trap(s))    