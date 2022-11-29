import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static Queue<Integer> q = new LinkedList<>();
	static int [] visited = new int[100001];
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int [][] data = new int[n][2];
		for(int i=0; i<n; i++) {
			String s = br.readLine();
			String [] arr = s.split(" ");
			data[i][0] = Integer.parseInt(arr[0]);
			data[i][1] = Integer.parseInt(arr[1]);
		}
		Arrays.sort(data, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				// TODO Auto-generated method stub
				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				return o1[1]-o2[1];
			}
		});

		int cnt = 1;
		int end = data[0][1];
		for(int i=1; i<n; i++) {
			if(end <= data[i][0]) {
				cnt++;
				end = data[i][1];
			}
		}
		System.out.println(cnt);
	}
}
