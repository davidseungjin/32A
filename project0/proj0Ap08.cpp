#include<iostream>
#include<array>
#include<string>

using namespace std;

void ispalindrome(string& str){
	int forwards = 0;
	int backwards = str.length() - 1;

	while(backwards > 1){
		if(str[forwards++] != str[backwards--]){
			cout << str << " is Not Palindrome" << endl;
			return;
		}
	}
	cout << str << " is Palindrome" << endl;
}


int main(){

	string text;
	cout << "input text   " << endl;
	getline(cin, text);
	cout << "you input " << text << endl;
	cout << endl;

	ispalindrome(text);

	return 0;
}
