package com.rubix.staticExample;

public class Main {
    public static void main(String[] args) {
//        Human rubix = new Human(18, "Rubix", 100000, false);
//        Human rahul = new Human(34, "rahul", 15, true);
//        Human arpit = new Human(34, "arpit", 15, true);
//
//        System.out.println(Human.population);
    }

    // this is not dependent on objects
    static void fun() {
        // greeting(); // you can't use this because it requires an instance
        // but the function you are using it in does not depend on instances

        // To make "greeting()" work, we can do the following
        // You can't access non static stuff without referencing their instances in
        // a static context
        Main obj = new Main();
        obj.greeting();
    }

    // we know that something which is not static, belongs to an object
    void greeting() {
        System.out.println("Hello world");
    }
}
