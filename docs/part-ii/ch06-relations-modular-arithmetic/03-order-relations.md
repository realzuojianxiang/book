---
title: Order Relations
---

# Order Relations

Example 6.3.3. Define the following four relations on R:
(x, y) ∈R1 ⇐⇒x ≤y (x, y) ∈R2 ⇐⇒x < y (x, y) ∈R3 ⇐⇒x = y (x, y) ∈R4 ⇐⇒⌊x⌋= ⌊y⌋ (Recall that ⌊x⌋= max{a ∈Z | a ≤x} is the "floor" of a real number; it is the integer we get by rounding down.) Which of these are partial orders? Total orders? Neither? Think about this for a few minutes and try to sketch some proofs of your claims, or explain them out loud to a friend/classmate. Now, here are our thoughts. The relations R1 and R3 are both partial orders, but only R1 is a total order. The relations R2 and R4 are neither partial nor total orders (because R2 is not reflexive and R4 is not anti-symmetric). The idea behind any type of order relation---partial or total---is that we can somehow compare the elements of the set A and assign . . . well, an ordering to them. Heuristically speaking, a partial order induces "chains" of elements in A so that, along any chain, we can arrange the elements in a line, kind of like the number line and how we usually picture R; for a total order, there is only one "chain" and it is all of A. You might object to the idea that R2 isn't somehow an "order-like" relation, though, and you'd have a fair point. The only fundamental difference between R2 and R1 is that we don't allow equality; quite literally, the phrase "or equal to" is built into the definition of "≤", yet that phrase is left out of the definition of "<". This results in R2 being non-reflexive, but that's it. You might also notice that the relation R4 doesn't have this same type of relationship with R1; it seems to be something different (and we'll get to that soon enough). This motivates the following few definitions, wherein a partial or total order can be "relaxed" to a related ordering.
<div class="def-definition" markdown>
**Definition 6.3.4. Let A be a set and let R be a relation on A. We say R is**
</div>
irreflexive if and only if ∀x ∈A. (x, x) /∈R Notice that this is not the same as merely being not reflexive. Think about the quantifiers: reflexivity means every element is related to itself, so the logical negation of that means there exists at least one element that is not related to itself. Irreflexivity means that every element is not related to itself.
<div class="def-definition" markdown>
**Definition 6.3.5. Let A be a set and let R be a relation on A. We say R is a**
</div>
strict partial order if it is irreflexive, transitive, and anti-symmetric. We say R is a strict total order if it is irreflexive, transitive, anti-symmetric, and satisfies the following property: ∀x, y ∈A. x ̸= y =⇒[(x, y) ∈R ∨(y, x) ∈R]


> 🇨🇳 TODO: 待翻译


You might wonder what the connection is to non-strict order relations here. Well, there is a natural way to convert any order relation into a strict one, and vice-versa. We can always define one from the other by either building in, or removing, whether or not elements are related to themselves. The following lemma summarizes how to do this and, in so doing, shows that there are just as many strict orders as there are non-strict ones.
<div class="def-theorem" markdown>
**Lemma 6.3.6. Let (A, R1) be a partially ordered set. Then the relation S1 defined**
</div>
by (x, y) ∈S1 ⇐⇒[(x, y) ∈R1 ∧x ̸= y] is a strict partial order on A. Let (A, R2) be a totally ordered set. Then the relation S2 defined by (x, y) ∈S2 ⇐⇒[(x, y) ∈R2 ∧x ̸= y] is a strict total order on A. Let (A, S3) be a strictly partially ordered set. Then the relation R3 defined by (x, y) ∈R3 ⇐⇒[(x, y) ∈S3 ∨x = y] is a (non-strict) partial order. Let (A, S4) be a strictly totally ordered set. Then the relation R4 defined by (x, y) ∈R4 ⇐⇒[(x, y) ∈S4 ∨x = y] is a (non-strict) total order. Thinking back to the relations R1 and R2 defined above on R, it might seem a little odd to define "less than" by "less than or equal to and not equal to". It's certainly wordier! However, this is just a consequence of how we describe "≤" linguistically. Mathematically speaking, it is more natural to speak of reflexive relations and partial and total orders, and then alter those to become strict orders. We will see soon enough---when we talk about minimal elements---why reflexivity is a nice property, and this is a reasonable justification for why we would start with a partial order and then amend the definition to allow strict orders, as opposed to the other way around. For now, just notice that R2 is the strict total order that corresponds to the total order R1.
Question: is there a strict partial order that corresponds to the partial order
R3? If so, what is it? If not, why? The relation R4 is not any type of order relation, strict or otherwise. However, notice that R4 does nicely "package" the elements of R together. Essentially, every real number y satisfying 1 ≤y < 2 is "the same" under this relation. Likewise for every y satisfying 2 ≤y < 3, and every y satisfying, say, −5 ≤y < 4, and so on. Once that "packaging" is accomplished, we "know" that there is an ordering we can assign to those "packages", but no information about that order is encoded in the relation R4, itself. We would have to do some extra work to impose that ordering. This is why R4 is not an order relation


> 🇨🇳 TODO: 待翻译


of any kind, the way it is defined. However, it is what we call an "equivalence relation" because of this nice "packaging" property that partitions the elements of the set into separate classes. This is a notion we will explore in the next section. Once we have established those "packages", we can compare them and order them. Let's explore some examples in a context other than R. One of these following relations is actually a standard example of a partial order.
Example 6.3.7. Let S = [3] and consider the power set, P(S). (Remember that
the power set of S is the set of all subsets of S.) Define the following relations on P(S), where X, Y ⊆S: (X, Y ) ∈R1 ⇐⇒X ⊆Y (X, Y ) ∈R2 ⇐⇒X ⊂Y (X, Y ) ∈R3 ⇐⇒X ∩Y = ∅ (X, Y ) ∈R4 ⇐⇒X∆Y = S Recall that X∆Y is the symmetric difference of X and Y , and is defined as X∆Y = (X −Y ) ∪(Y −X) = (X ∪Y ) −(X ∩Y ). We claim that R1 is a partial order but not a total order. Before we go on to prove this claim, consider this challenge problem: Can you define a total order on P(S)? Can you do it in a way that would generalize to the case where S = [n], for some arbitrary n ∈N. Now, to prove that R1 is a partial order, we must show that it is reflexive, transitive, and anti-symmetric. To also show it is not a total order, we must show that it fails the additional property that says any two elements are somehow comparable. We will accomplish some of these steps, and leave the rest as exercises. • Let's prove R1 is anti-symmetric: Let X, Y ∈P(S) and assume (X, Y ) ∈ R1 and (Y, X) ∈R1. This means X ⊆Y and Y ⊆X, and therefore X = Y , by standard properties of sets. • Let's show R1 is not a total order. Consider X = {1} ⊆S and Y = {2, 3} ⊆S. Notice that X ⊈Y and Y ⊈X, so (X, Y ) /∈R1 and (Y, X) /∈ R1. That is, X and Y are incomparable under this relation. This relation separates the entire set P(S) into chains that are ordered within themselves, but separate chains may contain elements that are incomparable. For instance, consider the following subsets of P(S): A1 =  ∅, {1} , {1, 2} , {1, 2, 3}


> 🇨🇳 TODO: 待翻译


A2 =  ∅, {1} , {1, 3} , {1, 2, 3}


> 🇨🇳 TODO: 待翻译


A3 =  ∅, {2} , {1, 2} , {1, 2, 3}


> 🇨🇳 TODO: 待翻译


A4 =  {3} , {2, 3}


> 🇨🇳 TODO: 待翻译


These sets are not disjoint, so they do not form a partition of P(S). Notice, though, that R1 does induce a total order within each subset. By "induce" we mean that we use the same defining property of R1 but restrict our domain to the set A1, for instance, instead of all of P(S). Of course, there are even more sets we could define that are chains under this relation. Let's formalize this notion and then continue our example
<div class="def-definition" markdown>
**Definition 6.3.8. Let (A, R) be a partially ordered set, and let B ⊆A. Let ˆR**
</div>
denote the relation induced by R on B; that is, we set ∀x, y ∈A. (x, y) ∈ˆR ⇐⇒[x, y ∈B ∧(x, y) ∈R] If (B, ˆR) is a totally ordered set, then we say B is a chain of A (under R). With this definition in hand, we see that A1, A2, A3, A4 are chains of P(S) under R1. Now, try proving that R2 is a (strict) partial order, and then try writing some chains of P(S) under the relation R2. How do they compare to chains of P(S) under R1? In the next subsection, we will see why chains are important; specifically, we will look at special properties of partial orders, chains, and total orders, that allow us to find "smallest" and "greatest" elements of subsets. Before we move on, though, let's see two more related examples of partial orders.
Example 6.3.9. Consider the set R × R.
We define a relation R on R × R by establishing when a pair of real numbers is related to another pair of real numbers. Specifically, let's say  (u, v), (x, y)  ∈R ⇐⇒[u ≤x ∧v ≤y] One can prove that R is a partial order on R×R. We will prove the transitivity property and leave the rest as exercises:
<div class="def-proof" markdown>
*Proof.* Let (u, v), (x, y), (z, w) ∈R × R. Suppose that ((u, v), (x, y)) ∈R and
</div>
that ((x, y), (z, w)) ∈R. This means u ≤x and x ≤z, so u ≤z; also, this means v ≤y and y ≤w, so v ≤w. Thus, ((u, v), (z, w)) ∈R. This shows R is transitive. Hint: to prove R is not a total order, we must find a counterexample. That is, we need a pair (x, y), (u, v) such that neither ((x, y), (u, v)) ∈R nor ((u, v), (x, y)) ∈R. Think about the relation R visually, i.e. geometrically, to come up with such an example. Think about what the chains are under this relation. Try to describe them geometrically and draw a few representatives.
Example 6.3.10. Let A be the standard English alphabet of 26 letters, and let
W be the set of all finite strings of letters from A. That is, W is the set of all possible "words", where we allow any combination of letters to be included in our "dictionary". Let's try to define L, the standard lexicographic ordering on


> 🇨🇳 TODO: 待翻译


W. It helps to represent A as the set [26], where a = 1 and b = 2 and so on, until z = 26. Then, we say a word w ∈W is represented by w = (w1, w2, . . . , wn) where n ∈N and ∀i ∈[n]. wi ∈A Notice that for any two words v, w ∈W, we can compare them "letter by letter" reading left to right until we reach a difference between them. Wherever that difference occurs, we sort the two words according to the comparison of those two letters. If one word is longer than the other and they have the same letters otherwise, we want to sort the longer one after the shorter one, just like "there" comes before "therefore" in the dictionary. (v, w) ∈L ⇐⇒at the smallest index i where vi ̸= wi, we have vi < wi (and where a blank space is treated as 27) Think about why this corresponds to the usual ordering of words in the dictionary. (Could you define this using more rigorous mathematical notation? Try it!) Now that we've looked at several examples of order relations, we recommend you try several of the exercises to practice identifying these relations and proving their properties. After that, we can move on to talk about many other interesting and useful properties of order relations!
### 6.3.1 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the difference between a partial order and a total order? (2) Give an example of a partial order that is not total. Give an example of a total order. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let S = [2], and define R on P(S) by (x, y) ∈R ⇐⇒x has at least as many elements as y. Prove that S is not a partial order.


> 🇨🇳 TODO: 待翻译


(2) Let S = [3], T = [2], and define R ⊆S × T by (x, y) ∈R ⇐⇒x ⊇ y. Prove/disprove each of the four standard properties of relations for R (i.e. reflexive, symmetric, transitive, anti-symmetric.) Use your results to determine whether R is any kind of order relation(s).
## 6.4 Equivalence Relations
### 6.4.1 Definition and Examples
Let's shift gears only slightly and talk about another type of relation that satisfies a different subset of the four standard properties of relations. In fact, let's return to a particular relation we mentioned in a previous example: on the set R, define R to be the relation where (x, y) ∈R ⇐⇒⌊x⌋= ⌊y⌋ (In case you missed it in the Optional Reading , this is seen in Example 6.3.3.) Notice that this relation is • reflexive because ∀x ∈R. ⌊x⌋= ⌊x⌋ • symmetric because ∀x, y ∈R. ⌊x⌋= ⌊y⌋=⇒⌊y⌋= ⌊x⌋ • transitive because ∀x, y, z ∈R.  ⌊x⌋= ⌊y⌋∧⌊y⌋= ⌊z⌋  =⇒⌊x⌋= ⌊z⌋ This particular set of properties has some interesting and useful consequences, so we assign a name to any relation that has these three properties.
<div class="def-definition" markdown>
**Definition 6.4.1. Let A be a set and R a relation on A. If R is reflexive,**
</div>
symmetric, and transitive, then we say R is an equivalence relation. That's it! Given any relation R on a set S, all we have to do is go through and prove/disprove these three properties to determine whether R is, in fact, an equivalence relation. Let's run through some of the examples of relations that we have seen already and determine whether they are equivalence relations or not, based on what we've proven about them.
Example 6.4.2. (1) Look back at the equality relation on an arbitrary set X
that we defined in Example 6.2.9. This is an equivalence relation. Certainly, (x, x) ∈R, since x = x. However, the hypothesis x R y is false for any x ̸= y, which makes the conditional statement true. Thus, the only "relevant case" in the symmetric property is the one where x = y, in which case, yes, y = x, too. Similarly, for the transitive property, if either x ̸= y or y ̸= z, the hypothesis of the defining conditional statement is false, so the statement itself is true; and when x = y and y = z, yes, certainly x = z. This may not seem like a particularly enlightening development, but it is nice to know that there is always at least one equivalence relation we can define on any set.


> 🇨🇳 TODO: 待翻译


