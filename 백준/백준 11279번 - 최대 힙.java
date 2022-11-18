// https://www.acmicpc.net/problem/11279

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	static List<Integer> heap;
	public static void main(String[] args) throws NumberFormatException, IOException   {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		heap = new ArrayList<Integer>();
		heap.add(0);
		for(int i=0; i<n; i++) {
			int a = Integer.parseInt(br.readLine());

			if(a == 0) {
				if(heap.size() > 1) {
					pop();
				} else {
					System.out.println("0");
				}
			} else {
				push(a);
			}
		}
	}
	private static void push(int num) {
		// TODO Auto-generated method stub
		heap.add(num);
		int now_index = heap.size() - 1;
		while(now_index > 1 && heap.get(now_index/2) < num) {
			int tmp = heap.get(now_index/2);
			heap.set(now_index/2, num);
			heap.set(now_index, tmp);
			now_index /= 2;
		}
	}
	private static void pop() {
		// TODO Auto-generated method stub
		int del_item = heap.get(1);
		System.out.println(del_item);
		heap.set(1, heap.get(heap.size()-1));
		heap.remove(heap.size()-1);

		int position = 1;
		while(position * 2 < heap.size()) {
			int max_val = heap.get(position*2);
			int max_pos = position*2;

			if(position*2+1 < heap.size()) {
				if(max_val < heap.get(position*2+1)) {
					max_val = heap.get(position*2+1);
					max_pos = position*2+1;
				}
			}

			if(max_val < heap.get(position)) {
				break;
			}

			int tmp = heap.get(position);
			heap.set(position, max_val);
			heap.set(max_pos, tmp);
			position = max_pos;
		}
	}

}
