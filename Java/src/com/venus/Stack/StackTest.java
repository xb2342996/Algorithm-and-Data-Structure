package com.venus.Stack;

public class StackTest {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        // push
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        // pop & top
        System.out.println(stack.top());
        stack.pop();
        System.out.println(stack.top());
        stack.pop();
        System.out.println(stack.top());
        stack.pop();
        System.out.println(stack.top());
    }
}
