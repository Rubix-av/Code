package com.rubix;

public class CheckPalindrome {
    public static void main(String[] args) {
        String a = "abcdcba";
        String b = "abcdef";

        boolean ans1 = isPalindrome(a);
        System.out.println(ans1);

        boolean ans2 = isPalindrome(b);
        System.out.println(ans2);
    }

    static boolean isPalindrome(String str) {
        str = str.toLowerCase();
        if (str.length() % 2 == 0) {
            return false;
        }

        for (int i = 0; i < str.length() / 2; i++) {
            char start = str.charAt(i);
            char end = str.charAt(str.length() - i - 1);

            if (start != end) {
                return false;
            }
        }

        return true;
    }
}
