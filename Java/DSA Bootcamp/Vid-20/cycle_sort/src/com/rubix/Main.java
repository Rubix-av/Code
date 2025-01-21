package com.rubix;

import java.util.Arrays;

/*
When given numbers from 1 to N, use Cyclic Sort
*/

public class Main {
    public static void main(String[] args) {
        int[] arr = {3, 5, 2, 4, 1};
        int[] sorted_arr = cyclicSort(arr);
        System.out.println(Arrays.toString(sorted_arr));
    }

    static int[] cyclicSort(int[] nums) {
        int i = 0;
        while (i < nums.length) {
            int correct = nums[i];
            if (nums[i] == nums.length) {
                i++;
                continue;
            }

            if (nums[i] != nums[correct]) {
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            } else {
                i++;
            }

        }

        return nums;
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}

/*
Worst case = O(N)
*/