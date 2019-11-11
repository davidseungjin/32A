#include<iostream>
#include<array>
#include<string>

using namespace std;

int main(){
	string text[] = {"a", "b", "abc", "abcdefghijklmnopqrstuvwxyz", "xyz", "z"};

	int lengthoftext = 0;
	int maxindex = 0;
	int i;
	cout << text[0].size() << endl;
	cout << text[2].length() << endl;

	for (i = 0; i < (sizeof(text)/sizeof(text[0])); i++){
		if(text[i].size() > lengthoftext){
			lengthoftext = text[i].size();
			maxindex = i;
		}
	}
	
	cout << "the longest text in the array is " << text[maxindex]
	<< " and it is index at " << maxindex << endl;

	return 0;
}
