---
title: Regular Induction
---

# Regular Induction

Look at all of these wordy sentences and phrases and hand-wavey terms. Some "fact" that depends on a natural number? Sounds like a variable proposition, right? "If . . . then we can conclude necessarily . . . " Sounds like a conditional statement, doesn't it? All of this language is meant to express some logical underpinnings, and we can restate the whole theorem now, using the concepts and notation developed in the previous chapter. Try your hand at doing this first, before looking at our version. While you're at it, try remembering how we proved that theorem. (Again, you might have missed this if you skipped this optional reading, and that's fine.) Look back to Section 3.8.2 and remind yourself, because we will follow that same proof here, but we'll use the logical symbols and tools that we now have in hand. Ready? Here we go!
<div class="def-theorem" markdown>
**Theorem 5.2.2 (Principle of Mathematical Induction). Let P(n) be a variable**
</div>
proposition. Suppose that (1) P(1) holds True, and (2) $\forall k \in \mathbb{N}. P(k) =\Rightarrow P$(k + 1) holds True Then $\forall n \in \mathbb{N}$. P(n) holds True. That's all there is to it! This encapsulates all the same ideas---that some initial fact holds, and that every fact implies the next one, making all the facts hold---but it does so using logical symbols and language. Do you see how they say the same thing? Make sure you do before reading on! Our goal now is to prove this theorem. Yes, we will prove that mathematical induction is a valid proof technique! Why shouldn't we? We proved (via a truth table) that a conditional statement is logically equivalent to its contrapositive, which gave us a proof strategy. Why shouldn't we prove this one, as well? Before we show the proof, though, we want you to read the section on defining the natural numbers, Section 3.8. It contains the following key definitions, which we will make use of in the forthcoming proof. In that section, we defined what it means to be an inductive set and then stated that N is the "smallest" inductive set, in the sense that N is a subset of all the inductive sets in the universe. This is the property we wanted N to have, and these definitions made it so. We will give you those important definitions right here---rewritten slightly, using logical notation and foregoing some set theoretic concepts---but we also suggest that you read that section to grasp the full extent of the discussion.
<div class="def-definition" markdown>
**Definition 5.2.3. Let I be a set. If the following conditions hold:**
</div>
1. 1 $\in I$, and 2. For any element k, the implication k \in I =$\Rightarrow k + 1 \in I$ holds; then I is called an inductive set.
<div class="def-definition" markdown>
**Definition 5.2.4. The set of all natural numbers is the set**
</div>
N := {x | for every inductive set I, x $\in I$}


> 🇨🇳 定义 5.2.3：设 $I$ 为集合。若下列条件成立：(1) 1 \in I，(2) 对任意元素 k，蕴涵式 $k \in I \Rightarrow k+1 \in I$ 成立；则称 I 为**归纳集**。定义 5.2.4：全体自然数的集合为 $\mathbb{N} := \{x \mid \text{对每个归纳集 } I,\ x \in I\}$。换言之，\mathbb{N} 是最小的归纳集：$\mathbb{N} = \bigcap_{I \in \{S \mid S \text{ 是归纳集}\}} I$。


Put another way, N is the smallest inductive set: N = \ I$\in${S|S is inductive} I Okay, now we're ready for the proof!
<div class="def-proof" markdown>
*Proof.* Let P(n) be a variable proposition, defined for every natural number n.
</div>
Suppose that the two conditions given in the theorem do hold, namely (1) P(1) holds True, and (2) $\forall k \in \mathbb{N}. P(k) =\Rightarrow P$(k + 1) holds True Let S be the set of instances for which P(n) is True. That is, define S = {n $\in \mathbb{N}$ | P(n) is True} By definition (using set-builder notation), S $\subseteq \mathbb{N}$. Condition (1) above guarantees that 1 \in S. Condition (2) above guarantees that \forall k $\in \mathbb{N}. k \in S =\Rightarrow k + 1 \in S$. Together, these two conditions guarantee that S is an inductive set. By the definition of N above, we therefore know that N \subseteq S. Thus, by a double-containent argument S = N. This means that the statement P(n) holds for every natural number n, i.e. \forall n $\in \mathbb{N}$. P(n) is True! Understanding the set-theoretic mechanics behin this proof are not essential to being able to use induction and write inductive proofs. However, we believe that thinking about these logical underpinnings can only help your understanding, or spark some curiosity in mathematical logic and set theory, or possibly both! The important thing that we have accomplished here, by restating the PMI, is that we now have a clear way of determining whether an inductive argument has succeeded. The entire crux of a "proof by induction" lies in verifying conditions (1) and (2) in the statement of the theorem (i.e. verifying that the "truth set" for the proposition P(n) is an inductive set).
### 5.2.2 Using Induction: Proof Template Taking the observation above, we can develop a proof template for a proper "proof by induction". (This can be added to the list of proof strategies from the last chapter, as well, thereby broadening our mathematical toolkit!) Notice that all of the steps in this template are motivated by making our proof readable, orderly, and logically correct: • We must define a proposition P(n)to show our reader what we aim to prove.


> 🇨🇳 我们必须定义命题 $P(n)$ 以向读者展示我们的证明目标。我们必须验证基础情形（BC）以满足数学归纳法原理中的条件 (1)。我们必须验证条件语句 $\forall k \in \mathbb{N}.\ P(k) \Rightarrow P(k+1)$ 以满足数学归纳法原理中的条件 (2)。为此，我们采用直接证明策略来证明条件语句，这包含两个部分：首先，建立归纳假设（IH），引入一个任意且固定的自然数 k 并假设 P(k) 成立；其次，执行归纳步骤（IS），由该假设推出 P(k+1) 也成立。至此，我们已验证了数学归纳法原理的全部条件，可以得出结论：$\forall n \in \mathbb{N}.\ P(n)$。


• We must verify the Base Case (BC) to show that condition (1) in the PMI is satisfied. • We must verify the the conditional statement $\forall k \in \mathbb{N}. P(k) =\Rightarrow P$(k+1) to show that condition (2) in the PMI is satisfied. To do this, we will apply the direct proof strategy for proving conditional statements; this has two parts: -- First, we make an Inductive Hypothesis (IH), which introduces an arbitrary and fixed natural number k and supposes P(k) holds. -- Second, we go through the Inductive Step (IS), which takes that assumption and deduces that P(k + 1), also holds. • Between these steps---the BC, the IH, and the IS---we have verified the conditions of PMI, and we can deduce its conclusion: $\forall n \in \mathbb{N}$. P(n). Finally, we make this conclusion to remind our reader of what we have accomplished. Template for a "Proof by Induction" Goal: Prove that $\forall n \in \mathbb{N}$. P(n)
<div class="def-proof" markdown>
*Proof.* Let P(n) be the proposition " ". We will prove $\forall n \in \mathbb{N}$. P(n) by induction on n. Base Case: Observe that P(1) holds because . Induction Hypothesis: Let k $\in \mathbb{N}$ be arbitrary and fixed. Suppose P(k) holds. Induction Step: Deduce that P(k + 1) also holds. By PMI, it follows that \forall n $\in \mathbb{N}$. P(n). Comments and Common Pitfalls What follows are some recommendations and suggestions. These are based on what we feel constitutes a good, well-written inductive argument, and also some mistakes that we see students consistently make over the years. • Be sure to define a proposition. Sometimes the claim is defined for you in the statement of a problem or exercise. However, it is not always defined explicitly as P(n). In that case, referring to a proposition P(n) later on has no meaning. So, be sure to define a statement if you want to refer to it! To be concise, you might say something like "Let P(n) be the claim defined
</div>


> 🇨🇳 请务必定义命题。有时问题陈述中已经为你定义了命题，但并非总是显式地写成 $P(n)$ 的形式，此时后续引用 $P(n)$ 便没有意义。所以，如果你想引用命题，请务必先加以定义！为简洁起见，你可以说"令 $P(n)$ 为上文定义的命题"。（但请确保 n 确实是上文命题中使用的变量字母，以保持一致性！）此外，请显式声明你在使用数学归纳法，并指出对哪个变量施行归纳。将来你可能会遇到归纳证明中有多个变量字母的情况。同时，仅因为你的证明遵循某种归纳结构，不要默认读者会理解你在使用归纳法——事先告知读者这一信息能省去他们很多麻烦。在基础情形中尽可能详尽、彻底。不要只是写出 P(1) 的含义就期待读者理解其为何为真——这个责任在于你，证明的书写者！归纳假设和归纳步骤一起构成 \Rightarrow 语句的直接证明策略。归纳假设引入一个任意且固定的自然数并假定蕴涵式 $P(k) \Rightarrow P(k+1)$ 的左端成立——这就是它被称为"假设"的原因。然后我们利用这一假设推出 P(k+1)，从而证明了数学归纳法原理中条件 (2) 的条件语句。请务必在此处量化变量 k！"假设 P(k)"这样的陈述没有意义——k 是什么？是自然数吗？"令 $k \in \mathbb{N}$ 并假设 $P(k)$"是可接受的形式。


above." (However, make sure that n is, indeed, the variable letter used in the claim above, for consistency's sake!) • Explicitly state that you are using mathematical induction and state the variable to which you are applying induction. In the future, you might have an induction proof where multiple variable letters are floating around. Also, just because your overall proof follows some kind of inductive structure, do not necessarily expect a reader to just understand you are using induction. Telling them this information up front saves them a lot of trouble. • Be as explicit and thorough as possible in the Base Case. Do not just write out what P(1) means and expect the reader to understand why it is True. This onus is on you, the proof-writer! Do not just write out what the statement P(1) is, itself, and put a ✓next to it. This does not prove anything! If the proposition P(1) is some kind of equation (which is common), demonstrate why both sides are actually equal, instead of just writing the equation and expecting a reader to see why it works out. • The IH and IS together apply the direct proof strategy for =$\Rightarrow$ statements. The IH introduces an arbitrary and fixed natural number and assumes the left-hand side of the implication P(k) =$\Rightarrow P$(k + 1). That's why it is our hypothesis. We then use this assumption to deduce P(k + 1). This proves the conditional statement in condition (2) in the PMI. Be sure to quantify the variable k here! A statement like "Assume P(k)" has no meaning. What is k? Is it a natural number? "Let k $\in \mathbb{N}$ and assume P(k)" is an acceptable form here. "Let k $\in \mathbb{N}$", to a mathematical reader, implicitly means "Let k $\in \mathbb{N}$ (be arbitrary and fixed)". • It helps to explicitly write out what P(k) means in the IH. For one, this helps a reader understand your assumption and follow the rest of the proof better. But also, this helps you figure out how to prove P(k + 1), which is your goal in this step. If you're struggling to work through this step in your head (perhaps on an exam or a homework problem), simply write out the meaning of P(k) at the top of your paper and the meaning of P(k + 1) at the bottom. Now do you see how they might be connected? Try to work downwards from P(k) and upwards from P(k + 1) and connect them in the middle.


> 🇨🇳 在归纳假设中显式写出 $P(k)$ 的含义会对证明很有帮助。一方面，这能帮助读者理解你的假设并更好地跟随后续证明；另一方面，这也有助于你弄清如何证明 P(k+1)——这正是此步骤的目标。如果你在脑海中难以理清此步骤（比如在考试或作业中），只需在纸的上方写出 P(k) 的含义，在下方写出 P(k+1) 的含义，然后试着从 P(k) 向下推导、从 $P(k+1)$ 向上推导，在中间汇合。此外，你必须在归纳步骤中的某处使用归纳假设！如果你根本没有用到归纳假设，那为什么需要归纳法呢？在使用归纳假设时，请明确说明你在这样做——不要默认读者会记得/认出你在做什么。最后，请做出结论，告诉读者你完成了什么。


• You must invoke the IH somewhere in the Induction Step! If you didn't use the IH at all, why did you need to use induction? When you use the IH, say that you are doing so. Don't expect the reader to remember/recognize that this is what you're doing. • Make a conclusion. Tell the reader what you have accomplished. Okay, now that we've dicussed how to write a good proof by induction, let's actually do so!
### 5.2.3 Examples
Here are a couple of examples of good induction proofs. Use them as guides when writing your own. We have omitted the usual discussion of how we came up with the arguments here, partly because we want to just emphasize the structure of the proofs, but also because we worked on those problem-solving aspects extensively in Chapter 2. Notice that we are using abbreviations for some components of these proofs, namely BC (for Base Case) and IH (for Induction Hypothesis) and IS (for Induction Step). Feel free to use this shorthand, as well!
Example 5.2.5. Sum of the odds is a square:
Claim: The sum of the first n odd natural numbers is n2.
(Note: We already saw this claim as a puzzle in Section 1.4.3, and then asked you to work through the inductive details in Section 2.3.4. We will present a good proof of the claim here.)
<div class="def-proof" markdown>
*Proof.* Let P(n) be the proposition
</div>
" 1 + 3 + 5 + $\cdot  \cdot  \cdot$ + 2n −1 = n X i=1 (2i −1) = n2 " We will prove that $\forall n \in \mathbb{N}$. P(n) by induction on n. BC: Consider n = 1. Notice that


> 🇨🇳 考虑 $n = 1$。注意到 $\sum_{i=1}^{1}(2i-1) = 1$，而 $1^2 = 1$，因此


X i=1 (2i −1) = 1 and 12 = 1 and so


> 🇨🇳 因此 $\sum_{i=1}^{1}(2i-1) = 1^2$，于是 $P(1)$ 为真，因为 $1 = 1$。


X i=1 (2i −1) = 12 Thus, P(1) is True, because 1 = 1.


> 🇨🇳 归纳假设（IH）：设 $k \in \mathbb{N}$ 为任意且固定的自然数。假设 P(k) 成立，即 $\sum_{i=1}^{k}(2i-1) = k^2$。归纳步骤（IS）：考虑 $k+1$。


IH: Let k $\in \mathbb{N}$ be arbitrary and fixed. Suppose P(k) holds. This means n X i=1 (2k −1) = n2 IS: Consider k + 1. We can write k+1 X i=1 (2i −1) = 2(k + 1) −1 + k X i=1 (2i −1) = 2k + 1 + k X i=1 (2i −1) by separating out the (k + 1)-th term of the summation. We now use the IH to replace the summation on the right-hand side and deduce that k+1 X i=1 (2i −1) = 2k + 1 + k2
Factoring then tells us
k+1 X i=1 (2i −1) = (k + 1)2 and therefore P(k + 1) holds. By the PMI, we conclude that $\forall n \in \mathbb{N}$. P(n). Here's another good induction proof of a useful fact about geometric series.
Example 5.2.6. Geometric series formula:
Claim: For every q $\in \mathbb{R}$ −{0, 1} and for every n $\in \mathbb{N}$, the following formula
holds: n−1 X i=0 qi = 1 + q + q2 + $\cdot  \cdot  \cdot$ + qn−1 = qn −1 q −1
<div class="def-proof" markdown>
*Proof.* Let q $\in \mathbb{R}$ −{0, 1} be arbitrary and fixed. Define P(n) to be the propo-
</div>
sition " n−1 X i=0 qi = qn −1 q −1 " We will prove $\forall n \in \mathbb{N}$. P(n) by induction on n. BC: Consider n = 1. Observe that n−1 X i=0 qi =


> 🇨🇳 考虑 $n = 1$。注意到 $\sum_{i=0}^{0} q^i = q^0 = 1$，因为 $q \neq 0$。同时，注意到 $\frac{q^n - 1}{q - 1} = \frac{q - 1}{q - 1} = 1$，因为 $q \neq 1$。于是 $P(1)$ 成立。


X i=0 qi = q0 = 1 since q \neq 0. Also, observe that qn −1 q −1 = q −1 q −1 = 1


> 🇨🇳 归纳假设（IH）：设 $k \in \mathbb{N}$ 为任意且固定的自然数，假设 P(k) 成立，即 $\sum_{i=0}^{k-1} q^i = \frac{q^k - 1}{q - 1}$。归纳步骤（IS）：要证 P(k+1) 成立，即 $\sum_{i=0}^{k} q^i = \frac{q^{k+1} - 1}{q - 1}$。


since q \neq 1. Thus, P(1) holds. IH: Let k $\in \mathbb{N}$ be arbitrary and fixed and suppose P(k) holds. This means k−1 X i=0 qi = qk −1 q −1 IS: WWTS P(k + 1) holds. (Remember, WWTS means "We want to show".) That is, WWTS k X i=0 qi = qk+1 −1 q −1 noticing that (k + 1) −1 = k. Observe that we can algebraically simplify and use our assumptions to write k X i=0 qi = k−1 X i=0 qi ! + qk summation notation = qk −1 q −1 + qk invoking IH = qk −1 + qk(q −1) q −1 common denominator = qk −1 + qk+1 −qk q −1 = qk+1 −1 q −1 algebra This shows that P(k + 1) holds, as well. By the PMI, \forall n $\in \mathbb{N}$. P(n) holds. Follow-up question: Why did we need q $\notin${0, 1} in the claim? What happens when q = 0? Where does this proof break down? Does the formula still holds? If so, prove it. If not, can you fix it? Try answering the same questions for q = 1, as well.
### 5.2.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What does the PMI (Principle of Mathematical Induction) state? How is it proven?


> 🇨🇳 (1) 数学归纳法原理（PMI）陈述了什么？它是如何被证明的？(2) 归纳证明的基础情形是什么？它与数学归纳法原理的陈述有何关系？(3) 归纳假设与归纳步骤有何关系？它们与数学归纳法原理的陈述有何关系？(4) 为什么在归纳步骤中的某处使用归纳假设是重要的？


(2) What is the Base Case of an induction proof? How does it relate to the statement of the PMI? (3) How are the Induction Hypothesis and Induction Step of a proof related? How do they relate to the statement of the PMI? (4) Why is it important to invoke the Induction Hypothesis somewhere in the Induction Step? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Prove that n X i=1 i3 = n(n + 1)


> 🇨🇳 (1) 证明 $\sum_{i=1}^{n} i^3 = \left[\dfrac{n(n+1)}{2}\right]^2$ 对一切 $n \in \mathbb{N}$ 成立。(2) 证明每个奇自然数的平方比 8 的倍数多 1，即证明 $(2n+1)^2 - 1$ 是 8 的倍数对一切 $n \in \mathbb{N}$ 成立。(3) 考虑以下命题：对一切 $n \in \mathbb{N}$，$7^n - 4^n$ 是 3 的倍数。用逻辑符号重写该命题，然后用归纳法证明它。(4) 回忆斐波那契数列的定义：$f_0 = 0$，$f_1 = 1$，$\forall n \in \mathbb{N} \setminus \{1\}.\ f_n = f_{n-1} + f_{n-2}$。用归纳法证明下列命题对一切 $n \in \mathbb{N}$ 成立：(a) $\sum_{i=1}^{n} f_i = f_{n+2} - 1 (b) \sum_{i=1}^{n} f_{2i-1} = f_{2n} (c) f_{4n}$ 是 3 的倍数 (d) 挑战 1：n 是 3 的倍数 $\Rightarrow f_n$ 是偶数 (e) 挑战 2：n 不是 3 的倍数 \Rightarrow $f_n$ 是奇数


2 holds for every n $\in \mathbb{N}$. (2) Prove that the square of every odd natural number is one more than a multiple of 8. That is, prove that (2n + 1)2 −1 is a multiple of 8 for every n $\in \mathbb{N}$. (3) Consider this claim: 7n −4n is a multiple of 3, for every n $\in \mathbb{N}$. Rewrite this claim using logical symbolic notation. Then, prove it by induction. (4) Recall that the Fibonacci Numbers are defined by f0 = 0 and f1 = 1 and \forall n $\in \mathbb{N}$ −{1}. fn = fn−1 + fn−2 Prove the following claims hold for every n $\in \mathbb{N}$, by induction on n: (a) n X i=1 fi = fn+2 −1 (b) n X i=1 f2i−1 = f2n (c) f4n is a multiple of 3 (d) Challenge 1: (n is a multiple of 3) =\Rightarrow(fn is even) (e) Challenge 2: (n is not a multiple of 3) =$\Rightarrow$(fn is odd)


> 🇨🇳 练习题解答提示：对于斐波那契数列的归纳证明，注意在 (d) 和 (e) 中需要仔细分析 $f_n$ 的奇偶性与 $n$ 是否为 3 的倍数之间的关系。建议对 (d) 和 (e) 使用强归纳法（见下一节）。


## 5.3 Other Variants of Induction Now that we're really comfortable with how induction works and have seen many examples, we can show you two modifications of this method. The idea is that there is "nothing special" about using induction to prove a statement holds for every n $\in \mathbb{N}$. Don't get us wrong; there is a lot that's special about N! What we mean is that it's possible to use induction to prove that a statement holds for every n $\in S$, where S might be some other kind of set. We will describe these sets for you in the following discussions and examples.
### 5.3.1 Starting with a Base Case other than n = 1 We need to have a base case in an induction proof, but there's nothing that says it always has to be n = 1. Perhaps we have a proposition P(n) that is True for n = 1 and n = 2, but then somehow False for n = 3 and n = 4, but then True for every n that is at least 5. How could we prove these claims? Well, we could just show the individual cases for n = 1, 2, 3, 4 separately, and then use induction to prove all the others. This will work because the set N −{1, 2, 3, 4} is also an inductive set. In terms of the Domino Analogy, this is like saying, "Let's just skip a few dominoes and start the line falling at n = 5. The rest will all fall down in the exact same way as we'd expect." In fact, we can even allow ourselves to talk about negative integers here! Let's slide to the left on the number line a bit and imagine that we actually have a line of dominoes numbered starting from, say, −3. That is, we'd have Domino
# −3 and Domino # −2 and Domino # −1 and Domino #0 and Domino #1
and all the rest. We can start the line falling at n = −3 and know that they will all fall into each other in much the same way as before. The whole idea here is that we still have an infinite line of dominoes moving offto the right with no gaps between them. It doesn't matter what numerical label we assign to the first domino. A line of dominoes like this will topple into each other no matter how we number that first one. This idea is what the next theorem encapsulates.
<div class="def-theorem" markdown>
**Theorem 5.3.1 (Induction with any base case). Let P(n) be a variable propo-**
</div>
sition. Let M $\in \mathbb{Z}$ be arbitrary and fixed. Let S = {z $\in \mathbb{Z}$ | z $\geq M$}. Suppose that (1) P(M) holds True, and (2) $\forall k \in S. P(k) =\Rightarrow P$(k + 1) holds True Then \forall n $\in S$. P(n) holds True. This theorem says exactly what we were discussing: if we want to prove a proposition holds for every value greater than or equal to some specific value (M, in the theorem statement), then we can just start inducting from that value.


> 🇨🇳 定理 5.3.1（任意基础情形的归纳）：设 $P(n)$ 为变元命题，$M \in \mathbb{Z}$ 为任意且固定的整数。令 $S = \{z \in \mathbb{Z} \mid z \geq M\}$。假设：(1) $P(M)$ 为真，(2) $\forall k \in S.\ P(k) \Rightarrow P(k+1)$ 为真。则 $\forall n \in S.\ P(n)$ 为真。该定理说明：若要证明命题对某个特定值 $M$ 以上的所有值都成立，只需从该值开始施行归纳即可——基础情形不必总是 $n = 1$。


