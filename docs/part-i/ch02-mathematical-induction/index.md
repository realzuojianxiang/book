---
title: 第2章：数学归纳法
description: Chapter 2: Mathematical Induction
---

# Chapter 2: Mathematical Induction

# 第2章：数学归纳法

Chapter 2
Mathematical Induction:
"And so on . . . "
2.1
Introduction
This chapter marks our first big step toward investigating mathematical proofs
more throughly and learning to construct our own. It is also an introduction
to the first significant proof technique we will see. As we describe below,
this chapter is meant to be an appetizer, a first taste, of what mathematical
induction is and how to use it. A couple of chapters from now, we will we be
able to rigorously define induction and prove that this technique is mathemati-
cally valid. That's right, we'll actually prove how and why it works! For now,
though, we'll continue our investigation of some interesting mathematical puz-
zles, with these particular problems hand-picked by us for their use of inductive
techniques.
2.1.1
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
• Define what an inductive argument is, as well as classify a presented ar-
gument as an inductive one or not.
• Decide when to use an inductive argument, depending on the structure of
the problem you are solving.
• Heuristically describe mathematical induction via an analogy.
• Identify and describe diﬀerent kinds of inductive arguments by comparing
and contrasting them, as well as identify the underlying structures of the
corresponding problems that would yield these similarities and diﬀerences.
2.1.2
Segue from previous chapter
As in the previous chapter, we won't assume any familiarity with more advanced
mathematics beyond basic algebra and arithmetic, and perhaps some visual,
geometric intuition. We will, however, make use of summation and product
notation fairly often, so if you feel like your notational skills are, go back and
review Section 1.3.5.
2.1.3
Motivation
Look back at the Puzzle in Section 1.4.3, where we proved that the sum of
the first n odd natural numbers is exactly n2. We first observed this pattern
geometrically, by arranging the terms of the sums (odd integers) as successively
larger "corner pieces" of a square. The first way we proved the result, though,
didn't seem to depend on that observation and merely utilized a previous result
(about sums of even and odd integers) in an algebraic way; that is, we did some
tricky manipulation of some equations (mutliplying and subtracting and what
have you) and then–voil`a!–out popped the result we expected. What did you
think about that approach? Did it feel satisfying? In a way, it didn't quite match
the geometric interpretation we had, at first, so it might be surprising that it
worked out so nicely. (Perhaps there is a diﬀerent geometric interpretation of
this approach. Can you find one?)
Our second approach was to model that initial geometric observation. We
transformed visual pieces into algebraic pieces; specifically, a sum was related to
the area of a square, and the terms of the sum were related to particular pieces of
that square. We established a correspondence between diﬀerent intepretations
of the same problem, finding a way to relate one to the other so that we could
work with either interpretation and know that we were proving something about
the overall result. The benefit of the visual interpretation is that it allowed us to
take advantage of a general proof strategy known as mathematical induction,
or sometimes just induction, for short. (The word induction has some non-
mathematical meanings, as well, such as in electromagnetism or in philosophical
arguments, but within the context of this book, when we say induction, we mean

> 🇨🇳 ……（"归纳"一词在电磁学或哲学论证中也有非数学含义，但在本书语境中，当我们说归纳时，我们指的是数学归纳法。）
