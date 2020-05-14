package com.venus.Queue;

import com.venus.List.DoublyLinkedList;

public class Deque<E> {
    private DoublyLinkedList<E> list = new DoublyLinkedList<>();

    public void enqueueRear(E element){
        list.add(element);
    }

    public void enqueueFront(E element){
        list.add(element, 0);
    }

    public E dequeueFront() {
        return list.remove(0);
    }

    public E dequeueRear() {
        return list.remove(list.size() - 1);
    }

    public E front() {
        return list.get(0);
    }

    public E rear() {
        return list.get(list.size() - 1);
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
