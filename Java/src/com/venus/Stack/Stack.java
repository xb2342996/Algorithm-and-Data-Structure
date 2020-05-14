package com.venus.Stack;

import com.venus.List.ArrayList;

/**
 * @copyright 熊彪
 *  * 栈
 *  * 注意点：为什么使用动态数组？ 动态数组在尾部节点删除和添加操作都是O（1）复杂度
 *   push : O(1)
 *   pop  : O(1)
 *   top  : O(1)
 */


@SuppressWarnings("all")
public class Stack<E> {
    private ArrayList<E> list = new ArrayList<>();

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public void push(E element){
        list.add(element);
    }

    public E pop(){
        return list.remove(list.size() - 1);
    }

    public E top() {
        return list.get(list.size() - 1);
    }


}
