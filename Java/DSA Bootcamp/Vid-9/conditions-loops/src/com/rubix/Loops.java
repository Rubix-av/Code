package com.rubix;

import java.util.Scanner;

public class Loops {
    public static void main(String[] args) {
        // Q: Print numbers from 1 to 5
//        for(int num=1; num<6; num++) {
//            System.out.println(num);
//        }

        // print numbers from 1 to n
        Scanner in = new Scanner(System.in);
//        int n = in.nextInt();

//        for (int num = 1; num <= n; num++) {
//            System.out.println(num + " ");
//        }

        // while loops
//        int num = 1;
//        while(num<=5) {
//            System.out.println(num);
//            num++;
//        }

        // do while loop
        /*
            Syntax: (Executes at least once)

            do {

            } while (condition);

        */
        int n = 1;
        do {
            System.out.println("Hello World");
        } while (n!=1);
    }
}
