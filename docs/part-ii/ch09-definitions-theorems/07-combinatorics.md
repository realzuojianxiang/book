---
title: A.7 Combinatorics
---

# A.7 Combinatorics

APPENDIX A. DEFINITIONS AND THEOREMS

A.7.4 Standard Counting Objects

• Cards: A standard deck of cards has 52 cards. Each card has a suit (either $\heartsuit$ or $\diamondsuit$ or $\clubsuit$ or $\spadesuit$) and a rank (either 2 or 3 or 4 or... or 10 or Jack or Queen or King or Ace).
• Tuples: Let $k, n \in \mathbb{N}$. The set $T_{n,k}$ is the set of all $n$-tuples from $[k]$. That is, it is the set of all ordered lists of length $n$ whose coordinates are elements of $[k]$.
• Words: This is equivalent to tuples, where $[k]$ represents the alphabet and $n$ represents the length of a word.
• Lattice Paths: Let $x, y \in \mathbb{N}$. A lattice path to $(x, y)$ is a sequence of points on the grid of natural-numbered points on the plane, starting at $(0, 0)$ and ending at $(x, y)$, where each successive move is either rightwards or upwards. There are $\binom{x+y}{x} = \binom{x+y}{y}$ many lattice paths to $(x, y)$.

A.7.5 Counting In Two Ways

This is a standard method for proving an identity using a combinatorial argument.

Method Outline:
1. State the result to be proven. Note: remember to quantify any variables that appear in the expression!
2. Define a set (let's call it $S$) of objects to be counted.
3. Count the elements of $S$ in one way by following a proper combinatorial argument. Equate the derived expression with $|S|$.
4. Count the elements of $S$ in another way by following a proper combinatorial argument. Equate the derived expression with $|S|$.
5. Conclude that since both derived expressions equal $|S|$, they must be equal, as well.

A.7.6 Results

These were proven in lecture by counting in two ways arguments. (You may cite these results without proof, but it is also helpful to remember the main idea of the counting arguments, as well, so that you can reconstruct the formula without having to just memorize it.)

• Pascal's Identity: $\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$


> 🇨🇳 **A.7.6 结果** 以下结果均由双向计数论证证明。
> - **Pascal 恒等式**：$\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$


• Chairperson Identity: $\binom{n}{k} \cdot k = n \cdot \binom{n-1}{k-1}$
• Binomial Theorem: $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$
• Summation Identity: $\sum_{i=k}^{n} \binom{i}{k} = \binom{n+1}{k+1}$

A.7.7 Inclusion/Exclusion

We have a universal set $U$ and some subsets $A_1, A_2, \ldots, A_n \subseteq U$. We want to count the elements of $U$ that are outside of all the $A_i$ sets.

$|U - A_1| = |U| - |A_1|$

$|U - (A_1 \cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \cap A_2|$

$|U - (A_1 \cup A_2 \cup A_3)| = |U| - |A_1| - |A_2| - |A_3| + |A_1 \cap A_2| + |A_1 \cap A_3| + |A_2 \cap A_3| - |A_1 \cap A_2 \cap A_3|$

and so on. In general, for $n$ many sets, we have $|U - (A_1 \cup A_2 \cup \cdots \cup A_n)| = \sum_{S \subseteq [n]} (-1)^{|S|} \left|\bigcap_{i \in S} A_i\right|$

where $\bigcap_{i \in \emptyset} A_i = U$

In the (convenient) case where the size of the intersection of $k$-many sets only depends on that value $k$ (and not which sets we are intersecting), then we can write $|U - (A_1 \cup A_2 \cup \cdots \cup A_n)| = \sum_{k=0}^{n} (-1)^k \binom{n}{k} |S_1 \cap S_2 \cap \cdots \cap S_k|$

A.7.8 Pigeonhole Principle

If a set $S$ with $|S| = n$ is partitioned into $k$ disjoint subsets whose union is $S$, and if $k < n$, then at least one of the subsets in the partition has more than one element. Furthermore, that part actually has at least $\lceil n/k \rceil$ elements. (That is, if we separate $n$ objects into $k$ piles, there must be one pile with at least $\lceil n/k \rceil$ objects in it.)


> 🇨🇳 - **主席恒等式**：$\binom{n}{k} \cdot k = n \cdot \binom{n-1}{k-1}$
> - **二项式定理**：$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$
> - **求和恒等式**：$\sum_{i=k}^{n} \binom{i}{k} = \binom{n+1}{k+1}$


> 🇨🇳 **A.7.7 容斥原理（Inclusion/Exclusion）** 设全域 $U$ 和子集 $A_1, A_2, \ldots, A_n \subseteq U$，要计 $U$ 中不属于所有 $A_i$ 的元素：
> - $|U - A_1| = |U| - |A_1|$
> - $|U - (A_1 \cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \cap A_2|$
> - $|U - (A_1 \cup A_2 \cup A_3)| = |U| - |A_1| - |A_2| - |A_3| + |A_1 \cap A_2| + |A_1 \cap A_3| + |A_2 \cap A_3| - |A_1 \cap A_2 \cap A_3|$
> - 一般地：$|U - (A_1 \cup \cdots \cup A_n)| = \sum_{S \subseteq [n]} (-1)^{|S|} \left|\bigcap_{i \in S} A_i\right|$（空集交集为 $U$）
> - 当 $k$ 个集合交集大小仅取决于 $k$ 时：$|U - (A_1 \cup \cdots \cup A_n)| = \sum_{k=0}^{n} (-1)^k \binom{n}{k} |S_1 \cap \cdots \cap S_k|$


> 🇨🇳 **A.7.8 鸽巢原理（Pigeonhole Principle）** 若 $|S| = n$ 的集合分成 $k$ 个不相交子集且并集为 $S$，若 $k < n$，则至少一个子集有多于一个元素，实际至少有 $\lceil n/k \rceil$ 个元素（即 $n$ 个物体分 $k$ 堆，必有一堆至少 $\lceil n/k \rceil$ 个）。


APPENDIX A. DEFINITIONS AND THEOREMS

A.8 Acronyms

A.8.1 General Phrases
• WWTS: We want to show
• AFSOC: Assume for sake of contradiction
• WOLOG: Without loss of generality

A.8.2 Induction
• PMI: Principle of Mathematical Induction
• BC: Base case
• IH: Induction hypothesis
• IS: Induction step


> 🇨🇳 **A.8 缩写（Acronyms）**
>
> **A.8.1 通用缩写**
> - WWTS：要证（We want to show）
> - AFSOC：反证假设（Assume for sake of contradiction）
> - WOLOG：不失一般性（Without loss of generality）
>
> **A.8.2 归纳法缩写**
> - PMI：数学归纳法原理（Principle of Mathematical Induction）
> - BC：基例（Base case）
> - IH：归纳假设（Induction hypothesis）
> - IS：归纳步（Induction step）

