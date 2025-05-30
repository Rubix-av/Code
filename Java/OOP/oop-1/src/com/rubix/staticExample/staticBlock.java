package com.rubix.staticExample;

// this is a demo to show initialisation of static variables
public class staticBlock {
    static int a = 4;
    static int b;

    // will only run once, when the first obj is created i.e. when the class is loaded
    static {
        System.out.println("I am in static block");
        b = a * 5;
    }

    public static void main(String[] args) {
        staticBlock obj = new staticBlock();
        System.out.println(staticBlock.a + " " + staticBlock.b);

        staticBlock.b += 3;

        staticBlock obj2 = new staticBlock();
        System.out.println(staticBlock.a + " " + staticBlock.b);
    }
}
