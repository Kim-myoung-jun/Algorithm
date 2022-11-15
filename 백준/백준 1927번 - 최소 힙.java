// https://www.acmicpc.net/problem/1927

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	
	static List<Integer> heap;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		heap = new ArrayList<Integer>();
		heap.add(0);
		
		for(int i=0; i<n; i++) {
			int a = Integer.parseInt(br.readLine());
			if(a == 0) {
				if(heap.size() == 1) {
					System.out.println("0");
				} else {
					peak();
				}
			} else {
				add(a);
			}
			
			//System.out.println(heap);
		}
	}
	
	private static void peak() {
		int del_item = heap.get(1);
		System.out.println(del_item);
		
		heap.set(1, heap.get(heap.size()-1));
		heap.set(heap.size()-1, del_item);
		heap.remove(heap.size()-1);
		
		int position = 1;
		while( (position*2) < heap.size() ) {
			int min = heap.get(position*2);
			int min_pos = position*2;
			
			if( position*2+1 < heap.size() ) {
				int right = heap.get(position*2+1);
				if( min > right ) {
					min = right;
					min_pos += 1;
				}
			}
			
			if(min > heap.get(position) ) {
				break;
			}
			
			int tmp = heap.get(position);
			heap.set(position, heap.get(min_pos));
			heap.set(min_pos, tmp);
			position = min_pos;
		}
	}

	public static void add(int num) {
		heap.add(num);
		swap(num);
	}

	private static void swap(int num) {
		int now_index = heap.size()-1;
		while(now_index > 1 && heap.get(now_index/2) > num) {
			heap.set(now_index, heap.get(now_index/2));
			heap.set(now_index/2, num);
			now_index /= 2;
		}
	}
}
