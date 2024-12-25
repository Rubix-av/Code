package com.rubix;

public class StringExample {
    public static void main(String[] args) {
        String personalized = myGreet("Akshobh");
        System.out.println(personalized);
    }

    static String myGreet(String greet) {
        String message = "Hello " + greet;
        return message;
    }
}
