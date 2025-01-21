package com.rubix;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC_645 {
    public static void main(String[] args) {
        int[] arr = {3, 2, 2};
        int[] sorted_arr = cyclicSort(arr);
        System.out.println(Arrays.toString(sorted_arr));
    }

    static int[] cyclicSort(int[] nums) {
        int i = 0;
        while (i < nums.length) {
            int correct = nums[i]-1;

            if (nums[i] != nums[correct]) {
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            } else {
                i++;
            }

        }

        int[] mismatch = new int[2];

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j+1) {
                mismatch[0] = nums[j];
                mismatch[1] = j+1;
            }
        }

        return mismatch;
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}
