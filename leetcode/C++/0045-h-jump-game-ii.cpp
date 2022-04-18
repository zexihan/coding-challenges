class Solution {
public:
    int jump(vector<int>& nums) {
        /*
        贪心思想
        同样每次记录你能够跳到的最远距离 k

        0  1  2  3  4  5  6 
        i
                 j
        假设从 0 起跳，最远能够跳到 3 位置，那么我们落脚到 1 2 3 位置，步数都是 1
        我们第 2 步可以从 1 2 3 之中任意一个点开始起跳，那么我们可以选择 1 2 3 中能跳得最远的点作为第二步的起跳点

        因为题目说了必定能够到达最后一个位置，这就是说
        0  1  2  3  4  5  6 
        i
                 j
        不会存在 0 能够跳到的最远距离是 3，而 1 2 3 中能够跳到的最远距离也是 3，即无论怎么跳到跳不出 3 这个位置，这种情况是不存在的
        即 1 2 3 中必定存在一个位置能够跳出 3 这个位置，这样才能到达终点
        换成数组来看的话，即是不存在 nums = [3, 2, 1, 0, 1, 2, 3]，这种情况怎么跳都跳不出 3 位置
        
        我们使用 end 记录 0 位置的最远距离， 即 3
        使用 k 记录 1 2 3 位置能够跳的最远距离
        当 i 遍历到 end 的时候，我们需要将步数 step + 1，即开始一次新的起跳，然后将 end 更新为 k
        */
        if (nums.size() == 1) 
            return 0;
        int reach = 0;
        int nextreach = nums[0];
        int step = 0;
        for (int i = 0; i < nums.size(); i++){
            nextreach = max(i + nums[i], nextreach);
            if (nextreach >= nums.size() - 1) 
                return step + 1;
            if (i == reach){
                step++;
                reach = nextreach;
            }
        }
        return step;
    }
};