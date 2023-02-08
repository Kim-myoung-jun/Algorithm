import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		BigInteger ans = new BigInteger("1");

		for( int i=n; i>m; i--) {
			ans = ans.multiply(BigInteger.valueOf(i));
		}
		for(int i=n-m; i>1; i--) {
			ans = ans.divide(BigInteger.valueOf(i));
		}
		System.out.println(ans);
	}

}
