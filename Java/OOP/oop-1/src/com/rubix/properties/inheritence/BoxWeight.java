package com.rubix.properties.inheritence;

public class BoxWeight extends Box{
    double weight;

    public BoxWeight() {
        this.weight = -1;
    }

    static void greeting() {
        System.out.println("Hey, I am in BoxWeight class. Greetings!");
    }

    public BoxWeight(double l, double h, double w, double weight) {
        super(l, h, w);
        this.weight = weight;
    }

    public BoxWeight(BoxPrice other) {
    }
}
