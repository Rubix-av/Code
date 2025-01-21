package com.rubix;

public class CeilingLetter {
    public static void main(String[] args) {
        char[] arr = {'c', 'f', 'j'};
        char target = 'f';

        char ans = CeilLetter(arr, target);
        System.out.println(ans);
    }

    static char CeilLetter(char[] arr, char target) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (target < arr[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return arr[low % arr.length ];
    }
}
