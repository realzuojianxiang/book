---
title: Definition and Examples
---

# Definition and Examples

Not only does the order of elements not matter within a set, the repetition of elements does not matter! That is, the set A = {a, a, a} and the set A = {a} are exactly the same. Again, remember that a set is completely characterized by its elements; we only care about what is "in" a set. (We will mention this again in Section 3.4.4, when we talk about the "bag analogy" for sets.) Writing A = {a, a, a} is just a triply-redundant way of saying a ∈A and that only a is an element of A. Thus, A = {a} is the most concise way of stating the same information. The Common Property Might Be Being an Element of That Set Now, still following the idea that we can define a set by writing all of the elements, consider the following definition of a set A: A = {2, 7, 12, 888} Surely, this is a set because we just defined it by listing its elements. What is the common, well-defined property that associates its elements, though? With the set V of vowels, we could list the elements and provide a linguistic definition, but for this set A, it seems as though we are relegated to listing the elements without knowing a way of describing their common property. Mathematically speaking, though, a common property uniting 2, 7, 12, 888 is that they are all elements of this set A! In the mathematical universe, we have a license for freedom of abstract thought, and merely by discussing this set A and its elements, we have given them that common property. Does this seem satisfactory to you? Can you come up with another common, well-defined property that would yield exactly the elements of A? (Hint: identify a polynomial p(x) whose roots are exactly 2, 7, 12, and 888.) If the elements of a set have more than one property that associates them together, do you think it matters which property we have in mind when referring to the set? And what do you think about the set S := {2, 7, M, Boston Red Sox}? Could there possibly be a common property other than the fact that we have listed them here? Ellipses Are Sometimes Okay, But Informal Sometimes, when there is no confusion about the set in question, or it has been defined in another way and we wish to list a few elements as illustrative examples, then it is convenient to use ellipses to condense the listing of elements of a set. For instance, we might write E = {even natural numbers} = {2, 4, 6, 8, 10, . . . } This set is infinitely large, in fact, so we could not even list all of its elements if we tried, but it is clear enough from the first few elements listed that we are referring to even numbers, especially because we have already referred to E as "the set of even natural numbers". However, we cannot stress enough that this is not a precise definition of the set in question. It suffices in an informal context, but it is not mathematically rigorous, and this will become clear as we discuss the following proper way of defining sets.


> 🇨🇳 TODO: 待翻译


Set-Builder Notation The best way to define or describing a set is to identify its elements as particular objects of another set that have a specific property. For instance, if we wished to refer to the set S of all natural numbers between 1 and 100 (inclusive), we could list all of those elements, but this requires a lot of unnecessary writing. We could also use the ellipsis notation S = {1, 2, 3, . . . , 100} but, again, this is not precise without already having a formal definition of S. (Someone might misinterpret the ellipses in a different way.) It is much more precise and concise to write S = {x ∈N | 1 ≤x ≤100} We read this as "S is the set of all objects x in the set N of natural numbers such that 1 ≤x ≤100". The bar symbol | is read as "such that" and indicates that the information to the left tells us what "larger set" the objects come from, while the information to the right tells us the specific property that those objects should have. (Caution: do not use | in other contexts to mean "such that". This is only acceptable in the context of defining sets. It is just used as a place-holder to separate the left side---the set we use to draw elements---from the right side---a description of the property those elements should have.) This is an example of the very popular and useful set-builder notation. We call it this because we are building a set by drawing elements from a "larger" set of possibilities, and only including those that have a particular property. To do this, we need to tell the reader (1) what the larger set is, and (2) what the common property is. Let's illustrate this idea with a few examples: S = {x ∈N | 1 ≤x ≤100} = {1, 2, 3, . . . , 100} T = {z ∈Z | we can find some k ∈Z such that z = 2k} = {. . . , −4, −2, 0, 2, 4, . . .} U =  x ∈R | x2 −2 = 0


> 🇨🇳 TODO: 待翻译


o V =  x ∈N | x2 −2 = 0


> 🇨🇳 TODO: 待翻译


= { } The last two examples show how the context is extremely important. The same common property (satisfying x2 −2 = 0) can be satisfied by a different set of elements when we change the larger set from which we draw elements. Two real numbers satisfy that property, but no natural numbers satisfy it! Do any rational numbers satisfy that property? What do you think? This is why it is absolutely essential to specify the larger set. A definition like "U =  x | x2 −2 = 0


> 🇨🇳 TODO: 待翻译


is meaningless because it is ambiguous and could yield completely different interpretations. Reading Notation Aloud We are really learning a new language here, and these are some of the basic words and rules of grammar. We'll need some practice translating these sen-


> 🇨🇳 TODO: 待翻译


tences into English (in our heads and out loud) and vice-versa. For example, we can say the definition for S above as any of the following, reasonably: S is the set of all natural numbers x such that x is between 1 and 100, inclusive. S is the set of all natural numbers between 1 and 100, inclusive. S is the set of all natural numbers x that satisfy the inequality 1 ≤x ≤100. S is the set of natural numbers x with the property that 1 ≤x ≤100. Notice that all of them identified the larger set and the common property; the only differences between them are linguistic/grammatical, and they do not alter the mathematical meanings. Try to write similar sentences for the other definitions. Try getting a verbal definition of a set from a friend and writing down what they said in mathematical symbols. Consider a definition of the rational numbers Q that we saw before, and notice that we can rewrite it as: Q = na b , where a, b ∈Z and b ̸= 0 o = n x ∈R | we can find a, b ∈Z such that a b = x and b ̸= 0 o Notice the subtle difference between the two definitions. The upper one tells us that all rational numbers are of the form a b , and then tells us the particular assumptions of a and b that must be satisfied. The lower one tells us that all rational numbers are real numbers with a particular property, namely that we can express that real number as a ratio of integers. We strongly prefer the lower definition, because it tells us more information. In general, if P(x) represents a sentence (involving English and/or mathematical language) that describes a specific, well-defined property, and X is a given set, then the notation S = {x ∈X | P(x)} is read as "S is the set of all elements x of the set X such that the property P(x) is true". In the notation P(x), the letter x represents a variable object, and depending on the particular object we use as x, the property P(x) may hold (i.e. P(x) is true) or may fail (i.e. P(x) is false). If the property holds, then we include x in S (so x ∈S), and if it fails, we do not include x in S (so x /∈S). Returning to our example of the set E of even natural numbers, it is more precise to write E = {even natural numbers} = {x ∈N | there is a natural number n such that x = 2n}


> 🇨🇳 TODO: 待翻译


Notice that there are two "layers" of properties here. A natural number is included in our set E if we can find another natural number n with the additional property that x = 2n. Try to write down a similar definition for the set of odd numbers, or the set of perfect squares. What about the set of primes? The set of palindromic numbers? The set of perfect numbers? Can you write definitions for these sets using set-builder notation?
### 3.3.4 The Empty Set What if no elements satisfy a property P(x)? What happens then? For instance, consider the definition S =  x ∈N | x2 −2 = 0


> 🇨🇳 TODO: 待翻译


We know that the number x we are "looking for" with that property is √ 2 (and − √ 2, too) but √ 2 /∈N. Thus, no matter what element of N we let x represent, the property P(x)---given by "x2 −2 = 0"---actually fails. Thus, there are no elements of this set. Is this really a set? Remember, a set is completely characterized by its elements, and a set having no elements, such as this one, is characterized by that fact. If we attempted to list its elements, we would end up writing {}. This set is so special, in fact, that we give it a name and symbol:
<div class="def-definition" markdown>
**Definition 3.3.2. The empty set is the set which has no elements.**
</div>
It is denoted by the symbol ∅. There are many ways to define the empty set using set-builder notation. (And yes, we do mean the empty set; there is only one set with no elements!) We saw one example above, and we're sure you can come up with many others. Consider for example, the following sets: {a ∈N | a < 0} {r ∈R | r2 < 0} {q ∈Q | q2 /∈Q} Do you see why these all define the same set, the one with no elements? Context Matters We should also note again the significance of specifying the larger set X from which we draw our variable element x in a set-builder definition like the one above. For instance, consider the following two sets: S1 = {x ∈N | |x| = 5} = {5} S2 = {x ∈R | |x| = 5} = {−5, 5} (Note: It is also quite common to index sets with the subscript notation you see above, allowing us to use the same letter many times.)


> 🇨🇳 TODO: 待翻译


This specification is clearly important, in this case, because it yields two entirely different sets! For this reason, we must be precise and clear when defining a set in this way. A definition like S = {x | |x| = 5} should be regarded as ambiguous and undesirable, since it leads to issues like the one above.
### 3.3.5 Russell's Paradox Perhaps it seems like we are picking nits here, but the reasoning behind our vehemence is rooted in some fundamental ideas of set theory. We wish to avoid some complex issues and paradoxes that might arise without this policy in place. There is a particularly famous example of a paradox involving sets that illustraes why we have the requirement described in the above paragraph, namely that we must specify a larger set when we use set-builder notation. This example is known as Russell's Paradox (after the British mathematician Bertrand Russell), and we we will present and discuss it in this section. Sets Whose Elements Are Sets First, we should point out that this discussion will introduce the notion that sets can also be elements of other sets. This may seem like a strange and far-fetchedly abstract idea right now, but it is a fundamental concept in mathematics. For a concrete example, think back to our set B of all Major League Baseball Teams. We could also regard each team as a set, where its elements are the players on the team. Thus, it would make sense to say Derek Jeter ∈New York Yankees ∈B since Derek Jeter is an element of the set New York Yankees, which is itself an element of the set B. (Notice, however, that Derek Jeter /∈B. The relationship signified by "∈" is not transitive. We will hold offon defining this term until much later. For now, we will point out that the relationship signified by "≤" on the set of real numbers is transitive. If we know x ≤y ≤z, then we can deduce x ≤z. This is not the case with the "∈" relationship, though.) Another example is S = {1, 2, 3, {10}, ∅}. Yes, the empty set itself can be an element of another set, as can the set {10}. Why couldn't they? As a thought exercise, we suggest thinking about the difference between ∅, {∅}, {{∅}}, and so on. Why are they different sets? One final example involves the natural numbers N. Let's use O and E to represent the odd and even natural numbers, respectively. What, then, is the set S = {O, E}, and how does it differ, if at all, from N? This is a subtle question, so think about it carefully. The Paradoxical "Set" Spend some time on the side thinking about this notion of sets whose elements are sets. For now, though, let us forge ahead with our explanation of Russell's Paradox. Consider the following definition of a "set". We say "set" because it


> 🇨🇳 TODO: 待翻译


is actually not a properly-defined set, but it remains to be seen exactly why this is the case. When it becomes clear this is not a set, this will be an argument for requiring the specification of a larger set to draw from when we use set-builder notation; this is because the definition below does not specify a larger set. Here is that definition: R = {x | x /∈x} That's it! Is this a set? What are the elements of R? Think about what the definition above says: the elements of R are sets that also happen to not have themselves as elements. Can you identify any elements of R? Can you identify any objects that are not elements of R? The first question is far easier to answer: any of the sets we have discussed so far would be elements of R. For instance, the empty set ∅contains no elements, so it certainly doesn't have itself as an element. Thus, ∅∈R. Also, notice thatN /∈N (because the set of natural numbers is not a natural number, itself) and thus N ∈R. Identifying objects that are not elements of R is a very tricky matter, and we will help you by asking the following question: Is R an element of itself? Is it true or false that R ∈R? Think about this carefully before reading on. We will walk you through the appropriate considerations. • Suppose R ∈R is True. The defining property of R tells us that any of its elements is a set that does not have itself as an element. Thus, we can deduce that R /∈R. Wait a minute! Knowing that R ∈R led us to deduce that, in fact, R /∈R. Surely, these contradictory facts cannot both hold simultaneously. Accordingly, it must be that our original assumption was bad, so it must be the case that R /∈R, instead. • Now, suppose R /∈R is True. The defining property of R tells us that any object that is not an element of R must be an element of itself. (Otherwise, it would have been included as an element of R.) Thus, we can deduce that R ∈R. Wait a minute! Knowing that R ∈R led us to deduce that, in fact, R /∈R. This is also contradictory. No matter which option we choose---R ∈R or R /∈R---we find that the other must also be true, but certainly these contradictory options cannot both be true. Therein lies the paradox. This is not a properly-defined set. If it were, we would find ourselves stuck in the two cases we just saw, and neither of them can be true. It is also not the case that R is simply ∅; no, it must be that R does not exist as a set.


> 🇨🇳 TODO: 待翻译


The "Set of all Sets" is Not a Set Could we amend the definition of R somehow to produce the "set" that the definition is trying to convey? What "larger set" should we draw our objects x from so that the definition makes sense and properly identifies a set? Look back at the English-language interpretation we wrote after the definition: "the elements of R are sets that also happen to not have themselves as elements." The objects x that we wish to test for the desired property (x /∈x) are really all sets. Perhaps, then, we should just define X to be the set of all sets, and use the phrase "x ∈X" as part of our definition of R. That would fix it, right? R = {x ∈X | x /∈x} Well, no, not at all! The "set of all sets" is, itself, not a set. If it were, this would lead us to exactly the same paradox as before! Nothing would be different, except we would have explicitly stated the "larger set" from which we draw objects x that was previously left implicitly-specified. The main issue is that not specifying a "larger set" from which to draw objects, or implicitly referring to the "set of all sets", results in this type of undesirable paradox. Accordigly, we must not allow such definitions. Any attempt to define a set that draws objects x from the "set of all sets", whether implicitly or explicitly, is not a proper definition of a set. Further Discussion There is nothing inherently wrong with the property P(x) given by "x /∈x", though. The issue is with that "larger set" we use. For instance, take the set S =  x ∈ 1 2, 3 4, 5


> 🇨🇳 TODO: 待翻译


  x /∈x  What are its elements? The only possibilities are those elements drawn from the larger set  1 2, 3 4, 5


> 🇨🇳 TODO: 待翻译


. Notice that none of those numbers are sets that contain themselves as elements. Thus, this is a proper definition of the set  1 2, 3 4, 5


> 🇨🇳 TODO: 待翻译


, itself! With the previous definition for R, the object we were attempting to define was allowed as one of the variable objects x in its own definition, and that is where the issue arose. We hope that we haven't led your thoughts too far astray from the original discussion of examples of sets, but we felt it was important to point out that it is possible to construct ill-defined "collections" that are not sets in the mathematical sense of the word. For the most part, we will not face any such issues with the sets we work with in this book, but to gloss over these issues or simply not mention them at all would be unfair to you, as a student. If you find yourself interested in these issues, seek out an introductory book on set theory. There are other ways that definitions of "sets" can be ill-formed, as well, but the ensuing examples are based on (English) linguistic issues and not any mathematical underpinnings, as in Russell's Paradox. For instance, we could


> 🇨🇳 TODO: 待翻译


say "Let N be the set of all classic novels from the 20th century." Being a "classic novel" is not a well-defined property, and cannot be used to identify elements of such a set. The notion of a "classic" is subjective and not rigorously precise. Also, we could say "Let B be the set of people who will be born tomorrow" but this temporal dependence in the definition ensures that we will never actually know what the elements of B are. When tomorrow arrives, the definition will then refer to the next day, and so on. Can you come up with some other examples of ill-formed "collections" of elements? Can you come up with any paradoxes like the one above? In general, the following statement is the most important idea to take away from this discussion of Russel's Paradox: Under the agreed-upon rules of sets (the axioms of set theory), there is no set of all sets.
### 3.3.6 Standard Sets and Their Notation We have referred to and used some common sets of numbers already, so we will list now some sets and their standard symbols: • The natural numbers: N = {1, 2, 3, 4, . . . } • The first n natural numbers: [n] := {1, 2, 3, . . . , n −1, n} • The integers: Z = {. . . , −3, −2, −1, 0, 1, 2, 3, . . . } • The rational numbers: Q =  m n | m, n ∈Z and n ̸= 0


> 🇨🇳 TODO: 待翻译


• The real numbers: R • The complex numbers: C We have used N and Z a few times already. The rational numbers Q (we use Q since R was already taken, and rational numbers are quotients) are all of the fractions, or ratios of integers, both positive and negative. The real numbers are harder to describe. Why could we not list a few elements, like we did with N and Z? Why is it that R ̸= Q? For now, we essentially take for granted our collective knowledge of these sets of numbers, but think for a minute about that. (We mention the complex numbers C because you might be familiar with them, but we will not have occasion to use them in this book.) How do we know that a set like N exists? Why is it that we think of R as a number line? How many "more" elements are there in Z, as compared to N? How many "more" elements are there in R, as compared to Q? Can we even answer these questions? In the very near future, we will rigorously derive the set N and prove that it exists as the only set with a particular property. This will be essential when we return to our investigation of mathematical induction. (Remember our goals from that chapter?)


> 🇨🇳 TODO: 待翻译


### 3.3.7 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What does the symbol "∈" mean? (2) How would you read the statement "x ∈S" out loud? (3) Is it possible for a set to be an element of another set? If so, give an example. Is it possible for a set to be an element of itself? (4) How would read the statement "{x ∈N | x ≤5}" out loud? Can you list the elements of this set? (5) What is this set: {z ∈Z | z ∈N}? (6) What is this set: {x ∈[10] | x ≥7}? (7) For each of the following sets, state how many elements they have: (a) ∅ (b) {1, 2, 10} (c) {1, ∅} (d) { ∅} (8) Is x ∈{ 1, 2, {x} }? Is {x} ∈{ 1, 2, {x} }? (9) Let A = {a, b, c} and B = {b, c, a} and C = {a, a, b, c, a, b}. Are these sets equal or not? (10) Is Z = Q? Why or why not? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Write a definition of the set of natural numbers that are multiples of 4 using set-builder notation. (2) Consider the set S = {3, 4, 5, 6}. Define S in two different ways using setbuilder notation.


> 🇨🇳 TODO: 待翻译


(3) Give an example of a set X that satisfies N ∈X but Z /∈X. (4) Give an example of a set with 100 elements. (5) Give an example of a sets A, B, C such that A ∈B and B ∈C but A /∈C. (6) Write a definition of the set of odd integers using set-builder notation. (7) Write a definition of the set of integers that are not natural numbers using set-builder notation. (8) Consider the following sets: A =  x ∈R | x2 −3x + 2 ≥0


> 🇨🇳 TODO: 待翻译


B = {y ∈R | y ≤1 or y ≥2} Explain why A = B. (9) Consider the following sets: C =  x ∈R | x2 −4 ≥0


> 🇨🇳 TODO: 待翻译


D = {y ∈R | y ≥2} Is C = D? Why or why not? Write your explanation with good mathematical notation, using ∈and /∈. (10) Try explaining Russell's Paradox to a friend, even one who does not study mathematics. What do they understand about it? Do they object? Do their ideas make sense? Have a discussion!
## 3.4 Subsets
### 3.4.1 Definition and Examples
Let's discuss a topic whose basic idea we have already been using. Specifically, let's investigate the notion of subsets.
<div class="def-definition" markdown>
**Definition 3.4.1. Given two sets A and B, if every element of A is also an**
</div>
element of B, then we say A is a subset of B. The mathematical symbol for subset is ⊆, so we would write A ⊆B. If we want to indicate that A is a subset of B but is also not equal to B, we would write A ⊂B and say that A is a proper subset of B. We can also write these relationships as B ⊇A, or B ⊃A, respectively. In these cases, we would say B is a superset of A or B is a proper superset of A, respectively.


> 🇨🇳 TODO: 待翻译


