// XOR
// 1. a xor 0 = a
// 2. a xor a = 0
// 3. a xor b xor a = b xor a xor a = b xor (a xor a) = b xor 0 = b
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int single_num = 0;
        for (int num : nums)
            single_num ^= num;
        return single_num;
    }
};