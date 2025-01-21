package com.rubix;

import java.util.Arrays;

public class RichestCustomerWealth {
    public static void main(String[] args) {
        int[][] accounts = {{1, 2, 3}, {3, 2, 1}};
        int ans = richestCustomer(accounts);
        System.out.println(ans);
    }

    static int richestCustomer(int[][] arr) {
        int max_wealth = Integer.MIN_VALUE;
        for (int[] customer : arr) {
            int total_wealth = 0;
            for (int wealth : customer) {
                total_wealth += wealth;

                if (total_wealth > max_wealth) {
                    max_wealth = total_wealth;
                }
            }
        }

        return max_wealth;
    }
}
