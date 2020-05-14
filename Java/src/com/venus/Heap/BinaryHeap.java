package com.venus.Heap;

import com.venus.Tree.printer.BinaryTreeInfo;
import com.venus.Tree.printer.BinaryTrees;

import java.util.Collection;
import java.util.Comparator;
import java.util.Objects;

@SuppressWarnings("ALL")
public class BinaryHeap<E> extends AbstractHeap<E> implements BinaryTreeInfo {

    private static final int DEFAULT_CAPACITY = 10;
    private E[] elements;

    public BinaryHeap() {
        this((E[]) null, null);
    }

    public BinaryHeap(Comparator<E> comparator) {
        this((E[]) null, comparator);
    }

    public BinaryHeap(E[] elements) {
        this(elements, null);
    }

    public BinaryHeap(E[] elements, Comparator comparator) {
        super(comparator);
        if (elements == null || elements.length == 0) {
            this.elements = (E[]) new Object[DEFAULT_CAPACITY];
        } else {
            int capacity = Math.max(elements.length, DEFAULT_CAPACITY);
            this.elements = (E[]) new Object[capacity];
            for (int i = 0; i < elements.length; i++) {
                this.elements[i] = elements[i];
            }
            size = elements.length;
            heapify();
        }
    }
    public BinaryHeap(Collection<E> elements, Comparator comparator) {
        super(comparator);
        size = elements.size();

        if (elements == null || size == 0) {
            this.elements = (E[]) new Object[DEFAULT_CAPACITY];
        } else {
            int capacity = Math.max(size, DEFAULT_CAPACITY);
            this.elements = (E[]) new Object[capacity];
            int i = 0;
            for (E e: elements) {
                this.elements[i++] = e;
            }
            heapify();
        }
    }

    @Override
    public void clear() {
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
        size = 0;
    }

    @Override
    public void add(E element) {
        notNullElementCheck(element);
        ensureCapacity();
        elements[size++] = element;
        siftUp(size - 1);
    }

    public void addAll(E[] elements){
        if (elements == null) return;
        for (E e: elements) {
            add(e);
        }
    }

    public void addAll(Collection<E> elements){
        if (elements == null) return;
        for (E e: elements) {
            add(e);
        }
    }

    private void siftUp(int index) {
        E node = elements[index];
        while (index > 0) {
            int parentIndex = (index - 1) >> 1 ;
            E parent = elements[parentIndex];
            if (compare(node, parent) <= 0) break;
            elements[index] = parent;
            index = parentIndex;
        }
        elements[index] = node;
    }

    @Override
    public E get() {
        emptyCheck();
        return elements[0];
    }

    @Override
    public E remove() {
        emptyCheck();
        int lastIndex = --size ;
        E root = elements[0];
        elements[0] = elements[lastIndex];
        elements[lastIndex] = null;
        siftDown(0);
        return root;
    }

    private void siftDown(int index) {
        E element = elements[index];
        int half = size >> 1;

        while (index < half) {
            int childIndex = (index << 1) + 1;
            int rightIndex = childIndex + 1;
            E child = elements[childIndex];
            if (rightIndex < size && compare(elements[rightIndex], child) < 0) {
                child = elements[childIndex = rightIndex];
            }

            if (compare(element, child) <= 0) break;
            elements[index] = child;
            index = childIndex;
        }
        elements[index] = element;
    }

    @Override
    public E replace(E element) {
        notNullElementCheck(element);
        E root = null;
        if (size == 0) {
            elements[0] = element;
            size ++;
        }else {
            root = elements[0];
            elements[0] = element;
            siftDown(0);
        }

        return root;
    }

    private void heapify() {
        for (int i = (size >> 1) - 1; i >= 0 ; i--) {
            siftDown(i);
        }
    }


    private void ensureCapacity() {

        int oldCapacity = elements.length;
        if (size + 1 <= oldCapacity) return;

        int newCapacity = oldCapacity + (oldCapacity >> 1);
        E[] newElements = (E[]) new Object[newCapacity];

        for (int i = 0; i < elements.length; i++) {
            newElements[i] = elements[i];
        }
        elements = newElements;
    }

    private void emptyCheck() {
        if (size == 0) {
            throw new IndexOutOfBoundsException("Heap is empty!");
        }
    }

    private void notNullElementCheck(E element) {
        if (element == null) {
            throw new IllegalArgumentException("element must not be null!");
        }
    }

    @Override
    public Object root() {
        return 0;
    }

    @Override
    public Object left(Object node) {
        int index = ((int)node << 1) + 1;
        return index >= size ? null : index;
    }

    @Override
    public Object right(Object node) {
        int index = ((int)node << 1) + 2;
        return index >= size ? null : index;
    }

    @Override
    public Object string(Object node) {
        return elements[(int)node];
    }
}
