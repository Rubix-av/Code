package com.rubix;

public class NumbersExample {
    public static void main(String[] args) {
        // write a function that takes in a number and prints it
        // print first 5 numbers: 1 2 3 4 5

        print1(1);
    }

    static void print1(int n) {
        System.out.println(n);
        if (n < 5) print1(n+1);
    }
}
