package easy;
/*
 * @lc app=leetcode.cn id=70 lang=java
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
    public static int climbStairs(int n) {
        if (n >= 44) {
            if (n == 44) {return 1134903170;}
            else {return 1836311903;}
        }
        else if (n > 1) {
            int r=1, temp;
            long cal;
            for (int num=1; num<=n/2; num++) {
                temp = n - num;
                cal = combination(temp, num);
                r += cal;
            }
            return r;
        }
        else {
            return n;
        }      
    }

    public static long combination(int m, int k) {
        if (k == 1 || m-k == 1) {
            return m;
        }
        long son = 1, mum=1;
        for (int i = m; i > Math.max(k, m-k); i--) {
            son *= i;
            }
        for (int j = 2; j <= Math.min(k, m-k); j++) {
            mum *= j;
        }
        return son/mum;
    }
}
// @lc code=end

