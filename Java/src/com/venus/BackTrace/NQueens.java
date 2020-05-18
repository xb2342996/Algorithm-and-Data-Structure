package com.venus.BackTrace;

public class NQueens {
    public static void main(String[] args) {
        new NQueens().place(8);
    }

    int[] cols;
    int methods = 0;
    void place(int n){
        cols = new int[n];
        placeQueens(0);

        System.out.println(methods);
    }
    void placeQueens(int row) {
        if (row == cols.length) {
            methods += 1;
            show();
            return;
        }
        for (int col = 0; col < cols.length; col++) {
            if (isValid(row, col)){
                cols[row] = col;
                placeQueens(row + 1);
            }
        }
    }

    boolean isValid(int row, int col) {
        for (int k = 0; k < row; k++) {
            if ((cols[k] == col) || Math.abs(col - cols[k]) == Math.abs(row - k)) return false;
        }
        return true;
    }

    void show() {
        for (int i = 0; i < cols.length; i++) {
            for (int j = 0; j < cols.length; j++) {
                if (cols[i] == j) {
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
