---
title: 1.1 真理与证明 | Truths and Proofs
description: 数学真理的本质——什么是证明，什么是正确与清晰的论证
tags:
  - 证明
  - 勾股定理
  - 素数
  - 无理数
---

# 1.1 Truths and Proofs

# 真理与证明

How do you know whether something is true or not? Surely, you've been told that the angles of a triangle add to $180°$, for example, but how do you know for sure? What if you met an alien who had never studied basic geometry? How could you convince him/her/it that this fact is true?

> 🇨🇳 你如何判断某件事是否为真？当然，你被告知过三角形内角和为 $180°$，但你如何确信呢？如果你遇到一个从未学过基础几何的外星人，你该如何说服他/她/它这个事实是真的？

In a way, this is what mathematics is all about: devising new statements, deciding somehow whether they are true or false, and explaining these findings to other people (or aliens, as the case may be).

> 🇨🇳 在某种意义上，这就是数学的全部：提出新的命题，判断它们是真还是假，并向其他人（或外星人，视情况而定）解释这些发现。

Unfortunately, it seems like many people think mathematicians spend their days multiplying large numbers together; in actuality, though, mathematics is a far more creative and writing-based discipline than its widely-perceived role as ever-more-complicated arithmetic.

> 🇨🇳 遗憾的是，许多人认为数学家整天在做大数乘法；但实际上，数学是一门远比大众认知的"越来越复杂的算术"更富创造性和写作性的学科。

---

## Triangle Tangle

We've introduced the idea of a proof by talking about what we hope proofs to accomplish, and why we would care so much about them. You might wonder, then, how one can define a proof. This is actually a difficult idea to address!

> 🇨🇳 我们通过讨论证明的目的和重要性引入了证明的概念。你可能会想，究竟如何定义一个证明。这其实是一个难以回答的问题！

<div class="def-theorem" markdown>
**Theorem 1.1.1** *(The Pythagorean Theorem)*. If a right triangle has base lengths $a, b$ and hypotenuse length c, then these values satisfy $a^2 + b^2 = c^2$.

> 🇨🇳 **定理 1.1.1** *（勾股定理）*。如果直角三角形的两条直角边长为 $a$、$b$，斜边长为 $c$，则有 $a^2 + b^2 = c^2$。
</div>

??? example "Proof 1 — 面积法 | Area Method"
    Draw a square with side length $a + b$. Inside this square, draw four copies of the right triangle, forming a square with side length $c$ inside the larger square.

    The area of the larger square can be computed in two ways:

 $$
 $(a + b)^2 = c^2 + 4 \cdot \frac{ab}{2} = c^2 + 2ab$
 $$

    Expanding and canceling:

 $$
    a^2 + 2ab + b^2 = c^2 + 2ab \implies a^2 + b^2 = c^2
 $$

    > 🇨🇳 画一个边长为 $a + b$ 的正方形。在其内部画四个直角三角形的副本，形成边长为 c 的内正方形。大正方形面积可通过两种方式计算：$(a+b)^2 = c^2 + 4 \cdot \frac{ab}{2} = c^2 + 2ab$。展开并消去公共项：$a^2 + 2ab + b^2 = c^2 + 2ab$，因此 $a^2 + b^2 = c^2$。

??? example "Proof 2 — 相似三角形法 | Similar Triangles Method"
    Suppose the Pythagorean Theorem is true and draw the right triangle with the altitude from the vertex corresponding to the right angle.

    Since the Pythagorean Theorem is true, we can apply it to all three of the right triangles in the diagram, namely $\triangle ABC, \triangle BCD, \triangle ACD$.

    > 🇨🇳 假设勾股定理成立，从直角顶点画高。因为勾股定理成立，我们可以对图中的三个直角三角形应用它，即 $\triangle ABC$、$\triangle BCD$、$\triangle ACD$。

??? danger "Proof 3 — 不清晰的论证 | Unclear Argument"
    This "proof" offers no explanation whatsoever. It makes it quite difficult to determine whether the claims are actually correct. A picture is included, but there is no indication of why they chose to draw a circle around the triangle, or why the stated equations follow from the diagram.

    > 🇨🇳 这个"证明"没有任何解释。这使得判断其断言是否正确变得非常困难。虽然包含了图片，但没有说明为什么要在三角形周围画圆，也没有说明所陈述的等式从图中如何得出。

??? failure "Proof 4 — 非论证 | Non-Argument"
    The Pythagorean Theorem must be true, otherwise my teachers have been lying to me.

    > 🇨🇳 勾股定理必须是真的，否则我的老师们一直在骗我。

    This is grammatically correct but proves nothing!

    > 🇨🇳 这在语法上是正确的，但什么也没有证明！

---

## What Makes a Good Proof?

From a historical perspective, mathematical proof-writing has evolved over the years and there is a good, general consensus as to what constitutes a "correct" proof:

- It is important that every step in the proof, every logical inference and claim, is valid, mathematically speaking.
- It is also important that the proof-writer makes (reasonably) clear why a statement follows from the previous work or from outside knowledge.

> 🇨🇳 从历史角度看，关于什么构成"正确"的证明有良好的普遍共识：1）证明中每一步逻辑推论和断言在数学上有效；2）证明作者合理清晰地说明命题如何从之前的工作或外部知识推出。

---

## Prime Time

A **prime number** is a positive integer that has exactly two distinct positive divisors: $1$ and itself. The first few primes are $2, 3, 5, 7, 11, 13, \ldots$

> 🇨🇳 **素数（Prime Number）**是恰好有两个不同正因数的正整数：$1$ 和它自身。前几个素数是 $2, 3, 5, 7, 11, 13, \ldots$

<div class="def-theorem" markdown>
**Theorem 1.1.2** *(Euclid)*. There are infinitely many prime numbers.

> 🇨🇳 **定理 1.1.2** *（欧几里得）*。素数有无穷多个。
</div>

??? note "证明思路 | Proof Idea"
    Suppose, for contradiction, that there are only finitely many primes $p_1, p_2, \ldots, p_n$. Consider the number $N = p_1 \cdot p_2 \cdots p_n + 1$.

    > 🇨🇳 反证法：假设只有有限个素数 $p_1, p_2, \ldots, p_n$。考虑数 $N = p_1 \cdot p_2 \cdots p_n + 1$。

---

## Irrational Irreverence

<div class="def-theorem" markdown>
**Theorem 1.1.3**. $\sqrt{2}$ is irrational.

> 🇨🇳 **定理 1.1.3.** $\sqrt{2}$ 是无理数。
</div>

??? note "证明思路 | Proof Idea"
    Suppose, for contradiction, that $\sqrt{2} = \frac{a}{b} where a, b$ are integers with no common factor.

    > 🇨🇳 反证法：假设 $\sqrt{2} = \frac{a}{b}$，其中 $a, b$ 为无公因子的整数。
