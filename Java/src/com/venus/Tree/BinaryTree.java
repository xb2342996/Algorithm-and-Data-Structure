package com.venus.Tree;

import com.venus.Tree.printer.BinaryTreeInfo;


import java.util.LinkedList;
import java.util.Queue;

@SuppressWarnings("ALL")
public class BinaryTree<E> implements BinaryTreeInfo{
    protected int size;
    protected Node<E> root;


    protected static class Node<E> {
        E element;
        Node<E> left;
        Node<E> right;
        Node<E> parent;

        public Node(E element, Node<E> parent) {
            this.element = element;
            this.parent = parent;
        }
        public boolean isLeaf() {
            return left == null && right == null;
        }

        public boolean hasTwoChildren() {
            return left != null && right != null;
        }

        public boolean isLeftChild() {
            return parent != null && this == parent.left;
        }
        public boolean isRightChild() {
            return parent != null && this == parent.right;
        }
        public Node<E> sibling() {
            if (isLeftChild()){
                return parent.right;
            }
            if (isRightChild()){
                return parent.left;
            }
            return null;
        }

        @Override
        public String toString() {
            return element + "";
        }
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public void clear() {
        root = null;
    }

    protected Node<E> createNode(E element, Node<E> parent){
        return new Node<>(element, parent);
    }

    public Node<E> predecessor(Node<E> node) {
        if (node == null) return null;

        Node<E> current = node.left;
        if (current != null) {
            while (current.right != null){
                current = current.right;
            }
            return current;
        }

        while (node.parent != null && node.parent.left == node){
            node = node.parent;
        }
        return node.parent;
    }

    public Node<E> successor(Node<E> node) {
        if (node == null) return null;

        Node<E> current = node.right;
        if (current != null) {
            while (current.left != null){
                current = current.left;
            }
            return current;
        }
        while (node.parent != null && node.parent.right == node) {
            node = node.parent;
        }
        return node.parent;
    }

    public void preorderTravesal(Visitor visitor) {
        preorderTravesal(root, visitor);
    }

    public void preorderTravesal(Node<E> node, Visitor visitor) {
        if (node == null || visitor == null) return;

        visitor.visit(node.element);
        preorderTravesal(node.left, visitor);
        preorderTravesal(node.right, visitor);
    }

    public void inorderTravesal(Visitor visitor) {
        inorderTravesal(root, visitor);
    }

    public void inorderTravesal(Node<E> node, Visitor visitor) {
        if (node == null || visitor == null) return;

        inorderTravesal(node.left, visitor);
        visitor.visit(node.element);
        inorderTravesal(node.right, visitor);
    }

    public void posterorderTravesal(Visitor visitor) {
        posterorderTravesal(root, visitor);
    }

    public void posterorderTravesal(Node<E> node, Visitor visitor) {
        if (node == null || visitor == null) return;

        posterorderTravesal(node.left, visitor);
        posterorderTravesal(node.right, visitor);
        visitor.visit(node.element);
    }

    public void levelOrderTravesal(Visitor visitor) {
        if (root == null || visitor == null) return;;
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            Node<E> current = queue.poll();
            visitor.visit(current.element);
            if (current.left != null) {
                queue.offer(current.left);
            }
            if (current.right != null){
                queue.offer(current.right);
            }
        }
    }

    public boolean isComplete() {
        if (root == null) return true;
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);

        boolean leaf = false;
        while (!queue.isEmpty()) {
            Node<E> node = queue.poll();

            if (leaf && !node.isLeaf()) return false;
            if (node.left != null && node.right != null) {
                queue.offer(node.left);
                queue.offer(node.right);
            } else {
                leaf = true;
                if (node.left != null) {
                    queue.offer(node);
                }
            }
        }
        return true;
    }

    public void reverse() {
        reverse(root);
    }

    public void reverse(Node node) {
        if (node == null) return;

        Node tmp = node.left;
        node.left = node.right;
        node.right = tmp;
        reverse(node.left);
        reverse(node.right);
    }

    public void reverseLevel() {
        if (root == null) return;;
        Node<E> node = root;
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(node);
        while (!queue.isEmpty()) {
            node = queue.poll();
            Node tmp = node.left;
            node.left = node.right;
            node.right = tmp;

            if (node.left != null) {
                queue.offer(node.left);
            }
            if (node.right != null) {
                queue.offer(node.right);
            }
        }
    }

    public int heightRecursive() {
        if (root == null) return 0;
        return heightRecursive(root);
    }

    protected int heightRecursive(Node<E> node) {
        if (node.right == null || node.left == null) {
            return 1;
        }
        return 1 + Math.max(heightRecursive(node.left), heightRecursive(node.right));
    }

    protected int heightNotRecursize() {
        if (root == null) return 0;
        int levelCount = 1;
        int height = 0;
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            Node<E> node = queue.poll();
            levelCount--;
            if (node.left != null) {
                queue.offer(node.left);
            }
            if (node.right != null) {
                queue.offer(node.right);
            }
            if (levelCount == 0) {
                levelCount = queue.size();
                height ++;
            }
        }
        return height;
    }

    public static interface Visitor<E> {
        void visit(E element);
    }

    public void checkNullElement(E element) {
        if (element == null) {
            throw new IllegalArgumentException("Element must not be null!");
        }
    }

    @Override
    public Object root() {
        return root;
    }

    @Override
    public Object left(Object node) {
        return ((Node<E>)node).left;
    }

    @Override
    public Object right(Object node) {
        return ((Node<E>)node).right;
    }

    @Override
    public Object string(Object node) {
        return node;
    }

}
