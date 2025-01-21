package com.rubix;

public class FindMin {
    public static void main(String[] args) {
        int[] nums = {34, 25, 62, 73, 4, 13, 32};
        int minNum = findMin(nums);
        int maxNum = findMax(nums);

        System.out.println("Min number: " + minNum);
        System.out.println("Max number: " + maxNum);
    }

    static int findMin(int[] arr) {
        int min = arr[0];

        for (int num : arr) {
            if (num < min) {
                min = num;
            }
        }

        return min;
    }

    static int findMax(int[] arr) {
        int max = arr[0];

        for (int num : arr) {
            if (num > max) {
                max = num;
            }
        }

        return max;
    }
}
