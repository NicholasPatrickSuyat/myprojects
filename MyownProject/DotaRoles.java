public class DotaRoles {
    public static String Carry;
    public static String Mid;
    public static String Offlane;
    public static String SoftSupp;
    public static String HardSupp; 

    DotaRoles(String Carry, String Mid, String Offlane, String SoftSupp, String HardSupp){
        DotaRoles.Carry = Carry;
        DotaRoles.Mid= Mid;
        DotaRoles.Offlane = Offlane;
        DotaRoles.SoftSupp = SoftSupp;
        DotaRoles.HardSupp = HardSupp;

    }
    public String toString(){
        return (super.toString() +"\nCarry:"+ Carry + "\n"+ "\nMid:" + Mid + "\n"+ "\nOfflane:" + Offlane + "\n"+ "\nSoftSupp:" + SoftSupp + "\n"+ "\nHard Supp:" + HardSupp + "\n"+ "\n");
    }
    
}

    