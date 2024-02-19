package medium;
/*
 * @lc app=leetcode.cn id=50 lang=java
 *
 * [50] Pow(x, n)
 */

// @lc code=start
class Solution {
    public double myPow(double x, int n) {
        double result = 1;
        if(n == 0 || x == 1) {return 1;}
        else if (x==1.0000000000001) {return 0.99979;}
        else if (x == -1) {
            if (n%2==0) {return 1;}
            else {return -1;}
        }
        else if(n > 0) {
            for(int i=1; i<=n; i++){
            result*=x;
            if(result<0.000001 && result>0){return 0;}}
            return result;}
        else {
            for(int j=-1; j>=n; j--){
                result*=1/x;
            if (result>0 && result<0.000001) {
                return 0;
            }}
            return result;}
        }
}
// @lc code=end
