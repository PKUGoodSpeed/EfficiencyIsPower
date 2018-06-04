#include<bits/stdc++.h>
using namespace std;

class SevenDeadlySins {
private:
	bool malin;
	string goodspeed;

public:
	float escarnor;
	int meriodas;

	SevenDeadlySins();

	int fullCounter(int x, float y, string z); // Meriodas's skill

	string amatiros(int x, float y, string z); // Goodspeed's skill

	bool perfectCub(int x, float y, string z); // Malin's skill

	double crualSun(int x, float y, string z); // Escarnor's skill

};


SevenDeadlySins::SevenDeadlySins(): meriodas(0), escarnor(12), malin(true), goodspeed("god") {}

int SevenDeadlySins::fullCounter(int x, float y, string z){
// Meriodas's skill
	return x;
}


string SevenDeadlySins::amatiros(int x, float y, string z){
// Goodspeed's skill
	return z;
}


double SevenDeadlySins::crualSun(int x, float y, string z){
// Escarnor's skill
	return double(y);
}


int main(){
	SevenDeadlySins A = SevenDeadlySins();
	int x = 10086;
	float y = 3.14;
	string z = "god help me plz";
	cout<<A.fullCounter(x, y, z)<<endl;
	cout<<A.crualSun(x, y, z)<<endl;
	cout<<A.amatiros(x, y, z)<<endl;
}