---
title: Set Operations
---

# Set Operations

The situation where two sets have no common elements, as seen in the above example, is common enough that we have a specific term to describe such sets:
<div class="def-definition" markdown>
**Definition 3.5.3. If A $\cap$B = $\emptyset$, then we say A and B are disjoint.**
</div>
Intersections and Subsets You might have observed already that we can say A $\cap$B $\subseteq$A and A $\cap$B $\subseteq$B, no matter what A and B are. Let's prove this fact!
Proposition 3.5.4. Let A and B be any sets. Then,
A $\cap$B $\subseteq$A and A $\cap$B $\subseteq$B By the way, a proposition like this is just a "mini result". It's not difficult or important enough to be called a theorem, but it does require a little proof.
<div class="def-proof" markdown>
*Proof.* Let's say we have two sets, A and B. To prove a subset relationship, like
</div>
A $\cap$B $\subseteq$A, we need to show that every element of the set on the left (A $\cap$B) is also an element of the set on the right (A). Let's consider an arbitrary element x $\in$A $\cap$B. By the definition of A $\cap$B, we know that x $\in$A and x $\in$B. Thus, we know that x $\in$A. This was our goal, so we have shown that A $\cap$B $\subseteq$A. Also, we know that x $\in$B, so we have also shown that A $\cap$B $\subseteq$B. This might seem like a simple observation and an easy proof, but we still need to go through these logical steps to rigorously explain why those subset relationships hold true. Also, notice the type of proof structure we used here. To prove a subset relationship holds true, we need to consider an arbitrary element of one set and deduce that it is also an element of the other set. This will be our method for proving any claim about subsets. What if A $\subseteq$B? What can we say about A $\cap$B, in relation to A and B? Try to prove a statement about this!
### 3.5.2 Union This operation collects the elements of either of two sets and includes them in a new set, called the union.
<div class="def-definition" markdown>
**Definition 3.5.5. Let A and B be any sets. The union of A and B is the set**
</div>
of elements that belong to either A or B, and is denoted by A$\cup$B. Symbolically, we define A $\cup$B = {x $\in$U | x $\in$A or x $\in$B} Notice that the "or" in the definition is an inclusive "or", meaning that A $\cup$B includes any element that belongs to A or B or possibly both sets.


> 🇨🇳 TODO: 待翻译


Example 3.5.6. Returning to the sets S1, S2, S3 we defined above in Example
3.5.2, we can say
S1 $\cup$S2 = {1, 2, 3, 4, 5, 7} S1 $\cup$S3 = {1, 2, 3, 4, 5, 7} S2 $\cup$S3 = {1, 2, 3, 4, 7} Also, since each of these unions are sets themselves, we could find their union with another set. For example, (S1 $\cup$S2) $\cup$S3 = {1, 2, 3, 4, 5, 7} $\cup${2, 4, 7} = {1, 2, 3, 4, 5, 7} Unions and Subsets Notice that A $\subseteq$(A $\cup$B) and B $\subseteq$(A $\cup$B), no matter what A and B are. Let's prove that!
Proposition 3.5.7. Let A and B be any sets. Then,
A $\subseteq$(A $\cup$B) and B $\subseteq$(A $\cup$B)
<div class="def-proof" markdown>
*Proof.* Let's say we have two sets, A and B. To prove A $\subseteq$(A $\cup$B), we need to
</div>
show that every element of A is also an element of A $\cup$B. Let x $\in$A be arbitrary and fixed. Then it is certainly that x $\in$A or x $\in$B (since x $\in$A). This shows x $\in$A $\cup$B. Since x was arbitrary, we have shown A $\subseteq$A $\cup$B. Let y $\in$B be arbitrary and fixed. Then it is certainly true that y $\in$A or y $\in$B (since we already know y $\in$B). This shows y $\in$A $\cup$B. Since y was arbitrary, we have shown B $\subseteq$A $\cup$B. What can you say about the relationship between A $\cap$B and A $\cup$B? If A $\subseteq$B, can we say anything about the relationship between B and A $\cup$B? Try to prove your observations! We should emphasize that claims like this---that A $\subseteq$A $\cup$B for any sets A and B---need to be proven; they do not hold by definition. The definition of the union of two sets is given above. Notice it says nothing about how A and A $\cup$B are related; it just tells us what the object A $\cup$B actually is. When you invoke or cite a definition and use it, be sure to do so; but also, be sure to explain any claim that isn't exactly a definition. Since we have proven these two little lemmas, we get to use them in the future by referencing them; had we not done so, we would have to re-explain these little facts every time we try to invoke them!


> 🇨🇳 TODO: 待翻译


### 3.5.3 Difference This operation takes the elements of one set and removes the elements that also belong to another set.
<div class="def-definition" markdown>
**Definition 3.5.8. The difference between A and B, denoted by A −B, is the**
</div>
set of all elements of A that are not elements of B. Symbolically, we define A −B := {x $\in$U | x $\in$A and x /$\in$B}
Example 3.5.9. Returning to the sets S1, S2, S3 we defined above in Example
3.5.2, we can say, for example, that
S1 −S2 = {2, 4, 5} S2 −S1 = {7} S2 −S3 = {1, 3} Set Difference Is Not Symmetric Notice that S1 −S2 ̸= S2 −S1 in the example above. In general, the operation "−", in the context of sets, is not symmetric, and this example here shows that. Can you find two sets A, B so that A −B = B −A? Can you find two sets A, B so that A −B = B −A ̸= $\emptyset$? Each of the other operations we have defined thus far is, in fact, symmetric. That is, A $\cap$B = B $\cap$A and A $\cup$B = B $\cup$A. Look back at the definitions for these operations and see why this makes sense. What is it about the language used in the property definition of the operation that makes this true? Notation Notes One more comment on this set difference notation. Notice that we use the standard subtraction symbol, "−", but this has nothing to do with "subtraction" in the way we usually think of it, like with numbers. This might be the first time you've encountered this ambiguity, or perhaps not, but there is a larger point that is relevant to mathematical notation and terminology: many symbols have different meanings depending on the context. When we write 7 −5, we clearly mean subtraction, i.e. 7 −5 = 2. However, when we write A −A where A has been identified as a set, we mean the set difference operation, i.e. A −A = $\emptyset$. Be sure to check the context of any statement to ensure that the symbols therein do mean what you think they mean!
### 3.5.4 Complement This operation identifies all of the elements that lie "outside" a set. This operation depends on the context of the universal set U. You'll notice that this is evident in the deifnition, and we will illustrate this through examples, as well.


> 🇨🇳 TODO: 待翻译


<div class="def-definition" markdown>
**Definition 3.5.10. The complement of A is the set of all elements that are**
</div>
not elements of A, and is denoted by ¯A. Symbolically, we define ¯A = {x $\in$U | x /$\in$A} Remember that we assumed A, B, U are given sets that satisfy A $\subseteq$U and B $\subseteq$U. Within this context, the set ¯A is well-defined, but this set certainly depends on A and U!
Example 3.5.11. For instance, let's return to the sets S1, S2, S3 we defined above
in Example 3.5.2. There, we used the context U = Z. In that case, ¯S1 = {6, 7, 8, 9, . . . } However, what if we had used U = {1, 2, 3, 4, 5, 6, 7}? In that case, ¯S1 = {6, 7} Since the symbolic notation ¯A makes no indication of the set U that it depends on, it is important to make this set clear in whatever context we are working. Try identifying some sets A, U1, U2 so that ¯A in U1 is different from ¯A in U2, and try identifying some sets so that ¯A is the same in both cases.
### 3.5.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the difference between a union and intersection of two sets? (2) What does it mean for two sets to be disjoint? (3) What is Z $\cap$N? What is Z $\cup$N? What is Z −N? (4) Is it possible for A −B = B −A to be true? How? (5) What is [3] in the context of N? What about in the context of Z? Of R? Try writing your answers using good mathematical notation, and set-buidler notation, perhaps. (6) Is (A $\cap$B) $\cap$C = (A $\cap$B) $\cap$C always true? Why or why not? What about with $\cup$instead of $\cap$? (7) What is the difference between the statements "7 −5" and "[7] −[5]"? (8) Suppose x $\in$A. Does A −x make sense, notationally? How can you change it to make sense? (9) What is (Z −N) $\cup$R?


> 🇨🇳 TODO: 待翻译


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) List the elements of the following sets: (a) [7] $\cup$[10] (b) [10] $\cap$[7] (c) [10] −[7] (d) ([12] −[3]) $\cap$[8] (e) (N −[3]) $\cap$[7] (f) (Z −N) $\cap$N (g) N $\cap${0}, in the context of Z (2) Find an example of sets A, B, C such that (A −B) −C = A −(B −C). Then, find an example where they are not equal. (3) State and prove a relationship between A and U −A. (4) Let A = [12], let E be the set of even integers, and let P be the set of prime natural numbers. What is A $\cap$E? What is A $\cap$P? What is (A $\cap$E) $\cap$P? Is it the same as A $\cap$(E $\cap$P)? Suppose the context is U = N. What are A $\cap$E and A $\cap$E? (5) What is {1} $\cap$P({1})? (6) Consider the sets {1} and {2, 3}. Compare the sets P({1} $\cup${2, 3}) and P({1}) $\cup$P({2, 3}). What do you notice? Repeat this exercise with "$\cap$" instead of "$\cup$". What do you notice? (7) Let A, U be sets, and suppose A $\subseteq$U. Let B = A, in the context of U. What do you think B is? Why?
## 3.6 Indexed Sets
### 3.6.1 Motivation Let's discuss a notion that we referenced briefly before and have been using already: the concept of indexing a collection of sets. This type of notation is convenient when we wish to define or refer to a large number of sets without writing out all of them explicitly. Using similar notation with the set operations we have defined already, we will be able to "combine" and "operate on" a large


> 🇨🇳 TODO: 待翻译


