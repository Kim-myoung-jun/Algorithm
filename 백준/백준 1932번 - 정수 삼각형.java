import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		int [][] data = new int[n][n];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<i+1; j++) {
				data[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i=1; i<n; i++) {
			for(int j=0; j<i+1; j++) {
				if(j == 0) {
					data[i][j] += data[i-1][j];
				} else if (j == i) {
					data[i][j] += data[i-1][j-1];
				} else {
					data[i][j] += Math.max(data[i-1][j], data[i-1][j-1]);
				}
			}
		}
		
		int max = 0;
		for(int i=0; i<n; i++) {
			if(data[n-1][i] > max) {
				max = data[n-1][i];
			}
		}
		System.out.println(max);
	}
}
