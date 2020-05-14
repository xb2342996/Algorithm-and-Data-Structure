package com.venus.Heap;

public interface Heap<E> {
    int size();
    boolean isEmpty();
    void clear();
    void add(E element);    // 添加元素
    E get();                // 获得堆顶元素
    E remove();             // 删除堆顶元素
    E replace(E element);  // 删除堆顶元素的同时插入一个新元素
}
