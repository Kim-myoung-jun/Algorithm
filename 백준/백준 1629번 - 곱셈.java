import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static long a;
	static long b;
	static long c;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Long.parseLong(st.nextToken());
		b = Long.parseLong(st.nextToken());
		c = Long.parseLong(st.nextToken());
		
		System.out.println(pow(b));
	}
	private static long pow(long b2) {
		if(b2 == 1) {
			return a%c;
		}
		else {
			long x = pow(b2/2);
			if( b2 % 2 == 0) {
				return x * x % c;
			} else {
				return (x * x % c) * a % c;
			}
		}
	}
}
