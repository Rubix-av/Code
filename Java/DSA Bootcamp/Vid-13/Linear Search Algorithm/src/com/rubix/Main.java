package com.rubix;

public class Main {
    public static void main(String[] args) {
        int[] nums = {23, 45, 1, 2, 8, 19, -3, 16, -11, 28};
        int target = 19;
        boolean ans = linearSearchAlg(nums, target);
        System.out.println(ans);
    }

    static boolean linearSearchAlg(int[] arr, int target) {
        if (arr.length == 0) {
            return false;
        }

        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }

        return false;
    }
}
