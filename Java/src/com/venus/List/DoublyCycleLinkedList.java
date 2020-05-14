package com.venus.List;

/**
 * @copyright 熊彪
 *  * 双向循环联链表
 *  * 注意点：添加操作：
 *              在尾部插入需考虑链表是否为空，若为空，则头尾指针均指向添加元素，并且连接前驱与后继指针，不为空则尾部连接新元素，然后移动尾指针
 *              在其他位置插入，直接插入进链表，若插入index为0，则移动头部指针
 *           删除操作：
 *              获取删除index，连接前驱与后继节点，若删除节点为头尾节点，移动头尾节点位置，若删除链表内最后一个元素，将头尾节点都置为null
 *  * 优点：不浪费内存空间，任意位置插入删除元素速度快
 *  * 缺点：开辟销毁内存次数多，
 *   add :    O(1) O(n)
 *   remove : O(1) O(n)
 *   get :    O(1) O(n)
 *   set :    O(1) O(n)
 */


@SuppressWarnings("all")
public class DoublyCycleLinkedList<E> extends AbstractList<E> {
    private Node head;
    private Node tail;

    private class Node<E> {
        E element;
        Node<E> next;
        Node<E> prev;

        public Node(E element, Node prev, Node next){
            super();
            this.element = element;
            this.next = next;
            this.prev = prev;
        }

        @Override
        public String toString() {
            StringBuilder s = new StringBuilder();

            s.append(element).append(":");
            s.append("{");
            if (prev != null){
                s.append("Prev: ").append(prev.element).append(",");
            }
            if (next != null){
                s.append("Next: ").append(next.element);
            }
            s.append("}");
            return s.toString();
        }
    }

    @Override
    public void clear() {
        size = 0;
        head = null;
        tail = null;
    }

    @Override
    public void add(Object element, int index) {

        if (index == size){
            Node newNode = new Node(element, tail, head);

            if (size == 0) {
                head = newNode;
                tail = newNode;
                newNode.next = newNode;
                newNode.prev = newNode;
            }else {
                tail.next = newNode;
                head.prev = newNode;
                tail = newNode;
            }
        }else {
            Node next = node(index);
            Node prev = next.prev;
            Node newNode = new Node(element, prev, next);
            next.prev = newNode;
            prev.next = newNode;
            if (index == 0){
                head = newNode;
            }
        }
        size++;
    }

    private Node<E> node(int index) {
        rangeCheck(index);

        if (index > (size >> 1)){
            Node<E> node = tail;
            for (int i = size - 1; i > index; i--) {
                node = node.prev;
            }
            return node;
        }else {
            Node<E> node = head;
            for (int i = 0; i < index; i++) {
                node = node.next;
            }
            return node;
        }

    }

    @Override
    public E get(int index) {
        return node(index).element;
    }

    @Override
    public E set(int index, E element){
        Node<E> node = node(index);
        E oldElement = node.element;
        node.element = element;
        return oldElement;
    }

    @Override
    public E remove(int index) {
        // 删除头部
        Node<E> removeElement = node(index);
        Node prev = removeElement.prev;
        Node next = removeElement.next;
        if (size == 1) {
            head = null;
            tail = null;
        }else {
            prev.next = next;
            next.prev = prev;
            if (index == 0) {
                head = next;
            } else if (index == size) {
                tail = prev;
            }
        }
        size--;
        return removeElement.element;
    }

    @Override
    public int indexOf(E element) {
        Node<E> node = head;
        if (element == null){
            for (int i = 0; i < size; i++) {
                if (element == node.element) return i;
                node = node.next;
            }
        }else {
            for (int i = 0; i < size; i++) {
                if (element.equals(node.element)) return i;
                node = node.next;
            }
        }
        return -1;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("Size: ").append(size).append(", LinkedList: [");
        Node node = head;
        for (int i = 0; i < size; i++) {
            if (i != 0) s.append(", ");
            s.append(node);
            node = node.next;
        }
        s.append("]");
        return s.toString();
    }
}
