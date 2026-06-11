---
title: The Idea of a Set
---

# The Idea of a Set

axioms for granted without rigorously proving them. This is not because such proofs are impossible, but merely because they would take too much time and space in this book to accomplish. What we will do is provide a definition of "set" that is satisfactory for the contexts in which we will be using sets in this book. We will also define some basic properties of sets, share some illustrative examples, and dicuss different operations we can perform on sets to create new ones.
## 3.3 Definition and Examples
### 3.3.1 Definition of "Set"
Let's start with a definition. As we started to explain above, we often think of sets as being characterized by the objects that are grouped together into that set and the property that makes that grouping make sense. The following definition attempts to make that notion as precise as we possibly can, while also introducing some relevant notation and terminology.
<div class="def-definition" markdown>
**Definition 3.3.1. A set is a collection of all objects that have a common, well-**
</div>
defined property. The objects contained in a set are called elements of the set. The mathematical symbol "∈" represents the phrase "is an element of" (and "/∈" represents "is not an element of").
### 3.3.2 Examples
Let's dive right in with some specific examples of sets (and non-sets, even) to illustrate this definition. It is common in mathematics to use capital letters to refer to sets and lowercase letters to refer to elements of sets, and we will frequently follow this convention (but not always). To define or describe a set, we need to identify that common, well-defined property that associates the elements of the set with each other. For instance, we could define B to be the set of all teams in Major League Baseball. Is this a well-defined property? If we present you with an object, is ther a definite Yes/No answer to the question of "Does this object have this defining property?" Yes, this is the case here, so this is a property that characterizes a set. (To avoid confusion for readers in the future, let us be more specific and say B refers to MLB teams from the 2012 season.) In the language of mathematics, we would write B = {Major League Baseball teams from the 2012 season} The "curly braces"---{ and }---indicate that the description between them will identify a set, and the text inside is a description of the objects and their common, well-defined property. It now makes sense to say Pittsburgh Pirates ∈ B and Pittsburgh Penguins /∈B. Common ways to read the mathematical symbol ∈in English are "is an element of" or "is a member of" or "belongs to" or "is in". We will mostly


> 🇨🇳 TODO: 待翻译


use "is an element of" because it is the least ambiguous of them, and uses the mathematical term element appropriately. Any of these other, equivalent, phrases may be used, depending on the context, but are less preferable. (In particular, "is in" can be confused with other set relationships, so we will avoid it entirely, and encourage you to do the same.) We've also already seen some commonly-used sets of numbers. You know what they are from previous work with these numbers, but you might not usually think of them as sets, which is what they are! N = { natural numbers } = {1, 2, 3, . . .} Z = { integers } = {. . . , −2, −1, 0, 1, 2, . . .} Q = { rational numbers } = {numbers of the form a b , where a, b ∈Z and b ̸= 0 } R = {real numbers} Think about how the second definition of Q above makes sense. We will see, quite soon, a more condensed way to write out a phrase like "numbers of the form . . . blah blah . . . with the additional information that . . . blah blah". Also, notice that we can't really define R except to just say they're the real numbers. How do you even define what a real number is? Have you ever tried?
### 3.3.3 How To Define a Set Another way of defining or describing a set is simply listing all of its elements. This is convenient when the number of elements in the set is small. For instance, the following definitions of the set V are all equivalent: V = {A,E,I,O,U} V = {vowels in the English language} V = {U,E,I,A,O} By "equivalent", we mean that each line above defines the same set V , using different terms. (Note: we have adopted the convention that y is a consonant, so y /∈V .) The common, well-defined property that associated the objects A, E, I, O, and U is the fact that they are all vowels (exhibited in the second definition) and since there are only five such objects, it is simple and convenient to list them all (as in the first definition). Order and Repetition Don't Matter Why do you think the third definition is the same as the others? It refers to the same collection of objects, and any set is completely characterized by its elements, so the order in which we write the elements does not matter. Is U∈V ? The answer to this question is "Yes", regardless of whether U is written first or last in the list of elements.


> 🇨🇳 TODO: 待翻译


