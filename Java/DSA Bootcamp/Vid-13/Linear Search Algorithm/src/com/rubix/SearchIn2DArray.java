package com.rubix;

import java.util.Arrays;

public class SearchIn2DArray {
    public static void main(String[] args) {
        int[][] arr = {
                {23, 4, 1},
                {18, 12, 3, 9},
                {78, 99, 34, 56},
                {18, 12}
        };
        int target = 182;

        boolean ans = searchIn2D(arr, target);
        System.out.println(ans);

    }

    static boolean searchIn2D(int[][] arr2D, int target) {
        for (int i = 0; i < arr2D.length; i++) {
            for (int num : arr2D[i]) {
                if (num == target) {
                    return true;
                }
            }
        }

        return false;
    }
}
