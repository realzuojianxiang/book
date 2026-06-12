---
title: Introduction
---

# Introduction

Chapter 5 Rigorous Mathematical Induction: A Formal Restatement
## 5.1 Introduction It might seem like we're being redundant by including this chapter after having already discussed mathematical induction. Our goals are many, though, and you will see afterwards why we have turned our eye backwards a bit to discuss this material once more. First, we feel a little uncomfortable with how informal (mathematically speaking) we were with our initial treatment of induction. Second, we left a few lingering questions back in Chapter 2. What was different about some of the later examples we saw, like the Takeaway game and the Tower of Hanoi? Didn't they seem to use "more assumptions" in their inductive arguments than the other examples, like our proof that P k$\in$[n] k = n(n+1)


> 🇨🇳 我们认为确实如此，并在此讨论这些差异。第三，还有许多有趣且有用的例子有待研究，通过它们能深化我们对数学语言的理解。第四，本章最后一个定理将是等价性的精彩示例——我们将用双条件语句（Biconditional Statement）把三个定理联系在一起！（这将是"以下命题等价……"型定理的第一个重要示例，如 4.9.6 节所指出的。）


? We think so, and we will adress those differences here. Third, there are plenty of examples left to be seen that are interesting and useful facts in their own right, and working through them will help to develop our understanding of the mathematical language we are beginning to speak with each other. Fourth, the final theorem stated and proved (with your help!) in this chapter will be a striking example of equivalence; specifically, we will show that three theorems are all connected by biconditional statements! (This will be the first great example of a "The following are equivalent. . . "-style theorem, like we pointed out in the proof strategy for biconditional statements, in Section 4.9.6.)
### 5.1.1 Objectives Since we have discussed induction before and are just returning to this topic, we will forego the usual introductory matter at the beginning of this chapter.


> 🇨🇳 我们将以一系列要点概述本章目标。本章结束时，你应能：陈述数学归纳原理（Principle of Mathematical Induction）并描述其证明与自然数集的关系；陈述强数学归纳原理（Principle of Strong Mathematical Induction）并与前者比较对比，描述其证明方法；用归纳论证（Inductive Argument）证明命题，特别要能识别何时需要强归纳论证；理解并解释数学归纳的若干变体（Variant），识别适合使用这些变体的问题；陈述良序原理（Well-Ordering Principle）并解释其与数学归纳的关系。


Instead, we will summarize the main objectives of this chapter here via a series of statements. By the end of this chapter, you should be able to . . . • State the Principle of Mathematical Induction and describe how its proof is related to the set of natural numbers. • State the Principle of Strong Mathematical Induction, compare and contrast this with the previous principle, and describe how it can be proven. • Use inductive arguments to prove claims and, in particular, identify when a strong inductive argument is required. • Understand and explain some variants of mathematical induction, and identify problems where these variants might be useful. • State the Well-Ordering Principle and explain its relationship to mathematical induction.
## 5.2 Regular Induction This first section concerns the kind of inductive arguments we have seen before. You will see why, in the next section, we would choose to refer to this as "Regular" Induction.
### 5.2.1 Theorem Statement and Proof
Here, let's recall the statement of the Principle of Mathematical Induction that we gave in Chapter 3. Think about how it follows the Domino Analogy, or whichever analogy works best to help you understand an inductive process. You might have missed this Theorem statement if you didn't complete the Optional Reading about Defining N, in Section 3.8, but that's okay. We're confident you can still read this and formulate it in a way that corresponds to an inductive process.
<div class="def-theorem" markdown>
**Theorem 5.2.1 (Principle of Mathematical Induction). Let P(n) be some**
</div>
"fact" or "observation" that depends on the natural number n. Assume that 1. P(1) is a true statement. 2. Given any k $\in \mathbb{N}$, if P(k) is true, then we can conclude necessarily that P(k + 1) is true. Then the statement P(n) must be true for every natural number n $\in \mathbb{N}$.


> 🇨🇳 定理 5.2.1（数学归纳原理）——设 $P(n)$ 是依赖于自然数 $n$ 的某个"事实"或"观察"。假设：(1) $P(1)$ 为真；(2) 对任意 $k \in \mathbb{N}$，若 $P(k)$ 为真则可必然推出 $P(k+1)$ 为真。则 $P(n)$ 对一切自然数 $n \in \mathbb{N}$ 必然为真。


