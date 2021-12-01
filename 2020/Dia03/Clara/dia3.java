import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class dia3 {
  public static void getTrees(int deltax) {
    try {
      File myObj = new File("Dia03/Clara/input.txt");
      Scanner myReader = new Scanner(myObj);

      int x=0;
      int count=0;
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        System.out.println(data.substring(x,x+1));
        String treeOrNot = data.substring(x,x+1);
        if (treeOrNot.equals("#")){
          System.out.println("Tree!");
          count++;
        }
        x+=deltax;
        if (x>30){
          x=x-31;
        }
      }

      System.out.println("Count is "+count);
      myReader.close();

    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
  public static void main(String[] args) {
    getTrees(3);
  }
}