package com.rubix.introduction;

public class Main {
    public static void main(String[] args) {
        Student rubix = new Student();
        Student abc = new Student();

//        System.out.println(rubix.rno);
//        System.out.println(rubix.name);
//        System.out.println(rubix.marks);

        rubix.greeting();
        abc.greeting();

    }
}

class Student {
    int rno;
    String name;
    float marks;

    Student() {
        this.rno = 13;
        this.name = "Akshobh Verma";
        this.marks = 88.5f;
    }

    void greeting() {
        System.out.println("Hello! My name is " + name);
    }
}
