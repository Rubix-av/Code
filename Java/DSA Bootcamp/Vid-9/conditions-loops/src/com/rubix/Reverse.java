package com.rubix;

public class Reverse {
    public static void main(String[] args) {

        int n = 12345;
        String rev_digit = "";

        while (n > 0) {
            int last_dig = n%10;
            rev_digit += last_dig;

            n = n/10;
        }

        System.out.println(rev_digit);
    }
}
