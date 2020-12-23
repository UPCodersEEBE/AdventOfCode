import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.math.BigInteger;
import java.util.Scanner; // Import the Scanner class to read text files

public class dia3_2 {
  public static int getTrees(int deltax, int deltay) {
    int count=0;
    try {
      File myObj = new File("Dia03/Clara/input.txt");
      Scanner myReader = new Scanner(myObj);

      int x=0;
      int linecount=0;
      count=0;
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        if (CheckLine(linecount,deltay)){
            System.out.println(data.substring(x,x+1));
            String treeOrNot = data.substring(x,x+1);
            if (treeOrNot.equals("#")){
                System.out.println("Tree!");
                count++;
                }
            x=x+deltax;
        }
        if (x>30){
          x=x-31;
        }

        linecount++;
      }

      System.out.println("Count is "+count);
      myReader.close();

    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return count;
  }

  public static Boolean CheckLine(int linenum,int deltay){
    if(Math.floorMod(linenum, deltay)==0){
        System.out.println("True in check");
        return true;
    }
    else{
        return false;
    }
  }

  public static void main(String[] args) {
    getTrees(1,1);
    getTrees(3,1);
    getTrees(5,1);
    getTrees(7,1);
    getTrees(1,2);

    int[] paths = {getTrees(1,1), getTrees(3,1), getTrees(5,1), getTrees(7,1), getTrees(1,2)};
    BigInteger mult=new BigInteger("1");
    for (int i:paths){
        mult=mult.multiply(BigInteger.valueOf(i));
        System.out.println(i+" X"+ mult+ "=");
        System.out.println(mult);
    }
    
  }
}