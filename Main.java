 interface Resizable 
{
    void resizeWidth(int width);
    void resizeHeight(int height);
 }
 class Rectangle implements Resizable 
{
    int width, height;
    public void resizeWidth(int width) 
    {
        this.width = width;
    }
    public void resizeHeight(int height) 
    {
        this.height = height;
    }
    void display() 
    {
        System.out.println("Width: " + width + ", Height: " + height);
    }
 }
 public class Main {
    public static void main(String[] args) 
    {
        Rectangle rect = new Rectangle();
        rect.resizeWidth(10);
        rect.resizeHeight(20);
        rect.display();
    }
 }
 
