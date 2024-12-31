package com.rubix;

import java.lang.reflect.Array;
import java.util.Scanner;

public class Input {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int[] arr = new int[5];
//        arr[0] = 23;
//        arr[1] = 45;
//        arr[2] = 233;
//        arr[3] = 543;
//        arr[4] = 3;

        for (int i = 0; i < arr.length; i++) {
            arr[i] = in.nextInt();
        }

        // Modify array at index 1
        // arr[1] = 99;

        for (int j : arr) {
            System.out.println(j);
        }
    }
}
