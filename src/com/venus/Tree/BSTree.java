package com.venus.Tree;

import com.venus.Tree.printer.BinaryTreeInfo;
import java.util.Comparator;

@SuppressWarnings("ALL")
public class BSTree<E> extends BinaryTree<E>{

    protected Comparator comparator;

    public BSTree() {
        this(null);
    }

    public BSTree(Comparator comparator) {
        this.comparator = comparator;
    }



    public void add(E element) {
        checkNullElement(element);

        Node<E> newNode = createNode(element, null);
        if (root == null){
            root = newNode;
            afterAdd(newNode);
            size++;
            return;
        }

        Node<E> node = root;
        Node<E> parent = root;
        int cmp = 0;
        while (node != null) {
            parent = node;
            cmp = compare(node.element, element);

            if (cmp < 0) {
                node = node.right;
            }else if (cmp > 0) {
                node = node.left;
            }else {
                node.element = element;
                return;
            }
        }

        if (cmp < 0) {
            parent.right = newNode;
        }else {
            parent.left = newNode;
        }
        newNode.parent = parent;
        afterAdd(newNode);
        size++;
    }

    public void afterAdd(Node<E> node) {

    }

    public void remove(E element) {
        remove(node(element));
    }

    private void remove(Node<E> node) {
        if (node == null) return;

        if (node.hasTwoChildren()) {
            Node<E> s = successor(node);
            node.element = s.element;
            node = s;
        }

        Node<E> replace = node.left != null ? node.left : node.right;
        if (replace != null) {
            replace.parent = node.parent;
            if (node.parent == null) {
                root = replace;
            } else if (node == node.parent.left) {
                node.parent.left = replace;
            } else {
                node.parent.right = replace;
            }
            afterRemove(replace);
        }else if (node.parent == null){
            root = null;
            afterRemove(node);
        } else {
            if (node.parent.left == node) {
                node.parent.left = null;
            } else {
                node.parent.right = null;
            }
            afterRemove(node);
        }
        size--;
    }

    public void afterRemove(Node<E> node){

    }

    private Node<E> node(E element){
        Node<E> node = root;
        while (node != null) {
            int cmp = compare(element, node.element);
            if (cmp > 0) {
                node = node.right;
            }else if (cmp < 0) {
                node = node.left;
            }else {
                return node;
            }
        }
        return null;
    }

    public boolean contains(E element){
        return node(element) != null;
    }

    protected int compare(E e1, E e2) {
        if (comparator != null){
            return comparator.compare(e1, e2);
        }
        return ((Comparable<E>)e1).compareTo(e2);
    }
}
