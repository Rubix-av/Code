package com.rubix;

public class Factorial {
    public static void main(String[] args) {
        int ans = factorial(5);
        System.out.println(ans);
    }

    static int factorial(int num) {
        if (num <= 1 ) {
            return 1;
        }

        return num * factorial(num - 1);
    }
}
