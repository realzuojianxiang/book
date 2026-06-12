---
title: 第8章：组合数学
description: Chapter 8: Combinatorics
---

# Chapter 8: Combinatorics

# 第8章：组合数学

Chapter 8
Combinatorics: Counting
Stuﬀ
8.1
Introduction
The field of combinatorics is one of the most active and exciting areas of
interest in modern mathematics. It is also sometimes known as "discrete math"
to distinguish it from analysis, which studies more "continuous" notions like
the real number line and functions defined on that set.
In this chapter we
will explore some of the fundamental ideas in combinatorics and apply them
to solve interesting problems. Essentially, we will be learning interesting and
useful principles about how to count the number of elements in finite sets where
those elements are described in some way but not enumerated for us.
8.1.1
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
• State the Rules of Sum and Product, and use and combine them to con-
struct simple counting arguments.
• Categorize several standard counting objects, as well as state correspond-
ing counting formulas and understand how to prove them.
• State the meaning of binomial coefficients and evaluate their numerical
formulae, know how to use them in counting arguments, and understand
how to derive those numerical formulae.
• Critique a proposed counting argument by properly demonstrating if it is
an undercount or overcount.
• Prove combinatorial identities by constructing "counting in two ways"
proofs.
• Understand various formulations of selection with repetition, and use them
to solve problems.
• State the Pigeonhole Principle and use it in counting arguments.
• State the Principle of Inclusion/Exclusion and use it in counting argu-
ments.
8.1.2
Segue from previous chapter
In Chapter 7, we left oﬀtalking about the cardinality of sets, both finite and
infinite. While many of the results about infinite sets are interesting and math-
ematically rich, that particular area can lead to some mind-bending and confus-
ing areas that are, alas, beyond the scope of our current studies. For now, we
will focus on finite sets. In particular, we will explore how some results about
the cardinality of finite sets can be used to solve problems about "counting"
mathematical objects. That is, we will explore how we can answer questions
of the form "How many objects are there with property X?" This branch of
mathematics is known as combinatorics.
You can think of it as "the study
of combinations of objects". While investigating this branch of mathematics,
we will develop some new notation and definitions, prove and use some results
about finite sets, and describe and study some particular objects that live in
the field of combinatorics and computer science. Importantly, we will learn an
entirely new proof technique based on counting objects!
8.1.3
Motivation
Think about playing poker. If you're unfamiliar with the game, just think of
it as a simple system where two players receive a hand of 5 random cards each
and then they compare to see who wins. Hands are ranked according to the
following list, from best to worst:

> 🇨🇳 ……每位玩家随机获得5张手牌，然后比较大小决定胜负。手牌从最强到最弱排列如下：
