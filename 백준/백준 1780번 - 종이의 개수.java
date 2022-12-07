import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

	static int m_1 = 0;
	static int zero = 0;
	static int p_1 = 0;
	static int [][] data;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		data = new int[n][n];
		for(int i=0; i<n;i++) {
			String s = br.readLine();
			String [] arr = s.split(" ");
			for(int j=0; j<n; j++) {
				data[i][j] = Integer.parseInt(arr[j]);
			}
		}
		
		recur(0, 0, n);
		System.out.println(m_1+"\n"+zero+"\n"+p_1);
	}
	
	public static void recur(int x, int y, int size) {
		if(check(x, y, size) == true) {
			if(data[x][y] == -1) {
				m_1++;
			} else if(data[x][y] == 0) {
				zero++;
			} else {
				p_1++;
			}
		} else {
			size /= 3;
			recur(x, y, size);
	        recur(x, y+size, size);
	        recur(x, y+size+size, size);
	        recur(x+size, y, size);
	        recur(x+size, y+size, size);
	        recur(x+size, y+size+size, size);
	        recur(x+size+size, y, size);
	        recur(x+size+size, y+size, size);
	        recur(x+size+size, y+size+size, size);
		}
	}
	
	static boolean check(int x, int y, int size) {
		int point = data[x][y];
		
		for(int i=x; i<x+size; i++) {
			for(int j=y; j<y+size; j++) {
				if(point != data[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}
