package com.rubix.asbtractionDemo;

public class Main {
    public static void main(String[] args) {
        Son son = new Son(18);
        son.career();

        Daughter daughter = new Daughter(39);
        daughter.career();

        // cannot create objects of an abstract class
        // Parent parent = new Parent();
    }
}
