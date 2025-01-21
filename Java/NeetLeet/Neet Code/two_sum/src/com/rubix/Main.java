package com.rubix;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        int k = 2;

        HashMap<Integer, Integer> myMap = new HashMap<>();
        int[] ans = new int[k];

        for (int i = 0; i < nums.length; i++) {
            if (myMap.get(nums[i]) == null) {
                myMap.put(nums[i], 1);
            } else {
                myMap.put(nums[i], myMap.get(nums[i]) + 1);
            }
        }
        System.out.println(myMap);
        System.out.println(myMap.values());
        System.out.println(myMap.keySet());
        List<Integer> mapList = new ArrayList<>(myMap.keySet());

        for (int i = mapList.size() - k, j = 0; i < mapList.size(); i++, j++) {
            ans[j] = mapList.get(i);
        }

        System.out.println(Arrays.toString(ans));
    }

}
