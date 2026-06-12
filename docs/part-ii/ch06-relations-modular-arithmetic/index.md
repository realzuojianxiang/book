---
title: 第6章：关系与模运算
description: Chapter 6: Relations and Modular Arithmetic
---

# Chapter 6: Relations and Modular Arithmetic

# 第6章：关系与模运算

Chapter 6
Relations and Modular
Arithmetic: Structuring
Sets and Proving Facts
About The Integers
6.1
Introduction
Now that we've built a strong foundation of mathematical terminology, con-
cepts, and material, you might be wondering what we're going to talk about
next!
Well, much like we wanted to rigorize the concept of mathematical
induction—something we intuitively "understood" but couldn't yet develop in
a precise mathematical way—we will, in the next two chapters, set on firmer
ground a concept that we have used in passing already, and one that you're
likely familiar with in an intuitive sense: a function.
To accomplish this, we will start by talking about relations.
This will
lead us into the particular area of equivalence relations, which allow us to
talk about some qualitative properties of sets. In particular, we will use some
equivalence relations on the set Z to state and prove many interesting properties
about integers. This will give us occasion to briefly explore the mathematical
branch of Number Theory. It is a rich, deep, and broad field, and we will
really only skim the surface by stating and proving a few helpful theorems and
using them to solve some interesting puzzles and problems. Then, we will move
right along to the next chapter and get back to our goal of discussing functions.
6.1.1
Objectives
The following short sections in this introduction will show you how this chapter
fits into the scheme of the book. They will describe how our previous work

will be helpful, they will motivate why we would care to investigate the topics
that appear in this chapter, and they will tell you our goals and what you
should keep in mind while reading along to achieve those goals. Right now,
we will summarize the main objectives of this chapter for you via a series of
statements. These describe the skills and knowledge you should have gained by
the conclusion of this chapter. The following sections will reiterate these ideas
in more detail, but this will provide you with a brief list for future reference.
When you finish working through this chapter, return to this list and see if you
understand all of these objectives. Do you see why we outlined them here as
being important? Can you define all the terminology we use? Can you apply
the techniques we describe?
By the end of this chapter, you should be able to . . .
• Define a relation and provide many examples.
• Define and understamd various properties that a relation might have, pro-
viding examples of relations that do and do not have these properties.
• Consider a defined relation and discover and prove what properties it has.
• Define equivalence relations and equivalence classes and explain why these
are particularly interesting and important examples of relations.
• Consider a defined equivalence relation and categorize its equivalence
classes.
• Use a particular equivalence relation on the set of integers to state and
prove interesting results in number theory.
• Define the concept of multiplicative inverses, understand what this means
in the particular context of modular arithmetic, and apply this idea to
prove/disprove the existence of solutions to particular equations.
• State and understand various theorems in number theory, and apply them
to solve given problems.
6.1.2
Segue from previous chapter
This chapter doesn't quite follow from the previous one directly, in the way that
others have. Instead, we are really moving into a new part of the book. From
now on, we will be taking all of the mathematical knowledge we have developed
thus far and applying it to learn about other interesting areas. We needed to
work through all of that other material first, to get to this point. From now on,
we will be stating complicated claims and applying proof techniques to prove
them. We will provide you with definitions and theorems and expect you to
use them to prove other claims.
In this sense, this chapter follows from all
of the previous chapters. We will be putting all of that acquired knowledge,
terminology, and experience to good use!

> 既然我们已经建立了坚实的数学术语、概念和材料基础，你可能想知道我们接下来要讨论什么！就像我们曾经想要将数学归纳法的概念严格化——那个我们直觉上"理解"但还无法用精确的数学方式表达的东西——在接下来的两章中，我们将把我们已经顺便使用过、而且你可能直觉上熟悉的概念建立在更坚实的基础之上：函数（Function）。为此，我们将从讨论关系（Relation）开始。这将引导我们进入等价关系（Equivalence Relation）这一特定领域，它使我们能够讨论集合的某些定性性质。特别地，我们将在集合 $\mathbb{Z}$ 上使用一些等价关系来陈述和证明关于整数的许多有趣性质。这将给我们一个机会简要探索数论（Number Theory）这一数学分支。这是一个丰富、深刻且广阔的领域，我们实际上只是浅尝辄止，通过陈述和证明一些有用的定理，并用它们来解决一些有趣的谜题和问题。然后，我们将直接进入下一章，回到讨论函数的目标上来。
