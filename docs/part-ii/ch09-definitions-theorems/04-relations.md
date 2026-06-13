---
title: A.4 Relations
tags:
  - 定义速查
  - 定理速查
---

# A.4 Relations

• If $R$ is an equivalence relation and $x \in A$, then the equivalence class corresponding to $x$ (under the relation $R$) is $[x]_R = \{y \in A \mid (x, y) \in R\}$ which is the set of all elements related to $x$.
• If $R$ is an equivalence relation, then $A/R$ is $A$ modulo $R$; it is the set of all equivalence classes: $A/R = \{[x]_R \mid x \in A\}$.
• Theorem: If $R$ is an equivalence relation on $A$, then the equivalence classes (i.e. the elements of $A/R$) form a partition of $A$.
• Theorem: If $I$ is some index set and $\{S_i \mid i \in I\}$ is a partition of $A$, then this corresponds to a unique equivalence relation on $A$ defined by relating two elements of $A$ if and only if they belong to the same part of the partition.


> 🇨🇳 • 若 $R$ 是等价关系（Equivalence Relation）且 $x \in A$，则 $x$ 在关系 $R$ 下对应的等价类（Equivalence Class）为 $[x]_R = \{y \in A \mid (x, y) \in R\}$，即所有与 $x$ 相关的元素组成的集合。• 若 $R$ 是等价关系，则 $A/R$ 是 $A$ 模 $R$ 的商集；它是所有等价类的集合：$A/R = \{[x]_R \mid x \in A\}$。• 定理：若 $R$ 是 $A$ 上的等价关系，则等价类（即 $A/R$ 的元素）构成 $A$ 的一个划分（Partition）。• 定理：若 $I$ 是某个指标集且 $\{S_i \mid i \in I\}$ 是 $A$ 的一个划分，则这对应于 $A$ 上的唯一一个等价关系，定义为当且仅当 $A$ 的两个元素属于划分的同一部分时它们是相关的。


APPENDIX A. DEFINITIONS AND THEOREMS

A.4.3 Modular Arithmetic

Congruence mod $n$

• Let $n \in \mathbb{N}$ be given. For any $x, y \in \mathbb{Z}$, we say $x$ and $y$ are congruent modulo $n$ if and only if $n \mid x - y$. Equivalently, this means that $x$ and $y$ have the same remainder upon division by $n$. (This equivalence is not part of the definition; rather, it follows from the Division Lemma stated below.) We write this as $x \equiv y \pmod{n}$. (Note: mod $n$ is not an operator or function; it is a modifier we place at the end of a line of arithmetic/algebra to indicate that all the operations have been performed modulo $n$.)
• The relation $\equiv$ is an equivalence relation, for every $n \in \mathbb{N}$.
• Division Lemma: Let $n \in \mathbb{N}$ be given. Let $x \in \mathbb{Z}$ be given. Then $\exists!\, k, r \in \mathbb{Z}$ such that $(x = kn + r) \wedge (0 \leq r \leq n-1)$. Notice that "$\exists!$" indicates this representation of $x$ as a multiple of $n$ plus a remainder is unique.
• Modular Arithmetic Lemma: Let $n \in \mathbb{N}$ be given. Let $a, b \in \mathbb{Z}$ be given. Suppose that $a \equiv r \pmod{n}$ and $b \equiv s \pmod{n}$. Then, $a + b \equiv r + s \pmod{n}$ and $a \cdot b \equiv r \cdot s \pmod{n}$.

Multiplicative Inverses in $\mathbb{Z}$ mod $n$

• Let $x, y \in \mathbb{Z}$ be given. We say $x$ and $y$ are relatively prime if and only if they have no common factors (divisors), other than 1.
• MIRP Lemma: (Multiplicative Inverses for Relative Primes) Suppose $n \in \mathbb{N}$ and $a \in \mathbb{Z}$, and that $a$ and $n$ are relatively prime. Consider the congruence $ax \equiv 1 \pmod{n}$. Then there exists a solution $x$ to this congruence. (In fact, there are infinitely-many solutions to this congruence, and they are all congruent modulo $n$.)
• When $ax \equiv 1 \pmod{n}$, we say $x$ is the multiplicative inverse of $a$ in the context of $\mathbb{Z}$ modulo $n$. We write this as $x \equiv a^{-1} \pmod{n}$. In fact, any integer $y$ congruent to $x$ modulo $n$ will satisfy $ay \equiv 1 \pmod{n}$, so we really consider the equivalence class $[x]_{\bmod{n}}$ to be the multiplicative inverse of the equivalence class $[a]_{\bmod{n}}$.


> 🇨🇳 附录 A. 定义与定理 A.4.3 模运算（Modular Arithmetic） 模 $n$ 同余（Congruence mod $n$）
> • 给定 $n \in \mathbb{N}$。对任意 $x, y \in \mathbb{Z}$，当且仅当 $n \mid x - y$ 时，我们说 $x$ 与 $y$ 模 $n$ 同余。等价地，这意味着 $x$ 和 $y$ 除以 $n$ 时有相同的余数。（这个等价关系不是定义的一部分；而是由下文所述的除法定理推出的。）我们将其写作 $x \equiv y \pmod{n}$。（注：mod $n$ 不是运算符或函数；它是一个修饰语，我们放在一行算术/代数运算的末尾，以表明所有运算都是在模 $n$ 意义下进行的。）
> • 关系 $\equiv$ 对每个 $n \in \mathbb{N}$ 都是一个等价关系。
> • 除法定理（Division Lemma）：给定 $n \in \mathbb{N}$。给定 $x \in \mathbb{Z}$。则 $\exists!\, k, r \in \mathbb{Z}$，使得 $(x = kn + r) \wedge (0 \leq r \leq n - 1)$。注意 $\exists!$ 表示将 $x$ 表示为 $n$ 的倍数加余数的方式是唯一的。
> • 模运算定理：给定 $n \in \mathbb{N}$。给定 $a, b \in \mathbb{Z}$。假设 $a \equiv r \pmod{n}$ 且 $b \equiv s \pmod{n}$。则 $a + b \equiv r + s \pmod{n}$，且 $a \cdot b \equiv r \cdot s \pmod{n}$。
>
> $\mathbb{Z}$ mod $n$ 中的乘法逆元（Multiplicative Inverse）
> • 给定 $x, y \in \mathbb{Z}$。当且仅当 $x$ 和 $y$ 除 1 外没有公因子（因子）时，我们说 $x$ 与 $y$ 互素（Relatively Prime）。
> • MIRP 引理（互素的乘法逆元）：假设 $n \in \mathbb{N}$，$a \in \mathbb{Z}$，且 $a$ 与 $n$ 互素。考虑同余方程 $ax \equiv 1 \pmod{n}$。则该同余方程存在解 $x$。（事实上，该同余方程有无穷多个解，且它们都模 $n$ 同余。）
> • 当 $ax \equiv 1 \pmod{n}$ 时，我们说 $x$ 是 $a$ 在 $\mathbb{Z}$ 模 $n$ 语境下的乘法逆元。我们写作 $x \equiv a^{-1} \pmod{n}$。事实上，任何与 $x$ 模 $n$ 同余的整数 $y$ 都满足 $ay \equiv 1 \pmod{n}$，因此我们实际上将等价类 $[x]_{\bmod{n}}$ 视为等价类 $[a]_{\bmod{n}}$ 的乘法逆元。


• Assuming $a^{-1}$ exists in the first place, $(a^{-1})^{-1} \equiv a \pmod{n}$.
• Let $p$ be a prime. Then all of the numbers $1, 2, 3, \ldots, p-1$ are guaranteed to be relatively prime to $p$, so they all have multiplicative inverses in the context of $\mathbb{Z}$ modulo $p$.
• If $a$ has a multiplicative inverse in the context of $\mathbb{Z}$ mod $n$, there is guaranteed to be such an inverse between $1$ and $n-1$. In practice, we can just check each of these candidates one-by-one until we find the inverse.

Results

• Chinese Remainder Theorem: Suppose $r \in \mathbb{N}$ and we have $r$ natural numbers, $n_1, n_2, \ldots, n_r$, that are pair-wise relatively prime. (That is, no two of the numbers have any common factors, besides 1.) Suppose we also have $r$ integers, $a_1, a_2, \ldots, a_r$. Then there exists a solution $X$ to the system of congruences defined by the $n_i$ and $a_i$; that is, $\exists X \in \mathbb{Z}.\, \forall i \in [r].\, X \equiv a_i \pmod{n_i}$. Furthermore, if we define $N = \prod_{i \in [r]} n_i$, then all of the infinitely-many solutions $Y$ to the system of congruences satisfy $X \equiv Y \pmod{N}$.


> 🇨🇳 • 假设 $a^{-1}$ 存在，则 $(a^{-1})^{-1} \equiv a \pmod{n}$。• 设 $p$ 为素数。则 $1, 2, 3, \ldots, p-1$ 中的所有数都与 $p$ 互素，因此它们在 $\mathbb{Z}$ 模 $p$ 的语境下都有乘法逆元。• 若 $a$ 在 $\mathbb{Z}$ 模 $n$ 的语境下有乘法逆元，则保证存在一个介于 $1$ 和 $n-1$ 之间的逆元。实际操作中，我们可以逐一检查这些候选值直到找到逆元。结果• 中国剩余定理（Chinese Remainder Theorem）：假设 $r \in \mathbb{N}$，我们有 $r$ 个正整数 $n_1, n_2, \ldots, n_r$ 它们两两互素。（即没有两个数有除 1 外的任何公因子。）假设我们还有 $r$ 个整数 $a_1, a_2, \ldots, a_r$。则由 $n_i$ 和 $a_i$ 定义的同余方程组存在解 $X$；即 $\exists X \in \mathbb{Z}.\, \forall i \in [r].\, X \equiv a_i \pmod{n_i}$。此外，若我们定义 $N = \prod_{i \in [r]} n_i$，则该同余方程组的所有无穷多个解 $Y$ 都满足 $X \equiv Y \pmod{N}$。


APPENDIX A. DEFINITIONS AND THEOREMS A.5 Functions

• Let $A, B$ be sets. Let $f$ be a relation between $A$ and $B$, so $f \subseteq A \times B$. Also, assume that $f$ has the property that $\forall a \in A.\, \exists!\, b \in B.\, (a, b) \in f$. That is, assume every element of the domain $A$ (the "input" set) has exactly one corresponding element of the codomain $B$ (the "output" set) so that the two elements are related, under $f$. Put even another way, "Every input has exactly one corresponding output." Such a relation is called a function from $A$ to $B$. We call $A$ the domain of the function and $B$ the codomain of the function. We write $f: A \to B$ to mean $f$ is a function from $A$ to $B$. If $a$ is related to $b$, i.e. $(a, b) \in f$, then we write $f(a) = b$ knowing that there is exactly one such $b$ for each $a$.
• Given a proposed domain set $A$, a proposed codomain set $B$, and a proposed "rule" $f$ that says what to output, given an element of $A$, then we say $f$ is a well-defined function if the rule is defined on all elements of $A$ and, for each $a \in A$, the rule outputs exactly one element that actually does lie in the set $B$. (Note: every function is a well-defined function; this rule applies when we are trying to determine whether a given "rule" actually is a function or not.)
• Let $f: A \to B$ and $g: A \to B$ be functions. We say $f$ and $g$ are equal (in the sense of functions) and write $f = g$ when $\forall a \in A.\, f(a) = g(a)$. That is, $f = g$ when the two functions yield the same output for every input.

A.5.1 Images and Pre-Images

• Let $f: A \to B$ be a function. Let $X \subseteq A$. The image of $X$ under the function $f$ is $\text{Im}_f(X) = \{b \in B \mid \exists a \in X.\, f(a) = b\}$.
An equivalent way of writing this set is $\text{Im}_f(X) = \{f(a) \mid a \in X\}$.


> 🇨🇳 附录 A. 定义与定理 A.5 函数（Function）• 设 $A$、$B$ 为集合。设 $f$ 是 $A$ 与 $B$ 之间的关系，即 $f \subseteq A \times B$。并假设 $f$ 具有如下性质：$\forall a \in A.\, \exists!\, b \in B.\, (a, b) \in f$。即假设定义域（Domain）$A$（"输入"集）的每个元素都恰好有一个陪域（Codomain）$B$（"输出"集）中的对应元素使两者在 $f$ 下相关。换一种说法，"每个输入恰好有一个对应的输出。"这样的关系称为从 $A$ 到 $B$ 的函数。我们称 $A$ 为函数的定义域，$B$ 为函数的陪域。我们用 $f: A \to B$ 表示 $f$ 是从 $A$ 到 $B$ 的函数。若 $a$ 与 $b$ 相关，即 $(a, b) \in f$，则我们写 $f(a) = b$，因为对每个 $a$ 有且仅有一个这样的 $b$。• 给定一个提议的定义域 $A$、一个提议的陪域 $B$ 和一个提议的"规则" $f$（指定给定 $A$ 的元素后输出什么），则当规则在 $A$ 的所有元素上都有定义，且对每个 $a \in A$，规则恰好输出一个确实属于 $B$ 的元素时，我们说 $f$ 是一个良定义的函数（Well-defined Function）。（注：每个函数都是良定义的函数；此规则适用于我们试图确定给定"规则"是否真的是函数的情况。）• 设 $f: A \to B$ 和 $g: A \to B$ 为函数。当 $\forall a \in A.\, f(a) = g(a)$ 时，我们说 $f$ 与 $g$ 相等（在函数的意义上），写作 $f = g$。即当两个函数对每个输入产生相同输出时，$f = g$。A.5.1 像与原像（Image and Pre-Image）• 设 $f: A \to B$ 为函数。设 $X \subseteq A$。$X$ 在函数 $f$ 下的像（Image）为 $\text{Im}_f(X) = \{b \in B \mid \exists a \in X.\, f(a) = b\}$。另一种等价写法是 $\text{Im}_f(X) = \{f(a) \mid a \in X\}$。

