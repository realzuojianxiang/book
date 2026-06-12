---
title: 第5章：严格数学归纳法
description: Chapter 5: Rigorous Mathematical Induction
---

# Chapter 5: Rigorous Mathematical Induction

# 第5章：严格数学归纳法

Chapter 5
Rigorous Mathematical
Induction: A Formal
Restatement
5.1
Introduction
It might seem like we're being redundant by including this chapter after having
already discussed mathematical induction. Our goals are many, though, and
you will see afterwards why we have turned our eye backwards a bit to discuss
this material once more.
First, we feel a little uncomfortable with how informal (mathematically
speaking) we were with our initial treatment of induction. Second, we left a
few lingering questions back in Chapter 2. What was diﬀerent about some of
the later examples we saw, like the Takeaway game and the Tower of Hanoi?
Didn't they seem to use "more assumptions" in their inductive arguments than
the other examples, like our proof that P
k$\in$[n] k = n(n+1)

? We think so, and
we will adress those diﬀerences here. Third, there are plenty of examples left
to be seen that are interesting and useful facts in their own right, and work-
ing through them will help to develop our understanding of the mathematical
language we are beginning to speak with each other. Fourth, the final theorem
stated and proved (with your help!) in this chapter will be a striking example of
equivalence; specifically, we will show that three theorems are all connected by
biconditional statements! (This will be the first great example of a "The follow-
ing are equivalent. . . "-style theorem, like we pointed out in the proof strategy
for biconditional statements, in Section 4.9.6.)
5.1.1
Objectives
Since we have discussed induction before and are just returning to this topic,
we will forego the usual introductory matter at the beginning of this chapter.

Instead, we will summarize the main objectives of this chapter here via a series
of statements.
By the end of this chapter, you should be able to . . .
• State the Principle of Mathematical Induction and describe how its proof
is related to the set of natural numbers.
• State the Principle of Strong Mathematical Induction, compare and con-
trast this with the previous principle, and describe how it can be proven.
• Use inductive arguments to prove claims and, in particular, identify when
a strong inductive argument is required.
• Understand and explain some variants of mathematical induction, and
identify problems where these variants might be useful.
• State the Well-Ordering Principle and explain its relationship to mathe-
matical induction.
5.2
Regular Induction
This first section concerns the kind of inductive arguments we have seen be-
fore. You will see why, in the next section, we would choose to refer to this as
"Regular" Induction.
5.2.1
Theorem Statement and Proof
Here, let's recall the statement of the Principle of Mathematical Induction
that we gave in Chapter 3. Think about how it follows the Domino Analogy,
or whichever analogy works best to help you understand an inductive process.
You might have missed this Theorem statement if you didn't complete the Op-
tional Reading about Defining N, in Section 3.8, but that's okay. We're confident
you can still read this and formulate it in a way that corresponds to an inductive
process.
Theorem 5.2.1 (Principle of Mathematical Induction). Let P(n) be some
"fact" or "observation" that depends on the natural number n. Assume that
1. P(1) is a true statement.
2. Given any k $\in$N, if P(k) is true, then we can conclude necessarily that
P(k + 1) is true.
Then the statement P(n) must be true for every natural number n $\in$N.

> 🇨🇳 TODO: 待翻译
