package com.venus.List;

import com.venus.List.*;

public class ListTest {
    public static void main(String[] args) {

    }

    public void doubleCycleLinkedListTest() {
        DoublyCycleLinkedList<Integer> list = new DoublyCycleLinkedList<>();
        list.add(1);
        list.add(2);
        list.add(14);
        list.add(17);
        list.add(20);
        System.out.println(list);

        list.add(53, 2);
        list.add(90, 0);
        System.out.println(list);
//        list.remove(3);
        list.remove(6);
//        list.remove(0);
//        list.remove(-1);
//        list.remove(7);
        System.out.println(list);
    }

    public void doublyLinkedListTest() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<Integer>();
        // add
//        list.add(9);
//        list.add(3);
//        list.add(4);
//        list.add(1);
//        list.add(8);
//
//        list.add(100, 0);
        list.add(20, -1);
        System.out.println(list);

        // remove
        list.remove(0);
        System.out.println(list);
        list.remove(5);
        System.out.println(list);
        list.remove(3);
        System.out.println(list);
//        list.remove(-1);
//        System.out.println(list);
//        list.remove(4);
//        System.out.println(list);

        // indexOf
        System.out.println(list.indexOf(4));
        System.out.println(list.indexOf(15));

        // get & set
        System.out.println(list.get(list.size()-1));
        System.out.println(list.set(0, 50));
        System.out.println(list);

        list.clear();
        System.out.println(list);
    }

    public void cycleLinkedListTest() {
        CycleLinkedList<Integer> list = new CycleLinkedList<>();
        // add
        list.add(1);
        list.add(2);
        list.add(4);
        list.add(0, 0);
        // remove
        list.remove(0);
        list.remove(1);
        list.remove(0);
        list.remove(0);
//        list.add(0, 0);
        System.out.println(list);
    }

    public void linkedListTest() {
        List<Integer> list = new LinkedList<>();

        // Add
//        list.add(1);
//        list.add(2);
//        list.add(4);
//        list.add(3);
        list.add(9, -1);
//        list.add(9, 4);
//        list.add(19, 0);
//        list.add(19, 9);
        System.out.println(list);

        // remove
//        list.remove(0);
//        list.remove(2);
//        list.remove(-1);
//        list.remove(6);
//        list.remove(5);
        // clear
//        list.clear();
        System.out.println(list);

        //get & set
        System.out.println(list.get(list.size()-1));
        System.out.println(list.set(0, 50));
        System.out.println(list);
    }

    public void arrayListTest() {
        // 初始化 默认capacity 10
        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>(30);


        // 添加元素 向空列表里添加数组
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        System.out.println(list);


        list.add(9, 5); // 添加元素 向尾部添加元素
        list.add(17, 2); // 添加元素 向中间添加元素
        list.add(10, -1); //报错 index越界
        list.add(145, 18); //报错 index越界
        // 动态扩容
        for (int i = 10; i < 100; i++) {
            list.add(i, 5);
        }

        list.remove(0); //删除某个索引
        list.remove(-1); // 报错 index越界
        list.remove(15); // 报错 index越界
        // 动态缩容
        for (int i = 10; i < 100; i++) {
            list.remove(1);
        }
        System.out.println(list.indexOf(3));
        System.out.println(list.indexOf(15));
        System.out.println(list.get(4));
        System.out.println(list.get(-2));
        System.out.println(list.get(100));
        System.out.println(list.set(4, 100));
        System.out.println(list.set(10, 20));
        System.out.println(list.contains(3));
        System.out.println(list.contains(30));
        System.out.println(list.contains(null));
        System.out.println(list.size());
        System.out.println(list);
        // 清空列表
        list.clear();
        System.out.println(list.isEmpty());
    }
}
