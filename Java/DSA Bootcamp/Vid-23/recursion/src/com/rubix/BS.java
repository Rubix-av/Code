package com.rubix;

public class BS {
    public static void main(String[] args) {
        int[] arr = {4, 35, 38, 45, 47, 61, 62, 99};

        int target = 47;
        int s = 0;
        int e = arr.length - 1;

        int ans = search(arr, target, s, e);
        System.out.println(ans);
    }

    static int search(int[] arr, int target, int s, int e) {

        if (s > e) {
            return -1;
        }

        int m = s + (e - s) / 2;

        if(arr[m] == target) {
            return m;
        }

        if (target < arr[m]) {
             return search(arr, target, s, m - 1);
        }

        return search(arr, target, m + 1, e);

    }
}
