package com.venus.Queue;

public class QueueTest {
    public static void main(String[] args) {

    }

    public void cycleDequeTest() {
        CycleDeque<Integer> queue = new CycleDeque<>();
        // rear & front enqueue
        for (int i = 0; i < 10; i++) {
            queue.enqueueRear(i);
            queue.enqueueFront(i + 10);
        }
        // dequeue from rear & front
        for (int i = 0; i < 5; i++) {
            System.out.println(queue.dequeueFront());
            System.out.println(queue.dequeueRear());
        }
        queue.enqueueRear(73);
        queue.enqueueFront(52 + 10);
        System.out.println(queue);
    }

    public void dequeTest() {
        Deque<Integer> deque = new Deque<>();
        deque.enqueueFront(15);
        deque.enqueueRear(19);
        deque.enqueueFront(83);
        deque.enqueueRear(76);

        for (int i = 0; i < 2; i++) {
            System.out.println(deque.dequeueFront());
            System.out.println(deque.dequeueRear());
        }
    }

    public void cycleQueueTest() {
        CycleQueue<Integer> queue = new CycleQueue<>();
        // enqueue
        for (int i = 0; i < 10; i++) {
            queue.enqueue(i * 7);
        }

        // dequque
        for (int i = 0; i < 5; i++) {
            queue.dequeue();
        }
        System.out.println(queue);

        // enqueue
        queue.enqueue(22);
        queue.enqueue(33);
        for (int i = 0; i < 10; i++) {
            queue.enqueue(i * 10);
        }

        System.out.println(queue);
    }

    public void queueTest() {
        Queue<Integer> queue = new Queue<>();

        queue.enqueue(4);
        queue.enqueue(14);
        queue.enqueue(29);
        queue.enqueue(28);

        for (int i = 0; i < 4; i++) {
            System.out.println(queue.dequeue());
        }
    }
}
