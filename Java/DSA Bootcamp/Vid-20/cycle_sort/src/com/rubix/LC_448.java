package com.rubix;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class LC_448 {
    public static void main(String[] args) {
        int[] arr = {4,3,2,7,8,2,3,1};
        List<Integer> sorted_arr = findDisappearedNumbers(arr);
        System.out.println(sorted_arr);
    }

    static List<Integer> findDisappearedNumbers(int[] nums) {
        int i = 0;

        while (i < nums.length) {
            int correct = nums[i] - 1;

            if (nums[i] != nums[correct]) {
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            }
            else if ((nums[i] == nums[correct]) & (i!=correct)) {
                i++;
                continue;
            } else {
                i++;
            }

        }

        List<Integer> missing_vals = new ArrayList<>();

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j+1) {
                missing_vals.add(j+1);
            }
        }

        return missing_vals;
    }
}

