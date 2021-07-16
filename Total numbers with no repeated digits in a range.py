#include<bits/stdc++.h>
using namespace std;
int check_repeated(int num){
    unordered_set<int> s;
    while(num != 0){
    int d = num%10;
    if(s.find(d)!=s.end()){
        return 0;
    }
    s.insert(d);
    num=num/10;}
    return 1;
}

int calculate(int l , int r){
    int ans=0;
    for(int i=l;i<=r;i++){
        ans+=check_repeated(i);
    }
    return ans;
}

int main() {
  int L = 1, R = 100;
  
    // Calling the calculate
    cout << calculate(L, R);
    return 0;
}