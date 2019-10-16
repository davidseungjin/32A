#include<iostream>
#include<string>

using namespace std;

int main(){
	string text1;
	string text2;
	cout << "what is the first text ?" << endl;
	cin >> text1;
	cout << "what is the second text ?" << endl;
	cin >> text2;

	string textsum;
	textsum = text1 + text2;
	
	cout << "concatenated text is  " << textsum << endl;


	return 0;
}
