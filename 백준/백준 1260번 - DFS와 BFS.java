// https://www.acmicpc.net/problem/1260

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static boolean [] visited_dfs;
	static boolean [] visited_bfs;
	static ArrayList<Integer>[] graph;
	static int n, m, v;
	static Queue<Integer> q = new LinkedList<>();

	public static void main(String[] args) throws IOException  {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());

		graph = new ArrayList[n+1];
		for(int i=1; i<=n; i++) {
			graph[i] = new ArrayList<>();
		}

		for(int i = 0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph[a].add(b);
			graph[b].add(a);
		}

		for(int i=1; i<=n; i++) {
			Collections.sort(graph[i]);
		}

		visited_dfs = new boolean[n+1];
		visited_bfs = new boolean[n+1];

		dfs(v);
		System.out.println();
		bfs(v);
	}

	private static void dfs(int now) {
		// TODO Auto-generated method stub
		visited_dfs[now] = true;
		System.out.print(now+" ");
		for(int next: graph[now]) {
			if(!visited_dfs[next]) {
				dfs(next);
			}
		}
	}


	private static void bfs(int now) {
		// TODO Auto-generated method stub
		visited_bfs[now] = true;
		q.add(now);
		while(!q.isEmpty()) {
			int v = q.poll();
			System.out.print(v+" ");
			for(int next: graph[v]) {
				if( visited_bfs[next] == false) {
					q.add(next);
					visited_bfs[next] = true;
				}
			}
		}

	}
}
