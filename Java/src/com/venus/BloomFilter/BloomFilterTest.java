package com.venus.BloomFilter;

public class BloomFilterTest {
    public static void main(String[] args) {
        filterTest();
    }
    public static void filterTest() {
        BloomFilter<Integer> bf = new BloomFilter<>(10000000, 0.01);
        for (int i = 1; i <= 10000000; i++) {
            bf.put(i);
        }
        int count = 0;
        for (int i = 10000001; i <= 20000000; i++) {
            if (bf.contains(i)){
                count++;
            }
        }
        System.out.println(count);
    }
}
