package easy;
/*
 * @lc app=leetcode.cn id=69 lang=java
 *
 * [69] x 的平方根 
 */

// @lc code=start
class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        else{
            double epsilon = 0.0000000000001;
            double s = x;
            while (true) {
            double nexts = 0.5*(s+x/s);
            if (Math.abs(s-nexts) < epsilon) {
                break;
            }
            s = nexts;
            }
            return (int)s;
        }
        
    }
}
// @lc code=end

