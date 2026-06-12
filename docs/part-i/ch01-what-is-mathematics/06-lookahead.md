---
title: 1.6 Lookahead
---

# 1.6 Lookahead

goals are to (a) formalize some of the intuitive ideas we have about mathematical objects, (2) see many examples of good proofs and develop the ability to create and write good proofs, (3) develop problem-solving skills and the ability to apply mathematical knowledge, and (4) cultivate an appreciation for both the art and science of mathematics. Scan the table of contents at the beginning of the book to get a sense for where our journey is headed. The phrases and terminology might be foreign to you now, but by the end of the book, we will all be speaking the same language: mathematics.

> 🇨🇳 我们的目标是：(a) 将我们对数学对象的直觉想法形式化；(2) 看到许多好的证明示例并培养创建和写好证明的能力；(3) 发展问题解决技能和运用数学知识的能力；(4) 培养对数学的艺术性和科学性的鉴赏力。浏览书前的目录以了解我们的旅程将走向何方。那些术语现在可能对你很陌生，但到本书结束时，我们都将说同一种语言：数学。


Chapter 2 Mathematical Induction: "And so on . . . "
## 2.1 Introduction This chapter marks our first big step toward investigating mathematical proofs more throughly and learning to construct our own. It is also an introduction to the first significant proof technique we will see. As we describe below, this chapter is meant to be an appetizer, a first taste, of what mathematical induction is and how to use it. A couple of chapters from now, we will we be able to rigorously define induction and prove that this technique is mathematically valid. That's right, we'll actually prove how and why it works! For now, though, we'll continue our investigation of some interesting mathematical puzzles, with these particular problems hand-picked by us for their use of inductive techniques.
### 2.1.1 Objectives The following short sections in this introduction will show you how this chapter fits into the scheme of the book. They will describe how our previous work will be helpful, they will motivate why we would care to investigate the topics that appear in this chapter, and they will tell you our goals and what you should keep in mind while reading along to achieve those goals. Right now, we will summarize the main objectives of this chapter for you via a series of statements. These describe the skills and knowledge you should have gained by the conclusion of this chapter. The following sections will reiterate these ideas in more detail, but this will provide you with a brief list for future reference. When you finish working through this chapter, return to this list and see if you understand all of these objectives. Do you see why we outlined them here as being important? Can you define all the terminology we use? Can you apply the techniques we describe?

> 🇨🇳 第2章数学归纳法："以此类推……" **2.1 引言** 本章标志着我们向深入研究数学证明迈出的第一大步，也是学习构建自己的证明的开始。它同时介绍了我们将看到的第一个重要的证明技巧。正如下面所描述的，本章旨在作为一道开胃菜，让你初次品尝数学归纳法（Mathematical Induction）是什么以及如何使用它。再过几章，我们将能够严格定义归纳法并证明这一技巧在数学上是有效的。没错，我们实际上会证明它是如何以及为什么有效的！现在，我们将继续研究一些有趣的数学谜题，这些问题是我们特意挑选的，因为它们使用了归纳技巧。**2.1.1 目标** 本引言的以下简短章节将向你展示本章如何融入全书框架。它们将描述我们之前的工作如何有所帮助，将说明为什么要研究本章出现的主题，还将告诉你我们的目标以及阅读时应该记住什么以实现这些目标。现在，我们通过一系列陈述来总结本章的主要目标。这些是你在本章结束时应该获得的技能和知识。以下章节将更详细地重申这些想法，但这为你提供了一个简要清单以供参考。当你完成本章的学习后，返回此清单，看看你是否理解了所有这些目标。你是否明白我们为什么将这些列为重要的？你能定义我们使用的所有术语吗？你能应用我们描述的技巧吗？


