// Stack
// 将原字符串以 '/' 分隔, 然后遍历:
// - 遇到正常的目录名, 入栈
// - 遇到 '.' 或 空名称 (对应 "//") 则忽略
// - 遇到 ".." 则从栈顶弹出一个元素 (如果栈为空则不弹栈, 对应 "/../")
// 最后将栈中的元素以 '/' 连接得到结果.
class Solution {
public:
    string simplifyPath(string const& path) {
        vector<string> dirs;

        for (auto i = path.begin(); i != path.end(); ++i) {
            auto j = find(i, path.end(), '/');
            auto dir = string(i, j);

            if (!dir.empty() && dir != ".") {// 当有连续 '///'时，dir 为空
                if (dir == "..") {
                    if (!dirs.empty())
                        dirs.pop_back();
                } else {
                    dirs.push_back(dir);
                }
            }
            i = j;
        }

        stringstream out;
        if (dirs.empty()) {
            out << "/";
        } else {
            for (auto dir : dirs)
                out << "/" << dir;
        }
        return out.str();
    }
};