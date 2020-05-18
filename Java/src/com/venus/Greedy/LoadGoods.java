package com.venus.Greedy;

import java.util.Arrays;

public class LoadGoods {
    public static void main(String[] args) {
        int[] goodWeights = {3, 5, 4, 10, 7, 14, 2, 11};
        int capacity = 30;
        new LoadGoods().load(goodWeights, capacity);
    }

    void load(int[] goods,int capacity) {
        if (capacity <= 0) return;
        if (goods.length == 0) return;

        Arrays.sort(goods);
        int restWeight = capacity;
        int count = 0;
        for (int i = 0; i < goods.length; i++) {
            if (restWeight >= goods[i]) {
                System.out.println("Load: " + goods[i]);
                restWeight -= goods[i];
                count ++;
            }
        }
        System.out.println("Loaded " + count + " goods");
    }
}
