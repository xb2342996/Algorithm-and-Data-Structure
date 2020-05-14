package com.venus.List;

/**
 * @copyright 熊彪
 *  * 动态数组
 *  * 注意点：添加删除可动态改变容量以节省内存，index操作需check range
 *  * 优点：查询速度快，尾部插入删除速度快
 *  * 缺点：可能造成内存空间浪费
 *   add :    O(1) O(n)
 *   remove : O(1) O(n)
 *   get :    O(1) O(1)
 *   set :    O(1) O(1)
 */

@SuppressWarnings("all")
public class ArrayList<E> extends AbstractList<E>{

    private static final int DEFAULT_CAPACITY = 10;

    private E[] elements;

    public ArrayList(int capacity) {
        capacity = capacity < DEFAULT_CAPACITY ? DEFAULT_CAPACITY : capacity;
        elements = (E[]) new Object[capacity];
    }

    public ArrayList() {
        this(DEFAULT_CAPACITY);
    }


    /**
     * 边界检测，保证数组容量，挪动元素腾出位置
     */
    public void add(E element, int index) {
        rangeCheckForAdd(index);
        ensureCapacity();
        for (int i = size; i > index; i--) {
            elements[i] = elements[i-1];
        }

        elements[index] = element;
        size++;
    }

    /**
     * 边界检测，是否index超出范围，为节省内存缩容
     */
    public E remove(int index) {
        rangeCheck(index);
        E element = elements[index];
        for (int i = index; i < size; i++) {
            elements[i] = elements[i+1];
        }
        size--;
        trim();
        return element;
    }


    public E set(int index, E element) {
        rangeCheck(index);
        E oldElement = elements[index];
        elements[index] = element;
        return oldElement;
    }

    public E get(int index) {
        rangeCheck(index);
        return elements[index];
    }


    /**
     * 注意element是否为null，null在java终不能作为对象调用方法，需要特殊处理
     */
    public int indexOf(E element) {
        if (element == null) {
            for (int i = 0; i < size; i++) {
                if (elements[i] == null) {
                    return i;
                }
            }
        }else {
            for (int i = 0; i < size; i++) {
                if (element.equals(elements[i])){
                    return i;
                }
            }
        }
        return ELEMENT_NOT_FOUND;
    }


    /**
     * 获取当前容量，如果当前元素个数 < 当前容量，则不需要扩充容量，新容量为当前的1.5倍，重新申请空间并拷贝内容
     */
    private void ensureCapacity(){
        int currentCapacity = elements.length;

        if (size + 1 < currentCapacity) return;
        int newCapacity = currentCapacity + (currentCapacity >> 1);

        E[] newElements = (E[]) new Object[newCapacity];
        for (int i = 0; i < size; i++) {
            newElements[i] = elements[i];
        }

        elements = newElements;
    }

    /**
     * 获取当前容量，如果当前元素个数 < 默认容量或者元素个数 > 当前容量的一半，不需要缩容，新容量为当前的0.5倍，重新申请空间并拷贝内容
     */
    private void trim() {
        int currentCapacity = elements.length;
        if (size >= currentCapacity >> 1 || currentCapacity < DEFAULT_CAPACITY) return;

        int newCapacity = currentCapacity >> 1;
        E[] newElements = (E[]) new Object[newCapacity];
        for (int i = 0; i < size; i++) {
            newElements[i] = elements[i];
        }
        elements = newElements;

    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("Size: ").append(size).append(", Length: ").append(elements.length).append(", [");
        for (int i = 0; i < size; i++) {
            if (i != 0) {
                s.append(", ");
            }
            s.append(elements[i]);
        }
        s.append("]");
        return s.toString();
    }
}
