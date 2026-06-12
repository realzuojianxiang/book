#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch08/06-pigeonhole-principle.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-ii/ch08-combinatorics/06-pigeonhole-principle.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    # 1: Pigeonhole Principle statement
    '鸽巢原理（Pigeonhole Principle）很非形式化，但能帮你看到它的用处。鸽巢原理在有若干对象分属若干类别时特别有用：若知道对象总数和类别数，就能保证存在某个类至少包含一定数量的对象。\n\n**例 8.6.1** 典型应用：任意 3 人中必有两人的性别相同——注意不说哪种性别出现至少两次，只保证这样的类别存在。枚举验证：MMM、MMF、MFF、FFF，每种情况至少一个性别出现两次（或更多）。等价说法：掷 3 枚硬币，至少两面相同。类似说法：掷 7 枚骰子，至少两面相同。更一般地说：若将 $n+1$ 张纸放入 $n$ 个抽屉，某个抽屉至少有 2 张。"pigeonhole"就是老式翻盖桌上那些小格的名称。\n\n**8.6.2 陈述与证明** 鸽巢原理有两个版本。\n\n**(1)** 若集合 $S$（$|S|=n$）被划分为 $k$ 个不相交子集且并集为 $S$，若 $k < n$，则至少一个子集有多于一个元素，实际上至少有 $\\lceil n/k \\rceil$ 个元素。\n\n**(2)** 若 $x_1, x_2, \\ldots, x_n$ 为实数且 $\\sum_{i=1}^{n} x_i \\geq z$，则存在某个 $i$ 使 $x_i \\geq z/n$。（即 $n$ 个实数中必有一个不小于平均值。）\n\n**证明** (1) 反证：设每个 $|S_i| < n/k$，则 $n = |S| = \\sum_{i=1}^{k} |S_i| < \\sum_{i=1}^{k} n/k = n$，矛盾！(2) 反证：设所有 $x_i < z/n$，则 $z = \\sum x_i < \\sum z/n = z$，矛盾！两个证明代数上完全相同，体现了同一个底层思想。',
    # 2: Example 8.6.4 NYC
    '百万人口。将"鸽洞"定义为头发数 0 到 100 万，8 百万人分入 100 万+1 个洞，由鸽巢原理得某个洞至少有 8 人。',
    # 3: Example 8.6.6 golfers
    '(为什么？你能补全细节吗？试试！)然而，我们无法保证两人战绩相同。例如 $n=3$ 时，选手 1 两战皆负，选手 2 胜 1 负 1，选手 3 两战皆胜，记录各不相同。但如果限制无人全胜，则可保证两人战绩相同。每人打 $n-1$ 场，无人 $n-1$ 胜，可能胜场数为 $0, 1, \\ldots, n-2$ 共 $n-1$ 种，而选手有 $n$ 人，由鸽巢原理必有两人胜场相同！',
    # 4: Example 8.6.7 mod 10
    '这样我们有 6 个盒子。',
    # 5: Exercise 3 - park distance
    '$\\frac{\\sqrt{2}}{2}$',
    # 6: Exercise 3 continued - boundary
    '$\\frac{\\sqrt{2}}{2}$',
    # 7: Section 8.7 transition
    '千米。接下来证明此界限是最优的——即给出一种放置 5 个洞的方法使任两洞距离不小于',
    # 8: optimal placement
    '$\\frac{\\sqrt{2}}{2}$',
    # 9: Inclusion/Exclusion motivation
    '**8.7 容斥原理（Inclusion/Exclusion）**\n\n**8.7.1 动机** 容斥原理帮助我们从一个大的集合中去除子集后清点剩余元素。简单形式我们已见过：若 $A \\subseteq U$，则 $|U-A| = |U| - |A|$。若去除两个集合呢？如果它们有重叠怎么办？三个？$n$ 个？能否写出一般表达式？\n\n以下是小情形的表达式。设全域 $U$ 和子集 $A_1, A_2, \\ldots, A_n \\subseteq U$，要计 $U$ 中不属于所有 $A_i$ 的元素：\n- $|U-A_1| = |U| - |A_1|$\n- $|U-(A_1 \\cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \\cap A_2|$\n- $|U-(A_1 \\cup A_2 \\cup A_3)| = |U| - |A_1| - |A_2| - |A_3| + |A_1 \\cap A_2| + |A_1 \\cap A_3| + |A_2 \\cap A_3| - |A_1 \\cap A_2 \\cap A_3|$\n\n理解方式：任取 $x \\in U$，考虑 $x$ 属于几个 $A_i$——在等式两边各被计了几次？是否被恰当地计数？也可将表达式理解为"先猜一个计数，然后不断修正"：先取 $|U|$ 减去各 $|A_i|$——哎，属于两个集合的元素被多减了一次，要加回来——哎，属于三个集合的元素又被多加了一次，要再减去……这就是下一节要推广和证明的。',
]

count = 0
for t in translations:
    idx = data.find(todo_marker)
    if idx >= 0:
        data = data[:idx] + t + data[idx+len(todo_marker):]
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(data)
print(f"Replaced {count} TODOs, remaining: {data.count('TODO')}")
