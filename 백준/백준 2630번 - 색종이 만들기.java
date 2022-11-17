// https://www.acmicpc.net/problem/2630

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static int white = 0;
	public static int blue = 0;
	public static int[][] data;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		data = new int[n][n];
		for(int i=0; i<n;i++) {
			String list = br.readLine();
			String [] arr = list.split(" ");
			for(int j=0; j<n; j++) {
				data[i][j] = Integer.parseInt(arr[j]);
			}
		}
		
		devide(0, 0, n);
		System.out.println(white+"\n"+blue);
	}

	private static void devide(int row, int col, int size) {
		// TODO Auto-generated method stub
		if(checkColor(row, col, size)) {
			if(data[row][col] == 0) {
				white++;
			} else {
				blue++;
			}
			return;
		}
		
		size /= 2;
		devide(row, col, size);
		devide(row+size, col, size);
		devide(row, col+size, size);
		devide(row+size, col+size, size);
	}

	private static boolean checkColor(int row, int col, int size) {
		// TODO Auto-generated method stub
		
		int fix = data[row][col];
		for(int i=row; i<row+size;i++) {
			for(int j=col; j<col+size; j++) {
				if(fix != data[i][j]) {
					return false;
				}
			}
		}
		return true;
	}

}
