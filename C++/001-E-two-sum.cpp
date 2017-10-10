#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	unordered_map<int, int> m;
    	for (int i = 0; i <= nums.size() - 1; i++){
    		int num = nums[i];
		    if (m.find(target-num) != m.end()){
		    	return {m[target-num], i};
		    }
    		m[num] = i;
    	}
    }

};

int main(){
    Solution run;
	vector<int> nums;
    vector<int> res(2);
    int target = 9;
    nums = {2,7,11,15};
    res = run.twoSum(nums, target);
    cout << res[0] << " " << res[1] <<endl;
    return 0;
}