"""
https://leetcode.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # digit이 발견되면 [substr] 의 substr을 재귀적으로 처리 후 ans에 추가한다.
        # 관건은 substr을 추출하는 것인데, 괄호가 nested 형태를 띌 수가 있다.
        # substr 발견 로직:
        # - [가 발견되면 stack에 push
        # - alpha일 경우 [가 열렸을 경우 substr에 추가, 아닐경우 ans에 추가
        # - ]가 발견되면 stack에서 pop, stack이 비었으면 현재까지 substr을 다시 재귀호출
        # (linear time에 할 수 있을까?)

        ans = ""
        stack_cnt = 0
        substr = ""
        mul = ""
        for c in s:
            if c == '[':
                if stack_cnt > 0:
                    substr += c
                stack_cnt += 1
            elif c == ']':
                stack_cnt -= 1
                if stack_cnt > 0:
                    substr += c
                if stack_cnt == 0:
                    ans += eval(mul) * self.decodeString(substr)
                    mul = substr = ""
            elif c.isnumeric():
                if stack_cnt > 0:
                    substr += c
                else:
                    mul += c
            else:
                if stack_cnt > 0:
                    substr += c
                else:
                    ans += c
        return ans
            

if __name__ == '__main__':
    # print(Solution().decodeString("10[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))