package com.rubix;

import java.util.Arrays;

public class Methods {
    public static void main(String[] args) {
        String name = "Akshobh Verma";
        System.out.println(Arrays.toString(name.toCharArray()));
        System.out.println(name.toLowerCase());
        System.out.println(name);
        System.out.println(name.toUpperCase());
        System.out.println(name);
        System.out.println(name.indexOf('h')); // returns index of first occurrence
        System.out.println("      Akshobh".strip());
        System.out.println(Arrays.toString(name.split(" ")));
    }
}
