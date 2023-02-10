# 7. 数字反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。

# 示例 1：

# 输入：x = 123
# 输出：321

#### 写代码时注意最大数和最小数
class Solution:
    def reverse(self, x: int) -> int:
        t = str(x)
        if t[0] == "-":
            r = "-" + "".join(reversed(t[1:]))
        else:
            r = "".join(reversed(t))
        r = int(r)
        if r > 4294967295 or r < -4294967296:
            return 0
        return r

x = 123
x = -123
x = -120
x = 1534236469
s = Solution()
print(s.reverse(x))
            
