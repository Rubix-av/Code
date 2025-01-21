package com.rubix;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {3, 1, 5, 4, 2};

        int[] sorted_arr = bubbleSort(arr);

        System.out.println(Arrays.toString(sorted_arr));
    }

    static int[] bubbleSort(int[] arr) {

        for (int i=0; i < arr.length; i++) {

            boolean swapped = false;

            for (int j=0; j < arr.length - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;

                    swapped = true;
                }
            }

            if (!swapped) break;
        }

        return arr;
    }
}

/*
Bubble sort is a stable algorithms, i.e., order of elements is preserved
*/