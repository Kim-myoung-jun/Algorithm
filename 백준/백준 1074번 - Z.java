import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();
		String [] s_arr = s.split(" ");
		int n = Integer.parseInt(s_arr[0]);
		int r = Integer.parseInt(s_arr[1]);
		int c = Integer.parseInt(s_arr[2]);
		int idx = 0;

		while(n != 0) {
			n--;
			double range = Math.pow(2, n);
			if(r < range && c < range) {
				idx += range * range * 0;
			} else if (r < range && c >= range) {
				idx += range * range * 1;
				c -= range;
			} else if (r >= range && c < range) {
				idx += range * range * 2;
				r -= range;
			} else {
				idx += range * range * 3;
				r -= range;
				c -= range;
			}
		}
		System.out.print(idx);
	}
}
