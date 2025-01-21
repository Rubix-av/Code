package com.rubix;

import java.util.ArrayList;

public class Operators {
    public static void main(String[] args) {
        System.out.println('a' + 'b');
        System.out.println("a" + "b");
        System.out.println((char)('a' + 3));
        System.out.println("a" + 1);
        System.out.println("Akshobh" + new ArrayList<>());
        System.out.println("Akshobh" + new Integer(56));
        System.out.println(new Integer(56) + "" + new ArrayList<>());
    }
}
