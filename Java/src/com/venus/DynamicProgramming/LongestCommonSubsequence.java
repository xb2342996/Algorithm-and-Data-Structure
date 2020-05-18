package com.venus.DynamicProgramming;

public class LongestCommonSubsequence {
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 5, 9, 10, 14, 15, 16};
        int[] nums2 = {1, 4, 9, 10, 12, 15, 16};
//        int ins = new LCS().lcs_recursive(nums1, nums2);
//        int ins = new LCS().lcs_dp(nums1, nums2);
        int ins = new LongestCommonSubsequence().lcs_dp_space(nums1, nums2);
        System.out.println(ins);
    }
    int lcs_recursive(int[] nums1, int[] nums2) {
        if (nums1 == null || nums1.length < 1) return 0;
        if (nums2 == null || nums2.length < 1) return 0;
        return lcs(nums1, nums1.length, nums2, nums2.length);
    }

    int lcs(int[] nums1, int i, int[] nums2, int j) {
        if (i == 0 || j == 0) return 0;

        if (nums1[i-1] == nums2[j-1]) {
            return lcs(nums1, i - 1, nums2, j - 1) + 1;
        }else {
            return Math.max(lcs(nums1, i, nums2, j-1), lcs(nums1, i-1, nums2, j));
        }
    }

    int lcs_dp(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0) return 0;
        int[][] dp = new int[nums1.length+1][nums2.length+1];
        for (int i = 1; i < nums1.length + 1; i++) {
            for (int j = 1; j < nums2.length + 1; j++) {
                if (nums1[i - 1] == nums2[j - 1]){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[nums1.length][nums2.length];
    }
    int lcs_dp_space(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0) return 0;
        int arrayLength;
        if (nums1.length > nums2.length) {
            arrayLength = nums2.length;
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        } else {
            arrayLength = nums1.length;
        }
        int leftTop = 0;
        int[] dp = new int[arrayLength+1];
        for (int i = 1; i < nums2.length + 1; i++) {
            for (int j = 1; j < nums1.length + 1; j++) {
                if (nums2[i - 1] == nums1[j - 1]){
                    dp[j] = leftTop + 1;
                }else {
                    leftTop = dp[j];
                    dp[j] = Math.max(dp[j-1], dp[j]);
                }
            }
        }

        return dp[arrayLength];
    }
}
