package com.rubix.introduction;

public class Main {
    public static void main(String[] args) {

        Student random = new Student();
        System.out.println(random.name);

        Student a = new Student();
        Student b = a;
        a.name = "xyz";
        System.out.println(b.name);
    }
}

class Student {
    int rno;
    String name;
    float marks = 90;

    void greeting() {
        System.out.println("Hello! My name is " + this.name);
    }

    void changeName(String name) {
        this.name = name;
    }

    Student () {
        // calling a constructor from another constructor
        // internally : new Student()
        this (13, "default person", 100.0f);
    }

    Student (int roll, String name, float marks) {
        this.rno = roll;
        this.name = name;
        this.marks = marks;
    }
}


