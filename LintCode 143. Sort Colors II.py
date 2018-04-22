"""
我们可以使用类似桶排序的思想，对所有的数进行计数。

1. 从左扫描到右边，遇到一个数字，先找到对应的bucket.比如

3 2 2 1 4

第一个3对应的bucket是index = 2 (bucket从0开始计算）

2. Bucket 如果有数字，则把这个数字移动到i的position(就是存放起来），然后把bucket记为-1(表示该位置是一个计数器，计1）。

3. Bucket 存的是负数，表示这个bucket已经是计数器，直接减1. 并把color[i] 设置为0 （表示此处已经计算过）

4. Bucket 存的是0，与3一样处理，将bucket设置为-1， 并把color[i] 设置为0 （表示此处已经计算过）

5. 回到position i，再判断此处是否为0（只要不是为0，就一直重复2-4的步骤）。

6.完成1-5的步骤后，从尾部到头部将数组置结果。（从尾至头是为了避免开头的计数器被覆盖）

例子(按以上步骤运算)：

3 2 2 1 4

2 2 -1 1 4

2 -1 -1 1 4

0 -2 -1 1 4

-1 -2 -1 0 4

-1 -2 -1 -1 0
"""
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        i = 0
        n = len(colors)

        while i < n:
            if colors[i] > 0:
                if colors[colors[i] - 1] > 0:
                    tmp = colors[i]
                    colors[i] = colors[colors[i] - 1]
                    colors[tmp - 1] = -1
                    i -= 1
                else:
                    colors[colors[i] - 1] -= 1
                    colors[i] = 0
            i += 1

        i = len(colors) - 1
        k = i

        while i >= 0:
            if colors[i] < 0:
                p = k + colors[i]
                while k > p:
                    colors[k] = i + 1
                    k -= 1
            i -= 1
