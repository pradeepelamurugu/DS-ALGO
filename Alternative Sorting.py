class Solution{


  public:
  vector<int> alternateSort(int arr[], int N)
  {
      // Your code goes here
      sort(arr,arr+N);
      vector<int> ans;
      int i=0;
      int j=N-1;
      while(i<j){
          ans.push_back(arr[j--]);
          ans.push_back(arr[i++]);
      }
      if(N%2!=0){
          ans.push_back(arr[i]);
      }
      return ans;
  }

};
