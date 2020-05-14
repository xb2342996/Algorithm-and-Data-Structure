package com.venus.Map;

import com.venus.Map.model.Key;
import com.venus.Map.model.SubKey1;
import com.venus.Map.model.SubKey2;

public class MapTest {
    public static void main(String[] args) {
//        treemapTest();

//        hashmapTest();
        linkedhashmapTest();
    }


    public static void linkedhashmapTest() {

        LinkedHashMap<Object, Integer> map = new LinkedHashMap<>();

//        test2(map);
//        test3(map);
        test4(map);

        map.travesal(new HashMap.Visitor<Object, Integer>() {
            @Override
            public boolean visit(Object key, Integer value) {
                System.out.println(key +": " + value);
                return false;
            }
        });
//        test5(map);
    }

    public static void hashmapTest() {
        HashMap<Object, Integer> map = new HashMap<>();

        test2(map);
        test3(map);
        test4(map);
        test5(map);
    }

    static void test2(HashMap<Object, Integer> map) {
        for (int i = 1; i <= 20; i++) {
            map.put(new Key(i), i);
        }
        for (int i = 5; i <= 7; i++) {
            map.put(new Key(i), i + 5);
        }

        System.out.println(map.size() == 20);
        System.out.println(map.get(new Key(4)) == 4);
        System.out.println(map.get(new Key(5)) == 10);
        System.out.println(map.get(new Key(6)) == 11);
        System.out.println(map.get(new Key(7)) == 12);
        System.out.println(map.get(new Key(8)) == 8);
    }

    static void test3(HashMap<Object, Integer> map) {
        map.put(null, 1); // 1
        map.put(new Object(), 2); // 2
        map.put("jack", 3); // 3
        map.put(10, 4); // 4
        map.put(new Object(), 5); // 5
        map.put("jack", 6);
        map.put(10, 7);
        map.put(null, 8);
        map.put(10, null);
        System.out.println(map.size() == 5);
        System.out.println(map.get(null) == 8);
        System.out.println(map.get("jack") == 6);
        System.out.println(map.get(10) == null);
        System.out.println(map.get(new Object()) == null);
        System.out.println(map.containsKey(10));
        System.out.println(map.containsKey(null));
        System.out.println(map.containsValue(null));
        System.out.println(map.containsValue(1) == false);
    }

    static void test4(HashMap<Object, Integer> map) {
        map.put("jack", 1);
        map.put("rose", 2);
        map.put("jim", 3);
        map.put("jake", 4);
        map.remove("jack");
        map.remove("jim");
        for (int i = 1; i <= 10; i++) {
            map.put("test" + i, i);
            map.put(new Key(i), i);
        }
        for (int i = 5; i <= 7; i++) {
            System.out.println(map.remove(new Key(i)) == i);
        }
        for (int i = 1; i <= 3; i++) {
            map.put(new Key(i), i + 5);
        }
//        System.out.println(map.size() == 19);
//        System.out.println(map.get(new Key(1)) == 6);
//        System.out.println(map.get(new Key(2)) == 7);
//        System.out.println(map.get(new Key(3)) == 8);
//        System.out.println(map.get(new Key(4)) == 4);
//        System.out.println(map.get(new Key(5)) == null);
//        System.out.println(map.get(new Key(6)) == null);
//        System.out.println(map.get(new Key(7)) == null);
//        System.out.println(map.get(new Key(8)) == 8);
        map.travesal(new HashMap.Visitor<Object, Integer>() {
            public boolean visit(Object key, Integer value) {
                System.out.println(key + "_" + value);
                return false;
            }
        });
    }

    static void test5(HashMap<Object, Integer> map) {
        for (int i = 1; i <= 20; i++) {
            map.put(new SubKey1(i), i);
        }
        map.put(new SubKey2(1), 5);
        System.out.println(map.get(new SubKey1(1)) == 5);
        System.out.println(map.get(new SubKey2(1)) == 5);
        System.out.println(map.size() == 20);
    }
    
    public static void treemapTest() {
        Map<String, Integer> map = new TreeMap<>();
        // put
        map.put("Sun", 123);
        map.put("Venus", 15);
        map.put("Earth", 223);
        map.put("Black Holl", 62);
        map.put("Mercury", 77);
        map.put("Mercury", 98);
        // get
        System.out.println(map.get("Sun"));
        System.out.println(map.get("Mars"));
        // remove
        map.remove("Sun");
        map.remove("Mars");
        // contains
        System.out.println(map.containsKey("Earth"));
        System.out.println(map.containsKey("Mars"));
        System.out.println(map.containsValue(77));
        System.out.println(map.containsValue(98));
        // travesal
        map.travesal(new Map.Visitor<String, Integer>() {
            @Override
            public boolean visit(String key, Integer value) {
                System.out.println(key + ", " + value);
                return false;
            }
        });
    }
}
