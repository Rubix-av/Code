package com.rubix.interfaces;

public class Car implements Engine, Brake, Media{

    int a = 30;

    @Override
    public void brake() {
        System.out.println("It brake like a normal car");
    }

    @Override
    public void start() {
        System.out.println("It start like a normal car");
    }

    @Override
    public void stop() {
        System.out.println("It stop like a normal car");
    }

    @Override
    public void accelerate() {
        System.out.println("It accelerates like a normal car");
    }
}
