package com.rubix;

import java.util.Arrays;

public class VarArgs {
    public static void main(String[] args) {
//        fun(2, 3, 4, 5, 56, 87, 23, 45, 65);
        multiple(2, 3, "Kunal", "Rahul", "dvsegsdf");
    }

    static void multiple(int a, int b, String ...v) {
        System.out.println(a);
        System.out.println(b);
        System.out.println(Arrays.toString(v));
    }

    static void fun(int ...v) {
        System.out.println(Arrays.toString(v));
    }
}
