package com.venus.Tree;

import java.util.Comparator;

public class BBSTree<E> extends BSTree<E>{

    public BBSTree(){
        this(null);
    }

    public BBSTree(Comparator<E> comparator) {
        super(comparator);
    }

    protected void rotateRight(Node<E> grand) {
        Node<E> parent = grand.left;
        Node<E> child = parent.right;

        grand.left = child;
        parent.right = grand;

        afterRotate(grand, parent, child);
    }

    protected void rotateLeft(Node<E> grand) {
        Node<E> parent = grand.right;
        Node<E> child = parent.left;

        grand.right = child;
        parent.left = grand;

        afterRotate(grand, parent, child);
    }

    protected void afterRotate(Node<E> grand, Node<E> parent, Node<E> child) {
        parent.parent = grand.parent;
        if (grand.isLeftChild()) {
            grand.parent.left = parent;
        }else if (grand.isRightChild()){
            grand.parent.right = parent;
        }else {
            root = parent;
        }

        if (child != null) {
            child.parent = grand;
        }
        grand.parent = parent;

    }

    protected void rotate(Node<E> r, Node<E> a, Node<E> b, Node<E> c, Node<E> d, Node<E> e, Node<E> f, Node<E>g) {

        d.parent = r.parent;
        if (r.isLeftChild()) {
            r.parent.left = d;
        }else if(r.isRightChild()) {
            r.parent.right = d;
        }else {
            root = d;
        }

        b.left = a;
        b.right = c;
        if (c != null) {
            c.parent = b;
        }
        if (a != null) {
            a.parent = b;
        }


        f.left = e;
        f.right = g;
        if (e != null) {
            e.parent = f;
        }
        if (g != null) {
            g.parent = f;
        }

        d.left = b;
        d.right = f;
        b.parent = d;
        f.parent = d;

    }
}
