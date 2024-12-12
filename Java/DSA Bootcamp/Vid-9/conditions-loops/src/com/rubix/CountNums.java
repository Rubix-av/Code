package com.rubix;

import java.util.Scanner;

public class CountNums {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter the number: ");
        int n = in.nextInt();

        System.out.print("Enter the digit: ");
        int check_digit = in.nextInt();

        int count = 0;
        while(n > 0) {
            int digit = n%10;
            if(digit == check_digit) {
                count++;
            }
            n = n/10;
        }

        System.out.println(count);
    }
}
