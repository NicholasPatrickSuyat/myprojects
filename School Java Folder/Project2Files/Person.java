package Project2Files;
class Person {
// name, address, phone number, and e-mail address
String Name;
String address;
String Phonenumber;
String Email;

Person(String Name, String address, String Phonenumber, String Email){

this.Name = Name;
this.address = address;
this.Phonenumber = Phonenumber;
this.Email = Email;
}
public String toString()
{
    return "\nName: " + Name + "\nAddress: " + address +
    "\nPhone number: " + Phonenumber + "\nEmail address: " + Email;
}
}



