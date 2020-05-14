package com.venus.List;

public abstract class AbstractList<E> implements List<E>{

    protected int size;

    public int size() {
        return size;
    }

    public void clear() {
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean contains(E element) {
        return indexOf(element) != ELEMENT_NOT_FOUND;
    }

    /**
     * 使用插入元素方法，避免代码复杂，插入位置为列表尾部
     */
    public void add(E element) {
        add(element, size);
    }

    /**
     * 检查范围，元素索引值为size-1，所以index == size已经超出范围
     */
    protected void rangeCheck(int index) {
        if (index < 0 || index >= size) {
            outOfBound(index);
        }
    }

    /**
     * 与rangecheck不同点为可在列表最后插入元素，所以index可以等于size
     */
    protected void rangeCheckForAdd(int index) {
        if (index < 0 || index > size){
            outOfBound(index);
        }
    }

    protected void outOfBound(int index) {
        throw new IndexOutOfBoundsException("Size: " + size + " Index: " + index + " Index must be in [0, size)...");
    }

}
