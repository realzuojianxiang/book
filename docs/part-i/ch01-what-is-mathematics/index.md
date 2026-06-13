---
title: 第1章 什么是数学？
description: Chapter 1 — What Is Mathematics? 数学的本质、真理与证明
tags:
  - 证明
  - 数学思维
  - 归纳
  - 符号
  - 逻辑基础
---

# Chapter 1: What Is Mathematics?

# 第1章：什么是数学？

---

## 1.1 Truths and Proofs

How do you know whether something is true or not? Surely, you've been told that the angles of a triangle add to $180°$, for example, but how do you know for sure? What if you met an alien who had never studied basic geometry? How could you convince him/her/it that this fact is true?

> 🇨🇳 你如何判断某件事是否为真？当然，你被告知过三角形内角和为 $180°$，但你如何确信呢？如果你遇到一个从未学过基础几何的外星人，你该如何说服他/她/它这个事实是真的？

In a way, this is what mathematics is all about: devising new statements, deciding somehow whether they are true or false, and explaining these findings to other people (or aliens, as the case may be).

> 🇨🇳 在某种意义上，这就是数学的全部：提出新的命题，判断它们是真还是假，并向其他人（或外星人，视情况而定）解释这些发现。

Unfortunately, it seems like many people think mathematicians spend their days multiplying large numbers together; in actuality, though, mathematics is a far more creative and writing-based discipline than its widely-perceived role as ever-more-complicated arithmetic.

> 🇨🇳 遗憾的是，许多人认为数学家整天在做大数乘法；但实际上，数学是一门远比大众认知的"越来越复杂的算术"更富创造性和写作性的学科。

One aim of this book is to convince you of this fact, but that's merely a bonus. This book's main goals are to show you what mathematical thinking, problem-solving, and proof-writing are really all about, to show you how to do those things, and to show you how much fun they really are!

> 🇨🇳 本书的目标之一是让你相信这一事实，但这只是额外的收获。本书的主要目标是向你展示数学思维、问题解决和证明写作究竟是什么，教你如何做这些事情，并让你发现它们有多有趣！

As a side note, you might even wonder "What does it mean for something to be true?" A full discussion of this question would delve into philosophy, psychology, and maybe linguistics, and we don't really want to get into that. The main idea in the context of mathematics, though, is that something is true only if we can show it to be true **always**.

> 🇨🇳 顺便一提，你甚至会想"某件事为真意味着什么？"对这个问题的完整讨论将涉及哲学、心理学甚至语言学，我们不想深入这些。但在数学的语境中，核心思想是：一个命题为真，仅当我们能证明它**永远**为真。

We know $1 + 1 = 2$ always and forever. It doesn't matter if it's midnight or noon, we can rest assured that equation will hold true. (Have you ever thought about how to show such a fact, though? It's actually quite difficult! A book called the *Principia Mathematica* does this from "first principles" and it takes the authors many, many pages to even get to $1 + 1 = 2$!)

> 🇨🇳 我们知道 $1 + 1 = 2$ 永远成立。无论是午夜还是正午都无关紧要，我们可以确信这个等式始终成立。（但你有没有想过如何证明这样的事实？实际上这相当困难！一本名为《数学原理》的书从"第一性原理"出发做到了这一点，作者们花了许许多多页才到达 $1 + 1 = 2$！）

This is quite different from, perhaps, other sciences. If we conduct a physical experiment 10 times and the same result occurs, do we know that this will always happen? What if we do the experiment a million times? A billion? At what point have we actually **proven** anything?

> 🇨🇳 这与其他科学有很大不同。如果我们做一个物理实验10次得到了相同的结果，我们能确定这总会发生吗？如果我们做一百万次呢？十亿次呢？到什么程度我们才算真正**证明**了什么？

In mathematics, repeated experimentation is not a viable proof! We would need to find an argument that shows why such a phenomenon would always occur.

> 🇨🇳 在数学中，反复实验不构成有效证明！我们需要找到一个论证来表明为什么这样的现象总会发生。

As an example, there is a famous open problem in mathematics called the **Goldbach Conjecture**. It is unknown, as of now, whether it is true or not, even though it has been verified by computer simulations up until a value of roughly $10^{18}$. That's a huge number, but it is still not enough to know whether the conjecture is True or False. Do you see the difference? We mathematicians like to prove facts, and checking a bunch of values but not all of them does not constitute a proof.

> 🇨🇳 举个例子，数学中有一个著名的未解决问题叫做**哥德巴赫猜想（Goldbach Conjecture）**。目前尚不知道它是否为真，尽管计算机模拟已经验证到大约 $10^{18}$ 的值。这是一个巨大的数字，但仍不足以确定该猜想是真还是假。你看到区别了吗？我们数学家喜欢证明事实，而只检查一部分值而非全部并不构成证明。

---

### 1.1.1 Triangle Tangle

We've introduced the idea of a proof by talking about what we hope proofs to accomplish, and why we would care so much about them. You might wonder, then, how one can define a proof. This is actually a difficult idea to address! To approach this idea, we are going to present several different mathematical arguments. We want you to read along with them, and think about whether they are convincing. Do they prove something? Are they correct? Are they understandable? How do they make you feel?

> 🇨🇳 我们通过讨论证明的目的和重要性引入了证明的概念。你可能会想，究竟如何定义一个证明。这其实是一个难以回答的问题！为了逐步理解这个概念，我们将展示几个不同的数学论证。我们希望你仔细阅读，并思考它们是否有说服力。它们证明了什么吗？它们正确吗？它们容易理解吗？它们给你什么感觉？

The mathematical arguments we will present here are all about triangles. Specifically, they concern the Pythagorean Theorem.

> 🇨🇳 我们将展示的数学论证都与三角形有关。具体来说，它们涉及勾股定理。

<div class="def-theorem" markdown>
**Theorem 1.1.1** *(The Pythagorean Theorem)*. If a right triangle has base lengths $a, b$ and hypotenuse length $c$, then these values satisfy


a^2 + b^2 = c^2


> 🇨🇳 **定理 1.1.1** *（勾股定理）*。如果直角三角形的两条直角边长为 $a$、$b$，斜边长为 $c$，则有 $a^2 + b^2 = c^2$。
</div>

How do we know this? It's a very useful fact, one that you've probably used many times in your mathematics classes (and in life, without even realizing). Have you ever wondered **why** it's true? How would you explain it to a skeptical friend? This is what a mathematical proof attempts to accomplish: a clear and concise explanation of a fact.

> 🇨🇳 我们怎么知道这是对的？这是一个非常有用的事实，你在数学课上（甚至在生活中不知不觉地）可能用过很多次。你有没有想过它**为什么**是对的？你如何向一个持怀疑态度的朋友解释？这就是数学证明试图做到的：对一个事实的清晰而简洁的解释。

The reasoning behind requiring a proof makes a lot of sense, too, and is twofold: it's a relief to know that what we thought was true is, indeed, true and it's nice to not have to go through the explanation of the fact every time we'd like to use it. After proving the Pythagorean Theorem (satisfactorily), we merely need to refer to the theorem by name whenever a relevant situation arises; we've already done the proof, so there's no need to prove it again.

> 🇨🇳 要求证明的理由也很充分，有双重意义：一方面，确认我们所认为为真的事情确实为真令人安心；另一方面，每次需要使用某个事实时不需要重新解释一遍也令人轻松。在（令人满意地）证明了勾股定理之后，每当遇到相关情形，我们只需引用定理的名称即可；我们已经完成了证明，所以不需要再证一遍。

#### Examples of "Proofs"

Let's look at some sample "proofs" and see whether they work well enough. (We say "proof" for now until we come up with a more precise definition for it, later on.)

> 🇨🇳 让我们看一些"证明"样本，看看它们是否足够好。（我们暂时称其为"证明"，直到后面给出更精确的定义。）

**"Proof" 1.** Draw a square with side length $a + b$. Inside this square, draw four copies of the right triangle, forming a square with side length $c$ inside the larger square.

The area of the larger square can be computed in two ways: by applying the area formula to the larger square or by adding the area of the smaller square to the area of the four triangles. Thus, it must be true that


$(a + b)^2 = c^2 + 4 \cdot \frac{ab}{2} = c^2 + 2ab$


Expanding the expression on the left and canceling a common term on both sides yields


a^2 + 2ab + b^2 = c^2 + 2ab


Therefore, $a^2 + b^2 = c^2$ is true.

> 🇨🇳 **"证明"1.** 画一个边长为 $a + b$ 的正方形。在这个正方形内部，画出四个直角三角形的副本，形成边长为 $c$ 的内正方形。
>
> 大正方形的面积可以通过两种方式计算：对大正方形应用面积公式，或将小正方形的面积与四个三角形的面积相加。因此，必定有：
>
> (a + b)^2 = c^2 + 4 \cdot \frac{ab}{2} = c^2 + 2ab
>
> 展开左边的表达式并消去两边的公共项，得到：
>
> $ $1^2 + 2ab + b^2 = c^2 + 2ab
>
> 因此，$a^2 + b^2 = c^2$ 成立。

**"Proof" 4.** The Pythagorean Theorem must be true, otherwise my teachers have been lying to me.

> 🇨🇳 **"证明"4.** 勾股定理必须是真的，否则我的老师们一直在骗我。

#### Discussion

From a historical perspective, mathematical proof-writing has evolved over the years and there is a good, general consensus as to what constitutes a "correct" proof:

- It is important that every step in the proof, every logical inference and claim, is valid, mathematically speaking.
- It is also important that the proof-writer makes (reasonably) clear why a statement follows from the previous work or from outside knowledge.

> 🇨🇳 从历史角度看，数学证明写作经历了多年的演变，关于什么构成"正确"的证明有一个良好的普遍共识：
>
> - 证明中的每一步、每一个逻辑推论和断言在数学上是有效的，这很重要。
> - 证明作者（合理地）清晰地说明为什么一个命题可以从之前的工作或外部知识推出，这也很重要。

What's nice about the truth requirement is that mathematics has been built up so that we can read through an argument and verify each claim as True or False. What's difficult to define is clear writing. In a way, it is much like Supreme Court Justice Potter Stewart's famous definition of obscenity: *"I know it when I see it"*.

> 🇨🇳 真值要求的好处在于，数学已经发展到这样的程度：我们可以通读一个论证并验证每个断言的真假。难以定义的是清晰的写作。在某种意义上，这很像最高法院大法官波特 $\cdot$ 斯图尔特对猥亵的著名定义：*"我看到时就知道"*。

---

### 1.1.2 Prime Time

A **prime number** is a positive integer that has exactly two distinct positive divisors: $1$ and itself. The first few primes are $2, 3, 5, 7, 11, 13, \ldots$

> 🇨🇳 **素数（Prime Number）**是恰好有两个不同正因数的正整数：$1$ 和它自身。前几个素数是 $2, 3, 5, 7, 11, 13, \ldots$

<div class="def-theorem" markdown>
**Theorem 1.1.2** *(Euclid)*. There are infinitely many prime numbers.

> 🇨🇳 **定理 1.1.2** *（欧几里得）*。素数有无穷多个。
</div>

> 🇨🇳 欧几里得证明了素数有无穷多个。其证明思路如下：假设只有有限个素数 $p_1, p_2, \ldots, p_n$，考虑数 $N = p_1 \cdot p_2 \cdots p_n + 1$。$N$ 除以任何一个素数 $p_i$ 都余1，因此 $N$ 要么本身是素数，要么有一个不在列表中的素因子——无论哪种情况，都说明列表之外还有素数，矛盾！

---

### 1.1.3 Irrational Irreverence

<div class="def-theorem" markdown>
**Theorem 1.1.3**. $\sqrt{2}$ is irrational.

> 🇨🇳 **定理 1.1.3.** $\sqrt{2}$ 是无理数。
</div>

> 🇨🇳 这里我们需要证明 $\sqrt{2}$ 不是有理数。采用反证法：假设 $\sqrt{2} = \frac{a}{b}$，其中 $a, b$ 为互素整数。则 $a^2 = 2b^2$，所以 $a^2$ 是偶数，从而 $a$ 是偶数。设 $a = 2c$，代入得 $4c^2 = 2b^2$，即 $b^2 = 2c^2$，故 $b$ 也是偶数。但 $a, b$ 互素，矛盾！因此 $\sqrt{2}$ 是无理数。

---

## 1.2 Exposition Exhibition

> 🇨🇳 本章介绍数学表述的基本要素：符号、写作规范、逻辑入门。

### 1.2.1 Simply Symbols

> 🇨🇳 符号系统简介：数学中使用的各种符号及其含义。

### 1.2.2 Write Right

> 🇨🇳 数学写作规范：如何清晰、准确地书写数学论证。

### 1.2.3 Pick Logic

> 🇨🇳 逻辑入门：数学推理中逻辑的基本要素。

### 1.2.4 Obvious Obfuscation

> 🇨🇳 显而易见的混淆：数学写作中常见的模糊与混淆问题。

---

## 1.3 Review, Redo, Renew

> 🇨🇳 本节回顾基础数学概念，为后续学习打好基础。

### 1.3.1 Quick Arithmetic

> 🇨🇳 快速算术：复习整数、分数等基本运算。

### 1.3.2 Algebra Abracadabra

> 🇨🇳 代数魔术：通过代数技巧解决有趣的数学问题。

### 1.3.3 Polynomnomnomials

> 🇨🇳 多项式：多项式的基本概念与运算。

### 1.3.4 Let's Talk About Sets

> 🇨🇳 初识集合：集合的基本概念，后续章节将深入讨论。

### 1.3.5 Notation Station

> 🇨🇳 记号站：数学中常用的记号与符号汇总。

---

## 1.4 Quizzical Puzzicles

> 🇨🇳 本节通过趣味问题引入数学思维，培养归纳推理的直觉。

### 1.4.1 Funny Money

> 🇨🇳 趣味货币问题。

### 1.4.2 Gauss in the House

> 🇨🇳 高斯求和：少年高斯巧妙地求出 $1+2+\cdots+n = \frac{n(n+1)}{2}$ 的故事。

### 1.4.3 Some Other Sums

> 🇨🇳 其他求和问题：探讨不同形式的求和公式。

### 1.4.4 Friend Trends

> 🇨🇳 朋友圈趋势：用图论思想研究朋友圈中的关系。

### 1.4.5 The Full Monty Hall

> 🇨🇳 蒙提霍尔问题：经典的概率悖论，换门是否更优？

---

## 1.5 It's Wise To Exercise

> 🇨🇳 本章练习题，帮助巩固所学概念。

---

## 1.6 Lookahead

> 🇨🇳 下一章预告：第2章将介绍数学归纳法。
