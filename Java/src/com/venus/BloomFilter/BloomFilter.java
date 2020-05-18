package com.venus.BloomFilter;

public class BloomFilter<T> {
    private int bitSize;
    private int hashSize;
    private long[] bits;

    public BloomFilter(int n, double p) {
        // 二进制位的个数
        double lg2 = Math.log(2);
        bitSize  = (int) (- (n * Math.log(p)) / (lg2 * lg2));
        // 哈希函数的个数
        hashSize  = (int) ((bitSize / n) * lg2);
        int bit_size = (bitSize + Long.SIZE - 1) / Long.SIZE;

        bits = new long[bit_size];
    }

    public boolean put(T value){
        nullValueCheck(value);
        int hash1 = value.hashCode();
        int hash2 = hash1 >>> 16;
        boolean result = false;
        for (int i = 1; i <= hashSize; i++) {
            int combinedHash = (hash2 * i) + hash1;
            if (combinedHash < 0) {
                combinedHash = -combinedHash;
            }
            int index = combinedHash % bitSize;
            if (set(index)) result = true;
        }

        return result;
    }

    private boolean set(int index) {
        long value = bits[index / Long.SIZE];
        int bitValue = 1 << (index % Long.SIZE);
        bits[index / Long.SIZE] = value | bitValue;
        return (value & bitValue) == 0;
    }

    private boolean get(int index) {
        long value = bits[index / Long.SIZE];
        return (value & (1 << (index % Long.SIZE))) != 0;
    }

    public boolean contains(T value){
        nullValueCheck(value);
        int hash1 = value.hashCode();
        int hash2 = hash1 >>> 16;
        for (int i = 1; i <= hashSize; i++) {
            int combinedHash = (hash2 * i) + hash1;
            if (combinedHash < 0) {
                combinedHash = -combinedHash;
            }
            int index = combinedHash % bitSize;
            if (!get(index)) return false;
        }
        return true;
    }

    private void nullValueCheck(T value) {
        if (value == null) {
            throw new IllegalArgumentException("value can not be null...");
        }
    }
}
