---
title: A.1 Sets
---

# A.1 Sets

Appendix A
Definitions and Theorems
A.1 Sets A.1.1 Standard Sets • The natural numbers are N = {1, 2, 3, 4, 5,... }
Note: 0 $\notin \mathbb{N}$.
• For every n $\in \mathbb{N}$, the set [n] ("brackets n") is defined by [n] = {x $\in \mathbb{N}$ | 1 $\leq x$ $\leq n$} = {1, 2, 3,..., n} • The integers are Z = {..., -3, -2, -1, 0, 1, 2, 3,... } • The rational numbers are Q = n x $\in \mathbb{R}$ | $\exists a$, b $\in \mathbb{Z}$. b \neq 0 and a b = x o • The real numbers are denoted by R. Every real number is either rational or irrational. • The empty set is the set that has no elements. We write it as \emptyset or { }. A.1.2 Set-Builder Notation • If U is a set and P(x) is some property that either does or does not hold for any given x, then we can always define a new set by writing S = {x $\in U$ | P(x) holds} • This is called set-builder notation. It is essential to identify the universal set U and the property P(x).


> **A.1.3 元素与子集（Elements and Subsets）**
>
> - 说"$x$ 是集合 $S$ 的元素（Element）"，我们写作 $x \in S$；说"$x$ 不是集合 $S$ 的元素"，我们写作 $x \notin S$。
> - 说"$S$ 是 $T$ 的子集（Subset）"，我们写作 $S \subseteq T$。这由条件语句定义："$S$ 的每个元素也是 $T$ 的元素"。


APPENDIX A. DEFINITIONS AND THEOREMS A.1.3 Elements and Subsets • To say "x is an element of the set S" we write x $\in S$ To say "x is not an element of the set S" we write x \notin S • To say "S is a subset of T" we write S \subseteq T This is defined by the conditional statement "Every element of S is also an element of T". This can be expressed as \forall x \in U. x \in S =$\Rightarrow x$ \in T That is, for every element x of the universal set (supposing S, T \subseteq U), whenever x \in S, we also know that x \in T. • To prove that a set is a subset of another set, like S \subseteq T, we need to do something like this: Let x \in S be arbitrary and fixed.... blah blah blah... Therefore, x \in T, as well. This shows S \subseteq T. • To say "S is a proper subset of T" we write S \subset T This means S \subseteq T and S \neq T. • It is true that $\emptyset \subseteq S$, for any set S. • It is true that S \subseteq S, for any set S. A.1.4 Power Set • Let S be a set. The power set of S is denoted by P(S) and is defined by P(S) = {A | A \subseteq S} That is, P(S) is the set of all subsets of S. • It is true that $\emptyset \in P(S) and S \in P$(S), for any set S.


> 🇨🇳 证明 $S \subseteq T$ 的方法：任取 $x \in S$ 为任意且固定的，推导出 $x \in T$，由此得 $S \subseteq T$。说"$S$ 是 $T$ 的**真子集（Proper Subset）**"写作 $S \subset T$，即 $S \subseteq T$ 且 $S \neq T$。对任意集合 $S$，有 $\emptyset \subseteq S$ 且 $S \subseteq S$。
>
> **A.1.4 幂集（Power Set）** 集合 $S$ 的幂集记为 $\mathcal{P}(S) = \{A \mid A \subseteq S\}$，即 $S$ 的所有子集的集合。对任意集合 S，有 $\emptyset \in \mathcal{P}(S)$ 且 $S \in \mathcal{P}(S)$。


A.1.5 Set Equality • To say "S and T are equal sets", we write S = T. This is defined by S = T if and only if S $\subseteq T and T \subseteq S$ • To prove two sets are equal, like S = T, we need to do something like this: First, we will prove S $\subseteq T. Let x \in S$ be arbitrary and fixed.... blah blah blah... Therefore, x $\in T. This shows S \subseteq T$. Second, we will prove T $\subseteq S. Let y \in T$ be arbitrary and fixed.... blah blah blah... Therefore, x $\in S. This shows T \subseteq S$. Therefore, S = T. This is known as a double-containment argument. A.1.6 Set Operations Suppose S, T, U are sets and S $\subseteq U and T \subseteq U$. • The union of two sets is defined by S \cup T = {x \in U | x $\in S or x \in T$} It is the set of all elements that belong to at least one of the two sets, S and T. • The intersection of two sets is defined by S \cap T = {x \in U | x $\in S and x \in T$} It is the set of all elements that belong to both sets, S and T. • The difference of two sets is defined by S -T = {x \in U | x \in S and x \notin T} It is the set of all elements of S that are not elements of T. • The complement of a set is defined by S = {x \in U | x \notin S} = U -S It is the set of all elements of the universal set that are not elements of S. • $The Cartesian product of two sets is defined by S \times T = {(x, y)$ | x \in S and y $\in T$} It is the set of all ordered pairs, where the first coordinate is an element of S and the second coordinate is an element of T.


> 🇨🇳 **A.1.5 集合相等（Set Equality）** $S = T$ 当且仅当 $S \subseteq T$ 且 $T \subseteq S$。证明集合相等采用**双向包含论证（Double-Containment Argument）**：先证 $S \subseteq T$——任取 $x \in S$，推出 $x \in T$；再证 $T \subseteq S$——任取 $y \in T$，推出 $y \in S$。
>
> **A.1.6 集合运算（Set Operations）** 设 $S, T \subseteq U$。**并集（Union）**：$S \cup T = \{x \in U \mid x \in S \text{ 或 } x \in T\}$，属于 $S$ 或 $T$ 的所有元素。**交集（Intersection）**：$S \cap T = \{x \in U \mid x \in S \text{ 且 } x \in T\}$，同时属于 $S$ 和 $T$ 的所有元素。**差集（Difference）**：$S - T = \{x \in U \mid x \in S \text{ 且 } x \notin T\}$，属于 $S$ 但不属于 $T$ 的元素。**补集（Complement）**：$\overline{S} = \{x \in U \mid x \notin S\} = U - S$，不属于 $S$ 的所有元素。**笛卡尔积（Cartesian Product）**：$S \times T = \{(x, y) \mid x \in S \text{ 且 } y \in T\}$，所有有序对的集合。


APPENDIX A. DEFINITIONS AND THEOREMS A.1.7 Indexed Set Operations Suppose I is an index set and U is a universal set, and we have defined (for every i $\in I) some sets Ai \subseteq U$. • The indexed union of all of the Ai sets is defined by [ i\in I Ai = {x \in U | $\exists k \in I. x \in A$k} It is the set of all elements x in the universal set such that x is an element of at least one of the indexed sets in the union. • The indexed intersection of all of the Ai sets is defined by \ i$\in I Ai = {x \in U$ | $\forall i \in I$. x $\in A$i} It is the set of all elements x in the universal set such that x is an element of all of the indexed sets in the intersection. A.1.8 Partition • Let S be a set. A partition of S is a collection of sets that are pairwise disjoint and whose union is S. That is, a partition is formed by an index set I and non-empty sets Si (defined for every i \in I) that satisfy: -- \forall i \in I. Si \neq \emptyset -- \forall i \in I. Si \subseteq S -- \forall i, j \in I. i \neq j =$\Rightarrow Si \cap Sj = \emptyset -- [ i\in I$ Si = S


> 🇨🇳 **A.1.7 指标集运算（Indexed Set Operations）** 设 $I$ 为指标集，$U$ 为全集，对每个 $i \in I$ 定义 $A_i \subseteq U$。**指标并集**：$\bigcup_{i \in I} A_i = \{x \in U \mid \exists k \in I.\, x \in A_k\}$，至少属于一个 $A_k$ 的所有元素。**指标交集**：$\bigcap_{i \in I} A_i = \{x \in U \mid \forall i \in I.\, x \in A_i\}$，属于所有 $A_i$ 的元素。
>
> **A.1.8 划分（Partition）** 集合 $S$ 的划分是一组两两不交且并集为 S 的集合。即由指标集 I 和非空集合 $S_i$（$i \in I$）组成，满足：(1) $\forall i \in I.\, S_i \neq \emptyset$；(2) $\forall i \in I.\, S_i \subseteq S$；(3) $\forall i, j \in I.\, i \neq j \Rightarrow S_i \cap S_j = \emptyset$；(4) $\bigcup_{i \in I} S_i = S$。


A.2 Logic A.2.1 Statements and Propositions • True and False are the only two truth values we consider. • A mathematical statement (or logical statement) is a grammaticallycorrect sentence that has exactly one truth value. • A variable proposition is a grammatically-correct sentence that involves one or more variables, such that it acquires exactly one truth value whenever a value(s) for the variable(s) is assigned. • When we define a statement or proposition, we assign it a letter name, indicate any dependence on variables (as well as assigning them letters), and enclose the actual statement/proposition within quotation marks. Here are two good examples: Define P to be "Every real number x satisfies x2 $\geq$0". Define Q(x, y) to be " xy $\leq$ { x+y


> 🇨🇳 T **A.2 逻辑（Logic）**
>
> **A.2.1 命题与陈述（Statements and Propositions）**
>
> - 只考虑真和假两种真值。
> - **数学命题**是一个语法正确的句子，具有唯一的真值。
> - **变量命题**是含一个或多个变量的语法正确的句子，对变量赋值后获得唯一真值。
> - 定义命题时赋予字母名称，标明变量依赖，将命题放在引号内。例如：定义 $ 为"每个实数 $ 满足 $^2 \geq 0 "；定义 (x,y)$ 为" $\leq$ rac{x+y}{2}$，对一切,y \in \mathbb{R}$"。
> - **排中律**：每个命题要么为真要么为假，且恰好一种成立。

}2 ", for every x, y $\in \mathbb{R}$. • The Law of the Excluded Middle is our assumption that every statement is either True or False. It states that, when we have a statement P, we are guaranteed that either P is True or P is False, and only one of those cases holds. A.2.2 Quantifiers • To say "for every" or "for all" we use the universal quantifier \forall "\forall x \in S. P(x)" says that "For every element x \in S, the property P(x) holds true". • To say "there exists" or "there is at least one" we use the existential quantifier \exists "\exists x \in S. P(x)" says that "There exists an element x \in S with the property P(x)". • We use the ". " dot to separate parts of a quantified statement. • When reading a quantified statement out loud, we say "such that" only after a \exists quantifier. • We use "!" to indicate that existence is unique; that is, the claim "\exists! x \in S. P(x)" says that "There exists an element x $\in S$ with property P(x), and there is exactly one such x".


> 🇨🇳 T **A.2.2 量词（Quantifiers）**
>
> - **全称量词**$orall$表示"对每一个"。"$orall x \in S.\, P(x)$"即"对 $ 中每个元素 $，(x)$ 成立"。
> - **存在量词**$\exists$表示"存在"。"$\exists x \in S.\, P(x)$"即"存在 $ 中的元素 $ 使 (x)$ 成立"。
> - 用"."点号分隔量词语句的各部分。
> - 读出量词语句时，"such that"仅在 $\exists$ 量词之后使用。
> - 用"!"表示唯一存在："$\exists!\, x \in S.\, P(x)$"即"存在唯一的 $\in S 使 (x)$ 成立"。

