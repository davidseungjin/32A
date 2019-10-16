#include<iostream>
#include<string>

using namespace std;

int main(){
	string name;
	int age;
	cout << "What is your name ?" << endl;
	cin >> name;
	cout << "How old are you ?" << endl;
	cin >> age;

	if(age==1){
		cout << "Your name is " << name << " and you are " << age << " year old." << endl;
	} else if (age > 1){
		cout << "Your name is " << name << " and you are " << age << " years old." << endl;
	} 

	return 0;
}
