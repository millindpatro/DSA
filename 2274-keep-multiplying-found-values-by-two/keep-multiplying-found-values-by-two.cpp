class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        int ans=original;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==ans){
                ans=nums[i]*2;
                i=-1;
            }
        }
            return ans;
        
    }
};