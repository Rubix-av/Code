package com.rubix;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();
        int age = input.nextInt();
        System.out.printf("Your name is %s and you are %d years old", name, age);
    }
}
