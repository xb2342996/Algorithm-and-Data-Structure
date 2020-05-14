package com.venus.Graph;

import java.util.Map;

public class GraphTest {
    static Graph.WeightManager<Double> weightManager = new Graph.WeightManager<Double>() {
        @Override
        public int compare(Double w1, Double w2) {
            return w1.compareTo(w2);
        }

        @Override
        public Double add(Double w1, Double w2) {
            return w1 + w2;
        }

        @Override
        public Double zero() {
            return 0.0;
        }
    };

    public static void main(String[] args) {
//        graphTest();
//        bfsTest();
//        dfsTest();
//        topoTest();
//        mstTest();
        multiSpTest();
    }

    static void multiSpTest(){
        Graph<Object, Double> graph = directedGraph(Data.SP);
        System.out.println(graph.multiShortestPath());
    }
    static void spTest(){
        Graph<Object, Double> graph = directedGraph(Data.SP);
        Map<Object, Graph.PathInfo<Object, Double>> sp = graph.shortestPath("A");
        sp.forEach((Object v, Graph.PathInfo<Object, Double> path) -> {
            System.out.println(v + ": "+path);
        });
    }
    static void mstTest() {
        Graph<Object, Double> graph = undirectedGraph(Data.MST_02);
        graph.mst();
    }
    static void graphTest() {
        ListGraph<String, Integer> graph = new ListGraph<>();
//        graph.addEdge("V0", "V1");
//		graph.addEdge("V1", "V0");
//		graph.addEdge("V0", "V2");
//		graph.addEdge("V2", "V0");
//
//		graph.addEdge("V0", "V3");
//		graph.addEdge("V3", "V0");
//
//		graph.addEdge("V1", "V2");
//		graph.addEdge("V2", "V1");
//
//		graph.addEdge("V2", "V3");
//		graph.addEdge("V3", "V2");

        graph.addEdge("V1", "V0", 9);
        graph.addEdge("V1", "V2", 3);
        graph.addEdge("V2", "V0", 2);
        graph.addEdge("V2", "V3", 5);
        graph.addEdge("V3", "V4", 1);
        graph.addEdge("V0", "V4", 6);
        graph.addEdge("V0", "V4", 100);
        graph.remove("V0", "V4");
		graph.print();
    }

    private static void bfsTest() {
        Graph<Object, Double> graph = undirectedGraph(Data.BFS_01);
        graph.bfs("A");
    }

    private static void dfsTest() {
        Graph<Object, Double> graph = directedGraph(Data.DFS_02);
        graph.dfs("a");
    }

    private static void topoTest() {
        Graph<Object, Double> graph = directedGraph(Data.TOPO);
        System.out.println(graph.topology());
    }
    /**
     * 有向图
     */
    private static Graph<Object, Double> directedGraph(Object[][] data) {
        Graph<Object, Double> graph = new ListGraph<>(weightManager);
        for (Object[] edge : data) {
            if (edge.length == 1) {
                graph.addVertex(edge[0]);
            } else if (edge.length == 2) {
                graph.addEdge(edge[0], edge[1]);
            } else if (edge.length == 3) {
                double weight = Double.parseDouble(edge[2].toString());
                graph.addEdge(edge[0], edge[1], weight);
            }
        }
        return graph;
    }

    /**
     * 无向图
     * @param data
     * @return
     */
    private static Graph<Object, Double> undirectedGraph(Object[][] data) {
        Graph<Object, Double> graph = new ListGraph<>(weightManager);
        for (Object[] edge : data) {
            if (edge.length == 1) {
                graph.addVertex(edge[0]);
            } else if (edge.length == 2) {
                graph.addEdge(edge[0], edge[1]);
                graph.addEdge(edge[1], edge[0]);
            } else if (edge.length == 3) {
                double weight = Double.parseDouble(edge[2].toString());
                graph.addEdge(edge[0], edge[1], weight);
                graph.addEdge(edge[1], edge[0], weight);
            }
        }
        return graph;
    }
}
