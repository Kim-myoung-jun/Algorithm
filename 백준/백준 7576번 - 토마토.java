import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
	
	public static int [][] data = null;
	public static Queue<String> q = new LinkedList<String>();
	public static int one_cnt = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		data = new int[m][n];
		
		for(int i=0; i<m; i++) {
			String s = br.readLine();
			String [] s_arr = s.split(" ");
			
			for(int j=0; j<n; j++) {
				data[i][j] = Integer.parseInt(s_arr[j]);
				if(data[i][j] == 1) {
					q.add(Integer.toString(i)+","+Integer.toString(j));
					one_cnt++;
				}
			}
		}
		
		System.out.println(bfs(n, m));
	}
	
	public static int bfs(int n, int m) {
		int [] dx = {-1, 1, 0, 0};
		int [] dy = {0, 0, -1, 1};
		
		int cnt = 1;
		
		while(!q.isEmpty()) {
			Queue<String> next_q = new LinkedList<String>();
			int next_cnt = 0;
			for(int i=0; i<one_cnt; i++) {
				String s_now = q.poll();
				String [] s_now_arr = s_now.split(",");
				int now_x = Integer.parseInt(s_now_arr[0]);
				int now_y = Integer.parseInt(s_now_arr[1]);
				
				for(int j=0; j<4; j++) {
					int next_x = now_x+dx[j];
					int next_y = now_y+dy[j];
					
					if(next_x < 0 || next_x >= m || next_y < 0 || next_y >= n) {
						continue;
					}
					if(data[next_x][next_y] == 0) {
						data[next_x][next_y] = cnt;
						next_q.add(Integer.toString(next_x)+","+Integer.toString(next_y));
						next_cnt++;
					}
				}
				
			}
			q = next_q;
			cnt++;
			one_cnt = next_cnt;
		}
		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++ ) {
				if(data[i][j] == 0) {
					return -1;
				}
			}
		}
		return cnt-2;
	}
}
