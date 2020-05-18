package com.venus.DynamicProgramming;

public class LongestIncreasingSubSequence {
    public static void main(String[] args) {
        int[] nums = {10, 2, 2, 5, 1, 7, 101, 18};
        int max = new LongestIncreasingSubSequence().lis(nums);
        System.out.println(max);
    }

    int lis(int[] nums) {
        if (nums == null || nums.length < 1) return -1;
        int dp[] = new int[nums.length];
        dp[0] = 1;
        int max = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }
}
