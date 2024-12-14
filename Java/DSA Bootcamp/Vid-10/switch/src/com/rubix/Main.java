package com.rubix;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
//        String fruit = in.next();

        /*
            Syntax:
            switch (expression) {

                //cases
                case one:
                    //do something
                    break;

                case two:
                    //do something
                    break;

                default:
                    //do something
            }
        */

//        switch (fruit) {
//            case "Mango" -> System.out.println("King of fruits");
//            case "Apple" -> System.out.println("A sweet red fruit");
//            case "Orange" -> System.out.println("Round fruit");
//            case "Grapes" -> System.out.println("Small fruit");
//            default -> System.out.println("Please enter a valid fruit");
//        }

        int day = in.nextInt();

        switch(day) {
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> System.out.println("Enter a valid day");
        }

        switch (day) {
            case 1,2,3,4,5 -> System.out.println("Weekday");
            case 6,7 -> System.out.println("Weekend");
            default -> System.out.println("Enter a valid day");

        }
    }
}
