package com.venus.UnionFind;

import java.util.HashMap;
import java.util.Objects;

public class GenericUnionFind<V> {

    HashMap<V, Node<V>> nodes = new HashMap<>();

    public void makeSet(V v) {
        if (nodes.containsKey(v)) return;
        nodes.put(v, new Node<>(v));
    }

    public V find(V v) {

        Node<V> node = findNode(v);
        return node == null ? null : node.value;
    }

    public Node<V> findNode(V v){
        Node<V> node = nodes.get(v);
        if (node == null) return null;
        while (!Objects.equals(node.value, node.parent.value)) {
            node.parent = node.parent.parent;
            node = node.parent;
        }
        return node;
    }

    public void union(V v1, V v2) {
        Node<V> n1 = findNode(v1);
        Node<V> n2 = findNode(v2);

        if (n1 == null || n2 == null) return;;
        if (Objects.equals(n1.value, n2.value)) return;;

        if (n1.rank > n2.rank) {
            n2.parent = n1;
        }else if(n1.rank < n2.rank){
            n1.parent = n2;
        }else {
            n1.parent = n2;
            n2.rank += 1;
        }

    }

    public boolean isSame(V v1, V v2) {
        return Objects.equals(find(v1), find(v2));
    }

    private static class Node<V>{
        V value;
        Node<V> parent = this;
        int rank = 1;
        Node(V value){
            this.value = value;
        }
    }
}
