package com.venus.Queue;

@SuppressWarnings("ALL")
public class CycleDeque<E> {

    private int size;
    private E[] elements;
    private int front;
    private static final int DEFAULT_CAPACITY = 10;

    public CycleDeque(){
        elements = (E[]) new Object[DEFAULT_CAPACITY];
    }

    public void enqueueRear(E element){
        ensureCapacity(size + 1);
        elements[index(size)] = element;
        size++;
    }

    public void enqueueFront(E element){
        ensureCapacity(size + 1);
        front = index(-1);
        elements[front] = element;
        size++;
    }

    public E dequeueFront() {
        E outElement = front();
        elements[front] = null;
        front = index(1);
        size--;
        return outElement;
    }

    public E dequeueRear() {
        int rearIndex = index(size - 1);
        E outElement = elements[rearIndex];
        elements[rearIndex] = null;
        size--;
        return outElement;
    }

    public E front() {
        return elements[front];
    }

    public E rear() {
        return elements[index(size - 1)];
    }

    public void clear() {
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
        size = 0;
        front = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    private int index(int index) {
        index += front;
        if (index < 0){
            return index + elements.length;
        }
        return index - (index >= elements.length ? elements.length : 0);
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
