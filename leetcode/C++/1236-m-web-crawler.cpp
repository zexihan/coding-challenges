/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */

class Solution {
private:
    void dfs(string startUrl, HtmlParser& htmlParser, string& host, unordered_set<string>& res) {
        if (startUrl.substr(0, host.size()) != host || res.find(startUrl) != res.end())
            return;
        res.insert(startUrl);
        vector<string> urls = htmlParser.getUrls(startUrl);
        for (string url : urls) {
            dfs(url, htmlParser, host, res);
        }
    }
        
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        string host = startUrl.substr(0, startUrl.find('/', 7));
        unordered_set<string> res;
        dfs(startUrl, htmlParser, host, res);
        return vector<string>(res.begin(), res.end());
    }
};