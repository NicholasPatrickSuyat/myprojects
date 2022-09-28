package Project2Files;
class Faculty extends Employee {
    // Office Hour, Rank
    String OfficeHour;
    String Rank;
    //This is the constructor
    Faculty(String Name, String address, String Phonenumber, String Email, String Office, double Salary, String OfficeHour, String Rank){
        super(Name, address, Phonenumber, Email, Office, Salary);
        this.OfficeHour = OfficeHour;
        this.Rank = Rank;
    }
        public String toString(){
            return super.toString() + "\nOffice hours: " + OfficeHour +
"\nRank: " + Rank;
    }
    }
    

