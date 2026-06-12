---
title: Defining the Natural Numbers
---

# Defining the Natural Numbers

Next to define 2, we consider sets containing two elements, like {$\emptyset$, {$\emptyset$}} , {$\emptyset$, {{$\emptyset$}}} , {{$\emptyset$} , {{$\emptyset$}}} and so on. We seek a natural representative, and we notice that the first set listed above contains the two objects, 0 and 1, that we have already defined! Thus, defining 2 = {0, 1} is a natural choice and, again, we know 2 ̸= 0 and 2 ̸= 1. Successors This gives us an intuitive idea of how to continue this process and define any natural number: for any n $\in$N, we define n = {0, 1, 2, . . . , n −2, n −1} However, given a set, it would be quite difficult to verify, using this definition, whether or not that set represents a natural number. We would like a better definition of the elements of N; we want to know, given any set, whether it belongs in N. Look back at the element n above; we could also write n = {0, 1, 2, . . . , n −2, n −1} = {0, 1, 2, . . . , n −2} $\cup${n −1} = (n −1) $\cup${n −1} Look at that! We have a natural way of defining an element of N in terms of the previous element and in terms of set operations. This motivates the following definition.
<div class="def-definition" markdown>
**Definition 3.8.1. Given any set X, the successor of X, denoted by S(X), is**
</div>
defined to be S(X) = X $\cup${X}. This definition applies to all sets, but in the context of natural numbers, it means that the successor of n is precisely that natural number we "know" intuitively to be one larger, namely n + 1. Inductive Sets This brings us closer to our definition of N. We certainly want 1 $\in$N and we also want S(n) $\in$N for any element n $\in$N. To codify this symbolically, we make the following definitions:
<div class="def-definition" markdown>
**Definition 3.8.2. A set I is called inductive provided**
</div>
1. 1 $\in$I 2. If n $\in$I, then S(n) $\in$I, as well. Certainly, N itself (as we hope to define it) should be an inductive set. Are there other inductive sets? Think about this. What properties would they have? Would they contain elements that are not natural numbers? We don't want to address these questions in depth, but for the sake of our discussion here, we will point out that there are, indeed, other inductive sets. We don't want any of those sets to be N, so we make this definition:


> 🇨🇳 TODO: 待翻译


<div class="def-definition" markdown>
**Definition 3.8.3. The set of all natural numbers is the set**
</div>
N := {x | for every inductive set I, x $\in$I} Put another way, N is the smallest inductive set, in the sense of set inclusion: N = \ I$\in${S|S is inductive} I This dictates that N is a subset of every inductive set. This gives us the "checking property" we desired. Any set x is a natural number (i.e. x $\in$N) if and only if it is an element of every inductive set (i.e. x $\in$I for every inductive set I). This also tells us that N $\subseteq$I for every inductive set I. There are some other set theoretic discussions that could be made here: How do we know that such an infinite set exists? (In actuality, we need to make this an axiom of set theory! Assuming these types of sets exist, how do we characterize those other inductive sets that are not N? Addressing these questions lies outside the scope and goals of this course, so we will not address them. We will, however, mention a few properties of N now, specifically ones that will be useful in setting mathematical induction on a rigorous foundation. (In case you're wondering, think about the set of integers, Z. Try to explain why this set is, indeed, inductive. What about R? What about Z −N?) Properties of N Before we define the principle of induction, let's think about some of the common properties and uses of natural numbers: orderings and arithmetic. Given any two natural numbers, we can compare them and decide which one is larger and which one is smaller (or if they are equal). We usually write this with symbols like 1 < 3, 1 $\leq$5, 4 ̸< 2, 3 = 3, etc. Can we phrase these comparisons in terms of sets, knowing that we have now defined the elements of N as sets, themselves? Yes, we can! Look back at the definition of successor. Built into that definition is the fact that X $\in$S(X)! This observation gives us the following definition:
<div class="def-definition" markdown>
**Definition 3.8.4. Given two natural numbers m, n $\in$N, we write m < n if and**
</div>
only if m $\in$n. This defines an order relation on the set N. We will discuss the concepts of relations and orders later on in the book (in Section 6.3). What about arithmetic? What is m + n in terms of the sets m and n? How do we define this operation and its output? How do we know m + n is another natural number? Can we be sure that m + n = n + m? These are questions we can address later on after discussing functions and relations.


> 🇨🇳 TODO: 待翻译


### 3.8.2 Principle of Mathematical Induction For now, let us present a more rigorous version of induction:
<div class="def-theorem" markdown>
**Theorem 3.8.5 (Principle of Mathematical Induction). Let P(n) be some**
</div>
"fact" or "observation" that depends on the natural number n. Assume that 1. P(1) is a true statement. 2. Given any k $\in$N, if P(k) is true, then we can conclude necessarily that P(k + 1) is true. Then the statement P(n) must be true for every natural number n $\in$N. Let us first prove this theorem before discussing its assumptions and consequences in detail.
<div class="def-proof" markdown>
*Proof.* Define the set S to be the natural numbers for which the statement P is
</div>
true. That is, define S = {n $\in$N | P(n) is true}. By definition, S $\subseteq$N. Furthermore, the assumptions of the theorem guarantee that 1 $\in$S and that whenever k $\in$S, we know k + 1 $\in$S, as well. This means S is an inductive set. By the observation we made after defining N, we know that N $\subseteq$S. Therefore S = N, so the statement P(n) is true for every natural number n. This is pretty slick, right? It seems that all of the desired conclusions "fell out of" our definitions! In this sense, the definitions and axioms are natural choices, because they accomplish what our intuition already "knew" about the set N and its properties. There are a few minor issues that we have left undiscussed. Specifically, what do we mean by a "fact" or "observation" that depends on a natural number n? What does it mean to necessarily conclude that P(k + 1) is true when P(k) is true? What do we even mean by true? These are all deep mathematical questions and involve a thorough study of logic, and we will discuss these issues in the next chapter! Onward! Huzzah!
### 3.8.3 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is an inductive set? Give an example of one that is not N or Z. (2) We defined S = {n $\in$N | P(n) is true} in the proof of the Principle of Mathematical Induction. What does this mean? Describe this set in words. (3) Come up with your own analogy for how Induction works.


> 🇨🇳 TODO: 待翻译


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) What if we changed the definition of successor to be S(X) = {X}. Using 0 = $\emptyset$, what are 1, 2, 3, and 4 in terms of sets? Do they still satisfy the equality n = {0, 1, . . . , n −1}? If not, do they satisfy some other relationship? Explore! (2) Have a debate with a friend about whether or not infinite sets exist. Why do we need to assume the existence of an inductive set to define N? Does this seem valid to you? Does it make sense, physically? Mathematically? (3) Consider a simple arithmetic statement, like 1 + 2 = 3. Write out the numbers 1, 2, and 3 in terms of sets, and see how this equation might make sense. What does "+" mean, in this context? (4) Investigate how one might define Z, using N. Do some exploring online or in books, or make up an idea on your own.
## 3.9 Proofs Involving Sets Now that we've gone through many definitions and examples, to introduce what sets are and how to manipulate them, let's actually write up some rigorous, mathematically correct, and well-written proofs about sets. All of the propositions/lemmas contained here are useful facts that we can cite later on, and we would expect you to be able to prove claims like these. (Note: A lemma is just a small result that requires some proof, and can be cited later to prove more significant theorems.) Furthermore, all of these proofs are of the type of quality and rigor that we will expect from you in the future, the very near future . . . Use these as guidelines, if you'd like!
### 3.9.1 Logic and Rigor: Using Definitions The main point we'd like to emphasize here---as we transition from descriptive, "wordy", and intuitive proofs into more rigorous, mathematically correct, and formally-written ones---is that formal definitions are very important. Fundamentally, they're essential because when we say, for example, "A $\cup$B", we need to know that you know exactly what that symbol means and how it operates on the sets A and B. As another example, when we say "Prove A = B", we have a very specific goal in mind, and you need to be on the same page. It always helps to have an intuitive understanding of the main concepts---"Oh, the statement A = B just


> 🇨🇳 TODO: 待翻译


