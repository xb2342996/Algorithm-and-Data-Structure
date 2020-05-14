package com.venus.Graph;


import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public abstract class Graph<V, E> {
    protected WeightManager<E> weightManager;

    public Graph() {}

    public Graph(WeightManager<E> weightManager) {
        this.weightManager = weightManager;
    }
    // 边的数量
    public abstract int edgeSize();
    // 顶点的数量
    public abstract int vertexSize();
    // 添加点
    public abstract void addVertex(V v);
    // 添加边 （无权重）
    public abstract void addEdge(V from, V to);
    // 添加边（有权重）
    public abstract void addEdge(V from, V to, E weight);
    // 移除顶点
    public abstract void remove(V v);
    // 移除边
    public abstract void remove(V from, V to);

    public abstract void bfs(V v);

    public abstract void dfs(V v);

    public abstract List<V> topology();

    public abstract void mst();
    public abstract Map<V, PathInfo<V, E>> shortestPath(V v);
    public abstract Map<V, Map<V, PathInfo<V, E>>> multiShortestPath();

    public interface WeightManager<E> {
        int compare(E w1, E w2);
        E add(E w1, E w2);
        E zero();
    }

    public static class EdgeInfo<V, E>{
        private V from;
        private V to;
        private E weight;

        public EdgeInfo(V from, V to, E weight) {
            super();
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        public V getTo() {
            return to;
        }

        public void setTo(V to) {
            this.to = to;
        }

        public E getWeight() {
            return weight;
        }

        public void setWeight(E weight) {
            this.weight = weight;
        }

        public V getFrom() {
            return from;
        }

        public void setFrom(V from) {
            this.from = from;
        }

        @Override
        public String toString() {
            return "EdgeInfo[" +
                    "from=" + from +
                    ", to=" + to +
                    ", weight=" + weight +
                    ']';
        }
    }

    public static class PathInfo<V, E>{
        E weight;
        LinkedList<EdgeInfo<V, E>> paths = new LinkedList<>();
        public PathInfo(){}

        public PathInfo(E weight){
            this.weight = weight;
        }

        public E getWeight() {
            return weight;
        }

        public void setWeight(E weight) {
            this.weight = weight;
        }

        public LinkedList<EdgeInfo<V, E>> getPaths() {
            return paths;
        }

        public void setPaths(LinkedList<EdgeInfo<V, E>> paths) {
            this.paths = paths;
        }

        @Override
        public String toString() {
            StringBuilder s = new StringBuilder();
            double total = 0.0;
            s.append(paths.getFirst().from);
            for (EdgeInfo<V, E> edgeInfo : paths) {
                s.append(" -> ").append(edgeInfo.to);
                total += (Double) edgeInfo.weight;
            }
            s.append(", weight:" + total);
            return s.toString();
        }
    }
}
