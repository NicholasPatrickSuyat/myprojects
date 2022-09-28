package Project2Files;
public class MainPerson {
    public static void main(String[] args) {
// Import the classes to the main and write the constructor
Person p=new Person("Nick","Philippines"," +183145","Nicky@gmail.com");

Person s=new Student("Pat","Philippines"," +198283","Patty@yahoo.com",3);

Person e=new Employee("Brian","Philippines","+192901","Brian@gmail.com "," Wellsfargo",60000);

Person f=new Faculty("Kim","Philippines"," +990123"," Kim@gmail.com     "," Pikespeak ",39000," 7am-7pm"," Manager");

Person st=new Staff("Mark","Philippines"," +120123","Mark@yahoo.com     ","  BMW      ",22000,"Programmer");

// Start Printing the output
System.out.println("----------------------------------------------------------------");
    System.out.println(p.toString());
    System.out.println(s.toString());
    System.out.println(e.toString());
    System.out.println(f.toString());
    System.out.println(st.toString());

System.out.println("----------------------------------------------------------------");
}

}


