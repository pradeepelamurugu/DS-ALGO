class Solution{
    public:
    //Function to return the count of the number of elements in
    //the intersection of two arrays.
    int NumberofElementsInIntersection (int a[], int b[], int n, int m )
    {
        // Your code goes here
        unordered_set<int> ans;
        unordered_set<int> ans1;
        int count = 0;
        for(int i=0;i<n;i++){
            ans.insert(a[i]);
        }
        for(int i=0;i<m;i++){
            if(ans.find(b[i])!=ans.end()){
                ans1.insert(b[i]);
            }
        }
        return ans1.size();
    }
};