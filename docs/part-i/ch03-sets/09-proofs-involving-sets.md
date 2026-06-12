---
title: Proofs Involving Sets
---

# Proofs Involving Sets

means that A and B have the same elements in them"---but this is not the type of language/ideas we want to use in a rigorous proof. To prove a statement like A = B, we need you to appeal to the definition of "=" in the context of sets: A = B if and only if A $\subseteq B and B \subseteq A$. This is what we mean when we say "satisfy a definition" or "appeal to a definition": to prove that some mathematical object has a certain property, you must demonstrate that the object satisfies the formal definition of that property. If you aren't familiar with that definition, or have forgotten how to state it precisely... by all means, go look it up! We realize this is a lot of new information to ingest, and there's nothing wrong with forgetting something when it's still new to you. By doing this, you'll start to internalize these ideas more quickly and more solidly. You'll see how we use the definitions of, for instance, "\subseteq" and "=" and "$\cap$" and so on in the examples below. For each proposition/lemma, we will end up writing a formal proof, but we will also write a little bit about how we would approach coming up with such a proof. Oftentimes this is the difficult part! We think you'll notice that many of those explanations will amount to just recalling a relevant definition and thinking about what it means and how it applies in the given situation. In a way, that's what a lot of mathematics is. We just allow our definitions we use to get more and more complicated.
### 3.9.2 Proving "$\subseteq$" Recall the definition of subset, because we will use it frequently here:
<div class="def-definition" markdown>
**Definition 3.9.1. Given two sets A and B, if every element of A is also an**
</div>
element of B, then we say A is a subset of B. Say we are presented with the following problem: Let A be the set... and let B be the set... Prove that A $\subseteq B$. How can we satisfy the definition of A $\subseteq B$ to prove this claim? Yes, the intuitive idea is that "every element of A is also an element of B", but we shouldn't just try to dance around the issue and try to make that sentence our conclusion. Rather, we need to verify that every element of A is also necesarily an element of B. This is where the wonderful phrase "arbitrary and fixed" will come in handy! The Phrase "Arbitrary and Fixed" How can we talk about all possible elements of A all at once? Of course, we might not need to do this if A has only, say, 3 elements; then, we can just work with them one by one. But what if A has 100 elements? Or 1 million? Or infinitely many? How can we prove something about all of them at once in a reasonable way? What we will do is introduce an arbitrary and fixed element of A so we have something to work with. This element will be arbitrary in the sense that


> 🇨🇳 意味着" A 和 B 含有相同的元素"——但这不是我们在严谨证明中想要使用的语言/思想。要证明 $A = B$ 这样的命题，我们需要诉诸集合语境下"="的定义：A = B 当且仅当 $A \subseteq B$ 且 $B \subseteq A$。这就是我们说"满足定义"或"诉诸定义"的含义：要证明某个数学对象具有某种性质，你必须证明该对象满足该性质的形式定义。如果你不熟悉那个定义，或者忘了如何精确表述——请去查阅！我们意识到需要消化大量新信息，忘记新学的东西是完全正常的。通过查阅定义，你会更快更扎实地内化这些思想。


we make no extra assumptions about what it is or what properties it has, only that it is an element of A. This element will be fixed in the sense that we will assign it some variable name (usually a letter, like a or x or t or something) and this letter will represent the same object throughout the remainder of our proof. As long as we can prove our goal for this element, then we will have simultaneously proven something about all elements of A. Voil`a!
Examples
Let's see this process in action to really get the point across. We'll begin with the statement to be proven, then describe our thought processes in coming up with a proof, and then present our formal, written proof.
<div class="def-theorem" markdown>
**Lemma 3.9.2. Let A, B, X be any sets.**
</div>
If X $\subseteq A and X \subseteq B, then X \subseteq A \cap B$. Intuition: Consider drawing a Venn diagram to represent this situation. To make sure the assumptions X $\subseteq A and X \subseteq B$ both hold true, we need to make the set X "lie inside" both A and B. Accordingly, this means X must lie entirely "inside" where A and B overlap, which is what A \cap B represents. This helps us realize that this statement is, indeed, True. But it doesn't prove anything! To prove the statement, we will introduce an arbitrary and fixed element x \in X. What do we know about it? Well, we assumed that X \subseteq A. The definition of "\subseteq" means that any element of X is also an element of A. But we know x is an element of X; this means it is also an element of A. How convenient! We can make some similar statements about x and X and B that will tell us x \in B. What does this mean, overall? Oh hey, the definition of "\cap" applies, and tells us x \in A $\cap B$. Brilliant! Now, let's write it up.
<div class="def-proof" markdown>
*Proof.* Let x $\in X$ be arbitrary and fixed.
</div>
By assumption X $\subseteq A, so x \in A$, as well, by the definition of \subseteq. Similarly, by assumption X \subseteq B, so x \in B, as well. Since x \in A and x \in B, this means that x \in A \cap B, by the definition of \cap. Overall, we have shown that whenever x \in X, it is also true that x \in A \cap B. Since x \in X was arbitrary, we conclude that X \subseteq A $\cap B$. Not so bad, right? Let's try another one, a slightly harder one, even.
Proposition 3.9.3. Let A and B be any sets. Then, P(A)$\cap P(B) \subseteq P(A\cap B$).
Whoa, is this really true? Look back at Problem 6 in Section 3.5, and you'll see an example. This claim states that it is true, in general, and not just for that example. Let's figure out why, and then prove it. Intuition: There are several layers of definitions at work here. In particular, the power set operation might be confusing to you. The key is to just remember


> 🇨🇳 我们不再对它做额外假设，只知道它是 A 的元素。这个元素是"固定的"，因为我们会给它赋予某个变量名（通常是一个字母，如 $a$、$x$、$t$ 等），且在证明的剩余部分这个字母始终代表同一对象。只要我们能为这个元素证明目标，就同时证明了关于 A 的所有元素的命题。瞧！


that definition: P(A) is the set of all subsets of A. Now, the main claim here is one of a subset relationship: whatever the set P(A) $\cap P$(B) is (we'll analyze it later, but it's important that you recognize immediately what type of object it is: a set), it is supposed to be a subset of whatever the set P(A \cap B) is. That's it, and it's important to notice that this is really motivates the overarching form of the forthcoming proof. Without even having to think about what P(A) \cap P(B) means, we can be sure that our proof will start with "Let X \in P(A) \cap P(B) be arbitrary and fixed". This is because we need to satisfy the definition of "\subseteq" by taking any old element of the set on the left and deducing that it is also an element of the set on the right. This is what we mean by the structure of the proof. What does an element X \in P(A) $\cap P$(B) "look like"? It's a set, and it's an element of both P(A) and P(B). This means... well, we're actually going to skip ahead and jump right into the formal proof now, because we'll just find ourselves repeating the same words down below anyway. But before going ahead to read ours, we think you should go offand try to write your own proof. Then, when you're done, you can compare and see whether you are correct, whether it has the same steps as ours, whether it's written clearly, and so on. See what you can do!
<div class="def-proof" markdown>
*Proof.* Let X $\in P(A) \cap P$(B) be arbitrary and fixed.
</div>
By the definition of $\cap, this means X \in P(A) and X \in P(B). Since X \in P(A), we know X \subseteq A$, by the definition of power set. Similarly, since X $\in P(B), we know X \subseteq B. Since X \subseteq A and X \subseteq B$, we know that X $\subseteq A \cap B$ by Lemma 3.9.2 that we just proved. Now, since X $\subseteq A \cap B, we know X \in P(A \cap B$), by the definition of power set. Since X was arbitrary, we conclude that P(A) $\cap P(B) \subseteq P(A \cap B$). Did you do what we did? Did you also cite the previous lemma? Did you instead prove that result all over again without realizing it? Consider that a lesson learned! One of the major benefits of proving results is that we get to use them in later proofs! There's nothing technically wrong with proving the previous result again in the middle of this proof; it just might save a little bit of time and writing to not do so. If you find yourself working on a problem and thinking, "Hey, this feels familiar... ", go back and look for related theorems or lemmas or examples. Maybe you can use some already-acquired knowledge to your advantage.


> 🇨🇳 那个定义：$\mathcal{P}(A)$ 是 $A$ 的所有子集的集合。这里的主要命题是一个子集关系：无论 $\mathcal{P}(A) \cap \mathcal{P}(B)$ 是什么集合，它应该是 $\mathcal{P}(A \cap B)$ 的子集。这就决定了证明的整体结构——我们的证明一定会以"设 $X \in \mathcal{P}(A) \cap \mathcal{P}(B)$ 是任意的和固定的"开头。你是否也引用了前面的引理？还是不经意地重新证明了那个结果？这是一个值得吸取的教训：证明结果的一大好处就是可以在后面的证明中使用它们！


### 3.9.3 Proving "=" Double-Containment Proofs Again, we will need to recall the definition of "=" (in the context of sets), since we will be using it frequently here.
<div class="def-definition" markdown>
**Definition 3.9.4. We say two sets, A and B, are equal, and write A = B, if**
</div>
and only if A $\subseteq B and B \subseteq A$. That's it! It's completely built up from a previous definition, that of "\subseteq" (since that of "\supseteq" is completely equivalent). Thus, this isn't really a new technique, per se, because it's really a repeated application of a previous technique. That is to say, to prove A = B, we just need to use the technique used in the last subsection and prove A \subseteq B and then prove B $\subseteq A$. This technique is so common, in fact, that it is given a name: doublecontainment. When we prove two sets are subsets of each other, both ways, and conclude that they are equal, we call this a double-containment proof.
Examples
Let's see an example of this double-containment technique in action.
<div class="def-theorem" markdown>
**Lemma 3.9.5. Let A and B be any sets. Then, A -(A $\cap B$) = A -B.**
</div>
Intuition: As usual, we could draw a Venn diagram to convince ourselves of this truth, but that doesn't prove anything. Instead, we will follow a doublecontainment proof. If we take an element x $\in A$ -(A $\cap B$), we can apply the definition of "-" first, and then "$\cap$", to deduce something about x. Hopefully, it will tell us that x \in A -B. Then, if we take an element y \in A -B, we can apply some definitions to hopefully deduce that x \in A -(A $\cap B$). Maybe we aren't sure yet exactly how to do so, but by looking at that Venn diagram and using the definitions, we can surely figure it out. Why don't you try to do it first, then read our proof!
<div class="def-proof" markdown>
*Proof.* We will show A -(A $\cap B$) = A -B by a double-containment proof.
</div>
("$\subseteq$") First, let x \in A -(A \cap B) be arbitrary and fixed. By the definition of "-", we know that x \in A and x \notin A \cap B. This means it is not true that x is an element of both A and B. We already know x \in A, so we deduce that x \notin B. Thus, x \in A and x \notin B, so by the definition of "-", we deduce that x \in A -B. This shows A -(A \cap B) \subseteq A -B. ("\supseteq") Second, let y \in A -B be arbitrary and fixed. By the definition of "-", this means y \in A and y \notin B. Now, since y is not an element of B, this means that certainly y is not an element of both A and B. That is, y \notin A \cap B, by the definition of "\cap". Since we know y \in A and y \notin A \cap B, we deduce that y \in A -(A $\cap B$). This


> 🇨🇳 **3.9.3 证明"="——双向包含证明** 再次，我们需要回忆集合语境下"="的定义。**定义 3.9.4：** 我们说两个集合 $A$ 和 $B$ 相等，写作 $A = B$，当且仅当 $A \subseteq B$ 且 $B \subseteq A$。就这么简单！要证明 $A = B$，我们只需证明 $A \subseteq B$，然后证明 $B \subseteq A$。这种技巧非常普遍，因此有了一个名称：**双向包含（double-containment）**。

> 证明的整体结构：我们预先告诉读者会有两部分，并适当地分隔它们。证明的意义在于说服别人你已经弄清楚的事实，所以要让读者尽可能容易跟上你的思路。


shows A -B $\subseteq A$ -(A $\cap B$). Overall, a double-containment proof has shown that A -(A $\cap B$) = A -B. Look at the overall structure of this proof. We knew there would be two parts to it, since it is a double-containment proof, but we were also kind enough to point this out ahead of time for our intrepid reader, and separate those two sections appropriately. It would be technically correct to ignore this and just dive right in to the proof, but this might leave a reader confused. The whole point of a proof is to convince someone else of a truth that you have already figured out, so you might as well make it as easy as possible for them to follow what you're doing. Let's see another example of proving two sets are equal. This one will be a little different, because one of the parts of the double-containment will make use of the complement operation. As a preview, spend a minute now thinking about why the statements A \subseteq B and B \subseteq A are equivalent (supposing there is some universal set A, B $\subseteq U$). Draw a Venn diagram and try some examples. Try to prove it, even!
Proposition 3.9.6.

x $\in \mathbb{N}$ | x + 8 x $\leq$6 = {2, 3, 4}
<div class="def-proof" markdown>
*Proof.* Let's define A =
</div>
 x $\in \mathbb{N}$ | x + 8 x $\leq$6


> 🇨🇳 这表明 $A - B \subseteq A - (A \cap B)$。总之，双向包含证明表明 $A - (A \cap B) = A - B$。

> 再看另一个证明集合相等的例子。**命题 3.9.6.** $\{x \in \mathbb{N} \mid x + \frac{8}{x} \leq 6\} = \{2, 3, 4\}$

> 设 $A = \{x \in \mathbb{N} \mid x + \frac{8}{x} \leq 6\}$，$B = \{2, 3, 4\}$。


, and B = {2, 3, 4}. To show A = B, we will show A $\subseteq B and B \subseteq A$. First, we will show B \subseteq A. We can consider each of the three elements separately, and verify that they satisfy the defining inequality of B: 2 + 8 2 = 6 \leq6 3 + 8 3 = 17 3 \leq6 4 + 8 4 = 6 \leq6 Since 2, 3, 4 $\in \mathbb{N}$, we deduce that 2 \in A and 3 \in A and 4 \in A, so B \subseteq A. Next, to show A \subseteq B, we will show that B \subseteq A, where the complement is taken in the context of N. That is, we will show that all of the natural numbers 1, 5, 6, 7,... are not elements of A. To show this, we will verify that the defining inequality of A is not satisfied by any of those elements. The first two cases can be considered easily: 1 + 8 1 = 9 ̸\leq6 and 5 + 8 5 = 33 5 ̸\leq6. To consider the other cases, we can take an arbitrary and fixed x $\in \mathbb{N} with x \geq$6. Notice, then, that x + 8 x $\geq$6 + 8 x > 6, since 8 x > 0.


> 🇨🇳 要证明 $A \subseteq B$，我们证明 $\overline{B} \subseteq \overline{A}$（在 $\mathbb{N}$ 的语境下取补）。即证明 $1, 5, 6, 7, \ldots$ 都不是 $A$ 的元素。前两种情况容易验证：$1 + \frac{8}{1} = 9 \not\leq 6$ 且 $5 + \frac{8}{5} = \frac{33}{5} \not\leq 6$。对于其他情况，取任意固定的 $x \in \mathbb{N}$，$x \geq 6$。注意到 $x + \frac{8}{x} \geq 6 + \frac{8}{x} > 6$（因为 $\frac{8}{x} > 0$）。


This shows that only 2,3,4 satisfy the defining inequality of A. Overall, by a double-containment argument, we have proven that A = B. Think carefully, again, about why the method employed in the second half of the proof is valid. (It is actually an instance of using the contrapositive of a conditional statement, but we haven't yet defined any of those terms; we will do so in the next chapter on logic.) Let's see another example of proving set equality. This one is only slightly different in that we are proving some set is actually the empty set and, to do so, we will prove that it has no elements.
Proposition 3.9.7. For every n $\in \mathbb{N}$, define Sn = N -[n]. Then
\ n$\in \mathbb{N} Sn = \emptyset$ We suggest you play around with this statement first, if it doesn't make sense. For instance, try identifying the element of the sets S1, and S1 $\cap S2, and S1 \cap S2 \cap S$3, and so on. Try to come up with a candidate element of the big intersection on the left, and then figure out why it actually is not an element of that set. After that, try to figure out a formal proof and write it out; then, look at ours below!
<div class="def-proof" markdown>
*Proof.* Let's define T =
</div>
\ n$\in \mathbb{N}$ Sn, so we can refer to it later. To prove T = \emptyset, we will show that T does not contain any elements. Notice that T is formed by an intersection of many sets of natural numbers, so it's clear that the only possibilities for elements of T are natural numbers. Consider an arbitrary and fixed x $\in \mathbb{N}$. We want to show that x \notin T. Observe that x \in[x] = {1, 2,..., x}. Thus, x $\notin \mathbb{N}$ -[x], by the definition of "-". By definition, T contains the elements that belong to all of the sets of the form N -[n]. We have identified (at least) one set, N -[x], of the intersection such that x does not belong to that set. Accordingly, x cannot be an element of T, since it does not belong to all such sets. Therefore, x \notin T. Since x $\in \mathbb{N}$ was arbitrary, we have proven that T contains no natural numbers as elements, and therefore it has no elements at all. Summary: Let's make one more statement about why this technique works. We showed that there are no elements of T, i.e. that T $\subseteq \emptyset$. This completes the entire process, because it is trivially true, as well, that $\emptyset \subseteq T$. (This claim holds for any set.) Thus, one of the parts of the double-containment argument is already achieved, and we can conclude T = $\emptyset$. Alright, one more example. We want to include this one because it gives us further practice in working with indexed set operations. You will find many


> 🇨🇳 这表明只有 2、3、4 满足 $A$ 的定义不等式。通过双向包含论证，我们证明了 $A = B$。仔细想想为什么证明后半部分使用的方法是有效的。（它实际上是使用了条件命题的逆否命题，但我们还没有定义这些术语；下一章讲逻辑时会定义。）

> 再看一个证明集合相等的例子。这次稍有不同：我们要证明某个集合是空集，为此证明它没有元素。

> **命题 3.9.7.** 对每个 $n \in \mathbb{N}$，定义 $S_n = \mathbb{N} - [n]$。则 $\bigcap_{n \in \mathbb{N}} S_n = \emptyset$。

> 证明概要：定义 $T = \bigcap_{n \in \mathbb{N}} S_n$。要证明 $T = \emptyset$，我们证明 $T$ 不包含任何元素。取任意固定的 $x \in \mathbb{N}$。注意到 $x \in [x]$，因此 $x \notin \mathbb{N} - [x]$。而 $T$ 包含属于所有形如 $\mathbb{N} - [n]$ 的集合的元素，但 $x$ 至少不属于 $\mathbb{N} - [x]$ 这个集合。因此 $x \notin T$。由于 $T \subseteq \emptyset$（已证）且 $\emptyset \subseteq T$（对任何集合都成立），所以 $T = \emptyset$。


similar problems in the exercises for this section. We encourage you to work on as many of them as you can!
Proposition 3.9.8. For every n $\in \mathbb{N}$, define An =

x $\in \mathbb{R}$ | 0 $\leq x$ < 1 n


> 🇨🇳 **命题 3.9.8.** 对每个 $n \in \mathbb{N}$，定义 $A_n = \{x \in \mathbb{R} \mid 0 \leq x < \frac{1}{n}\}$。


. Then, \ n$\in \mathbb{N}$ An = {0} Think about what this claim means. Draw a picture of the An sets on a number line. What does the "T" intersection accomplish? Why does it work out that 0 is an element of that intersection? Why is it the only element? The definition of T will be crucial in this proof, so let's recall the definition here. The key phrase is for every:
<div class="def-definition" markdown>
**Definition 3.9.9. The intersection of a collection of sets Ai indexed by the set**
</div>
I is \ i$\in I Ai = {x \in U$ | x $\in Ai for every i \in I$} where we assume there is a set U such that Ai $\subseteq U for every i \in I$. That is, remember that the indexed intersection of several sets collects together the elements that belong to all of the constituent sets. Thus, in our proof below, you will see that we need to prove that (1) 0 is, indeed, an element of all of the An sets, and (2) no other number is an element of all of them, i.e. for every nonzero real number, we can identify at least one of the An sets such that the number is not an element of that set.
<div class="def-proof" markdown>
*Proof.* First, we will prove that
</div>
{0} $\subseteq \ n\in \mathbb{N}$ An This requires us to show that 0 $\in An for every n \in \mathbb{N}. Let n \in \mathbb{N}$ be arbitrary and fixed. Notice that the inequality 0 $\le$0 < 1 n does, indeed hold. (Note: You might be worried because "in the limit" 0 is not less than every fraction


> 🇨🇳 则 $\bigcap_{n \in \mathbb{N}} A_n = \{0\}$。思考这个命题的含义：在数轴上画出 $A_n$ 集合。0 为什么是这个交集的元素？为什么它是唯一的元素？

> **定义 3.9.9.** 由集合 $I$ 索引的集合族 $\{A_i\}$ 的交集定义为：$\bigcap_{i \in I} A_i = \{x \in U \mid x \in A_i \text{ 对每个 } i \in I\}$。即索引交集收集属于所有组成集合的元素。在证明中，我们需要证明(1) 0 确实是所有 $A_n$ 的元素，以及 (2) 没有其他数是所有 $A_n$ 的元素。


n "all at once", but that is not the point! Think of it this way: Is 0 $\in A$1? Yes, 0 $\le$0 < 1. Is 0 $\in A$2? Yes, 0 $\le$0 < 1 2. Is 0 $\in A$3? Yes, 0 $\le$0 < 1 3. And so on. The inequality holds for every n $\in \mathbb{N}$ individually, so 0 is an element of every such set. If you weren't worried about this, never mind! Move right along!) Thus, 0 \in An for every n $\in \mathbb{N}$, and so 0 \in \ n$\in \mathbb{N}$ An, by the definition of "T". This shows that {0} \subseteq \ n$\in \mathbb{N}$ An.


> 🇨🇳 注意：你可能会担心因为"在极限中"0不可能同时小于每个分数 $\frac{1}{n}$，但这不是重点！这样想：$0 \in A_1$ 吗？是的，$0 \leq 0 < 1$。$0 \in A_2$ 吗？是的，$0 \leq 0 < \frac{1}{2}$。$0 \in A_3$ 吗？是的，$0 \leq 0 < \frac{1}{3}$。以此类推。这个不等式对每个 $n \in \mathbb{N}$ 单独成立，因此 0 是每个这样集合的元素。因此 $\{0\} \subseteq \bigcap_{n \in \mathbb{N}} A_n$。


Second, we will prove that \ n$\in \mathbb{N} An \subseteq${0} We will do this by considering the complements of these sets, in the context of R. Specifically, we will show that {0} \subseteq \ n$\in \mathbb{N}$ An which means we will show that every nonzero real number is not an element of every An. Let x $\in \mathbb{R}$ be arbitrary and fixed, with the property that x \neq 0. Either x > 0 or x < 0, then, so let's consider each case separately. Case 1: Suppose x > 0. Consider the number 1 x $\in \mathbb{R}$. Since the natural numbers are infinite and unbounded in R, we can choose a natural number M that is bigger than that real number. That is, we can choose M $\in \mathbb{N}$ such that M > 1 x. (Note: Think about why this works. We haven't proven that N is infinite, or that the numbers "go on forever" along the number line of R, but we hope these ideas make sense to you, intuitively.) Take such an M $\in \mathbb{N}$ with M > 1 x. Since x > 0, we can multiply the inequality on both sides by x; since M > 0 (so


> 🇨🇳 第二，证明 $\bigcap_{n \in \mathbb{N}} A_n \subseteq \{0\}$。我们在 $\mathbb{R}$ 的语境下考虑补集来证明，即证明每个非零实数不是所有 $A_n$ 的元素。取任意固定的 $x \in \mathbb{R}$，$x \neq 0$。分两种情况：**情况1**：设 $x > 0$。考虑 $\frac{1}{x} \in \mathbb{R}$。由于自然数无限且在 \mathbb{R} 中无上界，我们可以选择 $M \in \mathbb{N}$ 使 $M > \frac{1}{x}$。因为 $x > 0$，可以在不等式两边乘以 $x$——


M > 0) we can then multiply again by


> 🇨🇳 因为 $M > 0$，我们可以——


M. This yields x >


> 🇨🇳 $M$。这给出 $x >$ ——


M. Accordingly x $\notin A$M, because -1 M < x <


> 🇨🇳 $\frac{1}{M}$。因此 $x \notin A_M$，因为 $-\frac{1}{M} < x < \frac{1}{M}$——


M is False. Since x $\notin A$M, then surely x is not an element of all such sets. Therefore, x \notin \ n$\in \mathbb{N}$ An. Case 2: Next, suppose that x < 0. We will make a similar argument as the previous case; this time, we will just consider -x, since -x > 0. Using the same logic as above, we can surely identify a natural number M $\in \mathbb{N}$ that satisfies M >


> 🇨🇳 $\frac{1}{M}$ 不成立。既然 $x \notin A_M$，则 $x$ 不是所有这样集合的元素。**情况2**：设 $x < 0$。我们用类似于前一种情况的论证；考虑 $-x$（因为 $-x > 0$），同样可找到 $M \in \mathbb{N}$ 满足 $M >$ ——


-x = -1 x. Manipulating the inequality tells us that x < -1 M. Thus, x $\notin AM, and so x \notin \ n\in \mathbb{N}$ An. Therefore, we have shown that any x $\in \mathbb{R}$ with x \neq 0 is not an element of at least one of the An sets, so any such x is not an element of their intersection. Thus, {0} \subseteq \ n$\in \mathbb{N}$ An, and we have proven the claim by a double-containment argument. This proof is harder than the other ones, we think, so make sure to read it a couple times to make sure you see what happens in every step. In particular, think about how we came up with the step where we chose M $\in \mathbb{N}$ that satisfies M > 1 x. Do you think we magically intuited that choice? Or do we think we recognized that we wanted x <


> 🇨🇳 $\frac{1}{-x} = -\frac{1}{x}$。不等式操作告诉我们 $x < -\frac{1}{M}$，因此 $x \notin A_M$，于是 $x \notin \bigcap_{n \in \mathbb{N}} A_n$。我们证明了任何 $x \neq 0$ 都不是所有 $A_n$ 集合的元素，因此 $\bigcap_{n \in \mathbb{N}} A_n \subseteq \{0\}$，双向包含论证完成。这个证明比其他的难，请多读几遍确认每一步。特别是想想我们是怎么想到选择 $M \in \mathbb{N}$ 满足 $M > \frac{1}{x}$ 的——你觉得是我们凭直觉想出来的？还是先逆向构造再反向推导出来的？


M to be true for some M, and manipulated the inequality backwards to figure out how to make that happen?


> 🇨🇳 $\frac{1}{M}$ 对某个 $M$ 成立，然后倒推不等式来找出如何实现？


### 3.9.4 Disproving Claims Motivating Example Consider the following proposed claim: For any sets F, G, H, if F $\subseteq G \cup H$, then either F $\subseteq G or F \subseteq H$. Is this claim True? If so, how would we prove it? Well, we'd take an arbitrary and fixed element x $\in F. Since F \subseteq G \cup H$, this would tell us x \in G \cup H, as well. Accordingly, either x $\in G or x \in H$. Is that it? Are we done with the proof? We hope you recognize that this does not work! In particular, we have not satisfied the definition of "\subseteq" at the end. If our goal is to prove "either F \subseteq G or F \subseteq H", then we should conclude that one or the other of those claims holds: that every element of F is also an element of G, or else every element of F is also an element of H. What we found was that every element of F is itself either an element of G or H, but we cannot decide collectively that all elements of F are elements of one or the other, G or H. Read through these last two paragraphs again to make sure you follow that logical observation. It might be easy to actually write up a "proof" for this claim and not realize that you've made a false step! Identifying Errors This recognition of an error is one of the skills we are developing, and it will be helpful in several ways. You'll notice that many exercises (some thus far, but many more as we move onwards) ask you to find the flaw in a proposed "proof" of some claim. By pointing out that there exists a flaw, we are perhaps helping you to find it (or them, as the case may be). Reading a proposed proof for logical, factual, and clarity errors is an essential skill. What's more, this careful reading of others' writing will necessarily make you a more critical reader of your own writing, and it will help you to catch potential errors like the one in the preceding paragraphs. Do not worry if you didn't catch it; now that you've seen it, you'll be on the lookout for similar mistakes in the future! Like we said, as well, this skill is ongoing development, and by the end of this book, you will be a great reader of mathematical proofs, as well as a great writer. Counterexamples So, now what do we do? We just recognized that our "proof" above did not work. Does this mean the claim is actually False? Actually, all this means (so far) is that our attempt at a proof failed. Maybe some other logical route will magically take us to the elusive conclusion. Or, maybe the claim really is False. How could we show that? Think about the logical form of the claim: it says some statement holds true for any sets F, G, H. It says that the assumption F \subset G $\cup H$ will always imply, necessarily,


> 🇨🇳 **3.9.4 反证命题** **动机示例** 考虑以下命题：对任意集合 F, G, H，若 $F \subseteq G \cup H$，则 $F \subseteq G$ 或 $F \subseteq H$。这个命题为真吗？我们会取任意的 x \in F。由 $F \subseteq G \cup H$，得 $x \in G \cup H$，因此 $x \in G$ 或 $x \in H$。但这就完成证明了吗？我们希望你能认识到这行不通！我们没有满足"\subseteq"的定义。要证明"$F \subseteq G$ 或 $F \subseteq H$"，应得出：F 的所有元素都在 G 中，或所有元素都在 H 中。但我们发现的是 F 的每个元素各自属于 G 或 H，这并不意味着所有 F 元素集体属于某一个。

> **识别错误** 这是我们要培养的技能之一。许多人容易写出这样的"证明"却没意识到错误！

> **反例** 我们的证明失败了，这意味着命题为假吗？目前只是证明尝试失败了。要证明命题为假，我们需要找出**反例**（counterexample）——一个具体的例子说明命题不总是成立。


that F $\subseteq G or F \subseteq H$. To show that this does not always happen, we need to find what's called a counterexample. We will discuss all of these ideas again in the next chapter, when we formalize logic, but what you need to know for now is this: a counterexample is a specific, detailed, and described example that illustrates how a statement about "every... " or "any... " or "all possible... " does not actually hold for every case. A counterexample amounts to disproving a statement that a whole class of objects has a certain property, by exhibiting one object in that class without that property.
Example
Let's see how the process of finding and stating a counterexample would work for our example above.
Example 3.9.10. Recall the claim:
For any sets F, G, H, if F $\subseteq G \cup H$, then either F $\subseteq G or F \subseteq H$. This claim is supposed to work for any sets F, G, H, so when we describe our counterexample, we better describe exactly what those three sets are going to be. We can't just explain our way around the issue and argue about how there might exist three sets out there with a certain property. Nope, we have to tell a reader exactly what they are by explicitly defining them. This is what the first line of our disproof of the claim will be, but we can't just jump right into that, because we don't know how to define them yet! This is where the fun/work is: we need to play around with the desired properties of these sets to help us come up with an example. Recall that we want these sets to satisfy some properties: we should make sure the assumption F $\subseteq G \cup H$ holds True, but we want the conclusion---that either F $\subseteq G or F \subseteq H$---to be False. What does this mean? Well, we think you'll agree that, logically speaking, the "opposite" or "negation" of a statement like that would be "both F ̸\subseteq G and F ̸\subseteq H". (This concept of logical negation will return in the next chapter; for now, we think you can understand it by applying the logical principles that guide your daily life. Soon, we will formalize this idea.) We now have a specific goal: to find three sets F, G, H that satisfy all three of the following: F $\subseteq G \cup H$ F ̸\subseteq G F ̸\subseteq H One thing left to consider is what "̸\subseteq′′ means. We have a definition of "\subseteq", so what is the "opposite" or "negation" of that? For F $\subseteq G$ to be true, we require that every element of F is also an element of G; so, if this fails, then we must have at least one element of F that is not an element of G. The same


> 🇨🇳 要找到反例，我们需要显式定义三个集合 F, G, H 使：$F \subseteq G \cup H$ 为真，但 $F \subseteq G$ 和 $F \subseteq H$ 均为假。即 $F \not\subseteq G$（至少有一个 F 的元素不在 G 中）和 $F \not\subseteq H$（至少有一个 F 的元素不在 H 中）。


observation applies to F ̸$\subseteq H$. Now, we can restate our goals in a helpful way, by applying definitions: Every element of F is an element of either G or H There is at least one element of F that is not an element of G There is at least one element of F that is not an element of H This will be incredibly helpful in finally finding our counterexample! We've boiled down all the essential parts of the claim and have restated the properties in a more intuitive way. The rest of the work is to just play around on some scratch paper and see what we can come up with. One approach is to draw a sort of "empty" Venn diagram, for F and G and H and their potential "overlaps", and then fill in enough elements so that the three above properties are satisfied. The first condition requires the set F to "lie inside" both G and H, entirely; but, the second and third conditions require the existence of two elements of F, one of whom is not an element of G and the other of whom is not an element of H. That's all we need! A simple example, you might say, but an effective one, we say. Let's jump in and write up our disproof now:
<div class="def-proof" markdown>
*Proof.* The following claim is False:
</div>
For any sets F, G, H, if F $\subseteq G \cup H$, then either F $\subseteq G or F \subseteq H$. We will disprove it with a counterexample. Define F = {1, 2} and G = {1} and H = {2}. Notice that G\cup H = {1, 2}. Since F = G\cup H, then certainly F $\subseteq G \cup H$. Thus, the hypothesis of the claim holds true. However, notice that 2 \in F but 2 \notin G. Thus, F ̸\subseteq G. Likewise, notice that 1 \in F but 1 \notin H. Thus, F ̸$\subseteq H$. Therefore, the claim is False. One important lesson from this example is the following: Tour counterexample does not have to be the most interesting or complicated one, nor do you somehow need to characterize all possible counterexamples. We just need to see one counterexample, and we need to see how it works. That's it! This is exactly what we did in the above proof: we defined all of the important objects (the three sets F, G, H), and then we pointed out and described all the relevant properties they had. We did not leave it to the reader to check that the counterexample works; we showed them the details. We did not argue that some such sets exist somewhere out there in the universe; we defined them explicitly. This is important, and we expect your counterexamples to have similar proof structure to ours above. Most of the work will go on "behind the scenes", before


> 🇨🇳 反例定义为：$F = \{1, 2\}$，$G = \{1\}$，$H = \{2\}$。则 $G \cup H = \{1, 2\} = F$，所以 $F \subseteq G \cup H$。但 $2 \in F$ 而 $2 \notin G$，所以 $F \not\subseteq G$；$1 \in F$ 而 $1 \notin H$，所以 $F \not\subseteq H$。因此命题为假。

> 重要教训：反例不需要是最有趣或最复杂的，也不需要刻画所有可能的反例。我们只需要一个反例并展示它如何工作即可！


the proof starts, when you try to come up with your examples. Once you have it, though, just write it up much like we did.
### 3.9.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the definition of $\subseteq$? How do we use it to prove A \subseteq B? (2) What does it mean for two sets to be equal? (3) What is a double-containment proof? (4) What is a counterexample? (5) Suppose A, B, U are sets and A, B \subseteq U. Why can we prove B \subseteq A to prove that A \subseteq B? Try to convince a friend that this is a valid technique. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) First, prove the following claim: For any sets A, B, C, the subset relationship A -(B -C) \subseteq(A - B) $\cup \mathbb{C}$ holds. Second, find a counterexample to the claim that those sets are actually always equal. (2) Suppose A, B, C are sets and A \subseteq B. Prove that A 	imes C \subseteq B 	imes C. (3) Suppose A $\subseteq \mathbb{C} and B \subseteq D$. Prove that A $	imes B \subseteq \mathbb{C} 	imes$ D. (4) Let A = {x $\in \mathbb{R}$ | x2 > 2x + 8} and B = {x $\in \mathbb{R}$ | x > 4}. For each of the following claims, either prove it is correct or provide a counterexample to show it is False. (a) A \subseteq B (b) B $\subseteq A$


> 🇨🇳 **3.9.5 问题与练习** 自我提醒：(1) $\subseteq$ 的定义是什么？如何用它证明 $A \subseteq B$？(2) 两个集合相等意味着什么？(3) 什么是双向包含证明？(4) 什么是反例？(5) 设 A, B, U 为集合且 $A, B \subseteq U$，为什么证明 $\overline{B} \subseteq \overline{A}$ 就能证明 $A \subseteq B$？


(5) Let A, B, U be sets with A, B $\subseteq U$. Prove that A -B = A \cap B by a double-containment argument. (6) Let S = {x $\in \mathbb{R}$ | -2 < x < 5} and T = {x $\in \mathbb{R}$ | -4 $\leq x$ $\leq$3}. What is S \cap T, in the context of R? Identify a set and then prove it is correct, using a double-containment argument. (7) Prove the following claim: If A \subseteq B, then P(A) \subseteq P(B). (8) For every n $\in \mathbb{N}$ let Sn =

x $\in \mathbb{R}$ | -1 n < x < 1 n


> 🇨🇳 (8) 对每个 $n \in \mathbb{N}$，设 $S_n = \{x \in \mathbb{R} \mid -\frac{1}{n} < x < \frac{1}{n}\}$。


. Prove that \ n$\in \mathbb{N}$ Sn = {0} (9) Let I = {x $\in \mathbb{R}$ | 0 < x < 1}. For every x \in I, define Sx = {y $\in \mathbb{R}$ | x < y < x + 1}. Prove that [ x\in I Sx = {z $\in \mathbb{R}$ | 0 < z < 2} (10) For every n $\in \mathbb{N}$, define the sets An and Bn by An =

x $\in \mathbb{R}$ | 0 $\le$x < n -1 n Bn =

y $\in \mathbb{R}$ | -1 n < y < 1 Prove the following set equality by a double-containment argument: [ n$\in \mathbb{N} An = \ n\in \mathbb{N}$ Bn
## 3.10 Summary This was our first foray into some abstract conepts and results. We introduced the notion of a set, motivating it via several examples. We discussed the key relationships of being an element and being a subset, and pointed out how important is to distinguish the two! (Keeping the "Bag Analogy" in mind might help you in this regard.) We also discussed some notation, included setbuilder notation. As we continue to move into more abstract mathematics, using correct, formal notation will be more important than ever to ensure that we are properly expressing our ideas. One key idea that came up is the notion of the power set, which represents a place where the element and subset relationships are both at work. A discussion of set operations showed us how to combine sets and create new ones. All of these operations will be used throughout the remainder of our work in this book. We also showed how these operations can be indexed. This allows


> 🇨🇳 (10) 对每个 $n \in \mathbb{N}$，定义 $A_n = \{x \in \mathbb{R} \mid 0 \leq x < \frac{n-1}{n}\}$，$B_n = \{y \in \mathbb{R} \mid -\frac{1}{n} < y < \frac{1}{n}\}$。用双向包含论证证明 $\bigcup_{n \in \mathbb{N}} A_n = \bigcap_{n \in \mathbb{N}} B_n$。

> **3.10 总结** 本章是我们对抽象概念和结果的初次探索。我们引入了集合的概念，通过多个例子加以说明。我们讨论了"属于"和"子集"这两个关键关系，并指出区分它们多么重要！我们还讨论了一些记号，包括集合构造记号。随着我们继续深入学习更抽象的数学，使用正确、正式的记号将变得前所未有地重要。幂集的概念出现在哪里，属于关系和子集关系就同时出现在哪里。集合运算的讨论教会了我们如何组合集合并创建新集合。


us to use shorthand to write a union of several sets using just a few definitions and symbols. Again, these ideas will re-appear quite often throughout our work, so we will present many exercises relating to these ideas; we encourage you to attempt and work through as many as you can! We saw a proof technique relating to sets: namely, double-containment arguments. This is a fundamental proof technique in mathematics. You will see us use it often, and you will find it appearing in other courses and studies, as well. A couple of discussions came up that allowed us to touch upon some profound ideas in abstract set theory, although we couldn't completely dive into them. For one, Russell's Paradox showed us that there is no "set of all sets". For another, we talked about how the natural numbers can be formally defined in terms of sets. In practice, we won't use this definition, and will continue to rely on our intuitions about N. However, we hope it was interesting and somehow informative to read such a discussion.
## 3.11 Chapter Exercises These problems incorporate all of the material covered in this chapter, as well as any previous material we've seen, and possibly some assumed mathematical knowledge. We don't expect you to work through all of these, of course, but the more you work on, the more you will learn! Remember that you can't truly learn mathematics without doing mathematics. Get your hands dirty working on a problem. Read a few statements and walk around thinking about them. Try to write a proof and show it to a friend, and see if they're convinced. Keep practicing your ability to take your thoughts and write them out in a clear, precise, and logical way. Write a proof and then edit it, to make it better. Most of all, just keep doing mathematics! Short-answer problems, that only require an explanation or stated answer without a rigorous proof, have been marked with a. Particularly challenging problems have been marked with a $\star$. Problem 3.11.1. For each of the following statements about elements and subsets, state whether it is True or False. Be prepared to defend your choice to a skeptical friend! Throughout this problem, we will use the following definitions: A = {x $\in \mathbb{Z}$ | -3 $\leq x$ $\leq3} B = {y \in \mathbb{Z}$ | -5 < y < 6} C =

x $\in \mathbb{R}$ | x2 $\geq$9


> 🇨🇳 这些使我们能用简写来表达多个集合的并集。双重包含论证是与集合相关的基本证明技巧。罗素悖论告诉我们不存在"所有集合的集合"。我们还讨论了如何用集合形式化地定义自然数。


D = {x $\in \mathbb{R}$ | x < -3} E = {n $\in \mathbb{N}$ | n is even }


> 🇨🇳 附加定义：$D = \{x \in \mathbb{R} \mid x < -3\}$，$E = \{n \in \mathbb{N} \mid n \text{ 是偶数}\}$。


(a) A $\subseteq B (b) \mathbb{C} \cap D = \emptyset (c) 4 \in E \cap B (d) {4} \subseteq A \cap E (e) 10 \in \mathbb{C}$ -D (f) A $\cup B \supseteq \mathbb{C} (g) 3 \in A \cap \mathbb{C} (h) 0 \in$(A -B) $\cup D (i) E \cap \mathbb{C} \subseteq \mathbb{Z} (j) 0 \notin B$ -C Problem 3.11.2. Let m, n $\in \mathbb{N}. Suppose m \leq n$. Explain why P([m]) \subseteq P([n]). Problem 3.11.3. Look back at Problem 7 in Section 3.9. We proved that whenever two sets satisfy A \subseteq B, then they must also satisfy P(A) \subseteq P(B). Read through that proof, too, to remind yourself of the details. Now, does this claim "work the other way"? That is, suppose P(A) \subseteq P(B). Can you prove that A $\subseteq B$ is also true? Or can you find an example where this is not true? Problem 3.11.4. Rewrite the following sentences using the "set-builder notation" to define a set. Then, if possible, write out all the elements of the set, using set braces; if not possible, explain why not and write out three example elements of the set. (a) Let A be the set of all natural numbers whose squares are less than 39. (b) Let B be the set of all real numbers that are roots of the equation x2 -3x- 10 = 0. (c) Let C be the set of pairs of integers whose sum is non-negative. (d) Let D be the set of pairs of real numbers whose first coordinate is positive and whose second coordinate is negative and whose sum is positive. Problem 3.11.5. Define the following sets: A =

x $\in \mathbb{R}$ | x2 -x -12 > 0


> 🇨🇳 3.11 章节练习。标记 $\diamond$ 的为简答题，标记 $\star$ 的为挑战题。


B = {y $\in \mathbb{R}$ | -3 < y < 4} Prove that A = B.


> 🇨🇳 定义 $B = \{y \in \mathbb{R} \mid -3 < y < 4\}$。证明 $A = B$。


Problem 3.11.6. Let X be the set of students at your school. Identify a property P(x) such that A := {x $\in X$ | P(x)} is a proper subset of X and A \neq \emptyset. Then, identify a property Q(x) such that B := {x \in X | Q(x)} is a proper subset of A (i.e. B \subset A) and B \neq \emptyset. Problem 3.11.7. Let A, B, and C be sets with A $\subseteq \mathbb{C} and B \subseteq \mathbb{C}$. (a) Draw a Venn diagram for the sets A $\cap B and (A \cap B$). (b) Prove that A $\cap B \subseteq(A \cap B$). (c) Define specific sets A, B, C such that the containment is strict, i.e. A$\cap B \subset (A \cap B$) (d) Define specific sets A, B, C such that A $\cap B = (A \cap B$). Problem 3.11.8. Let S =

( m, n) $\in \mathbb{Z} 	imes$ Z | m = n2. How does S compare to the set T = {(m, n) $\in \mathbb{Z} 	imes$ Z | n = m2}? If one is a subset of the other, prove it. If not, provide examples to show this. Problem 3.11.9. Let (a, b) be a point on the Cartesian plane, i.e. (a, b) $\in \mathbb{R} 	imes$ R. Let ε (the Greek letter epsilon) be a nonnegative real number, i.e. ε $\in \mathbb{R}$ and ε $\geq$0. Let C(a,b),ε be the set of real numbers that are "close" to (a, b), defined as follows: C(a,b),ε = n (x, y) $\in \mathbb{R} 	imes$ R | p (x -a)2 + (y -b)2 < ε o 1. Come up with a geometric description of the set C(a,b),ε. What happens to the set as we change a and b? What happens as we change ε? 2. What is C(0,0),1 $\cap \mathbb{C}$(0,0),2? 3. What is C(0,0),1 $\cup \mathbb{C}$(0,0),2? 4. What is C(0,0),1 $\cap \mathbb{C}$(2,2),1? Problem 3.11.10. Consider the (false!) claim that [ n$\in \mathbb{N}$ P([n]) = P(N) (a) What is wrong with the following "proof" of the claim? Point out any error(s) and explain why it/they ruin the "proof". First, we will show that [ n$\in \mathbb{N} P([n]) \subseteq P$(N)


> 🇨🇳 练习 3.11.6—3.11.10。


Consider an arbitrary element X of the union on the left. By the definition of an indexed union, we know there exists some k $\in \mathbb{N} such that X \subseteq$[k]. Since [k] $\subseteq \mathbb{N}, and X \subseteq$[k], we deduce that X $\subseteq \mathbb{N}. Thus, X \in P$(N). Second, we will prove the "\subseteq" relationship holds in the other direction, as well. Consider an arbitrary Y $\subseteq \mathbb{N}$. By the definition of subset, and the fact that Y is a set of natural numbers, we know there exists some ℓ$\in \mathbb{N}$ such that Y \subseteq[ℓ]. By the definition of indexed union, we know Y \in [ n$\in \mathbb{N}$ P([n]). Since we have shown \subseteq and \supseteq, we know the two sets are equal. (b) Disprove the claim by defining an explicit example of a set S such that S \in P(N) and S \notin [ n$\in \mathbb{N}$ P([n]) Problem 3.11.11. Let A = [3] 	imes [4]. (Remember that [n] = {1, 2, 3,..., n}.) Let B = {(x, y) $\in \mathbb{Z}$ 	imes Z | 0 \leq3x -y + 1 \leq9}. (a) Prove that A \subseteq B. (b) Is it true that A = B? Why or why not? Prove your claim. Problem 3.11.12. Let n $\in \mathbb{N}$ be a fixed natural number. Let S = [n] $	imes$ [n]. Let T be the set T =

(x, y) $\in \mathbb{Z} 	imes$ Z | 0 $\leq n$x + y -(n + 1) $\leq n$2 -1


> 🇨🇳 (b) 举出一个显式反例 $S$ 使得 $S \in \mathcal{P}(\mathbb{N})$ 但 $S \notin \bigcup_{n \in \mathbb{N}} \mathcal{P}([n])$。问题 3.11.11—3.11.12。


Prove that S $\subseteq T$ but S \neq T. Problem 3.11.13. Suppose A and B are sets. (a) Prove that P(A) \cup P(B) \subseteq P(A \cup B) (b) Provide an explicit example of A and B where the containment in (a) is strict. Problem 3.11.14. Let S and T be sets whose elements are sets, themselves. Suppose that S \subseteq T. Prove that [ X\in S X \subseteq [ Y $\in T$ Y


> 🇨🇳 问题 3.11.13—3.11.14。


Problem 3.11.15. Let A, B, C, D be sets. (a) Prove that (A $	imes B) \cup(C 	imes D) \subseteq(A \cup \mathbb{C}) 	imes (B \cup D$) (b) Provide an explicit example of A, B, C, D where the containment in (a) is strict. Problem 3.11.16. Let A, B, C be sets. Prove that A 	imes (B $\cap \mathbb{C}$) = (A 	imes B) \cap(A 	imes C) and A 	imes (B -C) = (A 	imes B) -(A 	imes C) Problem 3.11.17. Let X, Y, Z be sets. Prove that (X \cup Y ) -Z \subseteq X \cup(Y -Z) but equality need not hold. Problem 3.11.18. Find an example of a set S such that S \in P(N) and S contains exactly 4 elements. Then, find an example of a set T such that T \subseteq P(N) and T contains exactly 4 elements. Problem 3.11.19. Find examples of sets R, S, T such that R \in S and S \in T and R \subseteq T but R \notin T. Problem 3.11.20. Identify what each of the following sets are, and prove your claims. \ n$\in \mathbb{N} [n] and [ n\in \mathbb{N}$ [n] Problem 3.11.21. Let I = {-1, 0, 1}. For each i \in I, define Ai = {i -2, i - 1, i, i + 1, i + 2} and Bi = {-2i, -i, i, 2i}. (a) Write out the elements of [ i\in I Ai. (b) Write out the elements of \ i\in I Ai. (c) Write out the elements of [ i\in I Bi. (d) Write out the elements of \ i\in I Bi. (e) Use your answers above to write out the elements of [ i\in I Ai ! - [ i\in I Bi !. (f) Use your answers above to write out the elements of \ i\in I Ai ! - \ i$\in I$ Bi !.


> 🇨🇳 问题 3.11.15—3.11.21。


(g) Write out the elements of [ i$\in I$ (Ai -Bi). How does this compare to your answer in (e)? (h) Write out the elements of \ i\in I (Ai -Bi). How does this compare to your answer in (f)? Problem 3.11.22. In this problem, we are going to "prove" the existence of the negative integers! We say "prove" because we won't really understand what we've done until later but, trust us, it's what we're doing. Because of this goal, you cannot assume any integers strictly less than 0 exist, so your algebraic steps, especially in part (d), should not involve any terms that might be negative. That is, if you consider an equation like x + y = x + z we can deduce that y = z, by subtracting x from both sides, since x -x = 0. However, if we consider an equation like x + y = z + w we cannot deduce that x -z = w -y. Perhaps y > w, so w -y does not exist in our context... Let P = N 	imes N. Define the set R by R = {((a, b), (c, d)) \in P 	imes P | a + d = b + c} (a) Find three different pairs (c, d) such that ((1, 4), (c, d)) $\in \mathbb{R}$. (b) Let (a, b) \in P. Prove that ((a, b), (a, b)) $\in \mathbb{R}$. (c) Let ((a, b), (c, d)) $\in \mathbb{R}$. Prove that ((c, d), (a, b)) $\in \mathbb{R}$, as well. (d) Assume ((a, b), (c, d)) $\in \mathbb{R}$ and ((c, d), (e, f)) $\in \mathbb{R}$. Prove that ((a, b), (e, f)) $\in \mathbb{R}$, as well.
## 3.12 Lookahead Now that we've introduced sets, defined them, seen many examples, and talked about operations and how to manipulate sets, it's time to move on to logic. We've already previewed some important logical ideas, specifically in Section
## 3.9 on how to write proofs about sets. In the next Chapter, we will make all
of these logical ideas more formal, explicit and rigorous. We will develop some


> 🇨🇳 问题 3.11.22：用 $\mathbb{N} \times \mathbb{N}$ 上的等价关系来"证明"负整数的存在性。


notation and grammar that will help us express logical ideas more precisely and concisely. We will use these to express our mathematical thoughts in a common language and communicate our ideas with others. In short, we will be able to confidently talk and write about mathematics!


> 🇨🇳 **3.12 展望** 既然我们已经引入了集合，定义了它们，看了许多例子，讨论了运算和如何操作集合，接下来就要进入逻辑了。在下一章中，我们将使所有这些逻辑思想更加形式化、明确和严谨。我们将发展一些记号和语法来帮助我们更精确、更简洁地表达逻辑思想。简言之，我们将能够自信地谈论和书写数学！
