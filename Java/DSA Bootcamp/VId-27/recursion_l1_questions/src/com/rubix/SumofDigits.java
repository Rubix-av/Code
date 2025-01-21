package com.rubix;

public class SumofDigits {
    public static void main(String[] args) {
        int ans = sumDigits(1234);
        System.out.println(ans);
    }

    static int sumDigits(int n) {

        if (n == 0) {
            return 0;
        }

        return (n%10) + (sumDigits(n/10));
    }
}
