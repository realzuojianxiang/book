# -*- coding: utf-8 -*-
"""Translate 04-logical-negation.md - 15 TODOs"""

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-i\ch04-logic\04-logical-negation.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    # 1. After "is logically equivalent to" universal negation (line 11)
    "> \U0001f1e8\U0001f1f3 即逻辑上等价于语句 $\forall x \in S. \neg R(x)$。这从直觉上是合理的：要反驳一个存在性主张，你需要证明无论取哪个值，该性质都不成立。假想你正在与朋友辩论：朋友告诉你某个 kwyjibo 具有 zooqa 的性质。你会怎么说？\"才不是呢！给我看任何一个 kwyjibo，我知道它不可能是一个 zooqa，因为以下原因……\" 当你说\"给我看任何一个\"时，你实际上执行了一次全称量化！你在说无论考虑哪个 kwyjibo，某事都成立——即 $\forall x \in K$（K 是所有 kwyjibo 的集合），某事为真。请思考并理解为什么我们发现的逻辑否定是有道理的。",

    # 2. After negating nested quantifiers step (line 18)
    "> \U0001f1e8\U0001f1f3 这一步使用了我们上面看到的另一个否定方法。然后将所有部分组合起来，我们可以说 $\neg A$ 是语句 $\forall y \in R. \exists x \in R. y \neq x^3$。这个命题可以被证明为真，从而说明原始语句必定为假。（我们将此证明留作练习。提示：给定任何 $y \in R$，定义一个 $x$ 的值使得 $y \neq x^3$ 为真。注意你对 $x$ 的选择将依赖于 $y$ 的值。）观察否定是如何产生的：我们认识到原始语句是一系列嵌套量词（Nested Quantifiers），末尾是一个变元命题，然后将否定从外层量词\"传递\"到内层量词。",

    # 3. After general procedure negation (line 24)
    "> \U0001f1e8\U0001f1f3 **一般法则**：要否定一个仅由量词和变元命题组成的语句，只需将每个 $\forall$ 换为 $\exists$，将每个 $\exists$ 换为 $\forall$，并否定末尾的命题。不要修改量化的集合，只修改量词本身及随后的命题——改变论域（Universe of Discourse）是没有意义的。",

    # 4. After "Don't Change the Quantification Set" (line 30)
    "> \U0001f1e8\U0001f1f3 原始主张只对集合 T 中的元素做了断言，因此它的否定也一样。你不能从别的房间拿来一本法语小说说\"看，你说错了！\"那不能证明关于我们书架的主张有任何问题——论域不同。同理，当我们否定 $\forall b \in T. P(b)$ 时，得到 $\exists b \in T. \neg P(b)$，而不改变论域 T。",

    # 5. After Law of Excluded Middle intro (line 43)
    "> \U0001f1e8\U0001f1f3 排中律的运用：$\sqrt{2}^{\sqrt{2}}$ 要么是有理数要么是无理数。（这就是排中律的用法。）让我们分别考虑两种情况。",

    # 6. After first case of proof (line 49)
    "> \U0001f1e8\U0001f1f3 假设 $\sqrt{2}^{\sqrt{2}}$ 确实是有理数。那么取 $a = \sqrt{2}$ 和 $b = \sqrt{2}$ 就是我们所需的例子，因为 $a$ 和 $b$ 都是无理数，而 $a^b$ 是有理数。",

    # 7. After second case intro (line 55)
    "> \U0001f1e8\U0001f1f3 现在假设 $\sqrt{2}^{\sqrt{2}}$ 是无理数。在这种情况下，我们可以取 $a = \sqrt{2}^{\sqrt{2}}$ 和 $b = \sqrt{2}$ 作为所求的例子，",

    # 8. After computation (line 61)
    "> \U0001f1e8\U0001f1f3 因为 $a$ 和 $b$ 都是无理数，而 $a^b = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = (\sqrt{2})^2 = 2$，这是有理数。",

    # 9. After product is rational conclusion (line 67)
    "> \U0001f1e8\U0001f1f3 在两种情况下，我们都找到了实数 $a, b \in R$ 使得 $a$ 和 $b$ 都是无理数但 $a^b$ 是有理数。这就是一个非构造性证明（Non-constructive Proof）的例子。它告诉我们某种东西存在（甚至缩小到了两种可能性），却没有确切告诉我们哪一种就是我们一直在寻找的那种。正是排中律（Law of the Excluded Middle）的直接使用导致了这种结果。大多数证明将是构造性的（但不全是）。",

    # 10. After "Maybe you can find one" (line 79)
    "> \U0001f1e8\U0001f1f3 构造性证明在主观上更好，因为如果我们声称某物存在，我们应该能够展示它。有时，构造性证明并不立刻清晰，我们必须做一个非构造性证明，就像我们在这里所做的那样。",

    # 11. After indexed set operations intro (line 87)
    "> \U0001f1e8\U0001f1f3 回顾第3.6.2节中定义的索引集运算——并和交。主要的想法是：一个对象是否属于索引并集，取决于它是否是至少一个组成集合的元素——这正是一个存在量化。一个对象是否属于索引交集，取决于它是否是所有组成集合的元素——这正是一个全称量化。有了这些观察，我们可以用新的量词记号重写索引集运算的定义。",

    # 12. After Definition 4.4.2 (line 97)
    "> \U0001f1e8\U0001f1f3 回到第3.6.2节的例子和练习重新尝试。现在这些定义是否更好理解了？通过量词，我们看到索引并集本质上是存在量化的集合版本，索引交集本质上是全称量化的集合版本。",

    # 13. After questions (line 103)
    "> \U0001f1e8\U0001f1f3 (a) $\forall a \in A. \exists b \in B. Q(a, b)$ 的否定是 $\exists a \in A. \forall b \in B. \neg Q(a, b)$ (b) $\forall a \in A. \neg P(a)$ 的否定是 $\exists a \in A. P(a)$ (c) $\forall c \in C. \forall d \in D. \neg Q(c, d)$ 的否定是 $\exists c \in C. \exists d \in D. Q(c, d)$ (d) $\exists a_1, a_2 \in A. \forall d \in D. R(a_1, a_2, d)$ 的否定是 $\forall a_1, a_2 \in A. \exists d \in D. \neg R(a_1, a_2, d)$ (e) $\forall b_1, b_2, b_3 \in B. \neg R(b_1, b_2, b_3)$ 的否定是 $\exists b_1, b_2, b_3 \in B. R(b_1, b_2, b_3)$ (f) $\exists b \in B. \forall c \in C. \forall d \in D. R(d, b, c)$ 的否定是 $\forall b \in B. \exists c \in C. \exists d \in D. \neg R(d, b, c)$",

    # 14. After contradiction proof also 2 case false hypothesis (after line 79 pt2)
    "> \U0001f1e8\U0001f1f3 请思考排中律为何如此重要：它保证每个陈述要么为真要么为假，没有中间地带。这使我们能够通过证明否命题为假来间接证明原命题为真——即反证法（Proof by Contradiction）的基础。",

    # 15. Last exercise block (questions & exercises exercise items)
    "> \U0001f1e8\U0001f1f3 **练习**：(1) 对下列每个语句写出其否定，哪个为真？(2) 对下列每个语句写出其否定，哪个为真？(3) 设 I = {x ∈ R | 0 < x < 1}，写出每个定义集合的判定条件。(4) 设 P = {y ∈ R | y > 0}，写出语句的逻辑否定。(5) 设 A, B, C, D 为任意集合，P(x), Q(x,y), R(x,y,z) 为任意变元命题，写出每个语句的否定。",
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
