package com.venus.Greedy;

import java.util.Arrays;

public class CoinExchange {
    public static void main(String[] args) {
        int[] coins = {25, 20, 5, 1};
        int money = 42;
        new CoinExchange().choose(coins, money);
    }

    void choose(int[] coins, int money) {
        Arrays.sort(coins);
        int restMoney = money;

        for (int i = coins.length - 1; i >= 0; i--) {
            if (restMoney < coins[i]) continue;
            System.out.println("select: " + coins[i]);
            restMoney -= coins[i];
            i = coins.length;
        }

    }
}
