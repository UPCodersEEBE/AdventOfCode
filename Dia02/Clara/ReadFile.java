import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

import java.util.regex.Pattern; //regex package
import java.util.regex.Matcher; //idk difference yet
import org.apache.commons.lang3.StringUtils;

public class ReadFile {
  public static void main(String[] args) {
    try {
      File myObj = new File("input1.txt");
      Scanner myReader = new Scanner(myObj);
      int numOfPasswords=0;
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        //System.out.println(Pattern.matches("[0-9]{1,2}", data));

        Pattern p = Pattern.compile("[0-9]{1,2}");
        Matcher m = p.matcher(data);


        int min = 0;
        int max = 0;
        String letter="";
        String password="";

        if (m != null){
            m.find();//true
            min=Integer.parseInt(m.group());

        }

        Pattern pp = Pattern.compile("(?<=-)[0-9]{1,2}");
        Matcher mm = pp.matcher(data);

        if (mm != null){
            mm.find();//true
            max=Integer.parseInt(mm.group());

        }

        Pattern letterPattern = Pattern.compile("[a-z]");
        Matcher letterMatcher = letterPattern.matcher(data);


        if (letterMatcher != null){
            letterMatcher.find();//true
            letter = letterMatcher.group();

        }

        Pattern passwordPattern = Pattern.compile("(?<=: )[a-z]*");
        Matcher passwordMatcher = passwordPattern.matcher(data);


        if (passwordMatcher != null){
            passwordMatcher.find();//true
            password = passwordMatcher.group();
        }

        int count = StringUtils.countMatches(password,letter);

        if (count<=max && count>=min){
            System.out.println(password);

            numOfPasswords++;
        }

      }
      myReader.close();
      System.out.println(numOfPasswords);
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}