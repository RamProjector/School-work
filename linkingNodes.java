public class Main {
    
    static class Node {
        int data;
        Node next;
        
        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    
    public static void main(String[] args) {
        
        Node first = new Node(10);
        Node second = new Node(20);
        Node third = new Node(30);
        Node fourth = new Node(40);
        Node fifth = new Node(50);
        
        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;
        
        Node current = first;
        while (current != null) {
        System.out.println(current.data);
        current = current.next;
        
        }
    }
}
