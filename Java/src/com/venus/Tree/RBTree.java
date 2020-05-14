package com.venus.Tree;

import java.util.Comparator;

@SuppressWarnings("ALL")
public class RBTree<E> extends BBSTree<E> {

    private static final boolean BLACK = true;
    private static final boolean RED = false;

    public RBTree() {
        this(null);
    }
    public RBTree(Comparator<E> comparator) {
        super(comparator);
    }

    @Override
    protected Node<E> createNode(E element, Node<E> parent) {
        return new RBNode<>(element, parent);
    }

    @Override
    public void afterAdd(Node<E> node) {
        Node<E> parent = node.parent;

        // 插入node的parent为空，说明是插入的是root，将node染成黑色，结束
        if (parent == null) {
            black(node);
            return;
        }
        // 4阶B树叶子节点只有一个节点情况，如果node的parent为黑色，结束
        if (isBlack(parent)) return;

        Node<E> uncle = parent.sibling();
        // 先将grand节点染成红色，后面涉及到grand节点都为红色
        Node<E> grand = red(parent.parent);

        // 4阶B树叶子节点有3个节点的情况，插入会破坏平衡，需要上溢节点，将parent与uncle染成黑色，grand染成红色，并将grand向上添加
        if (isRed(uncle)) {
            black(parent);
            black(uncle);
            afterAdd(grand);
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
    public void afterRemove(Node<E> node) {
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
        Node<E> parent = node.parent;
        if (parent == null) return;

        // 查看删除的节点是左节点还是右节点，parent可能为空
        boolean left = parent.left == null || node.isLeftChild();
        // 查找删除节点的兄弟节点
        Node<E> sibling = left ? parent.right : parent.left;

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

    // 将节点染色
    private Node<E> color(Node<E> node, boolean color){
        if (node == null) return node;
        ((RBNode<E>)node).color = color;
        return node;
    }
    // 将节点染成红色
    private Node<E> red(Node<E> node){
        return color(node, RED);
    }
    // 将节点染成黑色
    private Node<E> black(Node<E> node){
        return color(node, BLACK);
    }

    // 判断节点颜色
    private boolean colorOf(Node<E> node){
        return node == null ? BLACK : ((RBNode)node).color;
    }
    // 判断节点是不是黑色
    private boolean isBlack(Node<E> node){
        return colorOf(node) == BLACK;
    }
    // 判断节点是不是红色
    private boolean isRed(Node<E> node){
        return colorOf(node) == RED;
    }

    private static class RBNode<E> extends Node<E>{
        // 初始化节点为红色
        boolean color = RED;
        public RBNode(E element, Node<E> parent) {
            super(element, parent);
        }

        @Override
        public String toString() {
            String s = "";
            if (color == RED) {
                s = "(R)";
            } else {
                s = "(B)";
            }
            return element + s;
        }
    }
}
