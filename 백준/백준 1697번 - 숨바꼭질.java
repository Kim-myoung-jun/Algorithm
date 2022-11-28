import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static Queue<Integer> q = new LinkedList<>();
	static int [] visited = new int[100001];
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();
		String [] s_arr = s.split(" ");
		int n = Integer.parseInt(s_arr[0]);
		int k = Integer.parseInt(s_arr[1]);



		bfs(n, k);
	}

	public static void bfs(int n, int k) {
		if(n > k) {
			System.out.println(n-k);
			return;
		}
		q.add(n);
		while(!q.isEmpty()) {
			int now = q.poll();
			if(now == k) {
				System.out.println(visited[k]);
				return;
			}
			int [] next = {now-1, now+1, now*2};
			for(int i=0; i<3; i++) {
				if(next[i] >= 0 && next[i] <= 100000) {
					if(visited[next[i]] == 0) {
						visited[next[i]] = visited[now] + 1;
						q.add(next[i]);
					}
				}
			}
		}
	}
}
