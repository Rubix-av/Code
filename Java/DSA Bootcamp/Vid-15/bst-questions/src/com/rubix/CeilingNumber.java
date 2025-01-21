package com.rubix;

public class CeilingNumber {
    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 9, 11, 12, 14, 20, 36, 48};
        int target = 34;

        int ans = binarySearch(arr, target);
        System.out.println(ans);
    }

    static int binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2; // Avoids overflow

            if (target == arr[mid]) {
                return arr[mid];
            }
            if (target > arr[mid]) {
                low = mid + 1;

            } else {
                high = mid - 1;
            }
        }

        if (low == arr.length) {
            return -1;
        }
        return arr[low]; // Target not found
    }
}
