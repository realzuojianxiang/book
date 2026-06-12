# -*- coding: utf-8 -*-
"""Translate 02-mathematical-statements.md - 9 TODOs"""
import re

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-i\ch04-logic\02-mathematical-statements.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    # 1. After counterexample discussion (line 12)
    "> \U0001f1e8\U0001f1f3 希望目前大家能认识到这个反例（Counterexample）确实完成了证伪的任务。我们还可以同意，像\"为什么我们早上9点有课?!\"这样的句子绝对不是数学语句。它是一个完全有效的英语句子，但从数学角度来说，它没有意义：我们无法证明或证伪它。",

    # 2. After "Not Knowing the Truth Value" intro (line 24)
    "> \U0001f1e8\U0001f1f3 **哥德巴赫猜想（Goldbach Conjecture）**：任何大于等于4的偶自然数都可以写成两个素数之和。这个语句是真还是假？如果你有证明或证伪，数学界将非常乐意看到！目前无人知晓该主张是真还是假，但可以确定的是，只有一种真值适用——该语句不可能同时为真和假，也不可能是某种中间状态。要么所有大于等于4的偶自然数都具有该性质，要么至少有一个不具有。因此，这个句子确实满足我们对数学语句的定义。（术语注释：一般而言，猜想（Conjecture）是指某人相信为真但尚未被证明或证伪的主张。）",

    # 3. After Pinocchio paradox discussion (line 30)
    "> \U0001f1e8\U0001f1f3 如果他在说谎，那么他的鼻子会生长（根据定义），但这样一来他的陈述实际上变成了真的！这种悖论语句（Paradoxical Sentence）既是真又是假，或既不是真也不是假，总之是不自洽的。我们的定义不允许这类语句成为数学语句。一般来说，自指语句（Self-referential Sentence）——即引用自身的语句——相当诡异，可能产生我们希望排除的悖论。",

    # 4. After variable proposition format discussion (line 37)
    "> \U0001f1e8\U0001f1f3 定义变元命题（Variable Proposition）时请注意格式：(1) 给命题一个字母名称（如 P）；(2) 标明其依赖的变元（如 x 和 y）；(3) 用引号将命题本身括起来；(4) 不要引入在命题语境中没有含义的新字母。这种格式精确且无歧义，为命题中的每个字母赋予了明确的含义，并清楚地区分了什么属于命题、什么不属于。",

    # 5. After BAD definitions discussion (line 43)
    "> \U0001f1e8\U0001f1f3 一个正确定义的命题：命题 P(x) 应该依赖于输入值 x，但不允许在命题内部再次改变或进一步量化该变量！原写法有两种截然不同的解释，因此这是一个糟糕的定义。关于变元命题的最后一个说明：定义命题时不一定要说明变量来自哪里，可以在后续使用命题时再补充。",

    # 6. After word order discussion (line 49)
    "> \U0001f1e8\U0001f1f3 **词序的重要性**：前一句断言存在某个数是所有实数的立方（为假），后一句断言每个实数都有立方根（为真）。两个句子包含完全相同的词和符号，只是顺序不同。这个例子强调了词序（Word Order）的关键重要性。",

    # 7. Questions "Remind Yourself" (line 57)
    "> \U0001f1e8\U0001f1f3 **复习问题** (1) 数学语句（Mathematical Statement）的重要定义性质是什么？ (2) 数学语句与变元命题有什么区别？ (3) 为什么哥德巴赫猜想是一个数学语句？ (4) 以下定义变元命题的尝试有什么问题？设 Q(x, y, z) 为 7x − 5y + z",

    # 8. Exercise items (line 63)
    "> \U0001f1e8\U0001f1f3 (b) 对于每个 n ∈ N，∑_{k∈[n]} k = n(n+1)/2。请对以下每个句子判断它是否为数学语句。如果是，判断其为真还是假。如果不是，解释原因。",

    # 9. After exercises (line 69)
    "> \U0001f1e8\U0001f1f3 **练习提示**：注意区分数学语句与非数学语句的关键——是否恰好有一个真值（True 或 False）。变元命题在未被量化时不是数学语句，但通过赋值或量化可以使其成为数学语句。给定任何集合 X 和任何对象 x，必定有 x ∈ X 或 x ∉ X。",
]

old = "> \U0001f1e8\U0001f1f3 TODO: 待翻译"
count_before = content.count(old)
print(f"Before: {count_before} TODOs")

for i, trans in enumerate(translations):
    content = content.replace(old, trans, 1)

count_after = content.count(old)
print(f"After: {count_after} TODOs")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
