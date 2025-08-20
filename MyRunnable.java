 class MyRunnable implements Runnable
 {
    public void run() 
    {
        try {
            System.out.println("Thread running...");
            Thread.sleep(500);
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
 }
 public class ThreadDemo 
{
    public static void main(String[] args) 
{
 Runnable task = new MyRunnable();
 Thread thread = new Thread(task);
 thread.start();
 }
}