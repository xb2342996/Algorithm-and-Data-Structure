package com.venus.DynamicProgramming;

public class LongestCommonSubstring {
    public static void main(String[] args) {
        int ans = new LongestCommonSubstring().lcs("ABCBA", "BABCA");
        System.out.println(ans);
    }

    int lcs(String str1, String str2){
        if (str1 == null || str1.length() == 0) return 0;
        if (str2 == null || str2.length() == 0) return 0;
        char[] chars1 = str1.toCharArray();
        char[] chars2 = str2.toCharArray();
        int len1 = chars1.length;
        int len2 = chars2.length;

        int max = Integer.MIN_VALUE;
        int dp[][] = new int[len1 + 1][len2 + 1];
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (chars1[i-1] == chars2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    max = Math.max(max, dp[i][j]);
                }
            }
        }
        return max;
    }
}
