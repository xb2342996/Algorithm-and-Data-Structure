package com.venus.Map;


import com.sun.org.apache.bcel.internal.generic.RET;
import com.venus.Tree.BinaryTree;
import com.venus.Tree.RBTree;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class TreeMap<K, V> implements Map<K, V>{

    private static final boolean BLACK = true;
    private static final boolean RED = false;
    protected int size;
    protected Node<K, V> root;

    protected Comparator comparator;

    public TreeMap() {
        this(null);
    }

    public TreeMap(Comparator comparator) {
        this.comparator = comparator;
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

    private Node<K, V> createNode(K key, V value, Node<K, V> parent){
        return new Node<>(key, value, parent);
    }
    @Override
    public boolean containsKey(K key) {
        return node(key) != null;
    }

    @Override
    public boolean containsValue(V value) {
        if (root == null) return false;
        Node<K, V> node = root;
        Queue<Node<K, V>> queue = new LinkedList<>();
        queue.offer(node);
        while (!queue.isEmpty()) {
            node = queue.poll();
            if (valEqual(node.value, value)) return true;

            if (node.left != null) {
                queue.offer(node.left);
            }
            if (node.right != null) {
                queue.offer(node.right);
            }
        }
        return false;
    }

    private boolean valEqual(V v1, V v2){
        return v1 == null ? v2 == null : v1.equals(v2);
    }

    @Override
    public V put(K key, V value) {
        checkNullKey(key);

        Node<K, V> newNode = createNode(key, value, null);
        if (root == null){
            root = newNode;
            afterPut(newNode);
            size++;
            return null;
        }

        Node<K, V> node = root;
        Node<K, V> parent = root;
        int cmp = 0;
        while (node != null) {
            parent = node;
            cmp = compare(node.key, key);

            if (cmp < 0) {
                node = node.right;
            }else if (cmp > 0) {
                node = node.left;
            }else {
                node.key = key;
                V oldValue = node.value;
                node.value = value;
                return oldValue;
            }
        }

        if (cmp < 0) {
            parent.right = newNode;
        }else {
            parent.left = newNode;
        }
        newNode.parent = parent;
        afterPut(newNode);
        size++;
        return null;
    }

    private void afterPut(Node<K, V> node) {
        Node<K, V> parent = node.parent;

        // 插入node的parent为空，说明是插入的是root，将node染成黑色，结束
        if (parent == null) {
            black(node);
            return;
        }
        // 4阶B树叶子节点只有一个节点情况，如果node的parent为黑色，结束
        if (isBlack(parent)) return;

        Node<K, V> uncle = parent.sibling();
        // 先将grand节点染成红色，后面涉及到grand节点都为红色
        Node<K, V> grand = red(parent.parent);

        // 4阶B树叶子节点有3个节点的情况，插入会破坏平衡，需要上溢节点，将parent与uncle染成黑色，grand染成红色，并将grand向上添加
        if (isRed(uncle)) {
            black(parent);
            black(uncle);
            afterPut(grand);
            return;
        }

        // 4阶B树叶子节点有2个节点情况，确定B树是否有2个节点，判断插入的节点的uncle节点颜色是否是黑色
        // 寻找node和parent的节点方向，判断旋转方向
        if (parent.isLeftChild()){ // L
            if (node.isLeftChild()) { // LL
                // 左左情况，parent染成黑色，grand染成红色，右旋
                black(parent);
            }else { // LR
                // 左右情况，node染成黑色，grand染成红色，左旋，右旋
                rotateLeft(parent);
                black(node);
            }
            rotateRight(grand);
        }else { //  R
            if (node.isLeftChild()) { // RL
                // 右左情况，node染成黑色，grand染成红色，右旋，左旋
                rotateRight(parent);
                black(node);
            }else { // RR
                // 右右情况，parent染成黑色，grand染成红色，左旋
                black(parent);
            }
            rotateLeft(grand);
        }
    }

    @Override
    public V get(K key) {
        Node<K, V> node = node(key);
        return node != null ? node.value : null;
    }

    @Override
    public V remove(K key) {
        return remove(node(key));
    }

    private V remove(Node<K, V> node) {
        if (node == null) return null;

        size--;

        V oldValue = node.value;
        if (node.hasTwoChildren()) {
            Node<K, V> s = successor(node);
            node.key = s.key;
            node.value = s.value;
            node = s;
        }

        Node<K, V> replace = node.left != null ? node.left : node.right;
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
        return oldValue;
    }

    private void afterRemove(Node<K, V> node) {
//        if (isRed(node)) return;
        // 删除红色
        // 2种情况：1.如果删除的节点是红色，不用处理，结束
        //        2.如果删除拥有1个RED子节点的BLACK节点，node为删除节点的替代节点（前驱或者后继），将替代节点染成黑色，结束
        if (isRed(node)) {
            black(node);
            return;
        }

        // 删除黑色: 1.节点父节点是否为空，
        //         2.删除的节点是左节点还是右节点，
        //         3.node的sibling是否是红色，
        //         4.sibling的子节点是否有红色节点 （全黑，要递归parent）（反向判断全黑）
        //         5.有红色节点判断红色节点是左节点还是右节点 （反向判断黑色）
        // 获取删除节点的父节点
        // 删除节点为根节点，直接结束
        Node<K, V> parent = node.parent;
        if (parent == null) return;

        // 查看删除的节点是左节点还是右节点，parent可能为空
        boolean left = parent.left == null || node.isLeftChild();
        // 查找删除节点的兄弟节点
        Node<K, V> sibling = left ? parent.right : parent.left;

        if (left) {
            if (isRed(sibling)){
                black(sibling);
                red(parent);
                rotateLeft(parent);
                sibling = parent.right;
            }

            if (isBlack(sibling.left) && isBlack(sibling.right)) {
                boolean parentBlack = isBlack(parent);
                black(parent);
                red(sibling);
                if (parentBlack) {
                    afterRemove(parent);
                }
            } else {
                if (isBlack(sibling.right)) { // RL
                    rotateRight(sibling);
                    sibling = parent.right;
                }
                // RR
                color(sibling, colorOf(parent));
                black(parent);
                black(sibling.right);
                rotateLeft(parent);
            }
        } else { // 删除节点为右节点
            // 判断兄弟节点是否为红色
            if (isRed(sibling)){ // sibling为红色，染黑sibling，染红parent，右旋parent，更新sibling
                black(sibling);
                red(parent);
                rotateRight(parent);
                sibling = parent.left;
            }
            // sibling为黑色，
            // 并且sibling的左右子节点都是黑色，获取parent是否为黑色，染黑parent，染红sibling，如果parent是黑色，parent下溢，将parent当做移除节点继续处理
            if (isBlack(sibling.left) && isBlack(sibling.right)) {
                boolean parentBlack = isBlack(parent);
                black(parent);
                red(sibling);
                if (parentBlack) {
                    afterRemove(parent);
                }
                // sibling至少有一个红色子节点，
            } else {
                // 如果sibling的左节点是黑色，说明sibling的右节点是红色，讲sibling左旋，更换sibling
                if (isBlack(sibling.left)) { //LR
                    rotateLeft(sibling);
                    sibling = parent.left;
                }// LL
                // 将sibling染成parent的颜色，parent染成黑色，染黑sibling的左子节点，右旋parent
                color(sibling, colorOf(parent));
                black(parent);
                black(sibling.left);
                rotateRight(parent);
            }
        }
    }


    @Override
    public void travesal(Visitor<K, V> visitor) {
        if (visitor == null) return;
        travesal(root, visitor);
    }

    private void travesal(Node<K, V> node, Visitor<K, V> visitor) {
        if (node == null || visitor == null) return;

        travesal(node.left, visitor);
        visitor.visit(node.key, node.value);
        travesal(node.right, visitor);
    }

    private Node<K, V> node(K key){
        Node<K, V> node = root;
        while (node != null) {
            int cmp = compare(key, node.key);
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

    private Node<K, V> predecessor(Node<K, V> node) {
        if (node == null) return null;

        Node<K, V> current = node.left;
        if (current != null) {
            while (current.right != null){
                current = current.right;
            }
            return current;
        }

        while (node.parent != null && node.parent.left != null){
            node = node.parent;
        }
        return node.parent;
    }

    private Node<K, V> successor(Node<K, V> node) {
        if (node == null) return null;

        Node<K, V> current = node.right;
        if (current != null) {
            while (current.left != null){
                current = current.left;
            }
            return current;
        }
        while (node.parent != null && node.parent.right != null) {
            node = node.parent;
        }
        return node.parent;
    }

    private void rotateRight(Node<K, V> grand) {
        Node<K, V> parent = grand.left;
        Node<K, V> child = parent.right;

        grand.left = child;
        parent.right = grand;

        afterRotate(grand, parent, child);
    }

    private void rotateLeft(Node<K, V> grand) {
        Node<K, V> parent = grand.right;
        Node<K, V> child = parent.left;

        grand.right = child;
        parent.left = grand;

        afterRotate(grand, parent, child);
    }

    private void afterRotate(Node<K, V> grand, Node<K, V> parent, Node<K, V> child) {
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
    
    private static class Node<K, V> {
        // 初始化节点为红色
        K key;
        V value;
        boolean color = RED;
        Node<K, V> left;
        Node<K, V> right;
        Node<K, V> parent;

        public Node(K key, V value, Node<K, V> parent) {
            this.key = key;
            this.value = value;
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
        public Node<K, V> sibling() {
            if (isLeftChild()){
                return parent.right;
            }
            if (isRightChild()){
                return parent.left;
            }
            return null;
        }
    }
    // 将节点染色
    private Node<K, V> color(Node<K, V> node, boolean color){
        if (node == null) return node;
        node.color = color;
        return node;
    }
    // 将节点染成红色
    private Node<K, V> red(Node<K, V> node){
        return color(node, RED);
    }
    // 将节点染成黑色
    private Node<K, V> black(Node<K, V> node){
        return color(node, BLACK);
    }

    // 判断节点颜色
    private boolean colorOf(Node<K, V> node){
        return node == null ? BLACK : node.color;
    }
    // 判断节点是不是黑色
    private boolean isBlack(Node<K, V> node){
        return colorOf(node) == BLACK;
    }
    // 判断节点是不是红色
    private boolean isRed(Node<K, V> node){
        return colorOf(node) == RED;
    }

    private void checkNullKey(K key) {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null!");
        }
    }
    private int compare(K e1, K e2) {
        if (comparator != null){
            return comparator.compare(e1, e2);
        }
        return ((Comparable<K>)e1).compareTo(e2);
    }
}
