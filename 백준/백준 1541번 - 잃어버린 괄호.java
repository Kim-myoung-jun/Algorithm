import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();
		String [] arr = s.split("-");
		int total = 0;
		for(int i=0; i<arr.length; i++) {
			int sum = 0;
			if(arr[i].indexOf("+") > -1) {
				String [] arr_sum = arr[i].split("\\+");
				for(int j=0; j<arr_sum.length; j++) {
					sum += Integer.parseInt(arr_sum[j]);
				}
			} else {
				sum = Integer.parseInt(arr[i]);
			}

			if(i == 0) {
				total = sum;
			} else {
				total -= sum;
			}
		}
		System.out.println(total);
	}
}
