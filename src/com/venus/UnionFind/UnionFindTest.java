package com.venus.UnionFind;

public class UnionFindTest {

    static final int count = 8;

    public static void main(String[] args) {
        QFTest();
    }
    static void QFTest(){
        UnionFind_QF uf = new UnionFind_QF(count);
        uf.union(0, 1);
        uf.union(0, 3);
        uf.union(0, 4);
        uf.union(2, 3);
        uf.union(2, 5);
        uf.union(6, 7);

        System.out.println(uf.isSame(0,7));
        uf.union(4, 7);
        System.out.println(uf.isSame(0, 7));

        uf.show();
    }
}
