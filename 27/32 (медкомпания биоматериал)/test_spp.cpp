#include <iostream>
#include<fstream>
#include<vector>
#include<ctime>

using namespace std;

int main() {
  cout << "123";
  int n;
  ifstream f("27A.txt");
  f >> n;
  vector<int> a(n);
  for (int i=0;i<n;i++) f>>a[i];
  long long count = 0;
  for (int i=0; i<n;i++){
  	for (int j=i+1;j<n;j++){
  		if (a[i]+a[j]))%131 ==0) count++;
	  }
  }
  return 0;
  
}
