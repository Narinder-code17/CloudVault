class DivisionByZero extends Exception {
    public DivisionByZero(String message) {
        super(message);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            int a = 10, b = 0;
            if (b == 0) {
                throw new DivisionByZero("Cannot divide by zero");
            }
            System.out.println(a / b);
        } catch (DivisionByZero e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Execution completed.");
        }
    }
}