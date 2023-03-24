import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		int [][] house = new int [1001][n];
		house[0][0] = 0;
		house[0][1] = 0;
		house[0][2] = 0;
		
		for(int i=1; i<n+1; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			house[i][0] = Min(house[i-1][1], house[i-1][2]) + r;
			house[i][1] = Min(house[i-1][0], house[i-1][2]) + g;
			house[i][2] = Min(house[i-1][0], house[i-1][1]) + b;
		}
		System.out.println(Min(Min(house[n][0], house[n][1]), house[n][2]));
	}
	static int Min(int a, int b) {
		if( a > b )
			return b;
		else
			return a;
	}
}
