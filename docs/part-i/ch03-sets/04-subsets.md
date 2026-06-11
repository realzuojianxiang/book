---
title: Subsets
---

# Subsets

Notice the similarities between these symbols and the inequality symbols we use to compare real numbers. We write inequalities like x ≤2 or 5 > z > 0 and understand what those mean based on the "direction" of the symbol and whether we put a bar underneath it. The symbols ⊆, ⊂, ⊇, ⊃work exactly the same way, except they refer to "containment of elements" as opposed to "magnitude of a number". Standard Sets of Numbers The standard sets of numbers we mentioned in the last section are related via the subset relation quite nicely. Specifically, we can say N ⊂Z ⊂Q ⊂R ⊂C Again, we take for granted our collective knowledge of these sets of numbers to allow us to make these claims. However, there are some profound and intricate mathematical concepts involved in describing exactly why, say, the set R exists and is a proper superset of Q. For now, though, we use these sets to illustrate the subset relationship. Since we know the subset relationships above are proper, we used that corresponding symbol, "⊂". In general, it is common in mathematical writing to simply use the "⊆" symbol, even if it is known that "⊂" would apply. We might only resort to using the "⊂" symbol when it is important, in context, to indicate that the two sets are not equal. If that information is not essential to the context at hand, then we might just use the "⊆" symbol. Set-Builder Notation Creates Subsets One way that we have already "used" the idea of a subset was in our use of set-builder notation. This is used to define a set to be all of the elements of a "larger" set that satisfy a certain property. We define a property P(x), draw a variable object x from a larger set X, and include any elements x that satisfy the property P(x). Notice that any element of this new set must be an element of X, simply based on the way we defined it. Thus, the following relationship holds {x ∈X | P(x)} ⊆X regardless of the set X and the property P(x). Depending on the set X and the property P(x), it may be that the proper subset symbol ⊂applies but, in general, we can say for sure that ⊆applies. Try to come up with some examples of sets X and properties P(x) so that ⊆applies, then try to come up with some examples where ⊂applies. Try to come up with one set X and two different properties P1(x) and P2(x) so that ⊂applies for P1(x) and ⊆applies for P2(x). Try to identify two different sets X1 and X2 and two different properties P1(x) and P2(x) so that {x ∈X1 | P1(x)} = {x ∈X2 | P2(x)} Can you do it?


> 🇨🇳 TODO: 待翻译


Examples
A set is a subset of another set if and only if every element of the first one is an element of the second one. For instance, this means that the following claims all hold: {142, 857} ⊆N n√ 3, −π, 8.2 o ⊆R  x ∈R | x2 = 1


> 🇨🇳 TODO: 待翻译


⊆Z Do you see why these are True? For a subset relationship to fail, then, we must be able to find an element of the first set that is not an element of the second set. For instance, this means that the following claims all hold: {142, −857} ̸⊆N n√ 3, −π, 8.2 o ̸⊆Q  x ∈R | x2 = 5


> 🇨🇳 TODO: 待翻译


̸⊆Z Finding All Subsets of a Set Let's work with a specific set for a little while. Define A = {1, 2, 3}. Can we identify all of the subsets of A? Sure, why not? {1} ⊆A {2} ⊆A {3} ⊆A {1, 2} ⊆A {1, 3} ⊆A {2, 3} ⊆A A = {1, 2, 3} ⊆A ∅⊆A Identifying the first six subsets was fairly straightforward, but it's important to remember that A and ∅are subsets, as well. (Notice: it is true, in general, that for any set S, S ⊆S and ∅⊆S. Think about this!) Consider the set B whose elements are all of the sets we listed above: B =  {1} , {2} , {3} , {1, 2} , {1, 3} , {2, 3} , A, ∅


> 🇨🇳 TODO: 待翻译


It is true that any element X ∈B satisfies X ⊆A. Do you see why?


> 🇨🇳 TODO: 待翻译


### 3.4.2 The Power Set This process of identifying all subsets of a given set is common and useful, so we identify the resulting set with a special name.
<div class="def-definition" markdown>
**Definition 3.4.2. Given a set A, the power set of A is defined to be the set**
</div>
whose elements are all of the subsets of A. It is denoted by P(A). Our parenthetical observation from the above paragraph tells us that S ∈ P(S) and ∅∈P(S), for any set S. Look back at our example set A = {1, 2, 3} above. What do you notice about the number of elements in P(A)? How does it relate to the number of elements in A? Do you think there is a general relationship between the number of elements in S and P(S), for an arbitrary set S?
Example 3.4.3. Let's find P(∅). What are the subsets of the empty set? There
is only one, the empty set itself! (That is, ∅⊆∅, but no other set satisfies this.) Accordingly, the power set P(∅) has one element, the empty set: P(∅) = { ∅} Notice that this is different from the empty set itself: ∅̸= { ∅} Why is this true? Compare the elements! The empty set has no elements, but the set on the right has exactly one element. (In general, this can be a helpful way to compare two sets.) To give you some practice, we'll point out that would read the above line aloud as: "The empty set and the set containing the empty set are two different sets."
Example 3.4.4. Let's try this process with another set, say A = { ∅, {1, ∅} }.
We can list the elements of P(A) as P(A) = { {∅} , {{1, ∅}} , {∅, {1, ∅}} , ∅, } This may look strange, with all of the empty sets and curly braces, but it is important to keep the subset relationships straight. It is true, in this example, that ∅∈A, {∅} ⊆A, {∅} ∈P(A), {∅} ⊆P(A) Why are these relationships true? Think carefully about them, and try to write a few more on your own. The distinction between "∈" and "⊆" is very important!


> 🇨🇳 TODO: 待翻译


### 3.4.3 Set Equality When are two sets equal? The main idea is that two sets are equal if they contain "the same elements", but this is not a precise definition of equality. How can we describe that property more explicitly and rigorously? To say that two sets, A and B, have "the same elements" means that any element of A is also an element of B, and every element of B is also an element of A. If both of these properties hold, then we can be guaranteed that the two sets contain precisely the same elements and are, thus, equal. If you think about it, you'll notice that we can phrase this in terms of subsets. How convenient!
<div class="def-definition" markdown>
**Definition 3.4.5. We say two sets, A and B, are equal, and write A = B, if**
</div>
and only if A ⊆B and B ⊆A. (What happens if we use the ⊂symbol in the definition, instead of ⊆? Is this the same notion of set equality? Why or why not?) This definition will be very useful in the future when we learn how to prove two sets are equal and we can't simply list the elements of each and compare them. By constructing two arguments and proving the subset relationship in "both directions", we can show that two sets are equal. For now, let's see this definition applied to a straightforward example.
Example 3.4.6. How can we use this to definition to observe that the following
equality holds? {x ∈Z | x ≥1} = N We just need to see that the ⊆and ⊇relationship applies between the two sides. First, is it true that every integer that is at least 1 is a natural number? Yes! This explains why {x ∈Z | x ≥1} ⊆N Second, is it true that every natural number is a positive integer that is at least 1? Yes! This explains why {x ∈Z | x ≥1} ⊇N Together, this shows that the equality stated above is correct.
### 3.4.4 The "Bag" Analogy It has been our experience that sets are a rather difficult notion to grasp when they are introduced. Specifically, the notation associated with sets throws students for a loop, and they end up writing down things that make no sense! It is essential to keep straight the differences between the symbols ∈and ⊆. Here is a helpful analogy to keep in mind: a set is like a bag with some stuff in it. The bag itself is irrelevant; we just care about what kind of stuffinside (i.e. what the elements are). Think of the bag as a non-descript plastic bag you'd get at the grocery store, even. All those bags are identical; to distinguish between any two bags, we need to know what kind of things are inside them.


> 🇨🇳 TODO: 待翻译


If I put an apple and an orange in a grocery bag, surely it doesn't matter in what order I put them in. All you would need to know is that I have some apples and oranges. It also doesn't matter how many apples or oranges I have in the bag, because we only care about what kind of stuffis in there. Think of it as answering questions of the form "Are there any s in the bag? Yes or no?" It doesn't matter if I have two identical apples or seven or just one in my bag; if you ask me whether I have any apples, I'll just say "Yes". This is related to the notion that the order and repetition of elements in a set don't matter. A set is completely characterized by what its elements are. This also helps when we think about sets as elements of other sets, themselves. Who's to stop me from just putting a whole bag inside another bag¿ Look at the set A we defined in the example above: A = { ∅, {1, ∅} } This set A is a bag. What's inside the bag? There are two objects inside the bag (i.e. there are two elements of A). They both happen to be bags, themselves! One of them is a plain-old empty bag, with nothing inside it. (That's the empty set.) Okay, that's cool. The other one has two objects inside it. One of those objects is the number 1. Cool. The other such object is another empty bag. Distinguishing "∈" and "⊆" This analogy also helps with understanding the differences between "∈" and "⊆". Keep the example A in mind again. When we write x ∈A, we mean x is an object inside the bag A. If we peeked into A, we would see an x sitting there at the bottom amongst the stuff. Let's use this idea to compare two examples. • We see that ∅∈A is true here. If we look inside the bag A, we see an empty bag amongst the stuff(the elements). • We also see that {∅} /∈A is true here. If we look inside the bag A, we don't see a bag containing only an empty bag. (This is what {∅} is, mind you: an empty bag inside another bag.) Do you see such an object? Where? I defy you to show me, amongst the stuffinside the bag A, a bag containing only an empty bag. What do I see inside the bag A? Well, I see two things: an empty bag, and a bag that has two objects inside it (an empty bag, and the number 1). Neither of those objects is what we were looking for! When we write X ⊆A, we mean that the two bags, X and A, are somehow comparable. Specifically, we are saying that all of the stuffinside X is also stuff inside A. We are really rooting through all of the objects inside X, taking them out one by one, and making sure we also see that object inside A. Let's use this idea to compare two examples. • We see that {∅} ⊆A is true here. We are comparing the bag on the left with the bag on the right. What stuffis inside the bag on the left?


> 🇨🇳 TODO: 待翻译


There's just one object in there, and it is an empty bag, itself. Now, we peek inside A. Do we also see an empty bag in there? Yes we do! Thus, the "⊆" symbol applies here. • We also see that {1} ̸⊆A is true here. To compare these two bags, we'll pull out an object from the bag on the left and see if it is also in the bag A. Here, we only have one object to pull out: the number 1. Now, let's peek inside the bag A. Do we see a 1 sitting in there amongst the stuff? No, we don't! We would have to peek inside something at the bottom of the bag A to find the number 1; that number isn't just sitting out in plain sight. Thus, {1} ̸⊆A. Look back over some examples we have discussed already with this new analogy in mind. Does it help you understand the definitions and examples? Does it help you understand the difference between "∈" and "⊆" and "⊇"? If not, can you think of another analogy that would help you?
### 3.4.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) Is N ⊆R? Is R ⊆N? Is Q ⊆Z? Why or why not? (2) What is the difference between ⊂and ⊆? Give an example of sets A, B such that A ⊆B is True but A ⊂B is False. (3) What is the difference between ∈and ⊆? Give an example of sets C, D such that C ⊆D but C /∈D. (4) Let S be any set. What is the power set of S? What type of mathematical object is it? How is it defined? (5) Suppose S ⊆T. Does this mean S = T? Why or why not? (6) Explain why ∅⊆S and ∅∈P(S) for any set S. (7) Suppose X ∈P(A). How are X and A related, then? (8) Is it possible for A = P(A) to be true? (This one is rather tricky, but think about it!)


> 🇨🇳 TODO: 待翻译


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Write out the elements of the set P(P(∅)). (2) Write out the elements of the sets P([1]) and P([2]) and P([3]). Can you make a conjecture about how many elements P([n]) has? (Can you prove it? We don't expect you to now, but soon enough; think about it!) (3) Let A = {x, ♥, {4} , ∅}. For each of the following statements, decide whether it is True or False and briefly explain why. (a) x ∈A (b) x ⊆A (c) {x, ♥} ⊆A (d) {x, ∅} ⊂A (e) {x, ♥, z, 7} ⊇A (f) {x} ∈P(A) (g) {x} ⊆P(A) (h) {♥, x} ∈P(A) (i) {4} ∈P(A) (j) {∅} ∈P(A) (k) {∅} ⊆P(A) Hint: 7 of these are True, and 4 are False. (4) Give an example of sets A, B such that A ∈B and A ⊆B are both true. (5) Is {1, 2, 12} ⊆R? (6) Is {−5, 8, 12} ⊆N? (7) Is {1, 3, 7} ∈P(N)? (8) Is N ∈P(Z)? (9) Is P(N) ⊆P(Z)? Are they equal sets? Why or why not? (10) Give an example of an infinite set T such that T ∈P(Z) but T /∈P(N). (11) Suppose G, H are sets and they satisfy P(G) = P(H). Can we conclude that G = H? Why or why not? (Don't try to formally prove this; just think about it and try to talk it out.) (12) Give an example of a set W such that W ⊆P(N) but W /∈P(N).


> 🇨🇳 TODO: 待翻译


## 3.5 Set Operations When you first learned about numbers, a natural next step was to learn about how to combine them: multiplication, addition, and so on. Thus, a natural next step for us now is to investigate how we can take two sets and operate on them to produce other sets. How can we combine sets in interesting ways? There are several such operations that have standard, notational symbols and we will introduce you to those operations now. Throughout this section, we assume that we are given two sets A and B that are each subsets of a larger universal set U. That is, we assume A ⊆U and B ⊆ U. The reason we make this assumption is that each operation involves defining another set by identifying elements of a larger set with a specific property, so we must have some set U that is guaranteed to contain all of the elements of A and B so we can even work with those elements. (Again, ensuring this may seem nit-picky, but it is meant to avoid nasty paradoxes like the one we investigated before.) Assuming those sets A, B, U exist, though, we can forge ahead with our definitions.
### 3.5.1 Intersection This operation collects the elements common to two sets and includes them in a new set, called the intersection.
<div class="def-definition" markdown>
**Definition 3.5.1. Let A and B be any sets. The intersection of A and B**
</div>
is the set of elements that belong to both A and B, and is denoted by A ∩B. Symbolically, we define A ∩B = {x ∈U | x ∈A and x ∈B}
Example 3.5.2. Define the following sets:
S1 = {1, 2, 3, 4, 5} S2 = {1, 3, 7} S3 = {2, 4, 7} U = N Then, we see that, for example, S1 ∩S2 = {1, 3} S1 ∩S3 = {2, 4} S2 ∩S3 = {7} Also, since S1 ∩S2 is, itself, a set, it makes sense to consider (S1 ∩S2) ∩S3. However, those two sets share no elements, so we write (S1 ∩S2) ∩S3 = ∅


> 🇨🇳 TODO: 待翻译


