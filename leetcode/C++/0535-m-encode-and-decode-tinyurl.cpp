class Solution {
private:
    long count = 0;
    unordered_map<string, string> database;
    string chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
public:
    string getString() {
        long c = count;
        string s = "";
        while (c > 0) {
            s.push_back(chars[c % 62]);
            c /= 62;
        }
        while (s.length() < 6) {
            s = "0" + s;
        }
        return s;
        
    }
    
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        if (database.find(longUrl) != database.end())
            return "http://tinyurl.com/" + database[longUrl];
        
        string key = getString();
        database[key] = longUrl;
        database[longUrl] = key;
        count++;
        return "http://tinyurl.com/" + key;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string key = shortUrl.substr(19, 6);
        return database[key];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));