---
title: 1.3 Review, Redo, Renew
---

# 1.3 Review, Redo, Renew

Presumed Knowledge The main point is that we can't actually write proofs without imbuing them with some meaningful mathematical content. Accordingly, one of the main goals of this book is to share some interesting mathematical facts with you. Sometimes, this involves working with objects you already know about and have seen before (like triangles or prime numbers) and trying to do new things with them. Other times, we may be introducing you to completely new mathematical objects (like equivalence relations or binomial coefficients) and working with those. What we'd like to do now is discuss some mathematical objects and concepts that we will use rather frequently and that you might have seen before. We aren't necessarily assuming that you've seen all of these, but none of these ideas are too hard to learn/relearn quickly, and they will be quite useful throughout the remainder of this book, and the remainder of your mathematical life, as well! We've included a handful of problems for you to work on to give you some practice, both throughout this section and at the end of it.
### 1.3.1 Quick Arithmetic We won't be expecting you to multiply six digit numbers in your head or anything like that, but being able to manipulate "small" numbers via addition, subtraction and multiplication is an important skill. Sure, calculators and computing programs can be helpful, but we hope that it isn't necessary to run offto Maple or Mathematica or your TI-89 whenever we need to add a couple of four digit numbers, say. Technology provides us with many conveniences in the form of accuracy and time-efficiency but when we rely on these devices too heavily, we diminish our ability to verify those answers we get (in the event of a typo or missed keystroke, for instance) and when we use them too frequently, we may not actually save any time at all! We encourage you to continually try to perform any arithmetic steps we face either in your head or on a piece of scrap paper. It will be fairly infrequent that any problems/puzzles involve arithmetic with "large" numbers and even when they do, there may be a special trick that can reduce the problem to something easier. For instance, try to work on the following series of problems and see what you notice. Problem 1.3.1. For each of the following multiplications, try to identify the final digit of the resulting number. If your answer is "0" then try to identify how many zeroes are at the end of the resulting number. 1. 1 · 2 · 3 · 4 · 5 2. 1 · 2 · 3 · · · · · 10 3. 1 · 2 · 3 · · · · · 25 4. 1 · 2 · 3 · · · · · 100 5. 1 · 2 · 3 · · · · · 1000


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


6. 1 · 2 · 3 · · · · · 10000 7. 1 · 2 · 3 · · · · · 109 Try to write down a few sentences that would explain to a friend the procedure you used above. That is, given any number n, explain how to identify the number of zeroes at the end of the number resulting from multiplying 1·2·3·· · ··n What did you notice? Did you use your calculator for the first few? Surely that would work, or you could even do the first two or three by hand, but how did that help you later on? How did that help you to explain your procedure? Certainly, you needed to find a more general way of figuring out how to tackle this problem, and resorting to a calculator or computer might help you in some cases, but it won't provide you with any insight into the answer. If you haven't figured out a general procedure, we'll give you this: Hint: Think about how many multiples of 2 and how many multiples of 5 appear in the multiplication. Try to pair them together. (Why would you want to do that?)
### 1.3.2 Algebra Abracadabra The term algebra has a couple of meanings in the mathematical world with some different nuances to each. Usually, the term brings to mind manipulating equations with variables and trying to find a numerical solution for them. This is probably how you handled word problems in a high school algebra class. More generally, though, abstract algebra is a branch of mathematics that studies certain mathematical structures that have specific properties, oftentimes having no relation to integers or real numbers. Much of the groundwork for this field was laid by mathematicians before the 19th century who were seeking roots of polynomial equations where the variables were raised to the third or fourth or even higher powers. For a quadratic equation (containing a variable raised to the second power), you probably remember the formula for finding a root of the equation (i.e. a value for the variable that will make the expression evaluate to zero); this is the famous Quadratic Formula. Did you also know there is a procedure for finding the root of an expression involving a variable that is cubed? Or even raised to the fourth power? Interestingly enough, the mathematicians working on this general problem discovered that there are no such procedures possible for higher powers! A lot of the concepts and structures they were working with developed into some inherently interesting mathematics, and people have been studying those objects ever since, eventually branching offand working with the underlying properties of those objects, stripping away the numerical context of finding roots of equations. This is usually what a mathematician means when he/she says "algebra". In this particular context, though, we will be using "algebra" in the sense that you're likely thinking of it: manipulating multiple equations and variables


> 🇨🇳 TODO: 待翻译


to obtain numerical values for the variables that make the expressions evaluate to numbers that satisfy all of the equations involved. There is actually a rich and wonderful theory behind solving systems of linear equations, but this type of in-depth study is better suited for a course on matrix algebra (also called linear algebra). For now, we'll look at a couple of handy tricks and then let you practice them. Solving Systems of Linear Equations A system of linear equations is just a collection of equations involving a certain number of variables (all raised to the first power, hence linear) multiplied by coefficients and added together, and set equal to some constants. There are specific conditions on the coefficients and constants that guarantee whether or not a solution exists (and whether there are infinitely many or just one, in fact) but we won't get into those specific details. Suffice it to say that the systems of equations we will have to handle in this book will have unique solutions, and this means that the number of equations we have will be the same as the number of variables involved. Knowing that ahead of time, how do we manipulate a system of equations to find that unique solution? In practice, the most time-efficient way of solving a system depends on the coefficients and constants, as well, and perhaps spotting a particular way of applying the methods we are about to explain. That said, simply following these methods will always work in a short amount of time, anyway, so don't be too concerned with finding the absolute shortest method in any given case. Method 1: The first method involves a system of two equations and two unknowns. In this case, we can use one of the equations to express one variable in terms of the other, then substitute this into the second equation, yielding one equation and one unknown. From that, we can find a specific value for one variable, and substitute this back into the first equation to find a specific value for the other variable, thereby obtaining the solution we wanted. Let's see this process in action with a particular example. Consider the system of equations below: 7x + 4y = −2 −2x + 3y = 13 Following the method we just described, we would rearrange the first equation to write y in terms of x y = 1 4(−2 −7x) then substitute this into the second equation −2x + 3 · 1 4(−2 −7x) = 13


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


and solve that new equation for x: −2x −3 2 −21 4 x = 13 −29 4 x = 29


> 🇨🇳 TODO: 待翻译


x = −2 Then, we would use this value in the first equation and solve for y: 7 · (−2) + 4y = −2 4y = −2 + 14 = 12 y = 3 Therefore, the solution we sought is (x, y) = (−2, 3). What if we had used the value of x we found in the second equation instead of the first? Well, it would produce the same value of y, but maybe the arithmetic would have been slightly quicker. Or, what if we had done it the other way around, and expressed x in terms of y, solved for y, then went back and solved for x? Again, we would have found the same solution, but perhaps the numbers would work out more "nicely" and save us a few seconds of scratch work. This is what we mean by not worrying about finding the most "efficient" method. Sure, there are multiple ways to approach this system of equations, but they ultimately stem from the same method (substitute and solve) and yield the same solution. Method 2: An alternative way to handle a system of two equations and two unknowns is to multiply both equations through by particular values and then add them together, choosing those multipliers appropriately so that one of the variables is eliminated. Using the example from above, we could multiply the first equation by 2 and the second equation by 7, making the coefficient of x in both equations equal yet opposite; then, adding the equations reduces the system to one equation and one unknown, just y. Observe: 2 ·  7x + 4y = −2  7 ·  −2x + 3y = 13  14x + (−14x) + 8y + 21y = −4 + 91 29y = 87 y = 3 From there, we can substitute this value into the first or second equation and solve for x. You can use either of these approaches to handle any system of two equations and two unknowns. Perhaps one would be slightly quicker than the other, depending on the numbers involved, but you won't be saving more than a minute either way, so we encourage you to just choose one and work through it.


> 🇨🇳 TODO: 待翻译


Method 3: It can sometimes be convenient to interpret these systems of equations graphically; this is not usually an efficient way of identifying a specific solution to the system, but it can give an indication of whether a solution exists and a rough estimate of the magnitude of the values of the solution. With two unknowns, we can interpret an equation like ax + by = c in terms of a line in the plane by rearranging: y = −a b x + c b. This is the line with slope −a b and y-intercept c b. Given two such equations, we can draw two lines in the plane and locate the point of intersection visually. The (x, y) coordinates of that point are precisely the solution we would find by solving the system of equations as we described above. This visual method also applies to a system of three equations and three unknowns, but this requires drawing lines in three-dimensional space. This can be difficult to do in practice, but is technically achievable. These same concepts also apply to larger numbers of equations and unknowns, but drawing "lines" in four or more dimensions is impossible for us human beings to visualize! More than two variables: Reduce! The next part of this method builds upon the first by taking a system of more than two equations (and unknowns) and continually reducing it to smaller systems, eventually obtaining a system of two equations and two unknowns, where we can apply the first part of the method. We will illustrate the method by considering a system of three equations and three unknowns, like the one below: 6x −3y + z = −1 −3x + 4y −2z = 12 5x + y + 8z = 6 The first goal is to eliminate one of the three variables. In essence, this can be done in one of two ways, much like the method for two equations and two unknowns. Let's say we're going to try to eliminate z from the system; we can try to express z in terms of x and y and substitute somehow, or we can multiply some equations and add them together to cancel the coefficients of z. The only difference here is that, whichever option we choose, we need to do it twice. Let's use the first equation to write z = −6x + 3y −1 After substituting this expression for z into both the second and third equations, we will have a system of two equations and two unknowns. One way to think about this is that we need information from all three equations to ultimately arrive at an answer, and in reducing the system to two equations, we need to somehow retain information from all three of the original equations. The expression we have for z came from the first equation, so we need to subtitute it into the other two to retain all of the information we need. Compare this to the following sequence of steps: rearrange the first equation to isolate z and substitute this into the second equation, then rearrange the second equation to isolate z and substitute this into the first equation. What


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


happens? The intuition is that we have somehow "lost" information from the third equation and, yes, we will obtain a system of two equations and two unknowns, but it will have insufficient information to yield a unique solution for x and y. If you actually perform the steps we just described (try doing this to check our work), you obtain the following "system" of two equations after minimal simplification: 9x −2y = 10


> 🇨🇳 TODO: 待翻译


2x −y = 5 These are really the same equation! Accordingly, we wouldn't actually be able to solve them for unique values of x and y. Let's return to where we were and substitute the expression for z above into the second and third equations −3x + 4y −2 · (−6x + 3y −1) = 12 5x + y + 8 · (−6x + 3y −1) = 6 and then simplify 9x −2y = 10 −43x + 25y = 14 Applying one of the methods from the first problem will give us the solution (x, y) = (2, 4). Having both of these values in hand, we can now return to any one of the original three equations and solve for z; better yet, we can just use the isolated expression for z we found already from the first equation: z = −6x + 3y −1 = −6 · (2) + 3 · 4 −1 = −12 + 12 −1 = −1 More than two variables: Reduce another way! Another way to reduce a system from three equations to two equations is related to the "multiply and add" method from before, but we still have to be careful about ensuring that we retain information from all three equations. Using the same system of three equations from above, we might notice that after multiplying the first equation by 8 and the second equation by 4, the coefficient of z in all three equations is either ±8. This allows us to add/subtract the equations in a convenient way to reduce the system to two equations and two unknowns. Specifically, let's do the multiplication we just mentioned 48x −24y + 8z = −8 −12x + 16y −8z = 48 5x + y + 8z = 6 and then add the first equation to the second (48x −12x) + (−24y + 16y) + (8z −8z) = −8 + 48 36x −8y = 40


> 🇨🇳 TODO: 待翻译


and the second equation to the third (−12x + 5x) + (16y + y) + (−8z + 8z) = 48 + 6 −7x + 17y = 54 This produces two equations involving only x and y; furthermore, we have combined information from all three original equations to produce these, so we can be assured that we haven't "lost" anything. Solving this new system 36x −8y = 40 −7x + 17y = 54 via any of the previous methods we discussed produces the solution (x, y) = (2, 4). Substituting these values into any of the three original equations and solving for z produces the ultimate answer we sought. We could have performed similar steps to eliminate y from the system of three equations, too; for instance, we could add 4 times the first equation to three times the second, and subtract 4 times the third equation from the second. Any of these methods would produce the same ultimate answer, but some of them may shorten the arithmetic steps or involve "nicer" numbers (i.e. fewer fractions, smaller multiplications, what have you). Solving a system with more equations amounts to the same general procedure: multiply the equations and add to eliminate one variable from the system and continue doing this until there are only two equations and two unknowns; then, solve for the values of those two variables and work backwards, substituting those values to solve for the values of the variables that had been eliminated. Algebra Practice Problem 1.3.2. Solve the following system of equations for (x, y, z): x + y + z = 15 2x −y + z = 8 x −2y −z = −2 Now, solve this similar system for (x, y, z): x + y + z = 15 2x −y + z = 9 x −2y −z = −2 Compare the changes in the values of x, y, and z between the two systems. Which variable changed the most? The least? What is the ratio of these changes? How large/small can you make this ratio by changing the constant on the righthand side of the second equation of the system?


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


Problem 1.3.3. A father, mother and son were sitting in a restaurant eating dinner, when they were approached by another family consisting of a father, mother and son. This second family was struck by their resemblance to the first family, so the second father asked the first, "How old are the three of you? I'm guessing we are all about the same age". The first father happened to be a mathematician and did not feel like giving away his family member's ages so easily, and thus "revealed" them to the others in a tricky way. He said, "Well, our current ages combine to make 72, and I happen to be six times as old as my son. However, in the future when I am just twice his age, our combined age will be twice our current combined age. How old do you think we are?" How old are the three family members?
### 1.3.3 Polynomnomnomials Sometimes we will need to work with variables that are squared or cubed or raised to even higher powers. In general, a polynomial is the term we use for a function that has one or more variables raised to integer powers, multiplied by coefficients, and added together. Here are some examples of polynomials: x2 −7x + 1, 7p6 + 5p4 + 3p2 + 2p,


> 🇨🇳 TODO: 待翻译


2z2 + 9y2z −2y + z3y2 −7z These types of functions are quite common and popular in mathematics, partly due to their convenient properties and partly due to their prevalence in nature. We will see them appear throughout this book. For now, though, let's focus on polynomials that only have one input variable. Roots of Polynomials Sometimes, we will define a polynomial function in the context of a puzzle and wonder whether there are any values for the input variable that make the ouput value 0. These input values are called roots of the polynomial. One way to identify roots of a polnyomial is to factor it into linear terms; that is, we try to express the function as a series of multiplications instead of additions, since we can declare that (at least) one of the factors must be 0 to achieve a 0 value. The motivation behind this technique relies on the following fact:
Fact: If a and b are real numbers and ab = 0, then a = 0 or b = 0
(or possibly both).
Example 1.3.4. Let's see a specific example. Let's try to factor the following
polynomial: p(x) = x2 + 6x + 8 (It is common notation to define polynomials as p(x), where p stands for polynomial, x is the input variable, and p(x) is the output value corresponding to the input value x. This doesn't have to be the case, though.)


> 🇨🇳 TODO: 待翻译


You might notice that p(x) = x2 + 6x + 8 = (x + 4) · (x + 2) = (x + 4)(x + 2) (It is also fairly common to drop the · when there are factors separated by parentheses, so we will adopt that convention from here on out, as well.) The reason this factorization works is because we are applying the distributive property multiple times, in reverse. If we were to expand the factorization we just found, explicitly showing every step, it would look like: p(x) = (x + 4)(x + 2) = x(x + 2) + 4(x + 2) = (x2 + 2x) + (4x + 8) = x2 + 2x + 4x + 8 = x2 + 6x + 8 All we really did to write down the factorization was to notice that the terms +4 and +2 have product +8, which is the constant term, and they have sum +6, which is the coefficient on the x term. Knowing how the subsequent expansion of those factors would work out allows us to write down that factorization without really checking it.
Factoring Quadratics
Let's take what we did with that specific example and try to generalize to any quadratic function. If we want to factor a quadratic polynomial like p(x) = x2 + bx + c we seek values r and s so that r · s = c and r + s = b. Usually, we can do this "by inspection", or by just staring at these two equations and thinking for a minute to come up with the appropriate values. (That's what we did with the last example!) What do we do if the coefficient of the x2 is not 1 but some other number a? Well, notice that if we can factor the polynomial p(x) a = x2+ b ax+ c a, then we can find a factorization of the original polynomial p(x), as well, by just multiplying by a. This won't affect our ability to find roots of the polynomial (our original goal), because we're assuming a ̸= 0 (otherwise we didn't really have a quadratic polynomial to begin with and wouldn't need to factor it). Once we've found this factorization, it's easy to identify the roots of p(x); since we want to figure out when p(x) = 0, we can just use the factorization and the fact we mentioned above to conclude that 0 = p(x) = (x + r)(x + s) implies x + r = 0 or x + s = 0 which implies x = −r or x = −s That is, the roots must be −r and −s.


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


What if we have a polynomial of the form p(x) = x2 −a2? This particular type of function is known as a difference of squares, and has a quick factorzation trick. This is a quadratic polynomial so, following the method from above, we would seek values r, s such that rs = −a2 and r + s = 0 (since there is no x term in p(x)). The second constraint tells us r = −s and using this in the first constraint tells us r2 = a2. Thus, using r = a and s = −a achieves the factorization p(x) = (x −a)(x + a) and so the roots are ±a. (Notice that using r = −a and s = a also satisfies both constraints, yet it actually yields the same factorization of p(x).) Similar tricks can sometimes be applied to polynomials of higher degree (recall that "degree" means the highest power of the input variable). For instance, the following polynomial has degree 4 p(x) = 4x4 −x2 −3 but we can factor it easily if we define y = x2 and write it as a quadratic polynomial p(y) = 4y2 −y −3 = (4y + 3)(y −1) Notice that you can think about the factorizations of the coefficients of the y2, y, and constant terms to jump right to the factorization we found, or you can follow the division trick we mentioned. Here, we would want to factor p(y)


> 🇨🇳 TODO: 待翻译


= y2 −1 4y −3 4, so we need rs = −3 4 and r + s = −1 4; using r = −1 and s = + 3 4 works, so we obtain the factorization p(x)


> 🇨🇳 TODO: 待翻译


= (y + (−1))  y + 3


> 🇨🇳 TODO: 待翻译


 which can be simplified as p(x) = 4(y −1)  y + 3


> 🇨🇳 TODO: 待翻译


 = (y −1)(4y + 3) which is exactly what we had before. A Root Yields A Factor Of course, this trick of identifying roots can work in reverse, too: if we can easily spot a root of a polynomial, that can help us in identifying one of the factors. As an example, look at the cubic polynomial below and see if you can find a root "by inspection"; that is, see if you can find an input value for x that will make p(x) evaluate to zero: p(x) = x3 −3x + 2 If you haven't spotted it yet, you might want to try plugging in some "easy values", like the first few integers (both positive and negative) to see what happens. If you do so, you'll find that p(1) = 1 −3 + 2 = 0. Accordingly, we


> 🇨🇳 TODO: 待翻译


know that a factorization of the polynomial p should include the factor (x −1), since this corresponds to the root x = 1. Knowing this, we want to divide p(x) by the factor (x −1) so that we can further factor that quotient and identify all of the roots of p. Polynomial "Division" How do we divide polynomials, though? We seek another polynomial q(x) so that p(x) = q(x) · (x −1), or in other words, we need to find p(x) x−1. One way to identify such a function is by using the same principles of long division that you learned all about in middle school when you were dividing integers. The same concepts apply to polynomial functions! Think back to how long division works, and try working through some basic examples--- like 22 ÷ 7, say---to refresh your memory about how it works. Now, let's try to apply those same principles to polynomials. Here's an example of the idea of long division applied to x3−3x+2 x−1 : x2 + x −2 x −1  x3 −3x + 2 −x3 + x2 x2 −3x −x2 + x −2x + 2 2x −2


> 🇨🇳 TODO: 待翻译


In each iteration of the method, we try to find the largest "factor" that can "go into" the larger term. In this case, these are just multiples of powers of x; we identify the largest power of x that can "go into" the current term in question. Since the dividend has x3 and the divisor has x, we write x2 above the division line. Then, we multiply (x−1) by x2, write this below the dividend, and subtract to find the remainder. We repeat the same process until we have a constant term above the division line (i.e. a multiple of x0) and see the remainder. Since the remainder here is 0, we know that we have a factorization with no remainder. We can then factor the resultant quadratic by noticing that r = 2 and s = −1 satisfy r + s = 1 and rs = −2, so we can finally write p(x) = (x −1)(x −1)(x + 2) = (x −1)2(x + 2) Accordingly, the roots of p(x) are x = 1 and x = −2. For this function, the degree of the polynomial is 3 but the function has only 2 roots. Does this strike you as odd? Can you think of a polynomial of degree 3 that has only 1 root? How about a polynomial of degree 3 with no roots? What about 4 roots, or 5 or more? Are any of these possible? Why or why not? What if we were working with a polynomial of degree 4? Of degree n? What can you say for sure about the number of roots a polynomial has, relative to its degree?


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


Expanding Factors Sometimes, when working on a puzzle, we start from a factorization of a polynomial and want to expand the factors completely so we can identify the coefficient of a particular term. How can we quickly and easily multiply polynomials together? In essence, we are trying to apply the distributive law over and over without having to write out all of the steps (although that thorough, step-bystep procedure is guaranteed to work, so if you are unsure of your answer, it is always a good idea to go back and check each step thoroughly). One particular instance where we can reduce the number of steps involved is when we need to expand a factorization like (a+b)n, where a and b represent any constant or variable and n is an integer. In this specific situation, there is a convenient way to identify the coefficients of the expanded polynomial, and those values come from Pascal's Triangle. This is an arrangement of rows of integers into a triangular shape, where each row corresponds to a particular value of n in such an expansion. The trick to generate Pascal's Triangle is to write the first two rows as all 1s, and the outside "legs" of the triangle as all 1s. In the interior of the triangle, any entry is filled in by finding the sum of the two entries immediately above that entry, to the left and to the right. Try generating the first few rows of the triangle yourself and compare to the one below to make sure you've done the procedure correctly. n = 0:


> 🇨🇳 TODO: 待翻译


We've written the n values on the left side to indicate the correspondence with the original problem of expanding (a+b)n. In general, any term of the expansion will be some coefficient (taken from the triangle) times akbn−k for some value of k between 0 and n; that is to say, in every term of the expansion, the sum of the powers of a and b in that term must be n. The numbers in any given row of the triangle are written in an order corresponding to decreasing powers of a, so that the first 1 is the coefficient of an, the next number is the coefficient of an−1b, and so on. If we were faced with expanding (a + b)2, we would read the n = 2 row of Pascal's Triangle and see that the coefficients should be 1, 2, 1, and that these are the coefficients for a2, ab, b2, respectively. Thus, (a + b)2 = a2 + 2ab + b2 which we could have also accomplished fairly easily by just expanding by hand. What if we were faced with expanding  x2 + 2 4, say? This isn't done as quickly by hand, so let's see what happens if we use Pascal's Triangle. The n = 4 row


> 🇨🇳 TODO: 待翻译


tells us the coefficients of a4, a3b, a2b2, ab3, b4 are 1, 4, 6, 4, 1, respectively, where a = x2 and b = 2. Thus, we can write  x2 + 2 4 = 1 ·  x24 + 4 ·  x23 · 2 + 6 ·  x22 · (2)2 + 4 · x2 · (2)3 + 1 · (2)4 = x8 + 4 · x6 · 2 + 6 · x4 · 4 + 4 · x2 · 8 + 16 = x8 + 8x6 + 24x4 + 32x2 + 16 Try performing this expansion step-by-step and compare, too. There are actually some very interesting properties of Pascal's Triangle that are deeply rooted in some other mathematical concepts, and these properties are particularly useful in the field of combinatorics. We will, in fact, examine many of these properties in greater detail later on! For example, you might wonder why it is the case that this procedure---adding the two entries above---yields entries that correspond to expanding factors like this. We will prove that it works when we discuss the Binomial Theorem and its related ideas! (See Section 8.4.4 if you're curious.) Completing the Square There is one more polynomial-related trick we need to mention before deriving an important result. Sometimes, it is useful to rewrite a polynomial as a squared term plus a constant term, so that we can separate the variables and constants in a convenient way. This amounts to adding and subtracting a particular term so that, overall, we have added 0 to the polynomial, but the term is chosen in a way that lets us rewrite the terms of the polynomial conveniently. This process is known as completing the square, in the sense that we add a term to create a squared factor, and complete the polynomial by subtracting a corresponding amount. Let's try this procedure with an example and then attempt to generalize. Start with the following polynomial: p(x) = x2 + 8x + 9 A factorization isn't immediately apparent here, so let's try to complete the square. We want to see a term like (x + a)2, where we know the coefficient of x is 1 since the polynomial has 1 · x2. Expanding a term like that gives x2 +2ax+a2. Since we need 8x to appear, we should use a = 4. This expansion gives x2 + 8x + 16, but we really want to see +9 as the constant term, so let's add and subtract 7 from the original polynomial: p(x) = x2 + 8x + 9 + 7 −7 = (x2 + 8x + 16) −7 = (x + 4)2 −7 Does this look familiar? Precisely, it's a difference of squares, and we know how


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


to factor that: p(x) = x2 + 8x + 9 = (x + 4)2 −7 = (x + 4)2 − √


> 🇨🇳 TODO: 待翻译


2 =  x + 4 + √


> 🇨🇳 TODO: 待翻译


 Accordingly, the roots of this polynomial are x = −4 − √ 7 and x = −4 + √ 7. Let's generalize! Suppose we start with a quadratic polynomial of the form p(x) = ax2 + bx + c and, to complete the square, we want to add and subtract a particular term. How did we find that term before? Well, the expansion of a term like (rx + s)2 yields r2x2 + 2rsx + s2, and to match these coefficients with the coefficients of the original polynomial, we see that we need r2 = a, so we should use r = √a. (Notice that this requires a ≥0, of course! What should we do if a < 0?) Then, to have 2rs = b, we need s = b 2r = b 2√a. Then, when this is expanded we have added on s2 = b2 4a, so we should subtract that from the polynomial. These steps are performed below, with some extra algebraic cleanup, of sorts, to make the terms look "nicer": p(x) = ax2 + bx + c = ax2 + bx + b2 4a + c −b2 4a = √ax + b 2√a 2 +  c −b2 4a  = √a ·  x + b 2a 2 +  c −b2 4a  = a  x + b 2a 2 +  c −b2 4a  This now tells us how to complete the square, given any quadratic polynomial! Visualizing Completing the Square Here's a helpful way to remember how to do this process. It's based on a visual representation of the areas of squares and rectangles. Let's suppose that a, b > 0 so that we can geometrically interpret ax2 + bx as the area of a rectangle. Specifically, let's take the ax2 term to be the area of a square. This means each side has length √a · x:


> 🇨🇳 TODO: 待翻译


√a · x √a · x How might we represent the bx term? We want to build this square into a larger square; this is what completing the square means. So, we should build some rectangles around this square that will help us proceed towards that goal. Let's split the area contributed by the bx term into two rectangles, each with area b 2x. Since we must have one side with length √a · x, and we want the total area to be b 2x, then we see that we need the other length to be b 2√a: √a · x √a · x b 2√a b 2√a ax2 b 2x b 2x What do we need to add to make this a square? We see that there is just a tiny square piece left to fill in the upper-right corner. Each side is length b 2√a, so its area---the term we need to add on---is b2 4a. √a · x √a · x b 2√a b 2√a ax2 b 2x b 2x b2 4a Look at that! This is the same term we produced above with our algebraic derivation. By adding that on, we were able to factor the terms as a perfect square. We just needed to make sure to subtract it off, as well, so that the net change to the original expression is zero.


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


This is a helpful trick to keep in mind. It can remind you about both the motivating process for completing the square, as well as how to achieve it. One thing you should ponder, though: Why is it that this visual representation works? We had to assume a, b > 0 to be able to draw these diagrams, so why is it that the general formula works no matter what a and b are? The Quadratic Formula Let's returning to the question of identifying the roots of a polynomial. Specifically, let's recall the quadratic formula. You may have memorized this formula as a way to "solve quadratic equations" but do you know why it actually works? Let's try to figure it out! In general, we start with a quadratic polynomial of the form p(x) = ax2 + bx + c where a ̸= 0 (otherwise, it's not actually quadratic), and we want to identify the values of x such that p(x) = 0. (Did you try to answer our questions above about how many roots this type of polynomial can have? Keep those concepts in mind throughout the following derivation.) We can't hope to factor the polynomial into linear factors too easily, so let's take advantage of the process we used above: completing the square. The benefit of that procedure is that we can set p(x) = 0 and rearrange the terms after completing the square to solve for x. Observe: 0 = p(x) = ax2 + bx + c = a  x + b 2a 2 +  c −b2 4a  simplifies to: b2 4a −c = a  x + b 2a 2 Now, we want to to start "undoing" the processes here to solve for x, and this would require taking the square root of boths sides. But what if b2 4a −c < 0? We couldn't take that square root at all! Or what if b2 4a −c = 0? Is that a problem? Do we have anything to worry about when b2 4a −c > 0? These are issues that are related to the questions we had before about the possible number of roots a polynomial can have. You may have deduced (correctly) that a quadratic polynomial can have at most two roots, but here we have uncovered the possibility (and reasons why) that a quadratic polynomial may have one or zero roots! • In the case where b2 4a −c < 0, then no value of x can possibly satisfy the last line in the derivation above. Therefore, there would be no roots of p(x) in the set of real numbers. • In the case where b2 4a −c = 0, then taking the square root of both sides of the last line above is perfectly valid, but it will produce exactly one value


> 🇨🇳 TODO: 待翻译


of x: b2 4a −c = 0 = a  x + b 2a 2 0 = x + b 2a x = −b 2a The remaining case is when b2 4a −c > 0. Here, we can expect two roots of p(x) because taking the square root of both sides introduces two possible solutions. In general, when we have a situation like s2 = t, we can say that the only possible solutions are s = √ t and s = − √ t but we must consider both (we usually write this as s = ± √ t). Solving for x in that case yields b2 4a −c = a  x + b 2a 2 ± r b2 −4ac 4a = √a  x + b 2a  = √ax + b 2√a − b 2√a ± √ b2 −4ac √ 4a = √ax −b 2a ± √ b2 −4ac √ 4a2 = x Now, we need to be careful about the square root observation we made before. In general, √ 4a2 = ±2a, but we already know that the fractional term involving that square root already has an associated ±1 factor, so this factor won't change that. Therefore, we can conclude x = −b 2a ± √ b2 −4ac 2a = −b ± √ b2 −4ac 2a Voil`a, the quadratic formula! Remember that the final steps of the derivation were carried out under the assumption that b2 4a −c > 0. Does this formula still apply when b2 4a −c = 0? Could we have performed the same steps as we did immediately above while operating under that assumption? Why or why not? Problems Problem 1.3.5. Find all possible values of a so that x−a is a factor of x2+2ax−3. Problem 1.3.6. Find all possible values of b so that x3 + b is divisible by x + b with no remainder. Problem 1.3.7. Factor xn −1 for any natural number n.


> 🇨🇳 TODO: 待翻译


1.3. REVIEW, REDO, RENEW


> 🇨🇳 TODO: 待翻译


Problem 1.3.8. Determine the value of x defined by x = s 2 + r 2 + q 2 + √ 2 + · · · Hint: try to express the infinitely-nested square roots by using x, itself. Problem 1.3.9. Use completing the square to prove that the sum of a positive number n and its reciprocal is always greater than or equal to 2, and that the only number that makes the sum equal to 2 is n = 1. Hint: take the sum, add and subtract 2, and rearrange. Problem 1.3.10. How can we find the roots of a quartic polynomial of the form ax4 + bx2 + c?
### 1.3.4 Let's Talk About Sets We've mentioned some particular types of numbers already, but we want to specifically define the sets of numbers we will be working with in the future. Each of these collections of numbers is represented by a particular letter in the blackboard bold font. The natural numbers (also known as whole numbers or counting numbers) are so-called because they feel "natural" to say as we start counting objects. We can write N = {1, 2, 3, 4, 5, . . . } (There is a more specific and technical definition that we will explain later on.) We use N to stand for "natural". Using N, we can define a related collection of numbers: the set of all integers, which combines the natural numbers, 0, and the negative natural numbers. We can write Z = {. . . , −3, −2, −1, 0, 1, 2, 3, . . . } The letter Z comes from the German word Zahlen, meaning "number". From this set, we can define the collection of rational numbers. These numbers can be represented as a ratio of integers, but they don't seem to have a natural "listing" like the sets N and Z, so we can't write this set in the way that we did above. For this, we use a very common set notation, as follows: Q = na b | a, b ∈Z and b ̸= 0 o We read this as: "The set of rational numbers is the set of all numbers of the form a b , where a and b are both integers and b is nonzero." This conveys the necessary information that a rational number is a fraction, where the numerator and denominator are integers (but the denominator can't


> 🇨🇳 TODO: 待翻译


be 0 because division by 0 is disallowed). The reason we use the letter Q for the rational numbers is because R was already reserved for the real numbers and Q was the next previous letter available. Also, Q contains all of the quotients of integers, so that makes sense, too! The real numbers R have a very technical definition that we, unfortunately, cannot delve into completely in this book. (That just goes to show how difficult it is to mathematically define that set!) For now, one way to think of the real numbers is via a number line. The real numbers are all numbers that lie on the line, while the numbers of N, Z and Q are specific numbers that lie on the line, but they don't comprise the entirety of the line. In a way, R is the "completion" of Q, in the sense of "filling in the gaps" between rational numbers.
### 1.3.5 Notation Station A popular and convenient way of writing sums and products is to use a shortened notation that collects many terms or factors into one common form. For instance, what if we wanted to talk about the sum of the first 500 natural numbers? It would be tedious to write out all 500 terms of the sum, so it is common to write something like 1 + 2 + 3 + · · · + 499 + 500. (We've already used ellipses like this, in fact. Did you understand what we meant?) This is popular and does get the point across, but some mathematicians take offense to the unnecessary use of ellipses in the middle. We put offtalking about this issue until now because it's often the case that notation can be difficult to learn and comprehend. Rather than bombard you with new symbols right away, we appealed to our intuitive understanding of what ". . . " accomplish. Now, that we've brought it up, let's see how to avoid using ellipses. To write the sum we mentioned above, we would use the following notation: 1 + 2 + 3 + · · · + 499 + 500 =


> 🇨🇳 TODO: 待翻译


X i=1 i The large sigma P comes from the Greek letter corresponding to S, for "sum", and the index i tells us to find the values of the individual terms of the sum. Writing i = 1 below and 500 above the P sign means that we let i assume all of the natural number values between 1 and 500 (inclusive). Using those values, we substitute into the general expression for the term, which is just i, in this case. Accordingly, we find that the terms are 1, 2, 3, . . . , 500, as desired. Try to find a few other ways of writing this sum by altering the expression for the general term and/or the values of the index. What if we wanted to find the sum of the first 500 even natural numbers? What about all of the even natural numbers up to (and including) 500? Try to write those sums in the notation style above. Related to this is the Q notation. If we wanted to look at the product of the first 500 natural numbers, we would follow the same conventions of identifying


> 🇨🇳 TODO: 待翻译


values for the index and the general term: 1 · 2 · 3 · · · · · 499 · 500 =


> 🇨🇳 TODO: 待翻译


Y i=1 i The large pi Q comes from the Greek letter corresponding to P, for "product". Again, try expressing this in a different way by changing the general term and/or index values. What if we wanted to find the product of the first 500 even natural numbers? What about all of the even natural numbers up to (and including) 500? Try to write those products in the notation style above. Problems Problem 1.3.11. Write an English sentence that describes what the following equation means: n X i=1 i2 = n(n + 1)(2n + 1)


> 🇨🇳 TODO: 待翻译


Problem 1.3.12. Express, in appropriate notation, the sum and product of the first n powers of 2, starting with 20 = 1. Can you prove a formula for the sum? The product? Problem 1.3.13. Consider the sum of all the odd numbers between 17 and 33 (inclusive). Write this sum in summation notation where the index starts at 0. Now try writing it where the index starts at 1. Now try writing it where the index starts at 8, and again with 9. Which of these feels "more natural"? Why?
## 1.4 Quizzical Puzzicles Let's put into action some of the principles we have discussed so far. Specifically, let's examine some interesting mathematical puzzles and explain how to go about solving them. None of these involves knowing anything beyond basic algebra and arithmetic, but this does not mean they are "basic" or "easy", since they all involve critical thinking skills and keen insight to solve and understand. Along the way, we will be employing some logical ideas we have brought up already. We might have to work with polynomial functions, or solve some equations algebraically. We might have to think careful about order and flow of our arguments, making sure everything follows from previous knowledge or deductions. Overall, we should also be thinking about what constitutes a good and valid proof of the facts we discover!
### 1.4.1 Funny Money Problem Statement This classic puzzle is contained in a story about some friends paying for a shared hotel room:


> 🇨🇳 TODO: 待翻译


