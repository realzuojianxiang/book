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
defined property. The objects contained in a set are called elements of the set. The mathematical symbol "$\in$" represents the phrase "is an element of" (and "$\notin$" represents "is not an element of").
### 3.3.2 Examples
Let's dive right in with some specific examples of sets (and non-sets, even) to illustrate this definition. It is common in mathematics to use capital letters to refer to sets and lowercase letters to refer to elements of sets, and we will frequently follow this convention (but not always). To define or describe a set, we need to identify that common, well-defined property that associates the elements of the set with each other. For instance, we could define B to be the set of all teams in Major League Baseball. Is this a well-defined property? If we present you with an object, is ther a definite Yes/No answer to the question of "Does this object have this defining property?" Yes, this is the case here, so this is a property that characterizes a set. (To avoid confusion for readers in the future, let us be more specific and say B refers to MLB teams from the 2012 season.) In the language of mathematics, we would write B = {Major League Baseball teams from the 2012 season} The "curly braces"---{ and }---indicate that the description between them will identify a set, and the text inside is a description of the objects and their common, well-defined property. It now makes sense to say Pittsburgh Pirates $\in$ B and Pittsburgh Penguins \notin B. Common ways to read the mathematical symbol $\in i$n English are "is an element of" or "is a member of" or "belongs to" or "is in". We will mostly


> 🇨🇳 使用"是……的元素"这一读法，因为它是所有读法中歧义最小的，且恰当使用了数学术语"元素"（Element）。其他等价说法根据语境也可使用，但不够理想。（尤其需注意，"在……中"容易与集合的其他关系混淆，因此我们将完全避免该说法，也建议你这样做。）我们还已见过一些常用的数集：$\mathbb{N} = \{1, 2, 3, \ldots\}$（自然数）、$\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$（整数）、$\mathbb{Q} = \{a/b \mid a, b \in \mathbb{Z},\ b \neq 0\}$（有理数）、$\mathbb{R}$（实数）。想一想 $\mathbb{Q}$ 的第二种定义为何合理——我们很快将学到更简洁的表达方式。另外注意，除了直接说它们是实数，我们其实无法真正定义 $\mathbb{R}$。你试过定义实数吗？


use "is an element of" because it is the least ambiguous of them, and uses the mathematical term element appropriately. Any of these other, equivalent, phrases may be used, depending on the context, but are less preferable. (In particular, "is in" can be confused with other set relationships, so we will avoid it entirely, and encourage you to do the same.) We've also already seen some commonly-used sets of numbers. You know what they are from previous work with these numbers, but you might not usually think of them as sets, which is what they are! N = { natural numbers } = {1, 2, 3, . . .} Z = { integers } = {. . . , −2, −1, 0, 1, 2, . . .} Q = { rational numbers } = {numbers of the form a b , where a, b $\in \mathbb{Z}$ and b \neq 0 } R = {real numbers} Think about how the second definition of Q above makes sense. We will see, quite soon, a more condensed way to write out a phrase like "numbers of the form . . . blah blah . . . with the additional information that . . . blah blah". Also, notice that we can't really define R except to just say they're the real numbers. How do you even define what a real number is? Have you ever tried?
### 3.3.3 How To Define a Set Another way of defining or describing a set is simply listing all of its elements. This is convenient when the number of elements in the set is small. For instance, the following definitions of the set V are all equivalent: V = {A,E,I,O,U} V = {vowels in the English language} V = {U,E,I,A,O} By "equivalent", we mean that each line above defines the same set V , using different terms. (Note: we have adopted the convention that y is a consonant, so y $\notin V$ .) The common, well-defined property that associated the objects A, E, I, O, and U is the fact that they are all vowels (exhibited in the second definition) and since there are only five such objects, it is simple and convenient to list them all (as in the first definition). Order and Repetition Don't Matter Why do you think the third definition is the same as the others? It refers to the same collection of objects, and any set is completely characterized by its elements, so the order in which we write the elements does not matter. Is U$\in V$ ? The answer to this question is "Yes", regardless of whether U is written first or last in the list of elements.


> 🇨🇳 顺序与重复无关——你认为第三种定义为何与前两种等价？因为它指的是同一组对象（Object），而任何集合都完全由其元素（Element）所刻画，因此书写元素的顺序无关紧要。$U \in V$ 吗？答案是"是"，无论 $U$ 在元素列表中排在第一位还是最后一位。


