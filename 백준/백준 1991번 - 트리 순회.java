import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static class Node {
		char data;
		Node leftNode;
		Node rightNode;
		
		public Node(char data) {
			this.data = data;
			this.leftNode = null;
			this.rightNode = null;
		}
		
		public void setLeftNode(Node node) {
			this.leftNode = node;
		}
		
		public void setRightNode(Node node) {
			this.rightNode = node;
		}
	}
	
	//전위 순회
	public static void preOrder(Node node) {
		if(node == null) {
			return;
		}
		System.out.print(node.data);
		preOrder(node.leftNode);
		preOrder(node.rightNode);
	}
	
	//중위 순회
	public static void inOrder(Node node) {
		if(node == null) {
			return;
		}
		inOrder(node.leftNode);
		System.out.print(node.data);
		inOrder(node.rightNode);
	}
	
	//후위 순회
	public static void postOrder(Node node) {
		if(node == null) {
			return;
		}
		postOrder(node.leftNode);
		postOrder(node.rightNode);
		System.out.print(node.data);
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		
		Node head = new Node('A');
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			char data = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);
			
			makeTree(head, data, left, right);
		}
		
		preOrder(head);
		System.out.println();
		
		inOrder(head);
		System.out.println();
		
		postOrder(head);
	}
	private static void makeTree(Main.Node head, char data, char left, char right) {
		if(head.data == data) {
			if(left == '.') {
				head.leftNode = null;
			} else {
				Node leftNode = new Node(left);
				head.leftNode = leftNode;
			}
			
			if(right == '.') {
				head.rightNode = null;
			} else {
				Node rightNode = new Node(right);
				head.rightNode = rightNode;
			}
		} else {
			if(head.leftNode != null) {
				makeTree(head.leftNode, data, left, right);
			}
			if(head.rightNode != null) {
				makeTree(head.rightNode, data, left, right);
			}
		}
	}
}
