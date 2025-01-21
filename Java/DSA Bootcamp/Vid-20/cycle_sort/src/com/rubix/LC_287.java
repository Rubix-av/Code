package com.rubix;

public class LC_287 {
    public static void main(String[] args) {
        int[] arr = {1, 3, 4, 2, 2};
        int duplicate = findDuplicate(arr);
        System.out.println(duplicate);
    }

    static int findDuplicate(int[] nums) {
        int i = 0;
        int duplicate_digit = 0;

        while (i < nums.length) {
            int correct = nums[i] - 1;

            if (nums[i] != nums[correct]) {
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            }
            else if ((nums[i] == nums[correct]) & (i!=correct)) {
                duplicate_digit = nums[i];
                break;
            } else {
                i++;
            }

        }

        return duplicate_digit;
    }


}
