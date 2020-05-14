package com.venus.Map;

import com.venus.Set.Set;

public interface Map<K, V> {
    int size();

    boolean isEmpty();

    void clear();
    boolean containsKey(K element);
    boolean containsValue(V value);

    V put(K key, V value);
    V get(K key);
    V remove(K key);

    void travesal(Visitor<K, V> visitor);

    public static abstract class Visitor<K, V> {
        boolean stop;
        public abstract boolean visit(K key, V value);
    }
}
