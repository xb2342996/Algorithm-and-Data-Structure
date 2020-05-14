package com.venus.Tree;

import com.venus.Tree.printer.BinaryTrees;

public class TreeTest {
    public static void main(String[] args) {
        bstTest();
//        avlTreeTest();
//        rbTreeTest();
    }

    public static void rbTreeTest() {
        Integer[] data = new Integer[] {
                95, 42, 87, 53, 17, 85, 46, 48, 73, 5, 20, 38, 41, 92, 19
        };
        RBTree<Integer> tree = new RBTree<>();
        // add node
        for (int i = 0; i < data.length; i++) {
            tree.add(data[i]);
//
        }
        tree.remove(41);
        BinaryTrees.println(tree);

        // remove node
//        for (int i = 0; i < data.length; i++) {
//            tree.remove(data[i]);
//            BinaryTrees.println(tree);
//        }
    }

    public static void avlTreeTest() {
        //
        Integer[] data = new Integer[] {
                97, 58, 51, 37, 78, 1, 42, 71, 18, 54, 57, 16, 41, 11, 66
        };
        AVLTree<Integer> tree = new AVLTree<>();
        // add node
        for (int i = 0; i < data.length; i++) {
            tree.add(data[i]);
            BinaryTrees.println(tree);
        }

        // remove node
        for (int i = 0; i < data.length; i++) {
            tree.remove(data[i]);
            BinaryTrees.println(tree);
        }

    }

    public static void bstTest() {
        Integer[] data = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3
        };
        BSTree<Integer> tree = new BSTree<>();
        // add node
        for (int i = 0; i < data.length; i++) {
            tree.add(data[i]);

        }
//        BinaryTrees.print(tree);
//        System.out.println();
        tree.add(1);
        // remove node
        tree.remove(7);
//        tree.add(10);
        BinaryTrees.print(tree);
        System.out.println();

        // reverse recursive
//        tree.reverse();
        // reverse level order
//        tree.reverseLevel();
//
//        BinaryTrees.print(tree);
//        System.out.println();


        // is complete
//        System.out.println(tree.isComplete());

        // tree height
//        System.out.println(tree.heightNotRecursize());
//        tree.remove(11);
//        BinaryTrees.print(tree);
//        System.out.println();
//
//        tree.remove(5);
//        BinaryTrees.print(tree);
//        System.out.println();
//        tree.remove(4);
//        BinaryTrees.print(tree);
//        System.out.println();

        // preorder travesal
//        tree.preorderTravesal();
        // inodrder travesal
//        tree.inorderTravesal(new BinaryTree.Visitor() {
//            @Override
//            public void visit(Object element) {
//                System.out.print(element + ",");
//            }
//        });
        // posterorder travesal
//        tree.posterorderTravesal(new BinaryTree.Visitor() {
//            @Override
//            public void visit(Object element) {
//                System.out.print(element + ",");
//            }
//        });
//         levelorder travesal
//        tree.levelOrderTravesal(new BinaryTree.Visitor() {
//            @Override
//            public void visit(Object element) {
//                System.out.print(element + ",");
//            }
//        });
    }
}
