#include<iostream>
#include<array>
#include<string>

using namespace std;

int numoftimes(char& c, string& text){
	int length = text.length();
	int count = 0;
	for (int i = 0; i < length; i++){
			if(c == text[i]){
				count += 1;
			}
	}
	return count;
}


int main(){

	string text;
	cout << "input text   " << endl;
	getline(cin, text);
	cout << "you input " << text << endl;
	cout << endl;

	char c;
	cout << "input character you want to count?" << endl;
	cin >> c;

	cout << "How many times the character you want to see is used? " << 
	numoftimes(c, text) << endl;

	return 0;
}
