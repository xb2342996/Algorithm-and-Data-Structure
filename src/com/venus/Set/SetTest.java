package com.venus.Set;

public class SetTest {
    public static void main(String[] args) {
//        listsetTest();
        treesetTest();
    }
    public static void treesetTest() {
        TreeSet<Integer> set = new TreeSet<>();

        set.add(0);
        set.add(1);
        set.add(1);
        set.add(4);
        set.add(2);
        set.add(4);
        set.travesal(new Set.Visitor<Integer>() {
            @Override
            public boolean visit(Integer element) {
                System.out.println(element);
                return false;
            }
        });
    }
    public static void listsetTest() {
        ListSet<Integer> set = new ListSet<>();

        set.add(0);
        set.add(0);
        set.add(1);
        set.add(1);
        set.add(2);
        set.add(2);
        set.travesal(new Set.Visitor<Integer>() {
            @Override
            public boolean visit(Integer element) {
                System.out.println(element);
                return false;
            }
        });
    }
}
