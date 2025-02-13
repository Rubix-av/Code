package com.rubix.introduction;

public class WrapperExample {
    public static void main(String[] args) {

        // swap won't work because reference variable isn't passed instead only the value is passed
//        int a = 10;
//        int b = 20;
//
//        Integer num = 45;

        // this too won't work because of the "final" keyword
//        Integer a = 10;
//        Integer b = 20;

//        swap(a, b);

        // can't change the value of variable after using "final" keyword
        // always initialize while declaring "final" keyword
        // holds true for primitive datatype
        final int BONUS = 2;

        // for non-primitive datatype, value can be changed, but can't be reinitialized
        // final Student rubix = new Student();
        // rubix.name = "new name";
        // but can't do (rubix = other object) with non-premitive datatypes

//        System.out.println(a + " " + b);

        A obj;

        for (int i = 0; i < 1000000000; i++) {
            obj = new A("Random name");
        }
    }

    static void swap (Integer a, Integer b) {
        int temp = a;
        a = b;
        b = temp;
    }
}

class A {
    final int num = 10;
    String name;

    public A(String name) {
        this.name = name;
    }

    // after garbage collection clears the object, the following method is triggered
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Object is destryoed");
    }
}