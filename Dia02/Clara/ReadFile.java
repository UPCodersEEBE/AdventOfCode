import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

import java.util.regex.Pattern; //regex package
import java.util.regex.Matcher; //idk difference yet

public class ReadFile {
  public static void main(String[] args) {
    try {
      File myObj = new File("input1.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        System.out.println(data);
        //System.out.println(Pattern.matches("[0-9]{1,2}", data));

        Pattern p = Pattern.compile("[0-9]{1,2}");
        Matcher m = p.matcher(data);

        if (m != null){
            m.find();//true
            System.out.println(m.group());

        }

        Pattern pp = Pattern.compile("(?<=-)[0-9]{1,2}");
        Matcher mm = pp.matcher(data);

        if (mm != null){
            mm.find();//true
            System.out.println(mm.group());

        }

        Pattern letterPattern = Pattern.compile("[a-z]");
        Matcher letterMatcher = letterPattern.matcher(data);

        if (letterMatcher != null){
            letterMatcher.find();//true
            System.out.println(letterMatcher.group());

        }

        Pattern passwordPattern = Pattern.compile("(?<=: )[a-z]*");
        Matcher passwordMatcher = passwordPattern.matcher(data);

        if (passwordMatcher != null){
            passwordMatcher.find();//true
            System.out.println(passwordMatcher.group());

        }

      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}