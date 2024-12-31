package com.rubix;

import java.util.Arrays;
import java.util.Scanner;

public class MultiDimension {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

//        int[][] arr2D = {
//                {1, 2, 3}, //0th index
//                {4, 5, 6}, //1st index
//                {7, 8, 9} // 2nd index
//        };

        int[][] arr = new int[3][3];

        // input
        for (int row = 0; row < arr.length; row++) {
            for (int col = 0; col < arr[row].length; col++) {
                arr[row][col] = in.nextInt();
            }
        }

        // output
        for (int[] a : arr) {
            System.out.println(Arrays.toString(a));
        }

    }
}
