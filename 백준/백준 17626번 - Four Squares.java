# https://www.acmicpc.net/problem/17626

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int [] dp = new int[50001];
		
		dp[0] = 0;
		dp[1] = 1;
		
		for(int i=1; i<=n; i++)
		{
			dp[i] = dp[i-1]+1;
			int j = 1;
			while(j*j <= i)
			{
				int tmp = dp[i - (j*j)] + 1;
				dp[i] = Math.min(dp[i], tmp);
				j++;
			}
		}
		System.out.println(dp[n]);
	}

}
