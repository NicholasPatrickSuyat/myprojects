package Project2Files;
class Employee extends Person {
// Office, Salary, and date hired
String Office;
double Salary;
MyDate dateHired;
public Employee(String Name, String address, String Phonenumber,
    String Email, String Office, double Salary) {
    super(Name, address, Phonenumber, Email);
    this.Office = Office;
    this.Salary = Salary;
    this.dateHired = new MyDate();
}


//return hire date
public String getDateHired() {
return dateHired.getMonth() + "/" + dateHired.getDay()
+ "/" + dateHired.getYear();
}


//to string method for the class
public String toString() {
return super.toString() + "\nOffice: " + Office +
"\nSalary: $" + Salary + "\nDate hired: " + getDateHired();
}
}


            
            
    

