---
title: A.4 Relations
---

# A.4 Relations

• If R is an equivalence relation and x ∈A, then the equivalence class corresponding to x (under the relation R) is [x]R = {y ∈A | (x, y) ∈R} which is the set of all elements related to x. • If R is an equivalence relation, then A/R is A modulo R; it is the set of all equivalence classes: A/R = {[x]R | x ∈A} • Theorem: If R is an equivalence relation on A, then the equivalence classes (i.e. the elements of A/R) form a partition of A. • Theorem: If I is some index set and {Si | i ∈I} is a partition of A, then this corresponds to a unique equivalence relation on A defined by relating two elements of A if and only if they belong to the same part of the partition.


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS A.4.3 Modular Arithmetic Congruence mod n • Let n ∈N be given. For any x, y ∈Z, we say x and y are congruent modulo n if and only if n | x −y. Equivalently, this means that x and y have the same remainder upon division by n. (This equivalence is not part of the definition; rather, it follows from the Division Lemma stated below.) We write this as x ≡y mod n. (Note: mod n is not an operator or function; it is a modifier we place at the end of a line of arithmetic/algebra to indicate that all the operations have been performed modulo n.) • The relation ≡is an equivalence relation, for every n ∈N. • Division Lemma: Let n ∈N be given. Let x ∈Z be given. Then ∃! k, r ∈Z.  (x = kn + r) ∧(0 ≤r ≤n −1)  Notice that "∃!" indicates this representation of x as a multiple of n plus a remainder is unique. • Modular Arithmetic Lemma: Let n ∈N be given. Let a, b ∈Z be given. Suppose that a ≡r mod n and b ≡s mod n. Then, a + b ≡r + s mod n and a · b ≡r · s mod n Multiplicative Inverses in Z mod n • Let x, y ∈Z be given. We say x and y are relatively prime if and only if they have no common factors (divisors), other than 1. • MIRP Lemma: (Multiplicative Inverses for Relative Primes) Suppose n ∈N and a ∈Z, and that a and n are relatively prime. Consider the congruence ax ≡1 mod n. Then there exists a solution x to this congruence. (In fact, there are infinitely-many solutions to this congruence, and they are all congruent modulo n.) • When ax ≡1 mod n, we say x is the multiplicative inverse of a in the context of Z modulo n. We write this as x ≡a−1 mod n. In fact, any integer y congruent to x modulo n will satisfy ay ≡1 mod n, so we really consider the equivalence class [x]mod n to be the multiplicative inverse of the equivalence class [a]mod n.


> 🇨🇳 TODO: 待翻译


• Assuming a−1 exists in the first place, (a−1)−1 ≡a mod n. • Let p be a prime. Then all of the numbers 1, 2, 3, . . . , p−1 are guaranteed to be relatively prime to p, so they all have multiplicative inverses in the context of Z modulo p. • If a has a multiplicative inverse in the context of Z mod n, there is guaranteed to be such an inverse between 1 and n−1. In practice, we can just check each of these candidates one-by-one until we find the inverse. Results • Chinese Remainder Theorem: Suppose r ∈N and we have r natural numbers, n1, n2, . . . , nr, that are pair-wise relatively prime. (That is, no two of the numbers have any common factors, besides 1.) Suppose we also have r integers, a1, a2, . . . , ar. Then there exists a solution X to the system of congruences defined by the ni and ai; that is, ∃X ∈Z. ∀i ∈[r]. X ≡ai mod ni Furthermore, if we define N = Y i∈[r] ni, then all of the infinitely-many solutions Y to the system of congruences satisfy X ≡Y mod N.


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS A.5 Functions • Let A, B be sets. Let f be a relation between A and B, so f ⊆A × B. Also, assume that f has the property that ∀a ∈A. ∃! b ∈B. (a, b) ∈f That is, assume every element of the domain A (the "input" set) has exactly one corresponding element of the codomain B (the "output" set) so that the two elements are related, under f. Put even another way, "Every input has exactly one corresponding output." Such a relation is called a function from A to B. We call A the domain of the function and B the codomain of the function. We write f : A →B to mean f is a function from A to B. If a is related to b, i.e. (a, b) ∈f, then we write f(a) = b knowing that there is exactly one such b for each a. • Given a proposed domain set A, a proposed codomain set B, and a proposed "rule" f that says what to output, given an element of A, then we say f is a well-defined function if the rule is defined on all elements of A and, for each a ∈A, the rule outputs exactly one element that actually does lie in the set B. (Note: every function is a well-defined function; this rule applies when we are trying to determine whether a given "rule" actually is a function or not.) • Let f : A →B and g : A →B be functions. We say f and g are equal (in the sense of functions) and write f = g when ∀a ∈A. f(a) = g(a). That is, f = g when the two functions yield the same output for every input. A.5.1 Images and Pre-Images • Let f : A →B be a function. Let X ⊆A. The image of X under the function f is Imf(X) = {b ∈B | ∃a ∈X. f(a) = b} An equivalent way of writing this set is Imf(X) = {f(a) | a ∈X}


> 🇨🇳 TODO: 待翻译


