---
title: 第7章：函数与基数
description: Chapter 7: Functions and Cardinality
---

# Chapter 7: Functions and Cardinality

# 第7章：函数与基数

Chapter 7
Functions and Cardinality:
Inputs, Outputs, and The
Sizes of Sets
7.1
Introduction
We are continuing our two-chapter development of functions. In this chapter, we
will formally define a function. Specifically, we will see that a function is really a
particular kind of relation with certain properties. That's why we took the time
to explore relations to begin with—besides the fact that they are interesting and
useful in their own right, of course. After defining a function, we will explore
what kinds of properties functions might have through many examples and
proofs. The definitions and theorems and proofs we see in this exploration will
make use of all of the concepts we have developed so far, especially the proof
techniques from Section 4.9.
Later in this chapter, we will use the concept of a bijective function—
essentially, a "pairing up" of elements of two sets—to talk about the "sizes"
of sets and how to compare them. This topic, cardinality, will show us some
rather remarkable and counterintuitive facts about infinite sets. It will also pro-
vide us an inroad into the next chapter, where we restrict our focus to finite
sets and how to count them.
7.1.1
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
• State the definition of a function, and provide many examples.
• Take informal descriptions and visual diagrams of functions and use them
to construct formal arguments about examples (and non-examples) of
functions and their properties.
• Define images and pre-images of sets, in the context of a function, and
prove various properties of these operations.
• State several properties of functions, as well as apply relevant techniques to
determine and prove whether or not a given function has these properties.
• Find the composition of two functions, recognize how this can be used to
create new functions, and identify and prove what consequences composi-
tion has on the properties of the functions of involved.
• Describe the relationship between bijective functions and inverses, and use
this to solve problems and prove claims.
• Use bijections to define the cardinalities of sets and prove claims about
these cardinalities.
• State the diﬀerence between finite, countably infinite, and uncountably
infinite sets, and provide several examples of each type.
7.1.2
Segue from previous chapter
The important idea from the previous chapter that will be helpful in this one
is that of a relation. As we mentioned already, we will see that a function is
just a particular kind of relation. This will come up in our formal definition of
what a function is.
The other ideas explored in the previous chapter—equivalence relations, and
results in number theory—will not appear so explicitly in this chapter. That
is to say, the examples of functions we explore here, and their properties, do
not depend on the other ideas explored in the last chapter. Rather, we will use
those ideas to create interesting examples and exercises here.

> 🇨🇳 ……也就是说，我们此处探讨的函数示例及其性质，并不依赖于上一章中的其他概念。相反，我们将利用那些概念来创建有趣的示例和练习。
