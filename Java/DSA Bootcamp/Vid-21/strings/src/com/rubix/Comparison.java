package com.rubix;

public class Comparison {
    public static void main(String[] args) {
        String a = "Akshobh";
        String b = "Akshobh";

        // checks for value and if reference variables are pointing to same object
        System.out.println(a == b); // true

        // creating a new object in with same value
        // strings are created in heap but outside the string pool
        String c = new String("Akshobh");
        String d = new String("Akshobh");

        // value is same but both reference variables are pointing to diff. objects
        System.out.println(c == d); // false

        // to only compare the values (.equals())
        System.out.println(c.equals(d)); // true
    }
}
