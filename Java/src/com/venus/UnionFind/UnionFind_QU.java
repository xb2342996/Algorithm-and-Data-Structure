package com.venus.UnionFind;

public class UnionFind_QU extends UnionFind{

    public UnionFind_QU(int capacity) {
        super(capacity);
    }

    @Override
    public int find(int v) {
        rangeCheck(v);
        while (parents[v] != v) {
            v = parents[v];
        }
        return v;
    }

    @Override
    public void union(int v1, int v2) {
        int p1 = parents[v1];
        int p2 = parents[v2];
        if (p1 == p2) return;
        parents[p1] = p2;
    }
}
