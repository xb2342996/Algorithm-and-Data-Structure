package com.venus.SkipList;

public class SkipListTest {
    public static void main(String[] args) {
        skiplistTest();
    }

    public static void skiplistTest() {
        SkipList<Integer, Integer> sl = new SkipList<>();
        int count = 10;
        int delta = 10;
        for (int i = 0; i < count; i++) {
            sl.put(i, i + delta);
        }
        System.out.println(sl);
    }
}
