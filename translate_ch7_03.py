#!/usr/bin/env python3
"""Translate ch07/03-images-and-preimages.md — 32 TODO items."""

import re

FILE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-ii\ch07-functions-cardinality\03-images-and-preimages.md"

translations = [
    # 1 — section heading "7.3. IMAGES AND PRE-IMAGES"
    "7.3 像与原像（Images and Pre-images）",

    # 2 — after Example 7.3.2 definition, before image list
    "以下是对函数 $g$ 的各种子集求像的结果：",

    # 3 — section break, between pages
    "接下来我们看一个需要通过双重包含论证来证明像的例子。",

    # 4 — before "to ImF(C)" text, double containment argument
    "我们要证明 $S = \operatorname{Im}_F(C)$，这等价于证明 $S \subseteq \operatorname{Im}_F(C)$ 且 $\operatorname{Im}_F(C) \subseteq S$。",

    # 5 — "+ 32 = 212" part of the proof
    "由此可知 $F(0) = 0 + 32 = 32$，$F(100) = \frac{9}{5} \cdot 100 + 32 = 212$。注意我们使用了严格不等号「$<$」，因为事实上 $0 \notin C$（定义域）。",

    # 6 — "F(x) = 95x + 32" in proof
    "由函数 $F$ 的定义，我们知道 $F(x) = \frac{9}{5}x + 32$。由于两边同乘正数并加上正数保持不等式方向，我们可以推导出",

    # 7 — inequality manipulation in proof
    "$\frac{9}{5} \cdot 0 + 32 < F(x) < \frac{9}{5} \cdot 100 + 32$，化简可得 $32 < F(x) < 212$。",

    # 8 — algebraic manipulation in proof (second half)
    "我们观察到 $F(c) = \frac{9}{5}c + 32 = \frac{9}{5} \cdot \frac{5}{9}(s-32) + 32 = (s-32) + 32 = s$。这表明 $s \in \operatorname{Im}_F(C)$。",

    # 9 — section break, between pages
    "和求解等式来寻找候选值 $c$。这个函数是线性的，所以这个过程只会产生一个这样的 $s$，但一般而言，可能有多个 $s$ 的值满足条件。",

    # 10 — "and solve the equality for c" continuation
    "最终我们只需要一个可行的值来完成证明的这一部分，所以可以选择任何一个有效的值。有时这使得寻找这样的值更加困难。",

    # 11 — before "Define the set T" in Example 7.3.4
    "定义集合 $T = \{y \in \mathbb{R} \mid 0 \leq y < 1\}$，我们声称 $T = \operatorname{Im}_f(\mathbb{R})$。",

    # 12 — in proof, inequality step x^2/(1+x^2)
    "由于 $x \in \mathbb{R}$，我们知道 $x^2 \geq 0$ 且 $0 < x^2 + 1$，从而 $0 < \frac{x^2}{x^2+1}$；又因为 $0 \leq x^2 < x^2 + 1$，所以 $\frac{x^2}{1+x^2} < 1$。",

    # 13 — in proof, T ⊆ Imf(R) second part
    "我们声称 $x = \sqrt{\frac{y}{1-y}}$ 可行。注意 $y \geq 0$，且 $y < 1$ 意味着 $-y > -1$，即 $1-y > 0$。因此 $\frac{y}{1-y} \geq 0$，从而 $x \in \mathbb{R}$ 有明确定义，且 $x$ 属于定义域 $\mathbb{R}$。",

    # 14 — section break, between pages
    "接下来注意到 $x^2 = \frac{y}{1-y}$，因此 $f(x) = \frac{x^2}{1+x^2} = \frac{\frac{y}{1-y}}{1+\frac{y}{1-y}} = \frac{y}{(1-y)+y} = y$。",

    # 15 — in proof, fraction simplification
    "$\frac{y}{1-y} \cdot \frac{1-y}{1-y} = \frac{y}{1}$。化简得 $f(x) = y$，这证明了 $y \in \operatorname{Im}_f(\mathbb{R})$。",

    # 16 — "= 1-y · 1-y" in proof
    "$= y$。这表明 $y \in \operatorname{Im}_f(\mathbb{R})$，因此 $T \subseteq \operatorname{Im}_f(\mathbb{R})$。综合两方面，由双重包含证明，我们得出 $T = \operatorname{Im}_f(\mathbb{R})$。",

    # 17 — before table in Example 7.3.5
    "下表列出了函数 $p$ 的一些值，其中左列表示 $a$ 的值，顶行表示 $b$ 的值，表格中的条目是 $p(a,b)$ 的值：",

    # 18 — "given" in proof
    "设这样的 $(a,b)$ 被给定。这意味着 $n = ab + a$。由于 $a, b \geq 1$，则 $ab \geq 1$，于是 $n = ab + a \geq 2$。",

    # 19 — section break, Imf(S)∩Imf(T) ⊄ Imf(S∩T)
    "为什么我们没有声称等式成立？事实上等式不一定成立！存在至少一个函数，使得反向包含——即 $\operatorname{Im}_f(S) \cap \operatorname{Im}_f(T) \subseteq \operatorname{Im}_f(S \cap T)$——为假。",

    # 20 — "We will use a schematic diagram"
    "我们将使用示意图来构造一个具有所需性质的例子。然后我们将用形式化的方式定义函数并陈述其性质。我们要指出，采用这种技巧是完全合理的，只要你之后写出形式化的定义。",

    # 21 — "⋆ Now, just to have a definition..."
    "现在，为了有一个定义在手，我们选择 $S = \{1, 2\}$。同时，我们应该使 $f(1) \neq f(2)$。否则 $\operatorname{Im}_f(S)$ 将只包含一个元素，让 $S$ 有两个元素就失去了意义。",

    # 22 — "⋆ S Imf(S)" schematic
    "现在我们需要选择 $T$。让 $S \cap T \neq \emptyset$ 会比较有趣，但如果 $T \supseteq S$ 可能太难处理。所以我们设 $T = \{2, 3\}$。然后只需选择 $f(3)$。",

    # 23 — "⋆ S Imf(S) T Imf(T) = Imf(S∩T)"
    "令 $f(3) = f(1) = \star$ 看起来可行！我们使得 $\operatorname{Im}_f(S) \cap \operatorname{Im}_f(T)$ 是 $\operatorname{Im}_f(S \cap T)$ 的严格超集。",

    # 24 — section break, before formal proof
    "回顾我们的构造过程，理解我们的思考过程。有哪些约束必须遵守？哪些地方我们有选择的自由？我们做了什么决定？请注意这绝对不是唯一的例子，试着想出其他的！",

    # 25 — "We have now seen an example..."
    "我们现在已经看到了如何证明关于任意函数和像的命题，以及如何构造特定的反例来推翻一个命题。在练习中，你将需要解决类似的问题。",

    # 26 — "### 7.3.3 Pre-Image" section header
    "### 7.3.3 原像（Pre-image）：定义与例子 你现在可能有一个自然的问题：反过来呢？我们能否取陪域的一个子集，找出那些输出"落在"该集合中的元素？当然可以！下面的定义给出了这个概念的术语。",

    # 27 — Examples with pre-images
    "以下是一些原像的例子，使用与上一节相同的函数 $g$：",

    # 28 — section break
    "以下是更多原像的例子：",

    # 29 — pre-image examples list
    "(1) $\operatorname{PreIm}_f(\{1\}) = \{-1, 1\}$ (2) $\operatorname{PreIm}_f(\{y \in \mathbb{R} \mid y < 0\}) = \emptyset$ (3) $\operatorname{PreIm}(\{y \in \mathbb{R} \mid y \geq 0\}) = \mathbb{R}$ (4) $\operatorname{PreIm}(\{y \in \mathbb{R} \mid 0 < y < 1\}) = \{x \in \mathbb{R} \mid -1 < x < 1\}$",

    # 30 — after proof about Pre-images
    "如果你在解决问题时卡住了，或者不确定从哪里开始……就把相关的定义写下来。试着将它们应用到你想要证明的命题上。看看会发生什么！",

    # 31 — Exercises section
    "### 7.3.5 问题与练习 **提醒自己** 简要回答以下问题：(1) 像与原像有什么区别？(2) 设 $f: A \to B$ 是函数，$\operatorname{PreIm}_f(B)$ 是什么？(3) 设 $g: \mathbb{R} \to \mathbb{R}$ 是函数，为什么表达式 $\operatorname{Im}_g(0)$ 不是一个正确的陈述？",

    # 32 — end, "### 7.4 Properties of Functions"
    "## 7.4 函数的性质 你可能已经注意到了一个有趣的事情：如果我们能确定给定函数的定义域的像，为什么还要设一个比该集合更大的陪域呢？",
]


def main():
    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Count how many TODO items
    count = content.count("> 🇨🇳 TODO: 待翻译")
    print(f"Found {count} TODO items, expected 32")

    # Replace each in order
    for i, tr in enumerate(translations, 1):
        old = "> 🇨🇳 TODO: 待翻译"
        new = f"> 🇨🇳 {tr}"
        content = content.replace(old, new, 1)

    # Verify
    remaining = content.count("> 🇨🇳 TODO: 待翻译")
    print(f"Remaining TODO items: {remaining}")

    if remaining == 0:
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("File written successfully")
    else:
        print("ERROR: Not all TODOs were replaced!")


if __name__ == "__main__":
    main()
