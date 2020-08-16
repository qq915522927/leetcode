// https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&&tqId=11155&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking 
#include <iostream>

// 关键点：
//  1. 原地操作字符串
//  2. 先遍历字符串求出 blank数量， 然后再计算出 新字符串的长度，从后往前排列字符
//  3. 注意 string溢出

using namespace std;
class Solution {
public:
	void replaceSpace(char *str,int length) {
		if(str == nullptr || length <= 0) {
			return;
		}
		int orign_len = 0;
		int blank_len = 0;
		char* start = str;
		while(*start != '\0') {
			orign_len++;
			cout << *start << endl;
			if (*start == ' ')
				blank_len++;

			start++;
		}
		cout << orign_len << endl;
		cout << blank_len << endl;

		int after_len = orign_len + 2 * blank_len;

		char* originLast = str + orign_len; // include the last \0
		char* afterLast = str + after_len;
		while (originLast >= str) {
			if (*originLast == ' ') {
				afterLast -= 2;
				afterLast[0] = '%';
				afterLast[1] = '2';
				afterLast[2] = '0';
				afterLast --;
				originLast--;

			} else {
				*afterLast = *originLast;
				originLast--;
				afterLast--;
			}
		}
	}
};

int main(int argc, char const *argv[])
{
	Solution  s = Solution();
	char str[20] = {' ', 'h', ' ', 'e', ' ', '\0'};
	s.replaceSpace(str, 20);
	cout << str << endl;
	return 0;
}

