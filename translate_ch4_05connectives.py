# -*- coding: utf-8 -*-
"""Translate 05-logical-connectives.md - 14 TODOs"""

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-i\ch04-logic\05-logical-connectives.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    # 1. After And section - notation about sets and logic (line 17)
    "> \U0001f1e8\U0001f1f3 **记号提示**：你可以注意到逻辑联结词\"∧\"与集合运算符\"∩\"之间的相似性。这不是巧合！正如我们将在第4.5.4节讨论的，我们可以用联结词\"∧\"来写出\"∩\"的定义，因为集合运算的逻辑基础就是它。但请注意区分这两个记号：如果 A 和 B 是集合，短语\"A ∧ B\"没有定义——应该写成\"A ∩ B\"。",

    # 2. After conditional statement intro (line 30)
    "> \U0001f1e8\U0001f1f3 条件语句是最难处理的逻辑联结词，持续给学生带来困惑，所以我们想格外小心和清晰地讨论它。我们要求语句\"若 P 则 Q\"在 P 为真时 Q 必然也为真的情况下具有真值真。也就是说，每当 P 为真时，Q 也为真，则该语句为真。",

    # 3. After truth table for conditional (line 40)
    "> \U0001f1e8\U0001f1f3 **定义**：条件语句 P ⇒ Q 的真值在假设 Q 每当 P 成立时也成立的情况下为真。唯一使 P ⇒ Q 为假的情况是 P 为真但 Q 为假。我们称 P 为条件语句的假设（Hypothesis），Q 为结论（Conclusion）。关键词\"每当\"应该向你说明为什么假假设（False Hypothesis）的情况是合理的——当 P 不为真时，我们无法宣称 P ⇒ Q 为假。",

    # 4. After examples of conditional statements (line 48)
    "> \U0001f1e8\U0001f1f3 **核心要点**：知道一个条件语句整体为真，并不告诉我们组成命题的真值。第三和第七个例子都是真条件语句，但我们当然不能由此得出亚伯拉罕·林肯还活着或 0 = 1 的结论。\"蕴含\"不等同于\"可以推出\"——知道 P ⇒ Q 为真，并不一定意味着我们可以从 P 直接推导出 Q。",

    # 5. After variable quantification in conditionals (line 54)
    "> \U0001f1e8\U0001f1f3 **变量的量化仍然重要**：条件声明 x > 1 ⇒ x² − 1 > 0 本身是一个变元命题，在实数 R 的语境下才有意义。要使其成为真正的数学语句，应当写成 $\forall x \in R. x > 1 \Rightarrow x^2 - 1 > 0$。我们建议你在组合逻辑联结词与变元命题时，始终确保变量在语句的某处被量化，以保证该句子是一个具有唯一真值的数学语句。",

    # 6. After writing ⇒ using ∨ (line 60)
    "> \U0001f1e8\U0001f1f3 **用\"∨\"表示\"⇒\"**：条件语句 P ⇒ Q 和语句 ¬P ∨ Q 具有相同的真值。这是一个逻辑等价（Logical Equivalence）的好例子。条件语句为真的两种情况是：(1) ¬P 成立（即假假设），或者 (2) Q 成立。在这两种情况下，P ⇒ Q 必然为真！",

    # 7. After weekday/lecture examples (line 68)
    "> \U0001f1e8\U0001f1f3 由于我们并不关心没有课的情况（假假设），我们只需要假设在 X 日有课，然后推出 X 是工作日。这就是我们将来用来直接证明条件语句的方法。另一种重要的是：\"如果今天是工作日，那么我们有课\"为假，因为在某个周二 Q 为真但 P 为假。",

    # 8. After set containment examples (line 77)
    "> \U0001f1e8\U0001f1f3 从以上分析可知 P ⇒ Q 为真——若 A ⊆ B，则 A − B = ∅。类似地，Q ⇒ P 也为真——若 A − B = ∅，则 A ⊆ B。而且 ¬Q ⇒ ¬P 和 ¬P ⇒ ¬Q 都为真。这些观察验证了条件语句与其逆否命题（Contrapositive）的逻辑等价性，我们将在下一节详细讨论。",

    # 9. After observations about ⇒ (line 82)
    "> \U0001f1e8\U0001f1f3 **关于\"⇒\"的观察与要点**：知道 P ⇒ Q 成立并不告诉我们关于 Q ⇒ P 的任何信息——逆命题（Converse）的真值不一定与原语句相同。另外，如果仅在纸上写下\"Blah blah ⇒ Yada yada\"，读者无法判断你在断言什么——应该用辅助句子来表明你在做推理或演绎。假假设使条件语句为真是排中律的直接推论。我们始终可以将条件语句改写为\"或\"语句：P ⇒ Q 与 ¬P ∨ Q 始终具有相同的真值。",

    # 10. After converse/contrapositive definition (line 92)
    "> \U0001f1e8\U0001f1f3 逆否命题（Contrapositive）总是与原语句具有相同的真值——这将在下一节证明。逆命题（Converse）有趣之处在于它的真值不一定与原语句相关。每当证明 P ⇒ Q 为真后，数学家通常会问\"逆命题也成立吗？\"逆命题也是日常逻辑谬误的来源——如果你的朋友反驳说\"B 不必然蕴含 A！\"你可以说\"你说的是逆命题，它与我原命题之间不一定有逻辑联系。\"",

    # 11. After subset definition with logic (line 103)
    "> \U0001f1e8\U0001f1f3 这个定义是有道理的：它表达了上面段落中的\"每当\"——每当 x ∈ A，我们也必须能推出 x ∈ B；\"若 x ∈ A 则 x ∈ B\"必须成立。同样回顾集合运算的定义——交集、并集、差集和补集——它们都可以用量词和逻辑联结词重写。",

    # 12. After set operations definition (line 119)
    "> \U0001f1e8\U0001f1f3 回顾定义3.6.9中我们最初定义分割的方式。你能看出我们在这里说的是同一回事，只是用了逻辑符号吗？分割的定义现在可以用逻辑联结词和量化来精确表达：(1) 每个 S_i 是 A 的子集；(2) 不同的 S_i 两两不交；(3) 所有 S_i 的并恰好是 A。",

    # 13. After questions section (line 125)
    "> \U0001f1e8\U0001f1f3 **复习问题** (1) ∧ 和 ∨ 有什么区别？ (2) ∧ 和 ∩ 有什么区别？∨ 和 ∪ 有什么区别？ (3) 写出 P ⇒ Q 的真值表。 (4) 为什么 P ⇒ Q 和 ¬P ∨ Q 逻辑等价？ (5) 条件语句的逆命题是什么？逆否命题是什么？ (6) 条件语句和其逆命题的真值有关吗？",

    # 14. After exercises (line 132+)
    "> \U0001f1e8\U0001f1f3 **练习**：(1) 将下列句子用逻辑记号重写并判断真假。 (2) 将每个 $\forall$ 断言改写为条件语句并判断真假。 (3) 将每个条件语句改写为 $\forall$ 断言并判断真假。 (4) 用定义的变元命题判断每个语句的真假。 (5) 对每个条件语句用逻辑记号写出它及其逆命题和逆否命题，然后判断这三者的真值。",
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
