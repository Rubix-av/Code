package com.rubix.properties.polymorphism;

public class Circle extends Shapes {

    // Used for checking if the function is overridden or not
    // function area is overriden hence we can apply this decorator
    @Override
    void area() {
        System.out.println("Area is pi * r * r");
    }

    // function below isn't overridden hence, override decorator will throw error
//    @Override
//    void area2() {
//        System.out.println("Not overridden function");
//    }
}
