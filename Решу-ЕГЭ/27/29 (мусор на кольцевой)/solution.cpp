#include <iostream>
#include<fstream>
#include<vector>
#include<ctime>
#include<cmath>
#include <string>
using namespace std;
// 1_200_031
int main() {
  cout << "Working..." << endl;
  int n;
  
  ifstream f("107_27_B.txt");
  f >> n;
  vector<int> a(n);
  for (int i=0; i<n; i++) f >> a[i];
  for (int i=0; i<n; i++) a[i] = a[i] * 3;
  long long mx = LONG_LONG_MAX, p, s, number=0;
  for (int i = 0; i < n; i++){
  	p = 0;
  	for (int j = 0; j < n; j++){
  		s = min(abs(i-j), n - abs(i-j));
  		p += s * a[j];  	
	  }
	  if (p < mx){
	  	mx=p;
	  	number = i + 1;
	  }
	cout << i << endl;
  }
  cout << number << " " << mx;
  return 0;
  
}
