package com.venus.SkipList;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Objects;

@SuppressWarnings("ALL")
public class SkipList<K, V> {
    private static final double probablity = 0.25;
    private static final int maxLevel = 32;
    private int size;
    private int level;
    private Comparator<K> comparator;
    private Node<K, V> first;

    private int compare(K k1, K k2){
        return comparator == null ? ((Comparable<K>)k1).compareTo(k2) : comparator.compare(k1 ,k2);
    }

    public SkipList() {
        this(null);
    }

    public SkipList(Comparator comparator) {
        this.comparator = comparator;
        first = new Node<>(null, null, maxLevel);
    }

    private class Node<K, V> {
        K key;
        V value;
        Node<K, V>[] nexts;
        int index;

        public Node(K key, V value, int level) {
            this.key = key;
            this.value = value;
            nexts = new Node[level];
        }

        @Override
        public String toString() {
            return "key: " + key + ", nexts: " + nexts.length;
        }
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public V get(K key) {
        checkKey(key);
        Node<K, V> node = first;
        for (int i = level - 1 ; i >= 0 ; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(node.nexts[i].key, key)) < 0) {
                node = node.nexts[i];
            }
            if (cmp == 0) return node.nexts[i].value;
        }
        return null;
    }

    private int randomLevel() {
        int level = 1;
        while (Math.random() < probablity && level < maxLevel) {
            level ++;
        }
        return level;
    }

    public V put(K key, V value) {
        checkKey(key);
        Node<K, V> node = first;
        Node<K, V>[] prevs = new Node[level];
        for (int i = level - 1 ; i >= 0 ; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(node.nexts[i].key, key)) < 0) {
                node = node.nexts[i];
            }
            if (cmp == 0) {
                V oldValue = node.nexts[i].value;
                node.nexts[i].value = value;
                return value;
            }
            prevs[i] = node;
        }

        int newLevel = randomLevel();
        Node<K, V> newNode = new Node<>(key, value, newLevel);

        for (int i = 0; i < newLevel; i++) {
            if (i >= level) {
                first.nexts[i] = newNode;
            }else {
                newNode.nexts[i] = prevs[i].nexts[i];
                prevs[i].nexts[i] = newNode;
            }
        }
        level = Math.max(level, newLevel);
        size ++;
        return null;
    }

    public V remove(K key) {
        checkKey(key);
        Node<K, V> node = first;
        Node<K, V>[] prevs = new Node[level];
        boolean exits = false;
        for (int i = level - 1 ; i >= 0 ; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(node.nexts[i].key, key)) < 0) {
                node = node.nexts[i];
            }
            if (cmp == 0) exits = true;
            prevs[i] = node;
        }
        if (!exits) return null;
        Node<K, V> removeNode = node.nexts[0];
        for (int i = 0; i < removeNode.nexts.length; i++) {
            prevs[i].nexts[i] = removeNode.nexts[i];
        }
        int newLevel = level;
        while (--newLevel > 0 && first.nexts[newLevel] != null){
            level = newLevel;
        }
        size -- ;
        return removeNode.value;
    }

    private void checkKey(K key) {
        if (key == null) {
            throw new IllegalArgumentException("key cannot be null..");
        }
    }


    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("Total Level: ").append(level).append("\n");

        for (int i = level - 1; i >= 0; i--) {
            Node<K, V> node = first;
            while (node.nexts[i] != null) {
                s.append(node.nexts[i]);
                s.append("\t");
                node = node.nexts[i];
            }
            s.append("\n");
        }

        return s.toString();
    }
}
