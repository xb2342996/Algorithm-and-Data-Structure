package com.venus.DivideConquer;

public class LCSsum {
    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        new LCSsum().brutalForce(nums);
        new LCSsum().brutalForce_Op(nums);
        new LCSsum().maxSubArray(nums);
    }

    void brutalForce(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }
                maxSum = Math.max(maxSum, sum);
            }
        }
        System.out.println("MAXSUM: " + maxSum);
    }

    void brutalForce_Op(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                maxSum = Math.max(maxSum, sum);
            }
        }
        System.out.println("MAXSUM: " + maxSum);
    }

    void maxSubArray(int[] nums) {
        
        int maxValue = maxSubArray(0, nums.length, nums);
        System.out.println("MAXSUM: "+maxValue);
    }
    int maxSubArray(int left, int right, int[] nums) {
        if (left == right - 1) {
            return nums[left];
        }

        int mid = (left + right) >> 1;
        int rightMax = Integer.MIN_VALUE;
        int rightSum = 0;
        for (int i = mid; i < right; i++) {
            rightSum += nums[i];
            rightMax = Math.max(rightMax, rightSum);
        }

        int leftMax = Integer.MIN_VALUE;
        int leftSum = 0;
        for (int i = mid - 1; i >= 0; i--) {
            leftSum += nums[i];
            leftMax = Math.max(leftMax, leftSum);
        }

        return Math.max(leftMax + rightMax, Math.max(maxSubArray(left, mid, nums), maxSubArray(mid, right, nums)));
    }
}
