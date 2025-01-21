package com.rubix;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {5, 3, 4, 1, 2};
        int[] sorted_arr = insertionSort(arr);
        System.out.println(Arrays.toString(sorted_arr));
    }

    static int[] insertionSort(int[] arr) {

        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j-1] > arr[j]) {
                    swap(arr, j, j-1);
                }
            }
        }

        return arr;
    }

    // Function to swap elements in an array
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

/*
Worst case = O(N^2)
Best case = O(N)

Adaptive:
Steps get reduced if array is sorted.
Number of steps reduced as compared to bubble sort

Stable = Yes

Used for smaller value of N => Works good when array is partially sorted
*/
