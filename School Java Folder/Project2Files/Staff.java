package Project2Files;

public class Staff extends Employee {
//has a title
String title;
//This is the constructor
    public Staff(String Name, String address, String Phonenumber, String Email, String Office, double Salary,String title) {
    super(Name,address,Phonenumber,Email,Office,Salary);
    this.title=title;
}
    public String toString() {
        return super.toString() + "\nTitle: " + title;
}
}

