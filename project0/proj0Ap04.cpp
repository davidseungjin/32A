#include<iostream>
#include<array>

using namespace std;

int main(){
	int num[] = {1, 3, 4, 5, 6, 7, 8};

	int capacity = sizeof(num)/sizeof(num[0]);
	int sum = 0;
	int i;
	for(i=0; i < capacity; i++){
		sum += num[i];
	}

	cout << "sum is " << sum << endl;
//	cout << "size of each index is " << sizeof(num[0]);

	return 0;
}
