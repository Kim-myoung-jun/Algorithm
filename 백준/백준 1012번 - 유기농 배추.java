# https://www.acmicpc.net/problem/1012

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int t = Integer.parseInt(st.nextToken());

		for (int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());

			int cnt = 0;
			int[][] data = new int[m][n];
			for (int j = 0; j < k; j++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				data[x][y] = 1;
			}

			for (int q = 0; q < m; q++) {
				for (int w = 0; w < n; w++) {
					if(dfs(data, q, w)) {
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}
	}

	private static boolean dfs(int[][] data, int q, int w) {
		// TODO Auto-generated method stub
		
		if(q==-1 || w == -1 || w == data[0].length || q == data.length) {
			return false;
		}
		
		if(data[q][w] == 1) {
			data[q][w] = 2;
			dfs(data, q-1, w);
			dfs(data, q+1, w);
			dfs(data, q, w-1);
			dfs(data, q, w+1);
			return true;
		}
		return false;
	}

}
