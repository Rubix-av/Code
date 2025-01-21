package com.rubix;

public class Fibonacci {
    public static void main(String[] args) {
        fibo(50);
    }

    static int fibo(int n) {

        if (n < 2) {
            return n;
        }

        return fibo(n-1) + fibo(n-2);
    }
}
