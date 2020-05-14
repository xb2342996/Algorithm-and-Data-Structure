package com.venus.Queue;

import com.venus.List.DoublyLinkedList;

/**
 * @copyright 熊彪
 *  * 队列
 *  * 注意点：可以使用ArrayList或者DoublyLinkedList来实现，为什么？
 *          ArrayList与DoublyLinkedList在头尾节点操作的时间复杂度均为O（1）
 *  *
 */
@SuppressWarnings("all")
public class Queue<E> {

    private DoublyLinkedList<E> list = new DoublyLinkedList<>();

    public void enqueue(E element){
        list.add(element);
    }

    public E dequeue() {
        return list.remove(0);
    }

    public E front() {
        return list.get(0);
    }

    public void clear() {
        list.clear();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public int size() {
        return list.size();
    }
}
