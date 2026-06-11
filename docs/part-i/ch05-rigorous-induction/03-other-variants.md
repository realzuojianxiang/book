---
title: Other Variants of Induction
---

# Other Variants of Induction

We make that our BC and apply the IH and IS to every value greater than or equal to it. Everything else is exactly the same. Formal Proof For the sake of illustration and completeness, we will formally prove this theorem. We hope that the discussion above---referencing the Domino Analogy---will help you intuitively understand how this works. Working through this proof will not directly and immediately affect your ability to apply induction as a technique. However, we do think that reading through it and trying to understand how it works will give you a better grasp of induction and proof techniques, and it will perhaps give you a deeper apprecation of the mathematics at work here. Specifically, we will use PMI to prove this modified version of itself!
<div class="def-proof" markdown>
*Proof.* Let P(n) be a variable proposition. Let M ∈Z be arbitrary and fixed.
</div>
Let S = {z ∈Z | z ≥M}. Suppose that (1) P(M) holds True, and (2) ∀k ∈S. P(k) =⇒P(k + 1) holds True Our goal is to prove that ∀n ∈S. P(n) holds True. Define the proposition Q(n) by setting Q(n) ⇐⇒P(n + M −1) Notice that, by algebraically manipulating the inequality, we have n ≥1 ⇐⇒n + M −1 ≥M This means that our goal now is to prove that ∀n ∈N. Q(n) holds True. (Doing so will prove that ∀n ∈S. P(n).) We will prove this by induction on n. BC: We know P(M) holds, by assumption. Notice that n + M −1 = M ⇐⇒ n = 1. This means Q(1) holds. IH: Let k ∈N be arbitrary and fixed. Suppose Q(k) holds. IS: Since Q(k) holds, we know P(k + M −1) holds. Also, since k ∈N, we know k ≥1. Thus, k + M −1 ≥M. Thus, By condition (2) that we assumed, we can deduce that P((k+M −1)+1) holds, i.e. that P(k + M) holds. This tells us that Q(k + 1) holds. By PMI, we deduce that ∀n ∈N. Q(n) holds. Then, by the definition of Q(n), this tells us that ∀n ∈S. P(n) holds.


> 🇨🇳 TODO: 待翻译


As we said, try to work through the details of the proof but, in general, just keep in mind the intuitive idea that we're just "sliding over" and using a different base case. The mechanics of the inductive process are identical.
Example
Let's see this modified technique in action. In fact, the example we will show you is of the flavor that we hinted at when introducing this method, wherein some proposition holds for a few small values, doesn't hold for some other small values, but does hold for every value after a certain point.
Example 5.3.2. How 2n compares to n2:
Claim:
2n > n2 ⇐⇒n ∈{0, 1} ∪{z ∈N | z ≥5} That is, the only integers z that satisfy 2z > z2 are z = 0, 1, 5, 6, 7 . . .. (We will leave it to you to play around and figure out how we might have come up with such a claim. Typically, as you will see in this section's exercises, such an inequality might be presented along with the question, "For which values of n does this hold?" In that case, you would have to do some scratch work to identify your claim before starting an induction proof.)
<div class="def-proof" markdown>
*Proof.* Let P(n) be the proposition " 2n > n2 ".
</div>
First, observe the following cases: 20 > 02 ⇐⇒1 > 0 so P(0) is True 21 > 12 ⇐⇒2 > 1 so P(1) is True 22 > 22 ⇐⇒4 > 4 so P(2) is False 23 > 32 ⇐⇒8 > 9 so P(3) is False 24 > 42 ⇐⇒16 > 16 so P(4) is False Notice that whenever z ≤−1, we have 2z < 1 and z2 ≥1, so 2z ̸> z2. Thus, P(n) is False for every n that satisfies n ≤−1. Next, define S to be the set S = {z ∈N | z ≥5}. We will prove ∀n ∈S. P(n) holds by induction on n. BC: Observe that P(5) holds because 25 = 32 and 52 = 25 and 32 > 25. IH: Let k ∈N be arbitrary and fixed. Suppose that P(k) holds. IS: Since k ∈S, we know k ≥5 and so k > 4. Thus, k −1 > 3 and so (k −1)2 > 9; certainly, then, (k −1)2 > 2.


> 🇨🇳 TODO: 待翻译


Observe the following chain of manipulations of this inequality: (k −1)2 > 2 =⇒(k −1)2 −2 > 0 =⇒k2 −2k −1 > 0 =⇒k2 > 2k + 1 =⇒2k2 > k2 + 2k + 1 =⇒2k2 > (k + 1)2 Since we observed the first inequality holds, we can deduce that the final inequality above also holds. (Note: In case you didn't realize, this chain of reasoning is a solution to practice exercise 2 from Section 4.9.9! To work this out, we did some scratch work, starting with the desired inequality at the bottom and "working backwards" until we found something obviously True. In writing it up here, we started with that obvious fact and worked down to the desired conclusion.) By the IH P(k), we know k2 < 2k. This tells us 2k2 < 2 · 2k = 2k+1 Applying the transitivity property of inequalities, we can deduce that (k + 1)2 < 2k2 < 2k+1 and so P(k + 1) holds. By PMI, ∀n ∈S. P(n) holds. Overall, we have considered every z ∈Z. We observed that P(z) fails for z ≤−1, that it holds for z = 0, 1, that it fails for z = 2, 3, 4, and that it holds for z ≥5. Together, these observations prove the claim. Phew! There was actually a lot going on in that proof. Did you notice that the claim was phrased as an if and only if, so that we had to consider all the integers in our proof? That was tricky, but we did it!
### 5.3.2 Inducting Backwards This variant of induction is useful when a proposition P(n) happens to hold for all values of n less than some particular value. In terms of the Domino Analogy, this is like imagining our infinite line of dominoes running offto the left, instead of to the right. We already know that, for the reasons discussed in the previous section, it doesn't matter how we number them. Now, we can see that it also doesn't matter which direction they're going; they'll obey the same principles! The following theorem encapsualtes this observation.
<div class="def-theorem" markdown>
**Theorem 5.3.3 (Backwards induction). Let P(n) be a variable proposition.**
</div>
Let M ∈Z be arbitrary and fixed.


> 🇨🇳 TODO: 待翻译


Let S = {z ∈Z | z ≤M}. Suppose that (1) P(M) holds True, and (2) ∀k ∈S. P(k) =⇒P(k −1) holds True Then ∀n ∈S. P(n) holds True. Notice the differences between this and Theorem 5.3.1 Formal Proof At this point in our development, we feel comfortable giving you important theorems to prove. Specifically, we want you to prove this modified version of PMI you see above, Theorem 5.3.3! Letting you work through the details yourself, instead of just seeing us perform them for you, will be far more helpful in the long run. Furthermore, the details of this proof we have in mind are quite similar to those for the proof we gave you (in Section 5.3.1) of Theorem 5.3.1. Leaving a proof as an "exercise for the reader" is actually quite common in mathematics, and in mathematics books, in particular. We're just doing our part to help you get used to this phenomenon! ,
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 1 in Section 5.3.4.
</div>
We will not show an example of this method in action because we believe it is exactly like the standard method of induction we have already seen. In fact, if you worked through the details of the proof above, you can probably even see how to "make up" an example for this section by just modifying some examples we've already seen! (What if we reverse an inequality . . . )
### 5.3.3 Inducting on the Evens/Odds Let's motivate this section with an observation, which will lead us into the first example usage of this method. Consider the sequence of perfect square numbers: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, . . . Look at what happens when we divide them by 8; specifically look at the remainders (indicated by the numerators of the fractions in each case): 0 + 1 8, 0 + 4 8, 1 + 1 8, 2 + 0 8, 3 + 1 8, 4 + 2 8, 6 + 1 8, . . . Notice that we left fractions like 4 8 and 2 8 unsimplified, keeping the denominator as 8, to indicate the remainders. Those remainders follow this pattern: 1, 4, 1, 0, 1, 2, 1, . . .


> 🇨🇳 TODO: 待翻译


It looks like every other remainder is 1. In fact, it looks like the remainder is 1 when we divide an odd number squared by 8. Interesting! You might wonder whether this pattern continues. A reasonable way to address this idea is to just jump right in and try to prove this claim by induction and see if it works. If it does succeed, then we have successfully discovered and proven a fact. If it doesn't succeed, then we might be able to figure out where it fails and why. This is a good, general recommendation for mathematical discovery: if you want to see if something is True, just try to prove it and see what happens!
Example
Try to work through the details of this one on your own before reading on. In doing so, you will have to figure out how to induct on the set of odd natural numbers, not all the natural numbers as we have done before. We will actually present the proof of this claim and afterwards discuss how the method works, but you should absolutely work on this on your own first! . . .
Example 5.3.4. Remainders of odd squares when divided by 8:
Claim: Let O be the set of odd natural numbers; that is,
O = {n ∈N | ∃m ∈N ∪{0}. n = 2m + 1} Let P(n) be the proposition "n2 is 1 more than a multiple of 8". Then ∀n ∈O. P(n)
<div class="def-proof" markdown>
*Proof.* Let P(n) be defined as in the claim above. We will prove ∀n ∈O. P(n)
</div>
by induction on n. BC: Observe that 12 = 1 and 1 = 0 · 8 + 1 (i.e. 1 is a multiple of 8 plus 1). Thus, P(1) holds. IH: Let k ∈O be arbitrary and fixed. Suppose P(k) holds. IS: Our goal now is to deduce P(k +2) holds. (This is because k +2 is the next odd natural number, after k.) Since k + 2 is odd, by assumption, we know ∃m ∈N ∪{0}. k = 2m + 1. Let such an m be given. By the IH, we know ∃ℓ∈N. k2 = 8ℓ+ 1. Let such an ℓbe given. Now, we take these observations and use them to see that (k + 2)2 = k2 + 4k + 4 = (8ℓ+ 1) + 4(2m + 1) + 4 = 8ℓ+ 8m + 8 + 1 = 8(ℓ+ m) + 1 Since ℓ, m ∈Z, we know ℓ+ m ∈Z, as well. Thus, (k + 2)2 is one more than a multiple of 8. Therefore, P(k + 2) holds.


> 🇨🇳 TODO: 待翻译


By induction, P(n) holds for every n ∈O. Follow-up questions: Can you also prove that the remainders of even squares when divided by 8 are not 1? (This would make the claim an if and only if statement.) Can you identify a pattern in the remainders of those even squares? Can you prove your claims? (Hint: You probably won't need induction for these claims!) Discussion of Method Let's discuss why this works. The underlying principle is exactly the same as the other forms of induction we have seen. The only difference lies in the induction step. Since the odd natural numbers are "two steps apart", our goal is to prove ∀k ∈O. P(k) =⇒P(k + 2) This encapsulates the same idea as standard induction: take one instance of the proposition and use it to deduce the "next" instance holds. The only difference here lies in what we mean by "next". For completeness' sake, we will state a theorem that conveys this method. Again, we will leave it to you to fill in the details of the proof.
<div class="def-theorem" markdown>
**Theorem 5.3.5 (Induction on the odds). Let O be the set of odd natural num-**
</div>
bers. Let P(n) be a variable proposition. Suppose that (1) P(1) holds, and (2) ∀k ∈O. P(k) =⇒P(k + 2) Then ∀n ∈O. P(n) holds.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 2 in Section 5.3.4.
</div>
Thinking in a very similar way, we can see that induction on the even natural numbers will also work. Here is a theorem that states this. Again, we will leave the proof to you.
<div class="def-theorem" markdown>
**Theorem 5.3.6 (Induction on the evens). Let E be the set of even natural**
</div>
numbers. Let P(n) be a variable proposition. Suppose that (1) P(2) holds, and (2) ∀k ∈E. P(k) =⇒P(k + 2) Then ∀n ∈E. P(n) holds.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 2 in Section 5.3.4.
</div>


> 🇨🇳 TODO: 待翻译


Combining and Modifying These Methods Let's say we have a proposition P(n) and we want to prove P(n) holds for every n ∈N. Perhaps the proposition, and the underlying ideas, are somehow tricky, and a regular old induction proof completely eludes us. Maybe it's because of some algebraic trick, maybe we just can't see how to do it in the most efficient way, or maybe there's actually something profound underlying the proposition that prevents us from doing so. Whatever the reason, we might be able to use a combination of these new induction methods and prove the proposition holds for all n ∈N in a couple of pieces. We can think of these new methods as "jumping" induction methods. Proving a proposition holds for every odd natural number amounts to the exact same inductive technique as before, but we just "skip over" the evens by adjusting what happens in the induction step. The same goes for inducting on the evens (although we also adjust the base case slightly, since 2 is the first even, not 1). If we perform the "odds" method first and then the "evens" method, overall we have proved that the proposition holds for all naturals. The following example does something just like this, but you'll notice that it actually makes "jumps" of size 3 (instead of 2, like with the "odds" and "evens" methods). We won't state and prove (or even ask you to do so) theorems that convey these methods. At this point, we will rely on our collective intuition for how induction works and point out that these theorems/proofs will be very similar to the ones we have been seeing. If you feel like getting the practice, or want to have them for your notes and records, by all means go ahead and state and prove theorems about the method we are about to use!
Example 5.3.7. Powers of 2 and multiples of 7:
Claim: For every n ∈N, the number 2n + 1 is not a multiple of 7.
(At this point, we recommend doing some scratch work to identify a pattern in the remainders of the numbers 2n + 1 when divided by 7. You'll see that they follow a cycle of length 3. Neato! That's essentially what we will prove here; it's just that the claim wasn't presented in that way, so we had to do some work on the side to reformulate it and come up with a proof.)
<div class="def-proof" markdown>
*Proof.* Define the sets A1, A2, A3 to be
</div>
A1 = {n ∈N | ∃m ∈N ∪{0}. n = 3m + 1} = {1, 4, 7, 10, . . . } A2 = {n ∈N | ∃m ∈N ∪{0}. n = 3m + 2} = {2, 5, 8, 11, . . . } A3 = {n ∈N | ∃m ∈N ∪{0}. n = 3m} = {3, 6, 9, 12, . . . } (That is, these three sets partition N based on remainders when divided by 3.) Let P(n) be the proposition "2n + 1 is not divisible by 3". We will prove ∀n ∈N. P(n) holds, by induction.


> 🇨🇳 TODO: 待翻译


Define the propositions Q(n) and R(n) and S(n) as follows: Q(n) is " ∃ℓ∈N ∪{0}. 2n + 1 = 7ℓ+ 3 " R(n) is " ∃ℓ∈N ∪{0}. 2n + 1 = 7ℓ+ 5 " S(n) is " ∃ℓ∈N ∪{0}. 2n + 1 = 7ℓ+ 2 " Observe that ∀n ∈N.  Q(n) ∨R(n) ∨S(n)  =⇒P(n) This is because a number that is a multiple of 7 plus 3 is not a multiple of 7, and neither is a multiple of 7 plus 5 or a multiple of 7 plus 2. First, we will prove that ∀n ∈A1. Q(n) holds, by induction on n. BC: Observe that 21 + 1 = 3 = 0 · 7 + 3. Thus, Q(1) holds. IH: Let k ∈A1 be arbitrary and fixed. Suppose Q(k) holds. IS: Our goal now is to deduce that Q(k + 3) holds. Since k ∈A1, we know ∃m ∈N. k = 3m + 1. Let such an m be given. By the IH, we know ∃ℓ∈N. 2k + 1 = 7ℓ+ 3. Let such an ℓbe given. This means 2k = 7ℓ+ 2. We can deduce that 2k+3 = 23 · 2k = 8 · (7ℓ+ 2) = 56ℓ+ 16 Thus, 2k+3 + 1 = 56ℓ+ 17 = 7(8ℓ) + 14 + 3 = 7(8ℓ+ 2) + 3 and so Q(k + 3) holds, as well. Therefore, ∀n ∈A1. Q(n). Second, we will prove that ∀n ∈A2. R(n) holds, by induction on n. BC: Observe that 22 + 1 = 5 = 0 · 7 + 5. Thus, R(2) holds. IH: Let k ∈A2 be arbitrary and fixed. Suppose R(k) holds. IS: Our goal now is to deduce that R(k + 3) holds. By the IH, we know ∃ℓ∈N. 2k + 1 = 7ℓ+ 5. Let such an ℓbe given. This means 2k = 7ℓ+ 4. We can deduce that 2k+3 = 23 · 2k = 8 · (7ℓ+ 4) = 56ℓ+ 32 Thus, 2k+3 + 1 = 56ℓ+ 33 = 7(8ℓ) + 28 + 5 = 7(8ℓ+ 4) + 5


> 🇨🇳 TODO: 待翻译


and so R(k + 3) holds, as well. Therefore, ∀n ∈A2. R(n). Third, we will prove that ∀n ∈A3. S(n) holds, by induction on n. BC: Observe that 23 + 1 = 9 = 1 · 7 + 2. Thus, S(3) holds. IH: Let k ∈A3 be arbitrary and fixed. Suppose S(k) holds. IS: Our goal now is to deduce that S(k + 3) holds. By the IH, we know ∃ℓ∈N. 2k + 1 = 7ℓ+ 2. Let such an ℓbe given. This means 2k = 7ℓ+ 1. We can deduce that 2k+3 = 23 · 2k = 8 · (7ℓ+ 1) = 56ℓ+ 8 Thus, 2k+3 + 1 = 56ℓ+ 9 = 7(8ℓ) + 7 + 2 = 7(8ℓ+ 1) + 2 and so S(k + 3) holds, as well. Therefore, ∀n ∈A3. S(n). Overall, we have proven that either Q(n) or R(n) or S(n) holds for every natural number (depending on a number's remainder when divided by 3). Accordingly, every natural number has the property that 2n + 1 is not a multiple of 7. In actuality, we proved a stronger result in our proof than what the claim presented. That is, not only did we show that no number of the form 2n +1 is a multiple of 7, but we also showed exactly how those numbers fail to be multiples of 7. In this section's exercises, we have included a couple of exercises that guide you through a proof like this by identifying the "jumps" and the claims. In this chapter's exercises, Section 5.7, we have included some problems that might require this kind of argument (but we won't necessarily tell you the overall structure of the argument, as we've done here). It's worth mentioning, at this point, that you could quite easily adapt these methods to any situation you face, as long as the "jumps" you want to make follow some easily identifiable pattern. In the previous example, we made jumps of size 3, and so we split the set of all natural numbers into three sets and jumped along within those sets. In essence, this relies on the fact that we had a "formula" for how to get to the "next" instance of the proposition: we start with P(k) and try to deduce P(k + 3). You could conceivably make jumps of size 4, or 10, or even make jumps that double your value; that is, you could prove that some proposition P(n) holds for every n that is a power of 2, say, by proving P(1) holds, and ∀n ∈N. P(n) =⇒P(2n) Again, all of this relies on having some kind of "formula" or "rule" that tells us what the next instance under consideration is. For this reason, we cannot induct on the set of all prime numbers. If you're trying to prove some fact holds


> 🇨🇳 TODO: 待翻译


for every prime number, don't even bother trying to use induction! You'd have to have some "rule" that says, "If k is a prime number, then the next prime number is . . . ". If you know of such a rule, the world of mathematics would love to hear from you! This would answer many outstanding, unresolved questions about the prime numbers and make you the most famous mathematician in all of history. Seriously!
### 5.3.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) How does the Domino Analogy describe an induction proof with a base case that is not 1? (2) Write out a proof template for proving a proposition P(n) that holds for every odd natural number greater than or equal to 7. (3) Why can't we "induct on the primes"? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Prove Theorem 5.3.3. (2) Prove Theorems 5.3.5 and 5.3.6. (3) State a theorem that represents a method for inducting on the set of all multiples of 5. Prove your theorem. (4) Consider the inequality n3 < 3n−1. (a) Prove that the inequality holds for every n that satisfies n ≥6. (b) Prove that the inequality fails for n ∈{1, 2, 3, 4, 5}. (This is easy.) (c) Prove that the inequality holds for every n that satisfies n ≤0. (5) Define a sequence of numbers by x1 = 2 and x2 = 2 and ∀n ∈N −{1, 2}. xn = xn−2 + 1


> 🇨🇳 TODO: 待翻译


Let P(n) be the proposition " xn = 1 2(n + 1) + 1


> 🇨🇳 TODO: 待翻译


 1 + (−1)n  (a) Let O be the set of odd natural numbers. Prove that ∀n ∈O. P(n) by induction. (b) Let E be the set of even natural numbers. Prove that ∀n ∈E. P(n) by induction. (6) Consider the following claim: n X k=1 (−1)k−1k2 = (−1)k−1 n X k=1 k That is, we claim that 12 −22 + 32 −42 + · · · + (−1)n−1n2 = (−1)n−1(1 + 2 + 3 + · · · + 9) holds for every n ∈N. (a) Prove that the above formula holds for n = 1 and n = 2. (b) Prove that whenever the formula holds for k, it also holds for k + 2. (c) Explain intuitively why (a) and (b) prove the claim.
## 5.4 Strong Induction Now, we will see why our previous work with induction constitutes "Regular" Induction. What follows is a technique known as Strong Induction. You will see why the term applies. Specifically, it refers to the inductive hypothesis, wherein we make a stronger assumption; informally, we will assume "more stuff" in that part of our proof, which allows us to make a conclusion more easily (or, sometimes, at all). The important part of this section, in addition to seeing several examples to get a handle on this modified technique, will be to actually prove that this stronger technique is even valid. To do that, we will actually invoke the PMI, itself!
### 5.4.1 Motivation Look back to the examples from Section 2.4. There, we made some observations about the number of ways to tile a 2 × n rectangular board with dominoes, and we played the game of Takeaway. In working through the inductive arguments for each of those examples, we found the situation to be slightly different than previous inductive arguments. When we proved something like n X k=1 n(n + 1)


> 🇨🇳 TODO: 待翻译


