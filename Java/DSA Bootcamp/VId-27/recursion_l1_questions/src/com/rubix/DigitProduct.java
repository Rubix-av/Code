package com.rubix;

public class DigitProduct {
    public static void main(String[] args) {
//        int ans = productDigit(12345);
//        System.out.println(ans);

        fun(5);

    }

    static int productDigit(int n) {
        if (n%10 == n) {
            return n;
        }

        return (n%10) * (productDigit(n/10));
    }

    static void fun(int n) {
        if (n == 0) {
            return;
        }

        System.out.println(n);
//        fun(n--); // First passes the value then subtracts
        fun(--n); // First subtracts the value then passes it
    }
}
