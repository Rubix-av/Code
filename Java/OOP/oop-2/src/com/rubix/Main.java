package com.rubix;

public class Main {
    public static void main(String[] args) {
        A obj = new A("asefsadf");
        System.out.println(obj);
    }
}

class A {
    final int num = 10;
    String name;

    public A(String name) {
        this.name = name;
    }
}
