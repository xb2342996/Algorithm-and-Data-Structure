package com.venus.List;

/**
 * @copyright 熊彪
 *  * 单向循环链表
 *  * 注意点：除链表注意点外，循环链表添加删除元素需对头部进行特殊处理，将尾部next指向新的头部。删除节点如果只有一个元素将head变成null
 *  * 优点：节省空间
 *  * 缺点：可能造成内存空间浪费
 *   add :    O(1) O(n)
 *   remove : O(1) O(n)
 *   get :    O(1) O(n)
 *   set :    O(1) O(n)
 */

@SuppressWarnings("all")
public class CycleLinkedList<E> extends AbstractList<E>{
    private Node head;

    private static class Node<E> {
        E element;
        Node<E> next;

        public Node(E element, Node<E> next) {
            super();
            this.element = element;
            this.next = next;
        }
    }


    @Override
    public void clear() {
        size = 0;
        head = null;
    }

    @Override
    public void add(E element, int index) {
        rangeCheckForAdd(index);
        if (index == 0){
            Node<E> newNode = new Node(element, head);
            Node<E> last = (size == 0) ? newNode : node(size-1);
            last.next = newNode;
            head = newNode;
        }else {
            Node prev = node(index - 1);
            prev.next = new Node(element, prev.next);
        }
        size++;
    }

    private Node<E> node(int index) {
        rangeCheck(index);
        Node node = head;
        for (int i = 0; i < index; i++) {
            node = node.next;
        }
        return node;
    }

    @Override
    public E get(int index) {
        return node(index).element;
    }

    @Override
    public E set(int index, E element) {
        Node<E> node = node(index);
        E oldElement = node.element;
        node.element = element;
        return oldElement;
    }

    @Override
    public E remove(int index) {
        rangeCheck(index);
        Node<E> removeElement = head;
        if (index == 0){
            if (size == 1){
                head = null;
            }else {
                head = head.next;
                Node<E> last = node(size - 1);
                last.next = head;
            }
        }else {
            Node<E> prev = node(index - 1);
            removeElement = prev.next;
            prev.next = removeElement.next;
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
            s.append(node.element);
            node = node.next;
        }
        s.append("]");
        return s.toString();
    }
}
