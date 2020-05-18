package com.venus.DynamicProgramming;

public class CoinExchange {
    
    int[] coins = {25, 20, 5, 1};
    int[] coinTable;

    public static void main(String[] args) {
//        int num_coins = new CoinExchange().recursive(41);
//        int num_coins = new CoinExchange().memorySearch(100);
        int num_coins = new CoinExchange().coins(100);
        System.out.println(num_coins);
    }

    int recursive(int money) {
        if (money < 1) return Integer.MAX_VALUE;
        if (money == 1 || money == 20 || money == 25 || money == 5) return 1;
        int min1 = Math.min(recursive(money - 1), recursive(money - 5));
        int min2 = Math.min(recursive(money - 20), recursive(money - 25));

        return Math.min(min1, min2) + 1;
    }

    int memorySearch(int money) {
        coinTable = new int[money + 1];
        for (int c: coins) {
            if (c > money) break;
            coinTable[c] = 1;
        }
        return search(money);
    }
    int search(int money){
        if (money < 1) return Integer.MAX_VALUE;
        if (coinTable[money] == 0){
            int min1 = Math.min(search(money - 1), search(money - 5));
            int min2 = Math.min(search(money - 20), search(money - 25));
            coinTable[money] = Math.min(min1, min2) + 1;
        }

        return coinTable[money];
    }

    int coins(int money) {
        if (money < 1) return -1;
        coinTable = new int[money + 1];
        for (int i = 1; i <= money; i++) {
            int min = Integer.MAX_VALUE;
            for (int c: coins) {
                if (c > i) continue;
                int v = coinTable[i - c];
                if (v < 0 || v >= min) continue;
                min = v;
            }
            if (min == Integer.MAX_VALUE) {
                coinTable[i] = -1;
            }else {
                coinTable[i] = min + 1;
            }
        }
        return coinTable[money];
    }
}
