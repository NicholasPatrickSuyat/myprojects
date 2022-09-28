package Project2Files;
class Student extends Person{
        // Class status
        final int freshmen = 1;
        final int sophmore = 2;
        final int junior = 3;
        final int senior = 4;
        String status="freshman";
        // This is the constructor
        Student(String Name, String address, String Phonenumber, String Email, int Status){
            super(Name, address, Phonenumber, Email);
            if(Status == 1){
                status = "freshmen" ;
            }
            if(Status == 2){
                status = "sophmore" ;
            }
            if(Status == 3){
                status = "junior" ;
            }
            if(Status == 4){
                status = "Senior" ;
            }
                status = "Student";
        }
            public String toString(){
                return super.toString() + "\nStatus: " + status;
            }
        }
       
