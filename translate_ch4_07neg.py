"""Translate 07-negation-of-any-statement.md - 7 TODOs"""
import re

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-i\ch04-logic\07-negation-of-any-statement.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    # 1. After correct negation formula ¬(P⇒Q) ⇔ P∧¬Q
    "> 🇨🇳 总结条件语句（Conditional Statement）的否定方法：要否定 P ⇒ Q，我们先将它改写为 ¬P ∨ Q，然后应用德摩根定律（DeMorgan's Law），得到 ¬(¬P ∨ Q) ⇔ P ∧ ¬Q。这意味着：要证明\"若 P 则 Q\"为假，我们需要找到 P 为真但 Q 为假的情况。这是唯一的否定结果：假设成立但结论不成立。",

    # 2. After Example 4.7.3
    "> 🇨🇳 注意否定过程中的规律：存在量词（Existential Quantifier）$\exists$ 变为全称量词（Universal Quantifier）$\forall$，合取（Conjunction）∧ 变为析取（Disjunction）∨，同时每个内部命题取反，不等式方向取反。",

    # 3. After parenthetical position discussion
    "> 🇨🇳 这个例子清楚地表明括号位置的重要性。第一个语句将\"X 的每个元素 x 满足 x ≥ 1\"放在条件语句的\"若\"部分中；第二个语句则将该量化放在条件语句之前。虽然两个语句包含相同的量词和变元命题，但括号位置的不同完全改变了语句的含义。我们断言方框中的第二个版本为假，鼓励你自己弄清楚原因。",

    # 4. Questions - Remind Yourself
    "> 🇨🇳 **复习问题** (1) 数学语句与其逻辑否定（Logical Negation）之间有什么关系？ (2) 条件语句的逻辑否定是什么？ (3) 考虑语句 P ⇒ Q。它的逆否命题（Contrapositive）是什么？逆否命题的逻辑否定是什么？你能看出它与原语句的逻辑否定必须具有相同的真值吗？ (4) 双条件语句 P ⇔ Q 的逻辑否定是什么？考虑到这样的语句关于 P 和 Q 的真值说了什么，为什么这是合理的？",

    # 5. Exercises continuation
    "> 🇨🇳 (b) $\\forall x \\in A. (\\forall y \\in B. x \\geq y) \\Rightarrow x^2 \\geq 4$ (3) 设 P = {x ∈ R | x > 0}。写出下列每个语句的逻辑否定，并确定它们的真值。",

    # 6. Exercise 5 hint
    "> 🇨🇳 提示/建议：形如 |a| < b 的语句可以写成 −b < a < b。同样，形如 a < b < c 的语句可以写成 a < b ∧ b < c。这在确定真值时可能有助于你重写这些语句。",

    # 7. After truth values and sets section - about universal set and truth sets
    "> 🇨🇳 如果该蕴含关系成立，那么对应的真值集（Truth Set）之间也有类似的关系：T_P ⊆ T_Q。这体现了逻辑与集合之间的深层联系——逻辑运算对应集合运算，逻辑蕴含对应子集关系。这就像德摩根定律（DeMorgan's Laws）在逻辑和集合两种语境下的对应一样。",
]

old = "> 🇨🇳 TODO: 待翻译"
count_before = content.count(old)
print(f"Before: {count_before} TODOs")

for i, trans in enumerate(translations):
    content = content.replace(old, trans, 1)

count_after = content.count(old)
print(f"After: {count_after} TODOs")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
