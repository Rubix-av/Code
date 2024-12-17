package com.rubix;

import java.util.Scanner;

public class NestedSwitch {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int empId = in.nextInt();
        String department = in.next();
        int[] temp = new int[];

        switch (empId) {
            case 1:
                System.out.println("Akshobh Verma");
                break;
            case 2:
                System.out.println("Rubix qub");
                break;
            case 3:
                switch (department) {
                    case "IT":
                        System.out.println("IT Department");
                        break;
                    case "Management":
                        System.out.println("Management Department");
                        break;
                    default:
                        System.out.println("No department entered");
                }
            default:
                System.out.println("Enter correct EmpID");
        }
    }
}
