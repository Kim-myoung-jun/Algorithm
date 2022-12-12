import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static char [][] data = null;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		data = new char[n][n];
		for(int i=0; i<n; i++) {
			data[i] = br.readLine().toCharArray();
		}

		devide(0,0,n);
		System.out.println(sb);
	}
	private static void devide(int a, int b, int size) {

		if( check(a, b, size) == true) {
			if(data[a][b] == '0') {
				sb.append("0");
			} else {
				sb.append("1");
			}
			return;
		} else {
			size /= 2;
			sb.append("(");
			devide(a, b, size);
			devide(a, b+size, size);
			devide(a+size, b, size);
			devide(a+size, b+size, size);
			sb.append(")");
		}
	}
	private static boolean check(int a, int b, int size) {
		char point = data[a][b];
		for(int i=a; i<a+size; i++) {
			for(int j=b; j<b+size; j++) {
				if(point != data[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}
