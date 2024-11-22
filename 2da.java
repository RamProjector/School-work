import java.util.Scanner;

  public class 2da {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
    
        System.out.println("The number of rows is:");
        int row = scanner.nextInt();
        System.out.println("The number of Coluymns is:");
        int col = scanner.nextInt();
        
        int[][] array = new int [row][col];
        
        int value = 1;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                array[i][j] = value;
                value++;
            }
        }
        
        System.out.println("The 2d array is:");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(array[i][j] + " ");
            }
         System.out.println();
        }
        
     }
}