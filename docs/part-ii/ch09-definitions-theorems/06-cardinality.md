---
title: A.6 Cardinality
tags:
  - 定义速查
  - 定理速查
---

# A.6 Cardinality

A.6. CARDINALITY


> 🇨🇳 **有限集（Finite Sets）**
> - 若 $A$、$B$ 有限，则 $A \cup B$ 有限。
> - 若 $A$、$B$ 有限且 $A \cap B = \emptyset$，则 $|A \cup B| = |A| + |B|$。
> - 若 $A$、$B$ 有限，则 $|A \times B| = |A| \cdot |B|$。
>
> **无限集（Infinite Sets）**
> - 若 $A$ 可数无限且 $B$ 有限或可数无限，则 $A \cup B$ 可数无限。
> - 若 $A$ 可数无限且 $B$ 有限或可数无限，则 $A \times B$ 可数无限。
> - 若 $A$ 不可数无限且 $B$ 为任意集合，则 $A \cup B$ 不可数无限。
> - 若 $A$ 不可数无限且 $B$ 为任意集合，则 $A \times B$ 不可数无限。
> - 若 $A \subseteq B$，则 $|A| \leq |B|$（有限与无限均适用）。
> - 对任意集合 $A$，$|A| < |\mathcal{P}(A)|$（有限与无限均适用！）。
> - 若 $A$ 无限，则存在 $C \subseteq A$ 使 $C$ 可数无限。
> - $A$ 无限 $\Leftrightarrow$ $\exists C \subset A$（真子集）使存在双射 $f: A \to C$。
> - 可数无限个可数无限集的并仍可数无限。
> - 可数无限个有限集的笛卡尔积不可数无限。
> - **Cantor-Schröder-Bernstein 定理**：若存在单射 $f: A \to B$ 和单射 $g: B \to A$，则存在双射 $h: A \to B$，故 $|A| = |B|$。

Finite Sets
• If $A$ and $B$ are finite, then $A \cup B$ are finite.
• If $A$ and $B$ are finite and $A \cap B = \emptyset$, then $|A \cup B| = |A| + |B|$.
• If $A$ and $B$ are finite, then $|A \times B| = |A| \cdot |B|$.

Infinite Sets
• If $A$ is countably infinite and $B$ is finite or countably infinite, then $A \cup B$ is countably infinite.
• If $A$ is countably infinite and $B$ is finite or countably infinite, then $A \times B$ is countably infinite.
• If $A$ is uncountably infinite and $B$ is any set, then $A \cup B$ is uncountably infinite.
• If $A$ is uncountably infinite and $B$ is any set, then $A \times B$ is uncountably infinite.
• If $A \subseteq B$, then $|A| \leq |B|$. (Note: this applies to both finite and infinite sets.)
• $|A| < |\mathcal{P}(A)|$ for any set $A$. (Note: this applies to both finite and infinite sets!)
• If $A$ is infinite, then there exists a set $C \subseteq A$ that is countably infinite.
• $A$ is infinite $\Leftrightarrow$ $\exists C \subset A$ such that there exists a bijection $f: A \to C$. (Note the strict subset inequality.)
• A countably infinite union of countably infinite sets is also countably infinite.
• A countably infinite product of finite sets is uncountably infinite. (Notice that this shows that a countably infinite product of any non-empty sets is uncountably infinite.)
• Cantor-Schröder-Bernstein Theorem: Suppose $A$ and $B$ are sets and there exist functions $f: A \to B$ and $g: B \to A$ that are both injections. Then there actually exists a bijection $h: A \to B$ so, in particular, $|A| = |B|$.


> 🇨🇳 **A.6.3 标准基数目录**
>
> **有限集**：$\emptyset$；$[n]$（$n \in \mathbb{N}$）。
>
> **可数无限集**：$\mathbb{N}$；$\mathbb{Z}$；奇/偶自然数与整数；$\mathbb{Q}$；$\mathbb{N} \times \mathbb{N}$；所有有限二进制字符串的集合。
>
> **不可数无限集**：$\mathbb{R}$；$\mathbb{R}$ 的区间（如 $\{y \in \mathbb{R} \mid a \leq y \leq b\}$，$\leq$ 可换为 $<$）；$\mathcal{P}(\mathbb{N})$；$\mathcal{P}(\mathbb{Z})$；所有无限二进制字符串的集合。


APPENDIX A. DEFINITIONS AND THEOREMS A.6.3 Standard Catalog of Cardinalities

• Finite sets:
-- $\emptyset$
-- $[n]$, for any $n \in \mathbb{N}$

• Countably Infinite sets:
-- $\mathbb{N}$
-- $\mathbb{Z}$
-- Odd naturals/integers, Even naturals/integers
-- $\mathbb{Q}$
-- $\mathbb{N} \times \mathbb{N}$
-- The set of all finite binary strings

• Uncountably Infinite sets:
-- $\mathbb{R}$
-- Intervals of $\mathbb{R}$; that is, $\{y \in \mathbb{R} \mid a \leq y \leq b\}$ for any $a, b \in \mathbb{R}$. (Note: the "$\leq$" in the interval can each be replaced by "$<$" as well.)
-- $\mathcal{P}(\mathbb{N})$
-- $\mathcal{P}(\mathbb{Z})$
-- The set of all infinite binary strings


> 🇨🇳 **A.7 组合数学（Combinatorics）**
>
> **A.7.1 定义**
> - $[n]$ 的**排列（Permutation）**是双射 $f: [n] \to [n]$。
> - $[n]$ 的 **$k$-选取（k-Selection）**是子集 $S \subseteq [n]$ 且 $|S| = k$。
> - $[n]$ 的 **$k$-排列（k-Arrangement）**是 $[n]$ 中 $k$ 个不重复元素的有序列表。
> - $[n]$ 的**可重复 $k$-选取**是 $[n]$ 中 $k$ 个元素的无序列表（元素可重复）。
> - $[n]$ 的**可重复 $k$-排列**是 $[n]$ 中 $k$ 个元素的有序列表（元素可重复）。


A.7. COMBINATORICS


> 🇨🇳 **A.7.2 计数原理**
> - **求和法则（Rule of Sum）**：设 $A$ 为有限集，$\{S_i \mid i \in [n]\}$ 为 $A$ 的划分，则 $|A| = \sum_{i=1}^{n} |S_i|$。
> - **乘积法则（Rule of Product）**：设过程分 $n$ 步完成，第 $i$ 步有 $w_i$ 种选择（与前步无关），则结果数为 $\prod_{i=1}^{n} w_i$。
>
> **A.7.3 公式**
> - $[n]$ 的排列数为 $n!$。
> - $[n]$ 的 $k$-选取数为 $\binom{n}{k} = \frac{n!}{k!(n-k)!}$。
> - $[n]$ 的 $k$-排列数为 $\binom{n}{k} k! = \frac{n!}{(n-k)!}$。
> - $[n]$ 的可重复 $k$-选取数为 $\binom{k+n-1}{k}$。
> - $[n]$ 的可重复 $k$-排列数为 $n^k$。


A.7.1 Definitions

• A permutation of the set $[n]$ is a bijection $f: [n] \to [n]$.
• A $k$-selection from the set $[n]$ is a subset $S \subseteq [n]$ with $|S| = k$.
• A $k$-arrangement from the set $[n]$ is an ordered list of $k$ elements of $[n]$, where no element is repeated.
• A $k$-selection with repetition from the set $[n]$ is an unordered list of $k$ elements of $[n]$, where elements can repeat.
• A $k$-arrangement with repetition from the set $[n]$ is an ordered list of $k$ elements of $[n]$, where elements can repeat.

A.7.2 Counting Principles

• Rule Of Sum: Let $A$ be a finite set. Let $n \in \mathbb{N}$. Suppose $\{S_i \mid i \in [n]\}$ is a partition of $A$. Then $|A| = \sum_{i=1}^{n} |S_i| = |S_1| + |S_2| + \cdots + |S_n|$
• Rule Of Product: Suppose we have a process that is completed in $n$ steps. Suppose that step $i$ (where $1 \leq i \leq n$) can be completed in $w_i$ ways, independent of the choices made in the previous step. Then the number of outcomes of this process is $\prod_{i=1}^{n} w_i = w_1 \cdot w_2 \cdots w_n$

A.7.3 Formulas

• There are $n!$ many permutations of $[n]$.
• There are $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ many $k$-selections from $[n]$.
• There are $\binom{n}{k} k! = \frac{n!}{(n-k)!}$ many $k$-arrangements from $[n]$.
• There are $\binom{k+n-1}{k}$ many $k$-selections with repetition from $[n]$.
• There are $n^k$ many $k$-arrangements with repetition from $[n]$.


> 🇨🇳 **A.7.4 标准计数对象**
> - **扑克牌**：标准牌组 52 张，每张有花色（$\heartsuit$、$\diamondsuit$、$\clubsuit$、$\spadesuit$）和面值（2–10、J、Q、K、A）。
> - **元组**：$T_{n,k}$ 是 $[k]$ 上所有 $n$-元组的集合。
> - **单词**：等价于元组，$[k]$ 为字母表，$n$ 为词长。
> - **格点路径（Lattice Path）**：从 $(0,0)$ 到 $(x,y)$ 的格点路径，每步向右或向上，共有 $\binom{x+y}{x}$ 条。
>
> **A.7.5 双向计数（Counting In Two Ways）** 证明恒等式的组合方法：(1) 陈述待证结果；(2) 定义计数对象集 $S$；(3) 用一种方式计数得表达式 = $|S|$；(4) 用另一种方式计数得另一表达式 = $|S|$；(5) 两个表达式相等。
>
> **A.7.6 结果**
> - **Pascal 恒等式**：$\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$。
> - **主席恒等式**：$\binom{n}{k} \cdot k = n \cdot \binom{n-1}{k-1}$。
> - **二项式定理**：$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$。
> - **求和恒等式**：$\sum_{i=k}^{n} \binom{i}{k} = \binom{n+1}{k+1}$。
>
> **A.7.7 容斥原理（Inclusion/Exclusion）** 设全域 $U$ 和子集 $A_1, \ldots, A_n \subseteq U$：
> - $|U - A_1| = |U| - |A_1|$
> - $|U - (A_1 \cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \cap A_2|$
> - 一般地：$|U - (A_1 \cup \cdots \cup A_n)| = \sum_{S \subseteq [n]} (-1)^{|S|} \left|\bigcap_{i \in S} A_i\right|$（空交集为 $U$）
> - 当 $k$ 个集合交集的大小仅取决于 $k$ 时：$|U - (A_1 \cup \cdots \cup A_n)| = \sum_{k=0}^{n} (-1)^k \binom{n}{k} |S_1 \cap \cdots \cap S_k|$
>
> **A.7.8 鸽巢原理（Pigeonhole Principle）** 若 $|S| = n$ 个元素分成 $k$ 个不相交子集且 $k < n$，则至少一个子集有多于一个元素，实际至少有 $\lceil n/k \rceil$ 个元素。
>
> **A.8 缩写（Acronyms）**
> - **通用**：WWTS（要证）、AFSOC（反证假设）、WOLOG（不失一般性）
> - **归纳法**：PMI（数学归纳法原理）、BC（基例）、IH（归纳假设）、IS（归纳步）

