package com.venus.Graph;

import com.venus.Heap.BinaryHeap;
import com.venus.Stack.Stack;
import com.venus.UnionFind.GenericUnionFind;
import com.venus.UnionFind.UnionFind;


import java.util.*;

@SuppressWarnings("ALL")
public class ListGraph<V, E> extends Graph<V, E>{

    private Map<V, Vertex<V, E>> vertices = new HashMap<>();
    private Set<Edge<V, E>> edges = new HashSet<>();

    private Comparator<Edge<V, E>> edgeComparator = (Edge<V, E> e1, Edge<V, E> e2) -> {
        return weightManager.compare(e1.weight, e2.weight);
    };

    public ListGraph(){}

    public ListGraph(WeightManager<E> weightManager) {
        super(weightManager);
    }

    private static class Vertex<V, E>{
        V value;
        Set<Edge<V, E>> inedges = new HashSet<>();
        Set<Edge<V, E>> outedges = new HashSet<>();

        public Vertex(V value) {
            this.value = value;
        }

        @Override
        public boolean equals(Object o) {
            return Objects.equals(value, ((Vertex<V, E>)o).value);
        }

        @Override
        public int hashCode() {
            return value == null ? 0 : value.hashCode();
        }

        @Override
        public String toString() {
            return value == null ? "null" : value.toString();
        }
    }

    private static class Edge<V, E>{
        Vertex<V, E> from;
        Vertex<V, E> to;
        E weight;

        public Edge(Vertex<V, E> from, Vertex<V, E> to) {
            this.from = from;
            this.to = to;
        }

        public EdgeInfo<V, E> info() {
            return new EdgeInfo<>(from.value, to.value, weight);
        }

        @Override
        public boolean equals(Object o) {
            Edge<V, E> edge = (Edge<V, E>) o;
            return Objects.equals(from, edge.from) &&
                    Objects.equals(to, edge.to);
        }

        @Override
        public int hashCode() {
            return from.hashCode() * 31 + to.hashCode();
        }

        @Override
        public String toString() {
            StringBuilder s = new StringBuilder();
            s.append("Edge [" + "from=").append(from).append(", to=").append(to);
            if (weight != null){
                  s.append(", weight=").append(weight);
            }
            s.append(']');
            return s.toString();
        }
    }

    @Override
    public int edgeSize() {
        return edges.size();
    }

    @Override
    public int vertexSize() {
        return vertices.size();
    }

    @Override
    public void addVertex(V v) {
        if (vertices.containsKey(v)) return;
        vertices.put(v, new Vertex<>(v));
    }

    @Override
    public void addEdge(V from, V to) {
        addEdge(from, to, null);
    }

    @Override
    public void addEdge(V from, V to, E weight) {
        Vertex<V, E> newFrom = vertices.get(from);
        if (newFrom == null) {
            newFrom = new Vertex<>(from);
            vertices.put(from, newFrom);
        }
        Vertex<V, E> newTo = vertices.get(to);
        if (newTo == null) {
            newTo = new Vertex<>(to);
            vertices.put(to, newTo);
        }

        Edge<V, E> newEdge = new Edge<V, E>(newFrom, newTo);
        newEdge.weight = weight;
        if (newFrom.outedges.remove(newEdge)) {
            newTo.inedges.remove(newEdge);
            edges.remove(newEdge);
        }
        edges.add(newEdge);
        newFrom.outedges.add(newEdge);
        newTo.inedges.add(newEdge);
    }

    @Override
    public void remove(V v) {
        Vertex<V, E> removeVertex = vertices.remove(v);
        if (removeVertex == null) return;

        for (Iterator<Edge<V, E>> iterator = removeVertex.outedges.iterator(); iterator.hasNext();) {
            Edge<V, E> edge = iterator.next();
            edge.to.inedges.remove(edge);
            iterator.remove();
            edges.remove(edge);
        }

        for (Iterator<Edge<V, E>> iterator = removeVertex.inedges.iterator(); iterator.hasNext();) {
            Edge<V, E> edge = iterator.next();
            edge.from.outedges.remove(edge);
            iterator.remove();
            edges.remove(edge);
        }
    }

    @Override
    public void remove(V from, V to) {
        Vertex<V, E> fromVertex = vertices.get(from);
        Vertex<V, E> toVertex = vertices.get(to);
        if (fromVertex == null || toVertex == null) return;

        Edge<V, E> edge = new Edge<>(fromVertex, toVertex);
        if (fromVertex.outedges.remove(edge)){
            toVertex.inedges.remove(edge);
            edges.remove(edge);
        }
    }

    public void print() {
        System.out.println("-------------------------------");
        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            System.out.println(v);
            System.out.print("Inedges:");
            System.out.println(vertex.inedges);
            System.out.print("Outedges:");
            System.out.println(vertex.outedges);
        });
        System.out.println("-------------------------------");
        edges.forEach((Edge<V, E> edge) -> {
            System.out.println(edge);
        });
    }

    @Override
    public void bfs(V v) {
        Vertex<V, E> vertex = vertices.get(v);
        if (vertex == null) return;

        Queue<Vertex<V, E>> queue = new LinkedList<>();
        Set<Vertex<V, E>> visitedV = new HashSet<>();
        queue.offer(vertex);
        visitedV.add(vertex);

        while (!queue.isEmpty()){
            vertex = queue.poll();
            System.out.println(vertex.value);
            for (Edge<V, E> edge: vertex.outedges) {
                if (visitedV.contains(edge.to)) continue;
                queue.offer(edge.to);
                visitedV.add(edge.to);
            }
        }
    }

    @Override
    public void dfs(V v) {
        Vertex<V, E> vertex = vertices.get(v);
        if (vertex == null) return;

        Set<Vertex<V, E>> visitedV = new HashSet<>();
        Stack<Vertex<V, E>> stack = new Stack<>();
        stack.push(vertex);
        visitedV.add(vertex);
        System.out.println(vertex.value);
        while (!stack.isEmpty()) {
            vertex = stack.pop();
            for (Edge<V, E> edge: vertex.outedges) {
//                System.out.println("visited node: "+ edge.to.value);
//                System.out.println(visitedV);
                if (visitedV.contains(edge.to)) continue;
                stack.push(edge.from);
                stack.push(edge.to);
                visitedV.add(edge.to);
                System.out.println(edge.to.value);
                break;
            }
        }
    }

    @Override
    public List<V> topology() {
        Map<Vertex<V, E>, Integer> index = new HashMap<>();
        List<V> list = new ArrayList<>();
        Queue<Vertex<V, E>> queue = new LinkedList<>();

        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            int indegree = vertex.inedges.size();
            if (indegree == 0) {
                queue.offer(vertex);
            }else {
                index.put(vertex, indegree);
            }
        });
        Vertex<V, E> vertex;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            list.add(vertex.value);
            for (Edge<V, E> edge: vertex.outedges) {
                int toIndegree = index.get(edge.to) - 1;
                if (toIndegree == 0) {
                    queue.offer(edge.to);
                } else {
                    index.put(edge.to, toIndegree);
                }
            }
        }

        return list;
    }

    @Override
    public void mst() {
//        prim();
        kruskal();
    }

    private Set<EdgeInfo<V, E>> prim() {
        Iterator<Vertex<V, E>> it = vertices.values().iterator();
        if (!it.hasNext()) return null;
        Vertex<V, E> vertex = it.next();

        Set<Vertex<V, E>> addedVertices = new HashSet<>();
        Set<EdgeInfo<V, E>> edgeInfos = new HashSet<>();
        addedVertices.add(vertex);
        BinaryHeap<Edge<V, E>> heap = new BinaryHeap<>(vertex.outedges, edgeComparator);
        while (addedVertices.size() < vertexSize() && !heap.isEmpty()) {
            Edge<V, E> minEdge = heap.remove();

            if (addedVertices.contains(minEdge.to)) continue;
            heap.addAll(minEdge.to.outedges);
            edgeInfos.add(minEdge.info());
            addedVertices.add(minEdge.to);
        }
        return edgeInfos;
    }

    private Set<EdgeInfo<V, E>> kruskal() {
        int edgeSize = vertices.size() - 1;
        if (edgeSize == 1) return null;

        Set<EdgeInfo<V, E>> edgeInfos = new HashSet<>();
        BinaryHeap<Edge<V,E>> heap = new BinaryHeap<>(edges, edgeComparator);
        GenericUnionFind<Vertex<V, E>> unionFind = new GenericUnionFind<>();
        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            unionFind.makeSet(vertex);
        });

        while (!heap.isEmpty()) {
            Edge<V, E> edge = heap.remove();
            if (unionFind.isSame(edge.from, edge.to)) continue;
            edgeInfos.add(edge.info());
            unionFind.union(edge.from, edge.to);
        }
        return edgeInfos;
    }

    public Map<V, Map<V, PathInfo<V, E>>> multiShortestPath() {
        Map<V, Map<V, PathInfo<V, E>>> paths = new HashMap<>();
        for (Edge<V, E> edge: edges) {
            Map<V, PathInfo<V, E>> map = paths.get(edge.from.value);
            if (map == null) {
                map = new HashMap<>();
                paths.put(edge.from.value, map);
            }
            PathInfo<V, E> info = new PathInfo<>(edge.weight);
            info.paths.add(edge.info());
            map.put(edge.to.value, info);
        }

        vertices.forEach((V vk, Vertex<V, E> vertexk) -> {
            vertices.forEach((V vi, Vertex<V, E> vertexi) -> {
                vertices.forEach((V vj, Vertex<V, E> vertexj) -> {
                    if (vk.equals(vi) || vk.equals(vj) || vj.equals(vi)) return;

                    PathInfo<V, E> pathik = getPathInfo(vi, vk, paths);
                    if (pathik == null) return;
                    PathInfo<V, E> pathkj = getPathInfo(vk, vj, paths);
                    if (pathkj == null) return;
                    PathInfo<V, E> pathij = getPathInfo(vi, vj, paths);

                    E newWeight = weightManager.add(pathik.weight, pathkj.weight);
                    if (pathij != null && weightManager.compare(newWeight, pathij.weight) >= 0) return;

                    if (pathij == null) {
                        pathij = new PathInfo<>();
                        paths.get(vi).put(vj, pathij);
                    }else {
                        pathij.paths.clear();
                    }
                    pathij.paths.addAll(pathik.paths);
                    pathij.paths.addAll(pathkj.paths);
                    pathij.weight = newWeight;
                });
            });
        });

        return paths;
    }

    private PathInfo<V, E> getPathInfo(V v1, V v2, Map<V, Map<V, PathInfo<V, E>>> paths) {
        Map<V, PathInfo<V, E>> map = paths.get(v1);
        return map == null ? null : map.get(v2);
    }

    public Map<V, PathInfo<V, E>> shortestPath(V v) {
//        return dijkstra(v);
        return bellmanFord(v);
    }

    private Map<V, PathInfo<V, E>> bellmanFord(V begin) {

        Vertex<V, E> beginVertex = vertices.get(begin);
        if (beginVertex == null) return null;

        Map<V, PathInfo<V, E>> selectedPath = new HashMap<>();
        selectedPath.put(begin, new PathInfo<>(weightManager.zero()));

        int count = vertices.size() - 1;
        for (int i = 0; i < count; i++) {
            for (Edge<V, E> edge: edges) {
                PathInfo<V, E> minPath = selectedPath.get(edge.from.value);
                if (minPath == null) continue;
                relax_bf(selectedPath, minPath, edge);
            }
        }
        for (Edge<V, E> edge: edges) {
            PathInfo<V, E> minPath = selectedPath.get(edge.from.value);
            if (minPath == null) continue;
            if(relax_bf(selectedPath, minPath, edge)){
                System.out.println("negative weight cycle, no shortest path");
                return null;
            }
        }
        selectedPath.remove(begin);
        return selectedPath;
    }

    private Map<V, PathInfo<V, E>> dijkstra(V begin){
        Vertex<V, E> beginVertex = vertices.get(begin);
        if (beginVertex == null) return null;

        Map<V, PathInfo<V, E>> selectedPath = new HashMap<>();
        Map<Vertex<V, E>, PathInfo<V, E>> paths = new HashMap<>();
        paths.put(beginVertex, new PathInfo<>(weightManager.zero()));
//        for (Edge<V, E> edge: beginVertex.outedges) {
//            PathInfo<V, E> pathInfo = new PathInfo<>();
//            pathInfo.weight = edge.weight;
//            pathInfo.paths.add(edge.info());
//            paths.put(edge.to, pathInfo);
//        };
        while (!paths.isEmpty()) {
            Map.Entry<Vertex<V, E>, PathInfo<V, E>> entry = getMin(paths);
            Vertex<V, E> minVertex = entry.getKey();
            PathInfo<V, E> minPath = entry.getValue();

            selectedPath.put(minVertex.value, minPath);
            paths.remove(minVertex);

            for (Edge<V, E> edge : minVertex.outedges) {
                if (selectedPath.containsKey(edge.to.value)) continue;
                relax_djs(paths, minPath, edge);
            }
        }
        selectedPath.remove(begin);
        return selectedPath;
    }

    private boolean relax_bf(Map<V, PathInfo<V, E>> paths, PathInfo<V, E> minPath, Edge<V, E> edge) {
        E newWeight = weightManager.add(minPath.weight, edge.weight);
        PathInfo<V, E> oldPath = paths.get(edge.to.value);
        if (oldPath != null && weightManager.compare(newWeight, oldPath.weight) >= 0) return false;
        if (oldPath == null) {
            oldPath = new PathInfo<>();
            paths.put(edge.to.value, oldPath);
        } else {
            oldPath.paths.clear();
        }

        oldPath.weight = newWeight;
        oldPath.paths.addAll(minPath.paths);
        oldPath.paths.add(edge.info());
        return true;
    }

    private void relax_djs(Map<Vertex<V, E>, PathInfo<V, E>> paths, PathInfo<V, E> minPath, Edge<V, E> edge) {

        E newWeight = weightManager.add(minPath.weight, edge.weight);
        PathInfo<V, E> oldPath = paths.get(edge.to);
        if (oldPath != null && weightManager.compare(newWeight, oldPath.weight) >= 0) return;
        if (oldPath == null) {
            oldPath = new PathInfo<>();
            paths.put(edge.to, oldPath);
        } else {
            oldPath.paths.clear();
        }

        oldPath.weight = newWeight;
        oldPath.paths.addAll(minPath.paths);
        oldPath.paths.add(edge.info());
    }

    private Map.Entry<Vertex<V, E>, PathInfo<V, E>> getMin(Map<Vertex<V, E>, PathInfo<V, E>> paths){
        Iterator<Map.Entry<Vertex<V, E>, PathInfo<V, E>>> it = paths.entrySet().iterator();
        Map.Entry<Vertex<V, E>, PathInfo<V, E>> minEntry = it.next();
        while (it.hasNext()) {
            Map.Entry<Vertex<V, E>, PathInfo<V, E>> entry = it.next();
            if (weightManager.compare(minEntry.getValue().weight, entry.getValue().weight) > 0) {
                minEntry = entry;
            }
        }
        return minEntry;
    }
}
