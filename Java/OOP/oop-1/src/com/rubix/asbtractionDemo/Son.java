package com.rubix.asbtractionDemo;

public class Son extends Parent{

    public Son(int age) {
        this.age = age;
    }

    @Override
    void career() {
        System.out.println("I am going to be a doctor");
    }

    @Override
    void partner() {
        System.out.println("I love Spider Man");
    }
}
