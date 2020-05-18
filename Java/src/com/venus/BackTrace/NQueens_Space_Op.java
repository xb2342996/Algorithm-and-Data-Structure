package com.venus.BackTrace;

public class NQueens_Space_Op {

    public static void main(String[] args) {
        new NQueens_Space_Op().placeQueen(4);
    }

    private int[] queens;
    private boolean[] cols;
    private boolean[] leftTop;
    private boolean[] rightTop;
    private int ways;

    private void placeQueen(int n) {
        cols = new boolean[n];
        leftTop = new boolean[(n << 1) - 1];
        rightTop = new boolean[(n << 1) - 1];
        queens = new int[n];
        place(0);
        System.out.println("Total methods: " + ways);
    }

    private void place(int row){

        if (row == cols.length) {
            ways++;
            show();
            return;
        }

        for (int col = 0; col < cols.length; col++) {
            if (cols[col]) continue;
            if (leftTop[row + col]) continue;
            if (rightTop[cols.length + row - col - 1]) continue;

            cols[col] = true;
            leftTop[row + col] = true;
            rightTop[cols.length + row - col - 1] = true;

            queens[col] = row;
            place(row + 1);

            cols[col] = false;
            leftTop[row + col] = false;
            rightTop[cols.length + row - col - 1] = false;
        }
    }
    void show() {
        for (int i = 0; i < cols.length; i++) {
            for (int j = 0; j < cols.length; j++) {
                if (queens[i] == j) {
                    System.out.print("1 ");
                }else {
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
        System.out.println("------------------");
    }
}
