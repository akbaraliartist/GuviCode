
package learning;

import java.util.Scanner;

public class Learning {

   
    public static void main(String[] args) {
     Scanner scan =new Scanner(System.in);
     int i=scan.nextInt();
     
     if(i>0){
         System.out.println("positive");
     }
     else if(i<0){
             System.out.println("negative");
               
     }
         else{
             System.out.println("zero");
         }
        
    }
    
}
