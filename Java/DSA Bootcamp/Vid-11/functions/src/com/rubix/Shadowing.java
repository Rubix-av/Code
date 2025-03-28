package com.rubix;

public class Shadowing {
    static int x = 90; // this will be shadowed at line 7
    public static void main(String[] args) {
        System.out.println(x); // 90
        int x = 40; // the class variable at line 4 will be shadowed by this
        System.out.println(x); // 40
        fun();
    }

    static void fun() {
        System.out.println(x); // 90
    }
}
