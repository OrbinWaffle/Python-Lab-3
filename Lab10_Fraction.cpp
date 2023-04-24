#include <iostream>
using namespace std;

//defining a Fraction class
class Fraction {           
    private:
        float num, den;
            
    public:
        Fraction(int n=0, int d = 1) {num = n; den = d;}  //constructor
        Fraction operator+(const Fraction & f) const {                //overloading + operator
 	return Fraction (num * f.den + den *f.num, den * f.den) ; }
        Fraction operator*(const Fraction & f) const { 	//overloading * operator
	return Fraction (num * f.num, den *f.den);}
        bool operator==(const Fraction & f) const {		//overloading == operator
               return  num*f.den == den*f.num; }
         void display() const {				//print out a fraction number
                   cout << num <<  "/" << den << endl; }		//in Python, use a __str__() method
}; //end of class Fraction

//main for testing
int main() {
     Fraction f1 = Fraction (3, 7);
     Fraction f2 = Fraction (2, 5);
     Fraction f3 = Fraction (1, 3);
     Fraction f4 = Fraction (2, 6);
     Fraction result = f1 + f2 * f3;
     result.display();	//in Python, this should be print(result)
     if (f1 == f3) cout << "f1 and f3 are the same" << endl; else cout <<"f1 and f3 not equal" << endl;
     if (f3 == f4) cout <<"f3 and f4 are the same" << endl; else cout << "f3 and f4 not equal" << endl;
     return 0;
}
//output
//59/105
//f1 and f3 not equal
//f3 and f4 are the same
