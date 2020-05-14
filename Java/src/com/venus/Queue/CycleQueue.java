package com.venus.Queue;

/**
 * @copyright 熊彪
 *  * 队列
 *  * 注意点：使用静态数组实现循环队列，入队列需要确定数组大小是否足够，空间不够情况需要扩充容量，从队头复制元素到新的空间，并且重置front指针，
 *  *        注意index位置可能大于数组长度，所以对index要取模操作。
 *  * enqueue O(1)
 *  * dequeue O(1)
 *  *
 */

@SuppressWarnings("ALL")
public class CycleQueue<E> {
    private int front;
    private int size;
    private E[] elements;
    private static final int DEFAULT_CAPACITY = 10;

    public CycleQueue() {
        elements = (E[]) new Object[DEFAULT_CAPACITY];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void clear() {
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
        size = 0;
        front = 0;
    }

    public void enqueue(E element) {
        ensureCapacity(size + 1);
        elements[index(size)] = element;
        size++;
    }

    public E dequeue() {
        E element = elements[front];
        elements[front] = null;
        front = index(1);
        size--;
        return element;
    }

    public E front() {
        return elements[front];
    }

    private void ensureCapacity(int minCapacity) {
        if (minCapacity > elements.length){
            int newCapacity = elements.length + (elements.length >> 1);
            E[] newElements = (E[]) new Object[newCapacity];
            for (int i = 0; i < size; i++) {
                newElements[i] = elements[index(i)];
            }
            elements = newElements;
            front = 0;
        }
    }

    private int index(int index) {
        index = front + index;
        return index - (index >= elements.length ? elements.length : 0);
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("Size: ").append(size).append(" Length: ").append(elements.length).append(", [");
        for (int i = 0; i < elements.length; i++) {
            if (i != 0){
                s.append(", ");
            }
            s.append(elements[i]);
        }
        s.append("]");
        return s.toString();
    }
}
