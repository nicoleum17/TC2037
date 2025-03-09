#include <iostream>

using namespace std;
			   // dig, +/-,  . , del, otro
int MT[5][5] = {{   1,   2,   3, 200, 200},
				{   1, 200,   3, 101, 200},
				{   1, 200,   3, 200, 200},
				{   4, 200, 200, 200, 200},
				{   4, 200, 200, 100, 200}};

int convert(char c) {
	switch(c) {
		case '0' :
		case '1' :
		case '2' :
		case '3' :
		case '4' :
		case '5' :
		case '6' :
		case '7' :
		case '8' :
		case '9' : return 0;
		case '+' :
		case '-' : return 1;
		case '.' : return 2;
		case ' ' :
		case '\0': return 3;
		default  : return 4;
	}
}

int main(int argc, char* argv[]) {
	char c, input[80];
	int i, state;

	cout << "Expression to evaluate: ";
	cin >> input;

	i = 0;
	state = 0;
	while (state < 100) {
		c = input[i++];
		state = MT[state][convert(c)];
		if (state == 100) {
			cout << "Accepted\n";
		} else if (state == 200) {
			cout << "ERROR\n";
		}
	}

	if(state == 101){
		cout << "Entero\n";
	} else if(state == 100){ 
		cout << "Flotante\n";}

	cout << "End Of Analysis\n";
	return 0;
}