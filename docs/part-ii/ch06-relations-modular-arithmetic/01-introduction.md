---
title: Introduction
---

# Introduction

Chapter 6 Relations and Modular Arithmetic: Structuring Sets and Proving Facts About The Integers
## 6.1 Introduction Now that we've built a strong foundation of mathematical terminology, concepts, and material, you might be wondering what we're going to talk about next! Well, much like we wanted to rigorize the concept of mathematical induction---something we intuitively "understood" but couldn't yet develop in a precise mathematical way---we will, in the next two chapters, set on firmer ground a concept that we have used in passing already, and one that you're likely familiar with in an intuitive sense: a function. To accomplish this, we will start by talking about relations. This will lead us into the particular area of equivalence relations, which allow us to talk about some qualitative properties of sets. In particular, we will use some equivalence relations on the set Z to state and prove many interesting properties about integers. This will give us occasion to briefly explore the mathematical branch of Number Theory. It is a rich, deep, and broad field, and we will really only skim the surface by stating and proving a few helpful theorems and using them to solve some interesting puzzles and problems. Then, we will move right along to the next chapter and get back to our goal of discussing functions.
### 6.1.1 Objectives The following short sections in this introduction will show you how this chapter fits into the scheme of the book. They will describe how our previous work


> 🇨🇳 TODO: 待翻译


will be helpful, they will motivate why we would care to investigate the topics that appear in this chapter, and they will tell you our goals and what you should keep in mind while reading along to achieve those goals. Right now, we will summarize the main objectives of this chapter for you via a series of statements. These describe the skills and knowledge you should have gained by the conclusion of this chapter. The following sections will reiterate these ideas in more detail, but this will provide you with a brief list for future reference. When you finish working through this chapter, return to this list and see if you understand all of these objectives. Do you see why we outlined them here as being important? Can you define all the terminology we use? Can you apply the techniques we describe? By the end of this chapter, you should be able to . . . • Define a relation and provide many examples. • Define and understamd various properties that a relation might have, providing examples of relations that do and do not have these properties. • Consider a defined relation and discover and prove what properties it has. • Define equivalence relations and equivalence classes and explain why these are particularly interesting and important examples of relations. • Consider a defined equivalence relation and categorize its equivalence classes. • Use a particular equivalence relation on the set of integers to state and prove interesting results in number theory. • Define the concept of multiplicative inverses, understand what this means in the particular context of modular arithmetic, and apply this idea to prove/disprove the existence of solutions to particular equations. • State and understand various theorems in number theory, and apply them to solve given problems.
### 6.1.2 Segue from previous chapter This chapter doesn't quite follow from the previous one directly, in the way that others have. Instead, we are really moving into a new part of the book. From now on, we will be taking all of the mathematical knowledge we have developed thus far and applying it to learn about other interesting areas. We needed to work through all of that other material first, to get to this point. From now on, we will be stating complicated claims and applying proof techniques to prove them. We will provide you with definitions and theorems and expect you to use them to prove other claims. In this sense, this chapter follows from all of the previous chapters. We will be putting all of that acquired knowledge, terminology, and experience to good use!


> 🇨🇳 TODO: 待翻译


### 6.1.3 Motivation You have possibly worked with functions in calculus (differentiating and integrating them) or in a high school algebra course (graphing a function or finding its roots) or even in computer science (coding an algorithm or using recursive programming). But try this: define what a function is. How would you explain it to your uncle who's never studied mathematics? How would you explain it to a hyper-intelligent alien? How would you attempt to explain it with the level of rigor that we've provided with mathematical induction? It's not so easy, is it? To develop a rigorous notion of functions, we will first talk about relations, a way to compare elements of sets. We will look at plenty of examples and their properties. Then, in the next chapter, we will see that a function is just a particular type of relation! While we talk about relations, we will explore their properties and discover that a particular combination of properties yields a special property. Specifically, we will see that equivalence relations yield natural partitions of sets, and vice-versa. This result will allow us to state and prove several results about the integers.
### 6.1.4 Goals and Warnings for the Reader This chapter will continue our foray into abstract ideas and rigorous mathematics, so it is essential (especially if you feel put offby or uncomfortable with this increasing level of abstraction and the language required as part of it) that you don't get swept up and think that none of this information is "important" or "applicable". All of these concepts will continue to appear throughout this book---and all of mathematics, of course!---so keep that in mind if you find yourself losing focus. We recommend jotting down notes to yourself about what you're learning to remind yourself of what you're doing. When you see a theorem and read through it several times and finally understand it, write down a summary of the theorem in the margin or something so you'll have it later. Draw a little picture to help you conceptualize the important components of an example or theorem. When you read a definition, write down a canonical example and a non-example. After reading a proof, jot down an outline of the steps of the argument so you can "chunk" the concepts and remember (and recall) them more effectively. If you don't understand a definition or theorem or proof, make a note about your confusion, too! Take it to a fellow student or smart mathy friend or your TA or professor in office hours and see if they can address your confusion. Most of all, just remember that it takes time to digest and internalize these types of abstract concepts and arguments, and it's as important as ever to always work through examples to make sure you follow along in a way that makes sense to you. If you can understand something well enough to explain it to someone else, then you're in great shape.


> 🇨🇳 TODO: 待翻译


## 6.2 Abstract (Binary) Relations
### 6.2.1 Definition
Let's jump right in and start talking about relations. We'll give you a definition and then a bunch of examples.
<div class="def-definition" markdown>
**Definition 6.2.1. Let A, B be sets. A relation between A and B is a set of**
</div>
ordered pairs, R ⊆A × B. Given elements a ∈A and b ∈B, we say a and b are related if and only if (a, b) ∈R. The set A is called the domain and the set B is called the codomain. The set R is called the relation set. If A = B, we say R is a relation on A. It is also fairly common to write x R y to mean (x, y) ∈R. When we have defined a relation in this way, we will stick to the notation (x, y) ∈R to indicate the underlying set structure. Later on, we will sometimes define relations by using some symbol, like x < y or x ⋆y, and so on.
Remark 6.2.2. A relation, as we defined it here, is also sometimes referred to
as a binary relation. This is because there are two "inputs" of the relation; the set R consists of ordered pairs. We could generalize this idea to ternary relations. That is, given sets A, B, C, we could define a set R ⊆A × B × C to be a ternary relation and say a, b, c are related if and only if (a, b, c) ∈R. We could generalize this further to relations with n "inputs", as well. In this context, though, we will only consider binary relations, so we will use the term relation to mean binary relation.
Remark 6.2.3. A relation R is often defined by identifying a property of elements
of A and B (phrased as a variable proposition P(a, b)) and setting (a, b) ∈R ⇐⇒P(a, b)
Examples
Example 6.2.4. Let W = {English words} and L = {English letters}. Define
the relation R by setting (w, ℓ) ∈R ⇐⇒w begins with ℓ Then, (mathematics,m) ∈R and (golf,g) ∈R because these are valid words and we have identified their starting letters. For some non-examples, notice that (knowledge,n) /∈R and (you,u) /∈R. Furthermore, note that (zyzyxyqy,z) /∈R because zyzyxyqy/∈W. It is often the case that A = B, so R defines a relation on pairs of elements from one set. The next example considers this situation.


> 🇨🇳 TODO: 待翻译


