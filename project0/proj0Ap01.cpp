#include<iostream>
#include<cmath>

using namespace std;

int main(){
	int width;
	int height;
	cout << "what is width of the right triangle? " << endl;
	cin >> width;
	cout << "what is height of the right triangle? " << endl;
	cin >> height;

	int slope;
	slope = sqrt(width^2 + height^2);
	
	int perimeter = slope + width + height;

	cout << "perimeter is " << perimeter << endl;


	return 0;
}
