package com.rubix.interfaces;

public class Main {
    public static void main(String[] args) {

        // Engine determines what properties car will take
        // Car() determines from where it will take those properties
//        Engine car = new Car();
//
//        car.start();
//        car.accelerate();
//        car.stop();
//
//        Media carMedia = new Car();
//        carMedia.stop();

        NiceCar car = new NiceCar();
        car.start();
        car.startMusic();
        car.upgradeEngine();
        car.start();

    }
}

// Don't use interfaces casually in performance critical code
