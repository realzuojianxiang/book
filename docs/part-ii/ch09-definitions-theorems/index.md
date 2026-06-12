---
title: 附录A：定义与定理
description: Appendix A: Definitions and Theorems
---

# Appendix A: Definitions and Theorems

# 附录A：定义与定理

Appendix A
Definitions and Theorems
A.1
Sets
A.1.1
Standard Sets
• The natural numbers are
N = {1, 2, 3, 4, 5, . . . }
Note: 0 $\notin \mathbb{N}$.
• For every n $\in \mathbb{N}$, the set [n] ("brackets n") is defined by
[n] = {x $\in \mathbb{N}$ | 1 $\leq x$ $\leq n$} = {1, 2, 3, . . . , n}
• The integers are
Z = {. . . , −3, −2, −1, 0, 1, 2, 3, . . . }
• The rational numbers are
Q =
n
x $\in \mathbb{R}$ | $\exists a$, b $\in \mathbb{Z}$. b \neq 0 and a
b = x
o
• The real numbers are denoted by R. Every real number is either ratio-
nal or irrational.
• The empty set is the set that has no elements. We write it as $\emptyset o$r { }.
A.1.2
Set-Builder Notation
• If U is a set and P(x) is some property that either does or does not hold
for any given x, then we can always define a new set by writing
S = {x $\in U$ | P(x) holds}
• This is called set-builder notation. It is essential to identify the uni-
versal set U and the property P(x).

APPENDIX A. DEFINITIONS AND THEOREMS
A.1.3
Elements and Subsets
• To say "x is an element of the set S" we write
x $\in S$
To say "x is not an element of the set S" we write
x $\notin S$
• To say "S is a subset of T" we write
S $\subseteq T$
This is defined by the conditional statement "Every element of S is also
an element of T". This can be expressed as
$\forall x \in U. x \in S$ =$\Rightarrow x \in T$
That is, for every element x of the universal set (supposing S, T $\subseteq U$),
whenever x $\in S$, we also know that x $\in T$.
• To prove that a set is a subset of another set, like S $\subseteq T$, we need to do
something like this:
Let x $\in S$ be arbitrary and fixed.
. . . blah blah blah . . .
Therefore, x $\in T$, as well.
This shows S $\subseteq T$.
• To say "S is a proper subset of T" we write
S $\subset T$
This means S $\subseteq T$ and S \neq T.
• It is true that $\emptyset \subseteq S$, for any set S.
• It is true that S $\subseteq S$, for any set S.
A.1.4
Power Set
• Let S be a set. The power set of S is denoted by P(S) and is defined
by
P(S) = {A | A $\subseteq S$}
That is, P(S) is the set of all subsets of S.
• It is true that $\emptyset \in P(S) and S \in P$(S), for any set S.

> 🇨🇳 即 $\mathcal{P}(S)$ 是 $S$ 的所有子集的集合。对任意集合 $S$，都有 $\emptyset \in \mathcal{P}(S)$ 且 $S \in \mathcal{P}(S)$。
