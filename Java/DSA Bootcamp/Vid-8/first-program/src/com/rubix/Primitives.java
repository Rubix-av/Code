/*
Primitive dtypes = like int, char, float, double, long, boolean cannot be further
                   splitted.
                   Ex, int rollno = 64 | char letter = 'r' | boolean check = false

Non-Primitive dtypes = like String, Integer, Boolean can be further splitted (String)
                       provides multiple methods for the object of these class.
                       Ex, String name = "Akshobh" | Integer age = 64
*/
package com.rubix;

public class Primitives {
    public static void main(String[] args) {
        int rollno = 64; // 4 bytes
        char letter = 'r';
        float marks = 98.67f; // 4 bytes
        double largeDecimalNumbers = 3254525.452; // 8 bytes
        long largeIntegerValues = 46345452453535L; // 8 bytes
        boolean check = true; // or false

        // String is not primitive
        String name = "Akshobh";
    }
}
