---
title: Compositions and Inverses
---

# Compositions and Inverses

Bijections "Pair" Elements Let's say there are 5 pens and 5 books on a table in front of us. But also, let's pretend that we didn't know how to count them. How could we verify that there are just as many pens as there are books? Instead of saying, "There are 5 pens and 5 books, and 5 = 5", can we somehow show the set of books and the set of pens has the same size, without knowing what that size is? This is where a bijection comes into play. We can pair offthe pens and books one-by-one. We can line them up on the table and draw a line between them, showing a correspondence between them. In the language of sets, we are identifying a bijection between the set of pens and the set of books. This idea is so important, that we want to impress it upon you with a quote: In the land of Cardinality, the Bijection is King. Imagine our study of cardinality is a journey through the Kingdom of Cardinality. In this Kingdom, we bow down to King Bijection, for he rules all. Only he can tell us when two sets have the same cardinality, whether they be finite or infinite. Moreover, we really need to use this set terminology, because we will see some surprising and counter-intuitive results. Using these formal definitions and concepts will allow us to be rigorous and precise. The examples and results we see might blow our minds a little bit (or a lot!), but having them rooted in concepts we've already seen and theorems we've already proven lets us actually belive these results, mathematically speaking!
Definitions and Notation
First, let's define what it means to be finite.
<div class="def-definition" markdown>
**Definition 7.6.1. Let S be any set. We say S is finite if and only if**
</div>
∃n ∈N ∪{0} such that there exists a bijection f : S →[n] In this case, we write |S| = n to indicate that the size of S is n.
Note: The empty set S = ∅is finite, since [0] = ∅.
This is why we said n ∈N ∪{0} in the definition, and not just n ∈N. The function f : ∅→∅ that is a bijection is simply the empty relation. (Remember that a function is a relation!) By definition, sets of the form [n] are finite. They are our standard examples of finite sets, with size |[n]| = n. Thus, to show that a set S has size n, we need to find a bijection between S and [n]. For example, consider the set {1, 3, 5}. This clearly looks like it has size 3. We can show this by exhibiting the bijection f : {1, 3, 5} →[3] defined by f(1) = 1 and f(3) = 2 and f(5) = 3. It's interesting to think about whether a finite set could have two different sizes. The definition technically doesn't preclude this, but we can prove that the size of a finite set is unique. Think about how to do that . . . We will do so after a few more essential definitions.


> 🇨🇳 TODO: 待翻译


