# -*- coding: utf-8 -*-
"""Translate 03-quantifiers.md - 13 TODOs"""

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-i\ch04-logic\03-quantifiers.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    # 1. After section header 4.3 intro (line 10)
    u"> \U0001f1e8\U0001f1f3 本节将介绍量词（Quantifier）的两种基本形式：存在量词（Existential Quantifier）$\exists$ 和全称量词（Universal Quantifier）$\forall$。它们让我们能够精确地表达\"存在某个……\"和\"对于所有……\"这类数学断言。",

    # 2. After Example 4.3.2 (line 17)
    u"> \U0001f1e8\U0001f1f3 注意这些例子中的模式：全称量词 $\forall$ 用于表达\"每个/所有\"，存在量词 $\exists$ 用于表达\"存在某个/至少有一个\"。大圆点\".\"分隔量词部分和关于变量所作的断言。辅助短语\"such that\"（使得）始终跟在存在量词之后。",

    # 3. After reading quantified statements aloud (line 26)
    u"> \U0001f1e8\U0001f1f3 **朗读量化语句**：建议在阅读逻辑符号时加上辅助词\"使得\"（such that）和\"成立\"（holds）来帮助理解。例如，$\exists y \in R$ such that $\forall x \in R$. $P(x, y)$ is True。在白板或纸上书写时，常用缩写\"s.t.\"代替\"such that\"，表明这个短语在数学写作中多么常见。",

    # 4. After misplaced "such that" discussion (line 32)
    u"> \U0001f1e8\U0001f1f3 \"such that\"的误放可能导致完全相反的含义！原语句 $\exists y \in R. \forall x \in R. P(x, y)$ 断言存在一个实数 y 使得对所有实数 x 都有 y = x³（这是假的）。但将\"such that\"误放在 $\forall$ 之后，可能被理解为 $\forall x \in R. \exists y \in R$ such that P(x,y)（这是真的）。我们必须始终只将\"such that\"放在存在量词之后。",

    # 5. After "such that" misplacement full discussion (line 39)
    u"> \U0001f1e8\U0001f1f3 \"such that\"的误放导致了一个合理的语言学解释，其含义与原意恰好相反。这就是为什么我们必须小心地始终且仅将\"such that\"放在存在量词之后。记住我们不会总是写出这个辅助短语，所以你在默读或朗读给自己听时，必须记住正确使用它，以确保你得到正确的理解。量词顺序的重要性再次得到强调。",

    # 6. After fixed variables introduction (line 46)
    u"> \U0001f1e8\U0001f1f3 **量化\"固定\"一个变量**：初始量化\"$\forall n \in X$\"的作用是固定一个特定的 n 值用于语句的其余部分。此后，断言\"$\exists a, b \in P$\"及随后的性质 Q(n, a, b) 依赖于那个固定的但任意的 n 值。量化顺序告诉我们 a 和 b 的值可能依赖于所选择的 n。这就是我们说 a 和 b 依赖于 n 的含义。",

    # 7. After quantification fixes variable more (line 52)
    u"> \U0001f1e8\U0001f1f3 确保你理解了以上讨论，思考以下问题：上面的语句与 $\exists n \in X. \exists a, b \in P. Q(n, a, b)$ 有什么区别？这个语句是真还是假？为什么？关键区别在于：原语句要求对每个 n 都存在适切的 a、b，而后者只要求存在某个 n 及相应的 a、b。",

    # 8. After specifying quantification set intro (line 64)
    u"> \U0001f1e8\U0001f1f3 **必须指定量化集合**：语句 $\forall x. x^2 \geq 0$ 看起来\"似乎为真\"，但事实上它没有意义——x 从哪里来？\"对于每个 x……\"从哪里来？如果 x 不是数呢？我们需要指明 x \"来自\"哪个集合，才能知道 $x^2 \geq 0$ 是否甚至是一个良定义的语法短语，更不用说是否为真。将句子改为 $\forall x \in R. x^2 \geq 0$ 就是一个良定义的语法正确的（且为真的！）数学语句。但改为 $\forall x \in C. x^2 \geq 0$ 就是为假的数学语句，因为 $i \in C$ 但 $i^2 = -1 < 0$。语境至关重要。",

    # 9. After "One Exception" discussion (line 70)
    u"> \U0001f1e8\U0001f1f3 因为不存在\"所有集合的集合\"（回顾罗素悖论 Russell's Paradox），我们无法用符号写出量化所有集合的语句。因此，我们将继续使用英文短语\"For any sets A, B, C...\"来代替符号形式。在草稿纸上可以写\"$\forall A, B, C$\"，但在正式写作中应使用上述措辞。",

    # 10. After exercises/questions section (line 78)
    u"> \U0001f1e8\U0001f1f3 **复习问题** (1) $\forall$ 和 $\exists$ 有什么区别？ (2) 你会如何朗读语句 $\forall x \in R. \exists y \in R. x = y^3$？ (3) 为什么语句 $\exists y. y + 3 > 10$ 不是正规的数学语句？下列两个语句之间有什么区别？$\exists x \in N. \exists y \in N. x + y = 5$ 与 $\exists x, y \in N. x + y = 5$。它们为真还是为假？ (4) 下列两个语句之间有什么区别？$\exists a, b \in Z. a \cdot b = -3$ 与 $\exists \heartsuit, \diamondsuit \in Z. \heartsuit \cdot \diamondsuit = -3$。它们为真还是为假？ (5) 为什么下列句子不是正规量化语句？$\exists x. x > 7$；$\forall y \in Z$；$\forall z > 2. z^2 > 4$；$\forall w \in Z. w^2 = t. \exists t \in N$。",

    # 11. After try it exercises (line 84)
    u"> \U0001f1e8\U0001f1f3 **练习题**：(1) 用符号、量词和集合构造记号写出第4.3.3节中定义的偶自然数集合 X 的定义。(2) 写一个以量词开头的数学语句，当该量词为 $\exists$ 时语句为真，为 $\forall$ 时语句为假。(3) 写一个变元命题 P(x)，使得 $\forall x \in Z. P(x)$ 为真但 $\forall x \in N. P(x)$ 为假。(4) 将下列每个数学语句用逻辑符号写出（确保先正确定义所需的变元命题），然后判断其真值。(5) 对每个量化语句大声朗读，然后判定真假。",

    # 12. After Q1,Q2/warmup (line 91)
    u"> \U0001f1e8\U0001f1f3 **逻辑否定（Logical Negation）简介**：Q1 是假的，Q2 是真的。我们知道 Q1 为假，是因为该语句声称存在某个实数具有某性质——要证明整个语句为假，我们需要验证该性质对所有实数 y 都不成立，但集合 R 是无穷大的！更高效的方法是证明该语句的否定为真。逻辑否定指的是原语句在逻辑意义上的\"反面\"——具有恰好相反的真值。",

    # 13. After negation intro leads to universal quantification (line 97)
    u"> \U0001f1e8\U0001f1f3 反例（Counterexample）的概念正来源于此：要反驳一个全称量化语句，我们必须证明一个存在量化语句——该证明涉及明确定义一个不满足指定性质的集合元素，故称\"反例\"。当我们说\"给我看任何一个\"时，实际上是在执行全称量化——你在说无论考虑哪个 kwyjibo，某事都成立。这正是 $\forall x \in S. \neg R(x)$ 与 $\exists x \in S. R(x)$ 具有相反真值的原因。",
]

old = u"> \U0001f1e8\U0001f1f3 TODO: 待翻译"
count_before = content.count(old)
print(f"Before: {count_before} TODOs")

for i, trans in enumerate(translations):
    content = content.replace(old, trans, 1)

count_after = content.count(old)
print(f"After: {count_after} TODOs")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
