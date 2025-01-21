package com.rubix;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {4, 5, 1, 2, 3};
        int[] sorted_arr = selectionSort(arr);
        System.out.println(Arrays.toString(sorted_arr));
    }

    static int[] selectionSort(int[] arr) {

        for (int i = arr.length-1; i > 0; i--) {
            int max = Integer.MIN_VALUE;
            int max_pos = 0;

            for (int j = 0; j <= i; j++) {
                if (arr[j] >= max) {
                    max = arr[j];
                    max_pos = j;
                }
            }

            int temp = arr[max_pos];

            arr[max_pos] = arr[i];
            arr[i] = temp;
        }

        return arr;
    }
}

/*
Worst Case = O(N^2)
Best Case = O(N^2)
Stable = No

It performs well on small lists
*/
