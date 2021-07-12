#include<iostream>
using namespace std;
void modify(int arr[],int size){
    if(size<1){
        return;
    }
    int prev = arr[0];
    arr[0] = arr[0]*arr[1];
    
    for(int i=1;i<size-1;i++){
        int curr = arr[i];
        arr[i]=prev*arr[i+1];
        prev = curr;
    }
    arr[size-1]=arr[size-1]*prev;
}


int main()
{
    int arr[] = {2, 3, 4, 5, 6};
    int n = sizeof(arr)/sizeof(arr[0]);
    modify(arr, n);
    for (int i=0; i<n; i++)
      cout << arr[i] << " ";
    return 0;
}