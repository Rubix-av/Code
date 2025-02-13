package com.rubix.access;

public class A {
    protected int num;
    String name;
    int[] arr;

    // when no access modifier is specified, the scope is limited to the package only
    // meaning it will be only available to the files in same package

    // public can be accessed anywhere

    // since num is private, it can't be accessed or modified outside this file hence we use setter & getter

    // getter
    public int getNum() {
        return num;
    }

    // setter
    public void setNum(int num) {
        this.num = num;
    }

    public A(int num, String name) {
        this.num = num;
        this.name = name;
        this.arr = new int[num];
    }
}
