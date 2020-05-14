package com.venus.List;

/**
 * @copyright 熊彪
 *  * 双向联链表
 *  * 注意点：添加删除特别注意头部尾部特殊处理，涉及index操作需要rangecheck，由于双向链表可获取index位置，所以添加与删除的rangecheck在获取节点时就已经处理好了，保证报错
 *  *        抛出indexOutOfBounds。搜索节点可从头尾两侧开始搜索，略微提高效率。
 *  * 优点：不浪费内存空间，任意位置插入删除元素速度快
 *  * 缺点：开辟销毁内存次数多，
 *   add :    O(1) O(n)
 *   remove : O(1) O(n)
 *   get :    O(1) O(n)
 *   set :    O(1) O(n)
 */


@SuppressWarnings("all")
public class DoublyLinkedList<E> extends AbstractList<E>{

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
            Node last = tail;
            tail = new Node(element, last, null);
            if (last == null){
                head = tail;
            }else {
                last.next = tail;
            }
        }else {
            Node next = node(index);
            Node prev = next.prev;
            Node node = new Node(element, prev, next);
            next.prev = node;
            if (index == 0){
                head = node;
            }else {
                prev.next = node;
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

        if (prev == null){
            head = next;
        }else {
            prev.next = next;
        }

        if (next == null){
            tail = prev;
        }else {
            next.prev = prev;
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
