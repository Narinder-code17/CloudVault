class Stack {
    private int[] arr;
    private int top;
    private final int MAX = 10;

    public Stack() {
        arr = new int[MAX];
        top = -1;  // stack is empty initially
    }

    // Push an element onto the stack
    public void push(int value) {
        if (top == MAX - 1) {
            System.out.println("Stack Overflow! Cannot push " + value);
            return;
        }
        arr[++top] = value;
        System.out.println(value + " pushed to stack.");
    }

    // Pop an element from the stack
    public int pop() {
        if (top == -1) {
            System.out.println("Stack Underflow! Cannot pop.");
            return -1; // or throw exception
        }
        int poppedValue = arr[top--];
        System.out.println(poppedValue + " popped from stack.");
        return poppedValue;
    }

    // Peek the top element without removing
    public int peek() {
        if (top == -1) {
            System.out.println("Stack is empty!");
            return -1; // or throw exception
        }
        return arr[top];
    }

    // Check if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }
}

public class StackDemo {
    public static void main(String[] args) {
        Stack stack = new Stack();

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Top element is: " + stack.peek());

        stack.pop();
        stack.pop();

        System.out.println("Top element after popping: " + stack.peek());

        stack.pop();

        System.out.println("Is stack empty? " + stack.isEmpty());

        stack.pop();  // Try popping from empty stack
    }
}