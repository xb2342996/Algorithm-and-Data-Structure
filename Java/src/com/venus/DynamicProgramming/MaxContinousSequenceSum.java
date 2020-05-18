package com.venus.DynamicProgramming;

public class MaxContinousSequenceSum {
    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int sum = new MaxContinousSequenceSum().maxSubArray(nums);
        System.out.println(sum);
    }

    int maxSubArray(int[] nums) {
        int dp[] = new int[nums.length];
        dp[0] = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (dp[i - 1] <= 0){
                dp[i] = nums[i];
            } else {
                dp[i] = nums[i] + dp[i - 1];
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }
}
