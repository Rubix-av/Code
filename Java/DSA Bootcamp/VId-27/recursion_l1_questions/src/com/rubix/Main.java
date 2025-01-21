package com.rubix;

import com.sun.source.tree.ErroneousTree;

public class Main {
    public static void main(String[] args) {
//        nToOne(5);
        OneToN(5);

    }

    static void nToOne(int num) {
        if (num == 0) {
            return;
        }

        System.out.println(num);
        nToOne(num-1);
    }

    static void OneToN(int num) {

        if (num == 0) {
            return;
        }

        OneToN(num - 1);
        System.out.println(num);
    }
}
