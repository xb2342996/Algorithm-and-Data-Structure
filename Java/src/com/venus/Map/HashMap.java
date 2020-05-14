package com.venus.Map;

import com.venus.Tree.printer.BinaryTreeInfo;
import com.venus.Tree.printer.BinaryTrees;

import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

@SuppressWarnings("ALL")
public class HashMap<K, V> implements Map<K, V> {

    private int size;
    private final static boolean RED = true;
    private final static boolean BLACK = false;
    private final static int DEFAULT_CAPACITY = 1 << 4;
    private Node<K, V>[] table;
    private final static float DEFAULT_LOAD_FACTOR = 0.75f;

    public HashMap() {
        table = new Node[DEFAULT_CAPACITY];
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public void clear() {
        if (size == 0) return;
        size = 0;
        for (int i = 0; i < table.length; i++) {
            table[i] = null;
        }
    }

    protected Node<K, V> createNode(K key, V value, Node<K, V> parent){
        return new Node<>(key, value, parent);
    }

    @Override
    public V put(K key, V value) {
        resize();

        int index = index(key);
        Node<K, V> root = table[index];

        if (root == null){
            root = createNode(key, value, null);;
            table[index] = root;
            fixAfterPut(root);
            size++;
            return null;
        }

        Node<K, V> node = root;
        Node<K, V> parent = root;

        K k1 = key;
        int h1 = hash(key);
        int cmp = 0;
        boolean searched = false;
        Node<K, V> result = null;
        while (node != null) {
            parent = node;
            K k2 = node.key;
            int h2 = node.hash;

            // 比较逻辑
            if (h1 > h2) {
                cmp = 1;
            }else if (h1 < h2){
                cmp = -1;
            }else if (Objects.equals(k1, k2)) {
                cmp = 0;
            }else if (k1 != null && k2 != null
                    && k1 instanceof Comparable
                    && k1.getClass() == k2.getClass()
                    && (cmp = ((Comparable)k1).compareTo(k2)) != 0){

            }else if(searched) {
                cmp = System.identityHashCode(k1) - System.identityHashCode(k2);
            }else {
                if ((node.left != null && (result = node(node.left, k1)) != null) ||
                        (node.right != null && (result = node(node.right, k1)) != null)){

                    node = result;
                    cmp = 0;
                }else {
                    searched = true;
                    cmp = System.identityHashCode(k1) - System.identityHashCode(k2);
                }

            }

            if (cmp > 0) {
                node = node.right;
            }else if (cmp < 0) {
                node = node.left;
            }else {
                node.key = key;
                V oldValue = node.value;
                node.value = value;
                node.hash = h1;
                return oldValue;
            }
        }


        Node<K, V> newNode = createNode(key, value, parent);
        if (cmp > 0) {
            parent.right = newNode;
        }else {
            parent.left = newNode;
        }

        fixAfterPut(newNode);

        size++;
        return null;
    }

    private void fixAfterPut(Node<K, V> node) {
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
            fixAfterPut(grand);
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

    private void resize() {
        if (size / table.length <= DEFAULT_CAPACITY) return;
        Node<K, V>[] oldTable = table;
        table = new Node[oldTable.length << 1];

        Queue<Node<K, V>> queue = new LinkedList<>();
        for (int i = 0; i < oldTable.length; i++) {

            Node<K, V> node = oldTable[i];
            if (node == null) continue;

            queue.offer(node);
            while (!queue.isEmpty()) {
                node = queue.poll();

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
                moveNode(node);
            }
        }
    }

    private void moveNode(Node<K, V> newNode) {

        newNode.left = null;
        newNode.right = null;
        newNode.parent = null;
        newNode.color = RED;

        int index = index(newNode);
        Node<K, V> root = table[index];

        if (root == null){
            root = newNode;;
            table[index] = root;
            fixAfterPut(root);

            return;
        }

        Node<K, V> node = root;
        Node<K, V> parent = root;

        K k1 = newNode.key;
        int h1 = newNode.hash;
        int cmp = 0;

        while (node != null) {
            parent = node;
            K k2 = node.key;
            int h2 = node.hash;

            // 比较逻辑
            if (h1 > h2) {
                cmp = 1;
            }else if (h1 < h2){
                cmp = -1;
            }else if (k1 != null && k2 != null
                    && k1 instanceof Comparable
                    && k1.getClass() == k2.getClass()
                    && (cmp = ((Comparable)k1).compareTo(k2)) != 0){
            }else {
                cmp = System.identityHashCode(k1) - System.identityHashCode(k2);
            }

            if (cmp > 0) {
                node = node.right;
            }else if (cmp < 0) {
                node = node.left;
            }
        }

        if (cmp > 0) {
            parent.right = newNode;
        }else {
            parent.left = newNode;
        }
        newNode.parent = parent;
        fixAfterPut(newNode);

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
    protected V remove(Node<K, V> node) {
        if (node == null) return null;
        // 要删除的节点
        Node<K, V> willNode = node;
        size--;

        V oldValue = node.value;
        if (node.hasTwoChildren()) {
            Node<K, V> s = successor(node);
            node.key = s.key;
            node.value = s.value;
            node.hash = s.hash;
            node = s;
        }
        Node<K, V> root = table[index(node)];
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
            fixAfterRemove(replace);
        }else if (node.parent == null){
            root = null;
            fixAfterRemove(node);
        } else {
            if (node.parent.left == node) {
                node.parent.left = null;
            } else {
                node.parent.right = null;
            }
            fixAfterRemove(node);
        }

        afterRemove(willNode, node);
        return oldValue;
    }
    protected void afterRemove(Node<K, V> willNode, Node<K, V> removeNode) {

    }

    @Override
    public boolean containsKey(K key) {
        return node(key) != null;
    }

    @Override
    public boolean containsValue(V value) {
        if (size == 0) return false;
        Queue<Node<K, V>> queue = new LinkedList<>();
        for (int i = 0; i < table.length; i++) {
            Node<K, V> node = table[i];
            if (node == null) continue;
            queue.offer(node);
            while (!queue.isEmpty()) {
                node = queue.poll();
                if (Objects.equals(node.value, value)) return true;

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return false;
    }

    @Override
    public void travesal(Visitor<K, V> visitor) {
        if (size == 0) return;
        Queue<Node<K, V>> queue = new LinkedList<>();
        for (int i = 0; i < table.length; i++) {
            System.out.println("遍历【" + i+ "】");
            Node<K, V> node = table[i];
            if (node == null) continue;
            queue.offer(node);
            while (!queue.isEmpty()) {
                node = queue.poll();
                if (visitor.visit(node.key, node.value)) return;

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
    }

    public void print() {
        if (size == 0) return;
        for (int i = 0; i < table.length; i++) {
            final Node<K, V> root = table[i];
            System.out.println("[index = " + i + "]");
            BinaryTrees.println(new BinaryTreeInfo() {
                @Override
                public Object root() {
                    return root;
                }

                @Override
                public Object left(Object node) {
                    return ((Node<K, V>)node).left;
                }

                @Override
                public Object right(Object node) {
                    return ((Node<K, V>)node).right;
                }

                @Override
                public Object string(Object node) {
                    return node;
                }
            });
            System.out.println("--------------------------------------------------");
        }
        return;
    }

    private Node<K, V> node(K key) {
        Node<K, V> node = table[index(key)];
        return node == null ? null : node(node, key);
    }

    private Node<K, V> node(Node<K, V> node, K key){

        K k1 = key;
        int h1 = hash(k1);
        Node<K, V> result = null;
        int cmp = 0;
        while (node != null) {
            K k2 = node.key;
            int h2 = node.hash;
            // 比较逻辑
            if (h1 > h2) {
                node = node.right;
            }else if (h1 < h2){
                node = node.left;
            }else if (Objects.equals(k1, k2)){
                return node;
            }else if (k1 != null && k2 != null
                    && k1.getClass() == k2.getClass()
                    && k1 instanceof Comparable
                    && (cmp = ((Comparable)k1).compareTo(k2)) != 0){
                node = cmp > 0 ? node.right : node.left;
            }else if (node.right != null && (result = node(node.right, k1)) != null){
                return result;
            }else {
                node = node.left;
            }
        }
        return null;
    }

    private void fixAfterRemove(Node<K, V> node) {
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
                    fixAfterRemove(parent);
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
                    fixAfterRemove(parent);
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

    private int index(K key) {
        return hash(key) & (table.length - 1);
    }
    private int hash(K key) {
        if (key == null) return 0;
        int hash = key.hashCode();
        return (hash ^ hash >>> 16);
    }
    private int index(Node<K, V> node) {
        return node.hash & (table.length - 1);
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
            table[index(grand)] = parent;
        }

        if (child != null) {
            child.parent = grand;
        }
        grand.parent = parent;

    }

    protected static class Node<K, V> {
        K key;
        V value;
        boolean color = RED;
        Node<K, V> left;
        Node<K, V> right;
        Node<K, V> parent;
        int hash;

        public Node(K key, V value, Node<K, V> parent) {
            this.key = key;
            this.value = value;
            this.parent = parent;
            int hash = key == null ? 0 : key.hashCode();
            this.hash =(hash >>> 16) ^ hash;
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

        @Override
        public String toString() {
            return "Node:" + key +
                    ": " + value;
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
}
