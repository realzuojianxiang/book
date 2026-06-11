---
title: Indexed Sets
---

# Indexed Sets

number of sets "all at once". There is really no new mathematical content in this section, but the notation involved in these ideas can be confusing and difficult to work with, at first, so we want to guide you through these ideas carefully. Relation to Summation Notation We'll start with a related concept that we have seen before. Remember when we investigated sums of natural numbers in Chapter 1? We mentioned some special notation that allowed us to condense a long string of terms in a sum into one concise form, using the P symbol. For instance, we could write an informal sum ("informal" meaning "not rigorous" because of the use of ellipses) in the P notation as follows: 1 + 2 + 3 + 4 + · · · + (n −1) + n = n X i=1 i Why does this notation work and make sense? The index variable i is the key component of condensing the sum into this form. Writing "i = 1" underneath the P symbol means that the value of the variable i should start at 1 and increase by 1 until it reaches the terminal value, n, written above the P symbol. For each allowable value of i in that range (from 1 to n), we include a term in the sum of the form written to the right of the P symbol; in this case, that term is i. Thus, we should have the terms 1, 2, 3, . . . , n with a + sign between each. We should point out that it is implicitly understood that writing i = 1 and n as the limits on the index variable i means i assumes all values that are natural numbers between 1 and n.
Example
Let's see the process of defining indexed sets via an example first. We will also see how to apply set operations to several sets by using an index variable.
Example 3.6.1. We can similarly condense some set operation notation. For
instance, let's define the sets A1, A2, A3, . . . , A10 by A1 = {1, 2} A2 = {2, 4} A3 = {3, 6} ... Ai = {i, 2i} ... A10 = {10, 20}


> 🇨🇳 TODO: 待翻译


We included the definition of Ai for an arbitrary value i to give these sets a rigorous definition. Without definining that set---which defines Ai for any relevant value of i---we would be leaving it up to the reader to interpret the pattern among the sets A1, A2, A3, A10, and there could be multiple ways of interpreting that. By defining the term Ai explicitly like this, there is no confusion as to what we want these ten sets to be. Furthermore, we can more easily express the union of all of these sets, for instance. Remember that the union of two sets is the set containing all elements of both sets (i.e. an element is included in the union if it is in the first set or the second set, or possibly both). What is the union of more than two sets? It follows the same idea as the definition for just two sets; we want to include an element in the union if it is in any of the constituent sets we are combining via the union operation. How can we write this union concisely and precisely? Let's follow the same motivation of the P notation. The index of these sets runs from 1 to 10, so we should write i = 1 below a "∪" symbol and 10 above it. Each term in the union is of the form {i, 2i}, so we should write that to the right of the "∪" symbol. For indexed unions like this one, though, we use a slightly larger "S" symbol, like so: A1 ∪A2 ∪A3 ∪· · · ∪A10 =


> 🇨🇳 TODO: 待翻译


[ i=1 {i, 2i} This is far more concise than writing the elements of all 10 sets, so you can see how useful this notation is. We will keep reminding you of the imprecision of the ellipses in the union on the left and tell you that, in fact, an expression like the one on the right is a truly rigorous mathematical statement about this union. The expression on the left is more of an intuitive, heuristic way of describing the union operation applied to these ten sets. When The Index Set Is Not a Range of Numbers Let's examine a more difficult example to motivate the next development in this notation technique. What if we asked you to write the following sum in summation notation: the sum of the squared reciprocals of all prime numbers. How can we accomplish this? (Note: We just want to express all the terms of the sum without evaluating the sum. That's a difficult endeavor left for another time!) Unfortunately, we cannot use the exact same notation as above, because we don't want to sum over a range of index values between two natural numbers; rather, we want to only include terms in the sum corresponding to prime numbers. The solution to this is to define an index set I that will describe the allowable values of the index that we will then "plug into" the arbitrary term written to the right of the sum. In this case, if we have a prime number i, we would like to include the term


> 🇨🇳 TODO: 待翻译


i2 in our sum, so this expression will be written to the right of the P symbol. We would like to express in our notation that the value i should be a prime


> 🇨🇳 TODO: 待翻译


number and that all possible prime numbers should be included. The index set I of allowable values should, therefore, be the set of all prime numbers. That is, we can write this sum as X i∈I


> 🇨🇳 TODO: 待翻译


i2 , where I = {i ∈N | i is prime} Look at what this notation accomplishes! Not only have we condensed an infinite number of terms into one expression, we have indicated that the values of the arbitrary index i should be restricted to prime numbers, which do not behave in the "usual" and convenient way as with a sum like Pn i=1 i.
Example 3.6.2. This concept of an index set is extremely useful and extends to
arbitrary sets and even non-mathematical objects. For instance, in our discussion of sets above we used the set B of all Major League Baseball teams. How can we use this set to express the set P of all Major League Baseball players? Each team is, itself, a set whose elements are the players on that team, so a union of all of the teams (i.e. a union of all sets in B) should produce exactly this set of all players! In this case, our index set is B, and for each element b ∈B, we want to include b as a set in our union. Thus, we would write P = [ b∈B b The individual terms in this union are not even dependent on natural numbers, so there would have been no way to express this union without the use of an index set, like this. Also, this union is dependent on the fact that the terms of the union are elements of the index set B, but they are also sets themselves; thus, applying the union operation to them makes mathematical sense. This might still seem like an odd idea, so be sure to think carefully about this idea of sets having elements that are sets, themselves. Reading Indexed Expressions Aloud To verbalize these types of expressions, and to help you think of them in your head, let's give you an example. We might read the expression up above as "The sum, over all i that are prime, of


> 🇨🇳 TODO: 待翻译


i2 ." or "The sum of


> 🇨🇳 TODO: 待翻译


i2 , where i ranges over all prime numbers." Likewise, we might read the other expression above as "The union, over all b that are MLB teams in the 2012 season, of those b." or "The union of all sets b, where b ranges over all MLB teams from the 2012 season."


> 🇨🇳 TODO: 待翻译


### 3.6.2 Indexed Unions and Intersections Let's give a precise definition of this union operation for more than one set, since we have only rigorously defined the union of two sets.
<div class="def-definition" markdown>
**Definition 3.6.3. The union of a collection of sets Ai indexed by the set I is**
</div>
[ i∈I Ai = {x ∈U | x ∈Ai for some (i.e. at least one) i ∈I} where we assume there is a set U such that Ai ⊆U for every i ∈I. In mathematical language, the phrase "for some i ∈I" means that we want there to be at least one i ∈I with the specified property. If an element x satisfies x /∈Ai for every i ∈I, then this says x is not in any of the sets in our collection, so it should not be included in the union. Following this idea, we can make a similar definition for set intersections.
<div class="def-definition" markdown>
**Definition 3.6.4. The intersection of a collection of sets Ai indexed by the set**
</div>
I is \ i∈I Ai = {x ∈U | x ∈Ai for every i ∈I} where we assume there is a set U such that Ai ⊆U for every i ∈I.
### 3.6.3 Examples
Let's return to a previous example and make these ideas clearer.
Example 3.6.5. Previously, in Example 3.6.1, we defined
Ai = {i, 2i} for every natural number i between 1 and 10. Another way of defining this collection is to consider the index set I = [10] (recall the notation [n] = {i ∈N | 1 ≤i ≤n}) and define A to be the set A = {Ai | i ∈I} , where Ai = {i, 2i} for every i ∈I This defines every set Ai, dependent on the index value i chosen from the index set I, and it "collects" all of these sets into one set A. Then, another way of writing that union we wrote before would be [ i∈I Ai with the given definitions of I and Ai. (Think carefully about how this union differs from the set A. Also, what exactly is this union? How can we express its elements conveniently? Do we need to list every element? What if we change the index set I to be N? What is the union in that case?)


> 🇨🇳 TODO: 待翻译


Example 3.6.6. Let I = {1, 2, 3} and, for every i ∈I, define
Ai = {i −2, i −1, i, i + 1, i + 2} Let's identify and write out the elements of the following sets: [ i∈I Ai and \ i∈I Ai Notice that we can write out the elements of each Ai set, as follows: A1 = {−1, 0, 1, 2, 3} A2 = {0, 1, 2, 3, 4} A3 = {1, 2, 3, 4, 5} Thus, [ i∈I Ai = A1 ∪A2 ∪A3 = {−1, 0, 1, 2, 3, 4, 5} and \ i∈I Ai = A1 ∩A2 ∩A3 = {1, 2, 3} Now, consider J = {−1, 0, 1}, with Aj defined in the same way as before. Let's identify the elements of the sets [ j∈J Aj and \ j∈J Aj Writing out the elements of each set, we can determine that [ j∈J Aj = A−1 ∪A0 ∪A1 = {−3, −2, −1, 0, 1, 2, 3} and \ j∈J Aj = A−1 ∩A0 ∩A1 = {−1, 0, 1} Try answering the same questions with different index sets. For instance, consider K = {1, 2, 3, 4, 5} or L = {−3, −2, −1, 0, 1, 2, 3}.
Example 3.6.7. Define the index set I = N. For every i ∈I, define the set
Ci =  x ∈R | 1 ≤x ≤i + 1 i  Then we claim that [ i∈I Ci = {y ∈R | 1 ≤y ≤2} and \ i∈I Ci = {1} Can you see why these are true? We will discuss the techniques required to prove such equalities later on. For now, we ask you to just think about why these are true. Can you explain them to a classmate or a friend? What sort of techniques might you use to prove these claims?


> 🇨🇳 TODO: 待翻译


Example 3.6.8. Let S be the set of students taking this course. For every s ∈S,
let Cs be the set of courses that student s is taking this semester. What do the following expressions represent? [ s∈S Cs and \ s∈S Cs We bet you can identify at least one element of the set on the right!
### 3.6.4 Partitions Now that we have a way of writing down a union of many sets, we can define a helpful notion: that of a partition. Linguistically speaking, a partition is a way of "breaking something apart into pieces", and that's pretty much what this word means, mathematically speaking. To wit, a partition is just a collection of subsets of a set that do not overlap and whose union is the entire set. Let's write down that definition here and then see some examples and non-examples. We will have occasion to use this definition many times in the future, so let's get a handle on it now while we're talking about sets and indexed unions.
<div class="def-definition" markdown>
**Definition 3.6.9. Let A be a set. A partition of A is a collection of sets that**
</div>
are pairwise disjoint and whose union is A. That is, a partition is formed by an index set I and non-empty sets Si (defined for every i ∈I) that satisfy the following conditions: (1) For every i ∈I, Si ⊆A. (2) For every i, j ∈I with i ̸= j, we have Si ∩Sj = ∅. (3) [ i∈I Si = A The sets Si are called parts of the partition. The idea here is that the sets Si "carve up" the set A into non-overlapping, nonempty pieces.
Example 3.6.10. Let's see a couple of examples.
(1) Consider the set N. Let O be the set of odd natural numbers, and let E be the set of even natural numbers. Then {O, E} is a partition of N. This is because • E, O ̸= ∅, and • E, O ⊆N, and • E ∩O = ∅, and • E ∪O = N


> 🇨🇳 TODO: 待翻译


(2) Consider the set R. For every z ∈Z, define the set Sz by Sz = {r ∈R | z ≤r < z + 1} We claim {. . . , S−2, S−1, S0, S1, S2, . . . } is a partition of R. Can you see why? Try to write out the conditions required for this collection of sets to be a partition, and see if you can understand why they hold. Specifically, remember that we need these sets to be pairwise disjoint. This means that any two sets must be disjoint. Notice that this is quite different from requiring the the intersection of all the sets together to be empty. For instance, consider the collection of sets  {1, 2}, {2, 3}, {3, 4}


> 🇨🇳 TODO: 待翻译


This collection is not pairwise disjoint because, for example, {1, 2} ∩{2, 3} = {2} ̸= ∅ However, the intersection of all three sets is empty, because no element is common to all three of them together.
Example 3.6.11. Now, let's see a couple of non-examples.
(1) Consider the set R. Let P be the set of positive real numbers and let N be the set of negative real numbers. Then {N, P} is not a partition because 0 /∈N ∪P. Can you modify the choices we made here to identify a partition of R into two parts? (2) Consider the set Z. Let A2 be the set of integers that are multiples of 2, let A3 be the set of integers that are multiples of 3, and let A5 be the set of integers that are multiples of 5. The collection {A2, A3, A5} is not a partition for two reasons. First, these sets are not pairwise disjoint. Notice that 6 ∈A2 and 6 ∈A3, since 6 = 2 · 3. Second, these sets do not "cover" all of Z. Notice that 7 ∈Z but 7 /∈A2 ∪A3 ∪A5. As we mentioned, we will have occasion to use this definition frequently in the future, so keep it in mind.
### 3.6.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 TODO: 待翻译


(1) What is an index set? (2) Let I = N, and for every i ∈I, let Ai = {i, −i}. Why are the following sets all the same set? [ i∈I Ai [ x∈N Ax [ j∈I Aj By the way, what are the elements of this set? (3) List the elements of the following sets: (a) [ x∈N {x} (b) \ x∈N {x} (c) [ x∈N {x, 0, −x} (4) Why do you think we didn't talk about an "indexed difference" or an "indexed complementation", and only talked about unions and intersections? (5) What is a partition? What conditions does a collection of sets have to satisfy to be a partition of a set? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let A = {−2, −1, 0, 1, 2}. Let B = {1, 3, 5}. For every i ∈Z, let Si = {i −2, i, i + 2, i + 4}. What is [ i∈A Si? What is \ x∈B Sx? (2) For every n ∈N, let An = [n]. What is \ n∈N An? What about [ n∈N An? (3) Find a way to write the set of all integers between -10 and 10 (inclusive) using set-builder notation. Then, define the same set using an indexed union. Can you do this in a way so that the sets in your union are pairwisedisjoint (meaning that no two of them have any elements in common)? (Hint: Yes, you can.)


> 🇨🇳 TODO: 待翻译


(4) For every n ∈N, let Mn be the set of all multiples of n. (For example, M3 = {3, 6, 9, . . . }.) Write a definition for Mn using set-builder notation. Then, express N as a union, using these sets. (Challenge: Can you use these sets to define a partition of N?) (5) Let X be any set. What is [ S∈P(X) S? What about \ S∈P(X) S? (It might help to try this with a specific set, like X = {1, 2}, to see what happens, first.) (6) Identify an index set and define some sets that allow you to express Q as an indexed union. Can you do this so that there are infinitely many elements in the index set? (Challenge: Can you make this collection a partition of Q?)
## 3.7 Cartesian Products There is one more way of "combining" sets to produce other sets that we want to investigate. This method is based on the idea of order. When we define sets by listing the elements, the order is irrelevant; that is, the sets {1, 2, 3} and {3, 1, 2} and {2, 1, 3} are all equal because they contain the same elements. (More specifically, they are all subsets of each other in both directions). Looking at mathematical objects where order is relevant, though, allows us to combine sets in new ways and produce new sets. You are likely already familiar with the idea of the real plane, R2 (also known as the Cartesian plane after the French matheamtician Ren´e Descartes). Each "point" on the plane is described by two values, an x-coordinate and a ycoordinate, and the order in which we write those coordinates is important. We usually think of the x-coordinate as first and the y-coordinate as second, and this helps to distinguish two points based on this order. For instance, the point (1, 0) lies on the x-axis but the point (0, 1) lies on the y-axis. They are not the same point. There is a deeper, mathematical idea underlying the Cartesian plane. Given any two sets, A and B, we can look at the set of all ordered pairs of elements from A and B. By pair we mean an expression (a, b) where a and b are elements of A and B, respectively. By ordered we mean that writing a first and b second is important. In the case of the real plane, it is especially important because any real number could appear as the x-coordinate or the y-coordinate of a point, but the point (x, y) is generally different from the point (y, x). (When are they equal? Think carefully about this.)
### 3.7.1 Definition
Let's give an explicit definition of this new set before examining some examples.


> 🇨🇳 TODO: 待翻译


