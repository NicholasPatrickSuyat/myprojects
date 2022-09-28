import java.util.Arrays;
import java.util.Scanner;


public class DotaMain {
   

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("***************************************************");
        System.out.println("Dota Characters with Roles");
        System.out.println("Enter your Steam Username: ");
        input.nextLine();
        System.out.println("***************************************************");

        DotaRoles dotaroles = new DotaRoles("Slark", "Tinker", "Magnus", "Rubick", "cm");
            System.out.println(dotaroles.toString());
        DotaRoles dotaroles2 = new DotaRoles("PA", "ShadowFiend", "Tide", "EarthShaker", "Shaman");
            System.out.println(dotaroles2.toString());
        DotaRoles dotaroles3 = new DotaRoles("PL", "Storm Spirit", "Tiny", "Willow", "Lion");
            System.out.println(dotaroles3.toString());
        DotaRoles dotaroles4 = new DotaRoles("TerrorBlade", "Void Spirit", "OD", "Windranger", "Treant");
            System.out.println(dotaroles4.toString());
        DotaRoles dotaroles5 = new DotaRoles("Naga", "Sniper", "Mars", "Warlock", "IO");
            System.out.println(dotaroles5.toString());
            
            
        
        
    
       
                    

            }

            }
        

           
        

        
    
