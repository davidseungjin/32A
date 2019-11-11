#include<iostream>
#include<array>
#include<string>

using namespace std;



bool lowercheck(string& plate){
	int length = plate.length();
	for (int i = 0 ; i < length; i++){
		char c = plate[i];
		if(islower(c)){
//				cout << "lowercheck if-statement true" << endl;
				return true;
		}
	}
//	cout << "lowercheck if-statement false" << endl;
	return false;
}

bool blankcheck(string& plate){
	int length = plate.length();
	for (int i = 0 ; i < length; i++){
		char c = plate[i];
		if(isblank(c)){
//				cout << "blankcheck if-statement true" << endl;
				return true;
		}
	}
//	cout << "blankcheck if-statement false" << endl;
	return false;
}


bool firstlast(string& plate){
	int length = plate.length();
	if(isupper(plate[0])){	
		if(isupper(plate[length-1])){
//		cout << "first, last if-statement true" << endl;
			return true;
		}
	}
//	cout << "first, last if-statement false" << endl;
	return false;
}


bool mustbeonenum(string& plate){
	int length = plate.length();
	for (int i = 0 ; i < length; i++){
		char c = plate[i];
		if(isdigit(c)){
//			cout << "mustbeonenum if-statement true" << endl;
			return true;
		}
	}
//	cout << "mustbeonenum if-statement false" << endl;
	return false;
}

int main(){
	

	bool loop = true;
	string plate;
	while(loop){
		cout << "input the value!!! " << endl;
		cin >> plate;

		if((!lowercheck(plate))&&(!blankcheck(plate))&&(firstlast(plate))&&(mustbeonenum(plate))){
			loop = false;
		}
	}

	return 0;
}
