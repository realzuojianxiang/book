---
title: A.3 Induction
---

# A.3 Induction

A.3.3 "Minimal Criminal" Argument • The second condition in the hypothesis of the Principle of Induction is a conditional statement, so we can prove it by contrapositive. The contrapositive says ¬P(k) =$\Rightarrow$¬P(1) ∨¬P(2) ∨ $\cdot$  $\cdot$  $\cdot$ ∨¬P(k −1) which is to say, "If the proposition fails for some particular value k, then we can find some prior instance of the proposition (from 1 to k −1) that also fails. • Proving a claim by a "minimal criminal" argument: Suppose we have a variable proposition P(n) that is defined for all n $\in$N, and we want to prove P(n) holds for every n $\in$N. Base Case(s): Prove that P(1) holds. (Depending on what happens in the Induction Step, you might need more than one Base Case.) Induction Hypothesis: Suppose that k is an arbitrary and fixed natural number that satisfies some inequality (k $\geq$ , depending on what happens in the Induction Step), and suppose that ¬P(k) holds; that is, suppose P(k) fails to hold. Induction Step: Prove that ¬P(1) ∨¬P(1) ∨¬P(2) ∨ $\cdot$  $\cdot$  $\cdot$ ∨ ¬P(k −1); that is, show that the proposition fails to hold at some prior instance, as well. Conclusion: By induction, $\forall$n $\in$N. P(n).


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS A.4 Relations • Let A, B be sets. A relation between A and B is a set of ordered pairs R $\subseteq$A × B. Given elements a $\in$A and b $\in$B, we say a and b are related if and only if (a, b) $\in$R. The set A is called the domain and the set B is called the codomain. The set R is called the relation set. We say R is a relation between A and B. When A = B, we say R is a relation on the set A. A.4.1 Properties of Relations Let A be a set and let R be a relation on A, i.e. R $\subseteq$A × A. (Note: These properties only apply in this case, and not to a relation between two different sets A and B.) • We say R is reflexive if $\forall$x $\in$A. (x, x) $\in$R (i.e. every element is related to itself). • We say R is symmetric if $\forall$x, y $\in$A. (x, y) $\in$R =$\Rightarrow$(y, x) $\in$R (i.e. the order of the comparison doesn't matter). • We say R is transitive if $\forall$x, y, z $\in$A. [(x, y) $\in$R ∧(y, z) $\in$R] =$\Rightarrow$(x, z) $\in$R (i.e. the relation always "transitions through a middle-man") • We say R is anti-symmetric if $\forall$x, y $\in$A.. [(x, y) $\in$R ∧(y, x) $\in$R] =$\Rightarrow$x = y (i.e. two elements related in both directions must be the same). A.4.2 Equivalence Relations Let A be a set and let R be a relation on A. • We say R is an equivalence relation if and only if R is reflexive, symmetric, and transitive.


> 🇨🇳 TODO: 待翻译


