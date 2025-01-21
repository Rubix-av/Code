package com.rubix;

public class EvenNumberDigits {
    public static void main(String[] args) {
        int[] nums = {12, 345, 2, 6, 7896};
        int[] nums2 = {555, 901, 482, 1771};

        int ans = evenNumDigits(nums);
        int ans2 = evenNumDigits(nums2);

        System.out.println(ans);
        System.out.println(ans2);
    }

    static int evenNumDigits(int[] arr) {
        int evenCount = 0;

        for (int num : arr) {
            int count = 0;
            while (num != 0) {
                num = num / 10;
                count++;
            }

            if (count%2 == 0) {
                evenCount++;
            }
        }

        return evenCount;
    }
}
