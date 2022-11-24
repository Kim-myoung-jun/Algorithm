import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		String s = br.readLine();
		String [] s_arr = s.split(" ");
		int [] data = new int[n];
		int [] sort_data = new int[n];

		for(int i=0; i<n; i++) {
			data[i] = sort_data[i] = Integer.parseInt(s_arr[i]);
		}

		//quickSort(sort_data, 0, n-1);
		Arrays.sort(sort_data);

		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		int idx = 0;
		for(int i=0; i<n; i++) {
			if(!map.containsKey(sort_data[i])) {
				map.put(sort_data[i], idx++);
			}
		}

		StringBuilder sb = new StringBuilder();
		for(int i=0; i<n;i++) {
			sb.append(map.get(data[i])).append(" ");
		}
		System.out.print(sb);
	}
	private static void quickSort(int[] sort_data, int start, int end) {
		// TODO Auto-generated method stub

		if(start >= end) {
			return;
		}

		int pivot = start;
		int left = start+1;
		int right = end;

		while (left <= right) {
			while (left <= end && sort_data[left] <= sort_data[pivot]) {
				left += 1;
			}
			while(right > start && sort_data[right] >= sort_data[pivot]) {
				right -= 1;
			}

			if(left > right) {
				int tmp = sort_data[pivot];
				sort_data[pivot] = sort_data[right];
				sort_data[right] = tmp;
			} else {
				int tmp = sort_data[pivot];
				sort_data[pivot] = sort_data[left];
				sort_data[left] = tmp;
			}
		}
		quickSort(sort_data, start, right-1);
		quickSort(sort_data, right+1, end);
	}
}
