class StockSpanner {
private:
    vector<pair<int, int>> vec;
    
public:
    StockSpanner() {
    }
    
    int next(int price) {
        if (vec.empty() || price < vec.back().first) {
            vec.push_back({price, 1});
            return 1;
        }
        int span = vec.back().second + 1;
        while (span <= vec.size() && price >= vec[vec.size() - span].first)
            span += vec[vec.size() - span].second;
        vec.push_back({price, span});
        return span;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */