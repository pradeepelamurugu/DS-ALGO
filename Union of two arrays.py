class Solution{
    public:
    //Function to return the count of number of elements in union of two arrays.
    int doUnion(int arr[], int n, int b[], int m)  {
        unordered_set<int> ans;
        //code here
        int i=0;
        int j=0;
       
        while(i<n && j<m){
            ans.insert(arr[i]);
            ans.insert(b[j]);
            i++;
            j++;
            
        }
        while(i<n){
            ans.insert(arr[i]);
            i++;
        }
        while(j<m){
            ans.insert(b[j]);
            j++;
        }
        return ans.size();
    }
};