#!/usr/bin/env python3
"""翻译 03-order-relations.md 的 9 处 TODO"""
import sys

FILE = "docs/part-ii/ch06-relations-modular-arithmetic/03-order-relations.md"

# 按顺序对应 9 个 TODO 的翻译
translations = [
    # TODO 1 (line 19): Example 6.3.3 到 Definition 6.3.5 的总体翻译
    """例6.3.3. 在 $\mathbb{R}$ 上定义以下四个关系：$(x, y) \in R_1 \Leftrightarrow x \leq y$，$(x, y) \in R_2 \Leftrightarrow x < y$，$(x, y) \in R_3 \Leftrightarrow x = y$，$(x, y) \in R_4 \Leftrightarrow \lfloor x \rfloor = \lfloor y \rfloor$。（回忆 $\lfloor x \rfloor = \max\{a \in \mathbb{Z} \mid a \leq x\}$ 是实数的"下取整"（floor）；即通过向下取整得到的整数。）其中哪些是偏序（partial order）？全序（total order）？都不是？想几分钟，试着勾画一些证明的轮廓，或者向朋友/同学口述解释。以下是我们的想法：关系 $R_1$ 和 $R_3$ 都是偏序，但只有 $R_1$ 是全序。关系 $R_2$ 和 $R_4$ 既不是偏序也不是全序（因为 $R_2$ 不自反（reflexive），$R_4$ 不反对称（anti-symmetric））。任何类型的序关系——偏序或全序——背后的核心思想是：我们能以某种方式比较集合 $A$ 的元素并为它们赋予……嗯，一种排序。启发式地说，偏序在 $A$ 中产生元素的"链"（chain），使得沿着任何一条链，我们可以将元素排成一条线，有点像数轴和我们通常对 $\mathbb{R}$ 的想象；对于全序，只有一条"链"且它就是整个 $A$。你可能对 $R_2$ 不算某种"类序"关系的说法有异议，而你的异议是有道理的。$R_2$ 和 $R_1$ 之间唯一的本质区别是我们不允许相等；字面上说，"或等于"这个短语被包含在"$\leq$"的定义中，但在"$<$"的定义中被省略了。这导致 $R_2$ 不自反，但仅此而已。你也可能注意到关系 $R_4$ 与 $R_1$ 没有这种类似的关系；它似乎是某种不同的东西（我们很快就会讲到）。这引出了以下定义，其中偏序或全序可以被"放宽"为一种相关的排序。

**定义6.3.4.** 设 $A$ 为集合，$R$ 为 $A$ 上的关系。我们称 $R$ 是**非自反的（irreflexive）**当且仅当 $\forall x \in A. (x, x) \notin R$。注意这与仅仅"不自反"（not reflexive）不同。想一想量词的含义：自反性意味着每个元素与自身有关系，所以其逻辑否定意味着存在至少一个元素与自身没有关系。非自反性则意味着每个元素与自身都没有关系。

**定义6.3.5.** 设 $A$ 为集合，$R$ 为 $A$ 上的关系。我们称 $R$ 是**严格偏序（strict partial order）**当它是非自反的、传递的且反对称的。我们称 $R$ 是**严格全序（strict total order）**当它是非自反的、传递的、反对称的，且满足以下性质：$\forall x, y \in A. x \neq y \Rightarrow [(x, y) \in R \lor (y, x) \in R]$""",

    # TODO 2 (line 31): 关于严格/非严格序之间转换的段落，以及 R4 的讨论
    """你可能想知道这与非严格序关系之间有什么联系。实际上，有一种自然的方式可以将任何序关系转换为严格的，反之亦然。我们总是可以通过加入或移除元素是否与自身有关系的条件来从一个定义出另一个。以下引理总结了如何做到这一点，并由此表明严格序与非严格序的数量一样多。

**引理6.3.6.** 设 $(A, R_1)$ 是偏序集。则由 $(x, y) \in S_1 \Leftrightarrow [(x, y) \in R_1 \wedge x \neq y]$ 定义的关系 $S_1$ 是 $A$ 上的严格偏序。设 $(A, R_2)$ 是全序集。则由 $(x, y) \in S_2 \Leftrightarrow [(x, y) \in R_2 \wedge x \neq y]$ 定义的关系 $S_2$ 是 $A$ 上的严格全序。设 $(A, S_3)$ 是严格偏序集。则由 $(x, y) \in R_3 \Leftrightarrow [(x, y) \in S_3 \lor x = y]$ 定义的关系 $R_3$ 是（非严格）偏序。设 $(A, S_4)$ 是严格全序集。则由 $(x, y) \in R_4 \Leftrightarrow [(x, y) \in S_4 \lor x = y]$ 定义的关系 $R_4$ 是（非严格）全序。

回想上面在 $\mathbb{R}$ 上定义的关系 $R_1$ 和 $R_2$，用"小于或等于且不等"来定义"小于"可能看起来有些奇怪。这确实更啰嗦！然而，这只是我们用语言描述"$\leq$"的方式造成的结果。从数学角度讲，先讨论自反关系以及偏序和全序更为自然，然后再修改这些定义来得到严格序。我们很快就会谈到——在讨论极小元时——为什么自反性是一个好性质，这也是我们以偏序为起点再修正定义来允许严格序的合理理由，而不是反过来。现在只需注意到 $R_2$ 就是对应于全序 $R_1$ 的严格全序。

问题：是否存在对应于偏序 $R_3$ 的严格偏序？如果有，它是什么？如果没有，为什么？

关系 $R_4$ 不是任何类型的序关系——严格的或其他的。不过，注意到 $R_4$ 确实巧妙地将 $\mathbb{R}$ 的元素"打包"了。本质上，每个满足 $1 \leq y < 2$ 的实数 $y$ 在这个关系下都是"相同的"（same）。同样适用于每个满足 $2 \leq y < 3$ 的 $y$，以及每个满足比如 $-5 \leq y < -4$ 的 $y$，以此类推。一旦完成了这种"打包"，我们就"知道"可以为这些"包"赋予一个排序，但关于该排序的信息并没有编码在关系 $R_4$ 本身之中。我们必须做额外的工作来施加那个排序。这就是为什么 $R_4$ 按其定义方式不是任何类型的序关系""",

    # TODO 3 (line 39): A1 链
    """$A_1 = \{\emptyset, \{1\}, \{1, 2\}, \{1, 2, 3\}$\}（从 $\emptyset$ 到全集的包含链）""",

    # TODO 4 (line 45): A2 链
    """$A_2 = \{\emptyset, \{1\}, \{1, 3\}, \{1, 2, 3\}$\}（另一条包含链）""",

    # TODO 5 (line 51): A3 链
    """$A_3 = \{\emptyset, \{2\}, \{1, 2\}, \{1, 2, 3\}$\}（又一条包含链）""",

    # TODO 6 (line 57): A4 链
    """$A_4 = \{\{3\}, \{2, 3\}$\}（一条较短的包含链）""",

    # TODO 7 (line 75): Example 6.3.10 词典序
    """例6.3.10. 设 $A$ 是标准的26个英文字母组成的集合，$W$ 是由 $A$ 中字母组成的所有有限字符串的集合。即 $W$ 是所有可能的"单词"的集合，其中我们允许任何字母组合被包含在我们的"词典"中。让我们尝试定义 $W$ 上的标准词典序（lexicographic ordering）$L$。将 $A$ 表示为集合 $[26]$ 会有所帮助，其中 $a = 1, b = 2, \ldots, z = 26$。于是，一个单词 $w \in W$ 可表示为 $w = (w_1, w_2, \ldots, w_n)$，其中 $n \in \mathbb{N}$ 且 $\forall i \in [n]. w_i \in A$。注意到对于任意两个单词 $v, w \in W$，我们可以从左到右逐字母比较它们，直到找到差异之处。在差异出现的位置，根据那两个字母的比较来排序两个单词。如果其中一个比另一个长且其余字母相同，我们希望将较长的排在较短的后面，就像词典中"there"排在"therefore"之前。$(v, w) \in L \Leftrightarrow$ 在使得 $v_i \neq w_i$ 的最小下标 $i$ 处，有 $v_i < w_i$（其中空格位置被视为27）。想想为什么这对应于词典中单词的通常排序。（你能否用更严谨的数学记号来定义它？试试看！）""",

    # TODO 8 (line 83): 练习段落
    """(1) 设 $S = [2]$，在 $\mathcal{P}(S)$ 上定义 $R$：$(x, y) \in R \Leftrightarrow x$ 至少有和 $y$ 一样多的元素。证明 $S$ 不是偏序。""",

    # TODO 9 (line 98): Example 6.4.2 等价关系
    """例6.4.2. (1) 回顾在任意集合 $X$ 上定义的相等关系（例6.2.9）。这是一个等价关系。显然，$(x, x) \in R$，因为 $x = x$。然而，对于任何 $x \neq y$，假设 $x \, R \, y$ 是假的，这使得条件语句为真。因此，对称性中唯一"相关的情况"是 $x = y$ 的情况，此时确实也有 $y = x$。类似地，对于传递性，如果 $x \neq y$ 或 $y \neq z$，定义条件语句的假设为假，从而语句本身为真；而当 $x = y$ 且 $y = z$ 时，当然有 $x = z$。这可能看起来不是一个特别有启发性的结论，但很高兴知道我们总能在任何集合上定义至少一个等价关系。""",
]

def main():
    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()

    marker = "> \U0001f1e8\U0001f1f3 TODO: 待翻译"

    parts = content.split(marker)
    if len(parts) - 1 != len(translations):
        print(f"ERROR: Found {len(parts)-1} TODO markers but have {len(translations)} translations")
        sys.exit(1)

    # Rejoin with translations
    result = parts[0]
    for i, trans in enumerate(translations):
        result += "> \U0001f1e8\U0001f1f3 " + trans + parts[i + 1]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"OK: Replaced {len(translations)} TODOs in {FILE}")

if __name__ == "__main__":
    main()
