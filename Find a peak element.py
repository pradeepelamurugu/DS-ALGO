#include<iostream>
using namespace std;
int findPeak(int arr[],int size){
    if(size<=1){
        return 0;
    }
    if(arr[0]>=arr[1]){
        return 0;
    }
    if(arr[size-1]>=arr[size-2]){
        return size-1;
    }
    for(int i=1;i<size-1;i++){
        if(arr[i]>=arr[i-1] && arr[i]>=arr[i+1]){
            return i;
        }
    }
    
    
}



int main()
{
    int arr[] = { 1, 3, 20, 4, 1, 0 };
    int n = sizeof(arr)/sizeof(arr[0]);
    int ans = findPeak(arr, n);
    cout << ans << " ";
    return 0;
}