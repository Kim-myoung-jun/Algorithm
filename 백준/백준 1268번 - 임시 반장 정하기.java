import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int [][] data = new int [n][5];
		int [][] result = new int[n][n];
		
		for(int i=0; i<n; i++) {
			String s = br.readLine();
			String [] arr = s.split(" ");
			for(int j=0; j<5; j++) {
				data[i][j] = Integer.parseInt(arr[j]);
			}
		}
		
		for(int j=0; j<5; j++) {
			for(int i=0; i<n-1; i++) {
				int cmp = data[i][j];
				for(int k=i+1; k<n; k++) {
					if(cmp == data[k][j]) {
						result[i][k] = 1;
						result[k][i] = 1;
					}
				}	
			}
		}
		
		int index = 0;
		int max = 0;
		for(int i=0; i<n; i++) {
			int tmp = 0;
			for(int j=0; j<n; j++) {
				if(result[i][j] == 1) {
					tmp++;
				}
			}
			if(max < tmp) {
				max = tmp;
				index = i;
			}
		}
		System.out.println(index+1);
	}
}
