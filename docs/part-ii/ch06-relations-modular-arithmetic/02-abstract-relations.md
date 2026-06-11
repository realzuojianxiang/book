---
title: Abstract (Binary) Relations
---

# Abstract (Binary) Relations

6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


Example 6.2.5. Let A = B = Z and define a relation R on Z by setting
(x, y) ∈R ⇐⇒x and y have the same parity Then (2, 8) ∈R and (−3, 7) ∈R and (−99, −99) ∈R, but (1, 2) /∈R and (0, −3) /∈R and (π, 0) /∈R (since π /∈Z).
Example 6.2.6. Define a relation L on R by setting
(x, y) ∈L ⇐⇒x < y Then (−1, π) ∈L and (0, 100) ∈L but (2, 2) /∈L and (π, −1) /∈L. Notice that these are ordered pairs (which we may forget about since A = B = R) so the order of the elements matters. Indeed, knowing that (x, y) ∈L doesn't necessarily imply that (y, x) ∈L, in general. In this example, that implication is always False, in fact! Recall that we sometimes write x L y to say (x, y) ∈L, so let us note that we could say -1 R π but π ̸R -1 here, and 2 ̸R 2. The Empty Relation
Remark 6.2.7. The examples we have seen thus far are interesting relations, in
some sense. Given any x, y ∈R, we can determine whether x < y or not by just comparing them and deciding whether that property holds. That is, each of the examples we have seen thus far were defined by saying (a, b) ∈R ⇐⇒P(a, b) is true for some property P(a, b). A relation doesn't necessarily need to be defined this way, though. For instance, we know ∅⊆S for any set S. Thus, given two sets, we can always define the trivial relation by using the fact that ∅⊆A×B; that is, the trivial relation is the one where no elements are related! This is relatively "uninteresting" for sure, but it still satisfies the definition of a relation, so we allow it. Any Set of Ordered Pairs is a Relation
Remark 6.2.8. Given sets A, B, any subset R ⊆A × B defines a relation. It
might be difficult (or impossible, perhaps) to identify a property that characterizes that relation. For instance, if A = {1, 3, 5} and B = {⋆, ♥}, then we can define a relation between A and B by setting R = { (1, ⋆), (5, ♥) } Why is 1 related to ⋆? Why is 3 not related to anything? Who knows? It's just a set of ordered pairs! This is, mathematically speaking, totally fine.


> 🇨🇳 TODO: 待翻译


The Equality Relation
Example 6.2.9. Another example of a way to define a relation on any set X is to
define the equality relation. That is, let (x, y) ∈R ⇐⇒x = y. Notice that this doesn't depend on what X is or what types of objects it contains as elements, merely that it is a set. Similarities Between Relations
Example 6.2.10. Let S be the set of students in your class. Define a relation
R1 between S and N by saying (s, n) ∈R1 if person s ∈S is n years old. Write out a few elements of this relation set. Now, define a relation R2 on S itself by saying (s, t) ∈S if persons s and t are the same age (in years). Write out a few elements of this relation set. How do the relations R1 and R2 compare? Do they somehow "encode" the same information about the elements of the set S? Why or why not? Is there a way we can use R1 to determine R2? What about the other way around? Think about this carefully and try to write a few sentences that summarize your thoughts about this. We will adress these questions immediately in the next subsection, but take some time now to investigate on your own! Relations "Encode" Information The previous example is meant to illustrate the real use of abstract relations and motivate why we even talk about them at all (besides our overarching goal of rigorizing the notion of a function). In some sense, a relation is a way of "storing" information about elements of two sets, or one set; it's a way of comparing two elements and declaring whether or not they satisfy some property. In a more general sense, though, a relation can provide information about how "well" a set's (or sets') elements behave in terms of a specific property. For instance, notice that in the previous example, the relation R1 told us a little "more" about the elements of S. Certainly, R1 tells us who is the same age as anyone else: we can look for two pairs like (s, n) and (t, n), say, with the same second coordinate. But R1 also tells us what that age is: just look at that second coordinate the pairs share. This does not work with R2. Knowing (s, t) ∈R2 just tells us students s and t are the same age; it does not tell us what that age is! In that sense, R1 is a "better" relation and provides "more" information. There are also reasons why R2 is "better", too, though! For example, look at one of its nice properties: if (x, y) ∈R2, it is necessarily true that (y, x) ∈R2, as well. This is certainly not true of R1 because when (s, n) ∈R1, it doesn't even make sense to say whether or not (n, s) ∈R1 because the order of the pair does not match the domain and codomain! Does this property now make R2 a "better" relation? Well, yes and no. It depends on context and what type of information we want to encode and retrieve. In certain situations, maybe you'd want to use R1, and other times you'd want to use R2.


> 🇨🇳 TODO: 待翻译


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


But we're getting slightly ahead of ourselves here! We can't yet describe to you what these properties mean and why they may or may not be desirable. On the whole, though, we are curious about these types of properties and when they do (and do not) hold for all pairs of elements in a given set. In the next subsection, we will define and explore several common properties of abstract relations. It is not a guarantee (or requirement) that any relation possess one or more of these properties, but these are the ones that have proven to be interesting and useful in the mathematical and real-world contexts in which relations arise. After that, we'll see lots of examples of relations and discuss how to prove these properties hold. While doing this, we'll develop some intuitions for how to work with relations and even figure out the kinds of claims we'd be trying to prove in the first place!
### 6.2.2 Properties of Relations Let's start right offby defining a few properties. For each of these properties, every relation either does or does not satisfy it. We encourage you to read each property one by one and try to construct a relation that does satisfy the property, and then one that doesn't. This will help you truly understand the underlying principles of the property and how relations work. (Then, try to define some relations that have some combination of the properties!) After these definitions, we will provide some canonical examples that you might have even come up with yourself! But seriously, do try to come up with some on your own and share any interesting ones that you have!
Definitions: Properties of a Relation on a Set
These properties rely on being able to reverse the order of a pair. That is, given (x, y) ∈R, we might wonder about the pair (y, x); however, the relationship between the domain and codomain demands that (y, x) ∈A×B, as well. Thus, we will require A × B = B × A, which only happens when A = ∅or B = ∅or A = B. (Remember we proved this earlier when talking about sets in Chapter 3!) Since A = ∅and B = ∅are uninteresting cases, we will assume in these properties that A = B (and A ̸= ∅), so we are defining a relation on one non-empty set and comparing its elements with each other.
<div class="def-definition" markdown>
**Definition 6.2.11. Let A be a set and let R be a relation on A, i.e. R ⊆A×A.**
</div>
• We say R is reflexive if ∀x ∈A. (x, x) ∈R That is, every element is related to itself. • We say R is symmetric if ∀x, y ∈A. (x, y) ∈R =⇒(y, x) ∈R That is, the order of the comparison doesn't matter.


> 🇨🇳 TODO: 待翻译


• We say R is transitive if ∀x, y, z ∈A. [(x, y) ∈R ∧(y, z) ∈R] =⇒(x, z) ∈R That is, relationships can transition through a middle-man. • We say R is anti-symmetric if ∀x, y ∈A. [(x, y) ∈R ∧(y, x) ∈R] =⇒x = y That is, two different elements can be related in at most one way, or not at all. To see why this is the same statement, let's look at the contrapositive of the conditional statement in the line above: ∀x, y ∈A. x ̸= y =⇒[(x, y) /∈R ∨(y, x) /∈R]
Note: it is important to point out that anti-symmetric is NOT the same
as not symmetric. Look carefully at the logical order and quantifiers of the properties to make sense of this. For example, the ≤relation on R is antisymmetric but not symmetric. Think about why this is the case. In fact, try to come up with a relation that is both anti-symmetric AND symmetric. It actually isn't that hard! We've already mentioned one fundamental relation that has this property.
### 6.2.3 Examples
Again, try to come up with some relations that do and do not satisfy the four properties we just defined. We will present some nice, canonical examples of relations defined on N below to give you some concrete ideas to keep in mind. Feel free to add to this list as you come up with simple examples, perhaps defined on other sets like Z and R.
Example 6.2.12. Throughout this example, relations are defined on the set N.
• Define R1 on N by (x, y) ∈R1 ⇐⇒x divides y (i.e. y is divisible by x, or ∃k ∈N such that y = kx. This definition is formally restated below; see Definition 6.2.15) Then R1 is reflexive, because x|x since x = 1 · x. The divisibility relation is reflexive. • Define R2 on N by (x, y) ∈R2 ⇐⇒x and y have the same parity Then R2 is symmetric because if x and y have the same parity then certainly y and x have the same parity. The "has the same parity" relation is symmetric.


> 🇨🇳 TODO: 待翻译


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


• Define R3 on N by (x, y) ∈R3 ⇐⇒x < y Then R3 is transitive because if x < y and y < z then x < y < z, so x < z. The "<" relation is transitive. • Define R4 on N by (x, y) ∈R4 ⇐⇒x ≤y Then R4 is anti-symmetric because if x ≤y and y ≤x then x ≤y ≤x so x = y. The "≤" relation is anti-symmetric.
Example 6.2.13. Remember that a relation is just a set of ordered pairs. We
don't have to define it in terms of a property. Let's see an example phrased this way, and investigate its properties: Define the relation R on the set S = {a, b, c} by R = {(a, a), (a, c), (b, c), (c, b)} Notice that this relation is: • Not Reflexive: (c, c) /∈R • Not Symmetric: (a, c) ∈R but (c, a) /∈R • Not Transitive: (a, c) ∈R and (c, b) ∈R but (a, b) /∈R • Not Anti-Symmetric: (b, c) ∈R and (c, b) ∈R but b ̸= c
Example 6.2.14. Let's get a little practice using slightly different notation for
relations. Remember that we can also write something like x R y to mean (x, y) ∈R. Define the relation ⋆on the set S of people in your class by saying, for any x, y ∈S, x ⋆y ⇐⇒ x and y were born in the same month We claim that this relation is reflexive, symmetric, and transitive. Do you see why? • The relation is reflexive because each person is certainly born in the same month as themself (i.e, x ⋆x). • The relation is symmetric because if person x and person y were born in the same month (i.e. x ⋆y), then certainly person y and person x (just a different order!) were born in the same month (i.e. y ⋆x). • The relation is transitive because . . . well, you get the idea, right? We're just appealing to the concept of the word "same" over and over!


> 🇨🇳 TODO: 待翻译


What about anti-symmetry here? It depends! Are there two different people in your class that were born in the same month? If so, this relation is not antisymmetric. However, was everybody in your class born in a different month? If so, this relation is anti-symmetric, because no one will be related to anybody but themself! Think about this . . .
### 6.2.4 Proving/Disproving Properties of Relations When we are presented with a set and a relation on that set, we will immediately wonder whether any of these properties hold. By playing around with some particular elements of the set in question, we can try to conjecture whether or not the relation satisfies a property, and then attempt to prove/disprove it. This sometimes amounts to a bit of "guessing and checking" but, ultimately, to prove a property holds, we must prove a statement of the form "For all . . . it is true that . . . ". (Look back at our proof techniques from Section 4.9!) Thus, proving a relations property amounts to taking an arbitrary element (or elements) and arguing about how they are related. To disprove such a statement, we would prove its logical negation, which is of the form "There exists . . . such that . . . ." (Again, look back at our proof techniques!) Thus, disproving a property amounts to finding a counterexample. Let's look at a couple of examples of proving/disproving relation properties. There are several more examples of these styles of proofs in the exercises, as well. The "Divides" Relation on Z We will present (or, perhaps, remind you of) one definition first, because it will be the basis of one of our examples. This is a formal definition of what it means for one integer to divide another integer.
<div class="def-definition" markdown>
**Definition 6.2.15. Let a, b ∈Z. We say x divides y, and write x | y, if and**
</div>
only if ∃k ∈Z. y = kx
Example 6.2.16. Define the relation R on Z by
(x, y) ∈R ⇐⇒x | y Let's determine whether R satisfies any of the four properties of relations, and then prove/disprove all our claims! In general, depending on the set and relation in question, you might immediately notice whether or not a property holds, via some intuition or just being able to "see" it right away. If so, great! If not (which is far more likely) we recommend starting a "proof" as if a property actually held, and seeing if you can finish. If you do, well then, you just proved the property! If you struggle at some point, maybe that's because the property doesn't hold, and the point in your proof where you're caught up will give you some insight into finding a counterexample. This strategy doesn't always work (maybe you're


> 🇨🇳 TODO: 待翻译


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


struggling through a proof because it's actually challenging, say) but it can be quite helpful, so keep it in mind. We will see it in action in this example, too. One other strategy---an even simpler one, actually---is to just make a statement out loud, or write down in words what the relation and the property in question is. Sometimes, just making yourself say something in plain language, instead of reading abstract symbols on the page, will force you brain into realizing something helpful! We'll see this strategy in action here, too. • Let's see if R is reflexive. What would that actually mean? Let's make ourselves say this out loud. Would we expect that: "Any integer is divisible by itself." Of course! Now, let's try to write that down in the symbolic terms required in a proof.
<div class="def-proof" markdown>
*Proof.* We claim R is reflexive. Let x ∈Z be arbitrary and fixed. Then
</div>
x | x since x = 1 · x and 1 ∈Z. Thus, (x, x) ∈R. Therefore, R is reflexive. Voil`a! Just thinking out loud helped us realize a fact, and that made it easier for us to write down that statement in mathematical language. • Let's see if R is symmetric. This property is defined in terms of an implication, a conditional statement. So, let's assume we have an arbitrary related pair, (x, y) ∈R. Would we necessarily believe (y, x) ∈R, too? Said another way: Assuming x divides y, can we also say that y divides x? This actually seems rather unlikely! Knowing x | y tells us that y = kx for some k ∈Z, but why would that lead us to believe that x = 1 ky means y | x? What if 1 k /∈Z? You might be tempted at this point to say something like "Well, 1 k is only an integer when k = 1 or k = −1 so that's that." That isn't quite a full explanation! Remember that to disprove a "For all . . . " claim, we need to provide an explicit counterexample whenever possible. We don't need to characterize all of the cases where the property does and does not hold and try to explain things in generality. We just need an example to convince someone that the property does not hold. This is much more illustrative and direct than flailing our arms about and pointing out how some counterexample exists out there somewhere. Let's just show our reader one and move on!
<div class="def-proof" markdown>
*Proof.* Consider 2, 6 ∈Z. Since 6 = 3 · 2, we have (2, 6) ∈R.
</div>
However, writing 2 = ℓ· 6 requires ℓ= 1 3, and 1 3 /∈Z. Thus, (6, 2) /∈R. This shows that R is not symmetric.


> 🇨🇳 TODO: 待翻译


• Let's see if R is transitive. In general, transitivity is typically the most difficult property to think about. This is partly due to the fact that it's defined by a conditional statement with two hypotheses, and it uses three variables. In this specific example, we will assume x | y and y | z, and then wonder whether x | z necessarily. Try saying that out loud with words and seeing if you believe it or not. It seems like it's true, right? Now, try writing down the hypotheses and the conclusion in mathematical language. Can you see how to piece those together? Try writing out your version of this proof before reading on.
<div class="def-proof" markdown>
*Proof.* Let x, y, z ∈Z be arbitrary and fixed. Suppose (x, y) ∈R and
</div>
(y, z) ∈R. This means x | y and y | z, so ∃k, ℓ∈Z such that y = kx and z = ℓy. Let such k, ℓbe given. Substituting the first equation into the second, we find that z = ℓy = ℓ(kx) = (kℓ)x Since kℓ∈Z, as well, we have shown that x | z. Thus, (x, z) ∈R, necessarily. Therefore, R is transitive. • Let's see if R is anti-symmetric. This property is also defined by a conditional statement with two hypotheses, so we will assume we have an x and a y and that x | y and y | x. Can we conclude that x = y? This question hearkens back to proving that R was not symmetric. Remember, we proved that x | y does not necessarily imply y | x and, actually, if you thought about it for a moment, it's actually very unlikely that x | y and y | x can both be true. How can this be? Think about it carefully and try to come up with your own proof before you read ours.
<div class="def-proof" markdown>
*Proof.* Let x, y ∈Z be arbitrary and fixed. Suppose (x, y) ∈R and (y, x) ∈R. This means x | y and y | x, so ∃k, ℓ∈Z such that y = kx and x = ℓy. Let such k, ℓbe given. Substituting the first equation into the second, we find that y = kx = k(ℓy) = (kℓ)y. We now have two cases. Case 1: Suppose y = 0. Then we cannot divide both sides by y. Instead, we observe that x = ℓy = ℓ· 0 = 0, and therefore x = 0, as well. Thus, x = y in this case. Case 2: Suppose y ̸= 0. Then we can divide both sides by y. This yields kℓ= 1. Since k, ℓ∈Z this means either k = ℓ= 1 or k = ℓ= −1.
</div>


> 🇨🇳 TODO: 待翻译


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


If k = ℓ= 1, then x = ℓy = y. In the other case . . . ̸ Oh, shucks! This doesn't work! Do you see what happened? In "most" of the cases, we did conclude that x = y, but there is actually a possibility that y = −x. For instance, when y = 3 and x = −3, notice that x | y and y | x but x ̸= y. THIS is the counterexample we need, and trying to finish our "proof" helped us find it. Perhaps you saw this case coming all along; if so, way to go! Let's wrap this up by presenting that counterexample:
<div class="def-proof" markdown>
*Proof.* Consider x = 3 and y = −3, so x, y ∈Z. Notice that x | y and
</div>
y | x because 3 = (−1)(−3) and −3 = (−1) · 3, and since −1 ∈Z. However, certainly x ̸= y. This shows that R is not anti-symmetric. As a follow-up question, consider what happens when we define this relation on the set N instead of Z. What changes? Which properties hold now? Are any answers different than with Z? Do think about this. The answers to those questions will motivate our next subsection. Constructing a Relation with Specific Properties One more example before we move on. An interesting "game" to play is to take a set and construct a relation R that satisfies some specific subset of the four properties. (Note: there are 16 different ways that the 4 properties can/cannot hold.) We will ask you questions like this in the exercises, so let's work through one example here.
Example 6.2.17. Goal: Let S be the set of students in this class. Define a
relation R that is (1) not reflexive, (2) not symmetric, (3) transitive, and (4) anti-symmetric. To ensure that R is not reflexive, we must make sure that no element is related to itself. To ensure R is not symmetric, we must make sure that whenever a pair (x, y) ∈R, then (y, x) /∈R. To ensure R is transitive, we must make sure whenever (x, y) ∈R and (y, z) ∈R, then (x, z) ∈R. And to ensure R is anti-symmetric, we will think of the contrapositive form of the property's definition, which requires that any pair of elements is related in at most one way. This last property is perhaps the hardest to think about; it says that for every x, y ∈S, either x is related to y but not the other way, or else y is related to x and not the other way, or else x and y just aren't related either way. That is, we must not allow any pairs to satisfy both (x, y) ∈R and (y, x) ∈R. (Again, reread the definition of anti-symmetric and write down the contrapositive of the conditional statement and think about why this works.) Now let's try to construct R so that it satisfies these properties. Property (1) means that our definition can't allow anything of the form "or is equal to", and (2) means that the definition must relate any x and y in "only one way". Thus, we might guess that a comparison property, something like the "less than" relation on Z, might work. Let's try it out and attempt to prove/disprove the desired properties.


> 🇨🇳 TODO: 待翻译


Let us define R on S by x R y ⇐⇒x is strictly younger than y (in years) Now, let's explore its properties and make sure they are what we wanted them to be. Try to prove/disprove them on your own before reading our solutions! Also, play around with a different relation on S (make one up!) and see how its properties are different. Can you come up with another relation that has the exact same properties as this one? • R is not reflexive. This is because any person x ∈S has the exact same age as him/herself, and so x ̸R x. • R is not symmetric. This is because if x is strictly younger than y, then y is strictly older than x, so y ̸R x • R is transitive. This is because if x is (strictly) younger than y and y is (strictly) younger than z, then certainly x is (strictly) younger than z. • R is anti-symmetric. This is because for any two people x, y ∈S, one of them must be younger than the other, or else they are the same age; they cannot both be strictly younger than each other. (Essentially, we are ensuring anti-symmetry holds by making sure the hypothesis of the conditional statement in that property's definition never holds, so the conditional itself is always True.) Thus, this relation R satisfies all of the desired properties. You'll notice that we were not completely rigorous in these arguments, but there's a good reason for it. Specifically, we didn't produce explicit counterexamples for the properties that fail. It would be best if we could identify two students in your class and show how one is younger than the other but not the other way around. But we don't know who's in your class! That's why we left our arguments as "explaining the existence of something without pointing to it explicitly". We will point out that, in general, a relation of this form---one defined as (x, y) ∈R ⇐⇒x is "less" than y (however "less" makes sense in that context)--- will be non-reflexive, non-symmetric, transitive, and anti-symmetric. In fact, we can even replace "less" with "greater" and this still holds. To see why this is true, think about the "<" relation on N, or Z, or R. Think about the ">" relation on those sets. Think about the "is younger than" relation on the set of people, or the "is taller than" relation, or the "has more children than" relation. What about the "≤" relation on Z? How is this different than the "<" relation? What properties change? (These types of questions will be explored a little bit further in the next subsection, where we examine a particular type of relation that behaves like these "≤" and "≥" relations. They are called order relations, naturally.)


> 🇨🇳 TODO: 待翻译


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 TODO: 待翻译


### 6.2.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) How is (binary) relation defined, in terms of sets? (2) Say we have a relation R defined between A and B. What must true about A and B for us to be able to talk about whether R is reflexive, say? (3) When is a relation reflexive? Give an example of a set and a reflexive relation on that set. (4) When is a relation symmetric? Give an example of a set and a symmetric relation on that set. (5) When is a relation transitive? Give an example of a set and a transitive relation on that set. (6) When is a relation anti-symmetric? Give an example of a set and an anti-symmetric relation on that set. (7) What is the difference between not symmetric and anti-symmetric? Give an example of a set and a relation on that set which is both symmetric and anti-symmetric. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Consider the set A = {1, 2, 3}. For each of the following relations, defined on A or P(A) as specified, decide whether it is (i) reflexive, (ii) symmetric, (iii) transitive, (iv) anti-symmetric. Not much justification is required, just a Yes or No and a sentence or two. (a) Ra on A defined by Ra = { (1, 1), (1, 2), (2, 1), (2, 2), (3, 3) } (b) Rb on A defined by Rb = { (1, 1), (1, 2), (2, 2), (2, 3), (3, 3) } (c) Rc on P(A) defined by ∀S, T ∈P(A). (S, T) ∈Rc ⇐⇒ S ∩T = ∅ (d) Rd on P(A) defined by ∀S, T ∈P(A). (S, T) ∈Rd ⇐⇒ S ∩T ̸= ∅


> 🇨🇳 TODO: 待翻译


(e) Re on P(A) defined by ∀S, T ∈P(A). (S, T) ∈Re ⇐⇒S ⊆T (2) Define the relation ⋆on Z by saying ∀x, y ∈Z. x ⋆y ⇐⇒3 | x −y (a) Prove that ⋆is reflexive. (b) Prove that ⋆is symmetric. (c) Prove that ⋆is transitive. (Remember that "|" means "divides". Be sure to use the formal definition; see Definition 6.2.15.) (3) Define the relation ∼on Z by saying ∀x, y ∈Z. x ∼y ⇐⇒3 | x + 2y (a) Prove that ∼is reflexive. (b) Prove that ∼is symmetric. (c) Prove that ∼is transitive. (4) Define the relation T on R by saying, for any x, y ∈R, (x, y) ∈T ⇐⇒  y x ∈R ∧y x ≥0  (a) Find x ∈R such that (x, x) /∈T. Does this mean T is not reflexive? Why or why not? (b) Find x, y ∈R such that (x, y) ∈T and (y, x) ∈T. Does this mean T is symmetric? Why or why not? (c) Find x, y ∈R such that (x, y) ∈T but (y, x) /∈T. Does this mean T is not symmetric? Why or why not? (d) Determine whether or not T is transitive, and prove your claim. (5) Define the relation ↔on P(N) by saying, for any X, Y ⊆N, X ↔Y ⇐⇒  X ⊆Y ∨ X ∩Y = ∅  Prove/disprove each of the four standard properties for this relation (i.e. reflexive, symmetric, transitive, anti-symmetric). (6) What is wrong with the following "proof" that the symmetric and transitive properties imply the reflexive property? Let A be a non-empty set. Let R be a relation on A. Suppose R is symmetric and transitive. We will show R is reflexive.


> 🇨🇳 TODO: 待翻译


Let x ∈A be arbitrary and fixed. Define the set T to be {y ∈A | (x, y) ∈R} Let y ∈T be given. Thus, (x, y) ∈R. Since R is symmetric, we can deduce (y, x) ∈R. Since R is transitive, and (x, y) ∈R and (y, x) ∈R, we deduce that (x, x) ∈R. Since x was arbitrary, we have shown that the reflexive property holds.
## 6.3 [Optional Reading] Order Relations Let us discuss some relations that behave like "≤" and have similar inherent properties. This is motivated by the fact that these relations are easily definable on the standard sets of numbers we have---N, Z, Q, R---and they also apply to some other, potentially surprising, situations. We will give a definition first and then consider some examples. We will then use those examples to motivate some interesting properties of order relations and then state and prove those facts.
<div class="def-definition" markdown>
**Definition 6.3.1. Let R be a relation defined on the set A.**
</div>
• If R is reflexive, transitive, and anti-symmetric, then we say R is a partial order on A. • If R is reflexive, transitive, and anti-symmetric and, in addition, it satisfies ∀x, y ∈A. (x, y) ∈R ∨(y, x) ∈R then we say R is a total order on A. (That is, a total order is a partial order such that every two elements of the set are comparable one way or the other.) This definition tells us what partial and total orders are. The next definition just gives us some useful shorthand for referring to partial and total orders on sets.
<div class="def-definition" markdown>
**Definition 6.3.2. When R is a partial order on A, we say that the pair (A, R)**
</div>
is a partially ordered set, or sometimes just a poset, for short. When R is a total order on A, we say that the pair (A, R) is a totally ordered set, or sometimes just a toset, for short. We will attempt to explain the reasons for these terms by giving several related examples.


> 🇨🇳 TODO: 待翻译


