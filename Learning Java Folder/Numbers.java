package JavaFolder;

public class Numbers {
    public static void main(String[] args) {
    
// To use integers, use this method
    int num1 = 5;
    int num2 = 10;
    int num3 = 15;

    System.out.println(num1+num2*num3);

// To use decimals, use this method
    double dec1 = 1.2123123;
    double dec2 = 2.61235235;
    double dec3 = 3.14234235234;

    System.out.println(dec1);

// To limit the decimals placement, use this method

    System.out.println(Math.round(dec1*100.0)/100.0);
    System.out.println(Math.round(dec2*1000.0)/1000.0);
    System.out.println(Math.round(dec3*10000.0)/10000.0);
    }
}
