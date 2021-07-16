#include<bits/stdc++.h>
using namespace std;

double findMean(int a[],int n){
    double ans = 0;
    for(int i=0;i<n;i++){
        ans+=a[i];
    }
    
    return ans/n;
}

double findMedian(int a[],int n){
    sort(a, a + n);
    if(n%2!=0){
        return (double) a[n/2];
    }
    return ((double) a[n/2] + (double) a[(n-1)/2]) / 2;
}


int main()
{
    int a[] = { 1, 3, 4, 2, 7, 5, 8, 6 };
    int n = sizeof(a) / sizeof(a[0]);
   
    // Function call
    cout << "Mean = " << findMean(a, n) << endl;
    cout << "Median = " << findMedian(a, n) << endl;
    return 0;
}