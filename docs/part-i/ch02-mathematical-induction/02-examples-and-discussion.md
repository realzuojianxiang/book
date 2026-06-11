---
title: Examples and Discussion
---

# Examples and Discussion

it is a mathematically elegant and simple explanation. Start with the 1-cube positioned as it is above and "enlarge" the 3 exposed faces by the appropriate amount, in this case by one block. This accounts for 3 of the 7 blocks, thus far: 23 = 13 + 3 + . Where are there "holes" now? The blocks we just added have created "gaps" between each pair of them, and each of those "gaps" can be filled with one block. This accounts for 3 more of the 7 total blocks: 23 = 13 + 3 + 3 + . Now what? There is just one block left to be filled, and it's the very top corner. Adding this block completes the 2-cube and tells us how to mathematically describe our construction process with the following picture and equation: 23 = 1 + 3 + 3 + 1 2-Cube into a 3-Cube Okay, we might now have a better idea of how to describe this process in general, but let's examine another case or two just to make sure we have the full idea.


> 🇨🇳 TODO: 待翻译


Let's start with a 2-cube and construct a 3-cube from it. (You can even try this out by hand if you happen to own various sizes of Rubik's Cubes!) We can follow a process similar to the steps we used in the previous case and just change the numbers appropriately. Starting with a similar picture we see that we need to "enlarge" the three exposed faces of the 2-cube but, in this case, the amount by which we need to enlarge them is different than before (with the 1-cube) since we are working with a larger initial cube. Specifically, each face must be enlarged by a 2×2 square of blocks (whereas, in the previous case, we added a 1 × 1 square of blocks). Thus, an equation to account for this addition is 33 = 23 + 3 · 22 + After we do this, we see that we need to fill in the gaps between those enlarged faces with 2 × 1 of blocks (whereas, in the previous case, we added 1 × 1 rows of blocks). An equation to account for the additions thus far is 33 = 23 + 3 · 22 + 3 · 2 +


> 🇨🇳 TODO: 待翻译


After we do this, we see that there is only the top corner left to fill in. Accordingly, we can depict our construction process and its corresponding equation: 33 = 23 + 3 · 22 + 3 · 2 + 1 n-Cube into an (n + 1)-Cube Do you see now how this process will generalize? What if we started with an n-cube? How could we construct an (n + 1)-cube? Let's follow the same steps we used in the previous two cases. First, we would enlarge the three exposed faces by adding three squares of blocks. How big is each square? Well, we want each square to be the same size as the exposed faces, so they will be n × n squares, accounting for n2 blocks for each face:


> 🇨🇳 TODO: 待翻译


(n + 1)3 = n3 + 3n2 + Next, we would fill in the gaps between these enlarged faces with rows of blocks. How long are those rows? Well, they each lie along the edges of the squares of blocks we just added, so they will each be of size n × 1, accounting for n blocks for each gap: (n + 1)3 = n3 + 3n2 + 3n + Finally, there will only be the top corner left to fill in! Therefore, (n + 1)3 = n3 + 3n2 + 3n + 1 "Wait a minute!" you might say, abruptly. "We already knew that, right?" In a way, yes; the equation above is an algebraic identity that we can also easily see by just expanding the product on the left and collecting terms: (n + 1)3 = (n + 1) · (n + 1)2 = (n + 1) · (n2 + 2n + 1) = (n3 + 2n2 + n) + (n2 + 2n + 1) = n3 + 3n2 + 3n + 1 So what have we really accomplished? Well, the main point behind deriving this identity in this geometric and visual way is that it exhibits how this identity represents some kind of inductive process. We sought to explain how to derive one "fact" (a cubic number, (n + 1)3) from a previously known "fact" (the next smallest cubic number, n3) and properly explained how to do just that. Compare this to one of the methods we used to investigate the fact that the sums of odd integers yield perfect squares, too. That observation also belies an


> 🇨🇳 TODO: 待翻译


inductive process and, although we didn't describe it as such at the time, we encourage you to think about that now. Look back at our discussion and try to write out how you could write (n + 1)2 in terms of n2 by looking at squares of blocks. Does it look anything like an "obvious" algebraic identity? (If you're feeling ambitious, think about what happens with writing (n + 1)4 in terms of n4. Is there any geometric intuition behind this? What about higher powers?) The benefit of the method we've used is that we now know how to describe cubic numbers in terms of smaller cubic numbers, all the way down to 1; that is, any time we see a cubic number in an expression, we know precisely how to write that value in terms of a smaller cubic number and some leftover terms. Furthermore, each of those expressions and leftover terms have an inherent structure to them that depends on the cubic number in question. Thus, by iteratively replacing any cubic number, like (n + 1)3, with an expression like the one we derived above, and continuing until we can't replace any more, should produce an equation that has some built in symmetry. This idea is best illustrated by actually doing it, so let's see what happens. Let's start with the expression we derived, for some arbitrary value of n, (n + 1)3 = n3 + 3n2 + 3n + 1 and then recognize that we now know a similar expression n3 = (n −1)3 + 3(n −1)2 + 3(n −1) + 1 We proved that this equation holds when we gave a general argument for the expression above for n3, since that only relied on the fact that n ≥1. We can follow the same logical steps, throughout replacing n with n −1, and end up with the second expression above, for (n −1)3. (Does this keep going, for any value of n? Think about this for a minute. Does our argument make any sense when n ≤0? Would it make physical sense to talk about, say, constructing a (−2) × (−2) × (−2) cube from a different cube?) Therefore, we can replace the n3 term in the line above (n + 1)3 =  n3 + 3n2 + 3n +


> 🇨🇳 TODO: 待翻译


+ (n −1)3 + 3(n −1)2 + 3(n −1) +


> 🇨🇳 TODO: 待翻译


This is also an algebraic identity, but it's certainly not one that we would easily think to write down just by expanding the product on the left-hand side and grouping terms. Here, we are taking advantage of the structure of our result to apply it over and over and obtain new expressions that we wouldn't have otherwise thought to write down. Let's continue with this substitution process and see where it takes us! Next, we replace (n −1)3 with the corresponding expression and find (n + 1)3 = 3n2 + 3n +


> 🇨🇳 TODO: 待翻译


 (n −1)3 + 3(n −1)2 + 3(n −1) +


> 🇨🇳 TODO: 待翻译


+ (n −2)3 + 3(n −2)2 + 3(n −2) +


> 🇨🇳 TODO: 待翻译


Perhaps you see where this is going? We can do this subsitution process over and over, and the columns that we've arranged above will continue to grow, showing us that there is something deep and mathematically symmetric going on here. But where does this process stop? We want to write down a concise version of this iterative process and be able to explain all of the terms that arise, so we need to know where it ends. Remember the very first step in our investigation of the cubic numbers? We figured out how to write 23 = 13 + 3 + 3 + 1. Since this was our first step in building this inductive process, it should be the last step we apply when building backwards, as we are now. Accordingly, we can write (n + 1)3 = 3n2 + 3n +


> 🇨🇳 TODO: 待翻译


+ 3(n −1)2 + 3(n −1) +


> 🇨🇳 TODO: 待翻译


+ 3(n −2)2 + 3(n −2) +


> 🇨🇳 TODO: 待翻译


+ 3(n −3)2 + 3(n −3) +


> 🇨🇳 TODO: 待翻译


... + ... + ... + 3 · 22 + 3 · 2 +


> 🇨🇳 TODO: 待翻译


+ 3 · 12 + 3 · 1 +


> 🇨🇳 TODO: 待翻译


This is definitely an identity we wouldn't have come up with offthe top of our heads! In addition to being relatively pretty-looking on the page like this, it also allows us to apply some of our previous knowledge and simplify the expression. To see how we can do that, let's apply summation notation to the columns above and collect a bunch of terms into some simple expressions: (n + 1)3 = 13 + 3 · n X k=1 k2 + 3 · n X k=1 k + n X k=1


> 🇨🇳 TODO: 待翻译


In the last chapter, we saw a couple of different proofs that told us n X k=1 k = n(n + 1)


> 🇨🇳 TODO: 待翻译


Let's use that fact in the line above, and also simplify the term on the far right, to write (n + 1)3 = 1 + 3 · n X k=1 k2 + 3n(n + 1)


> 🇨🇳 TODO: 待翻译


+ n What does this tell us? What have we accomplished after all this algebraic manipulation? Well, we previously proved a result about the sum of the first n natural numbers, so a natural question to ask after that is: What is the sum of the first n natural numbers squared? How could we begin to answer that? That's a trick question, because we already have! Let's do one or two more algebraic steps with the equation above by isolating the summation term and


> 🇨🇳 TODO: 待翻译


then dividing: (n + 1)3 −1 −n −3n(n + 1)


> 🇨🇳 TODO: 待翻译


= 3 · n X k=1 k2


> 🇨🇳 TODO: 待翻译


3(n + 1)3 −1 3(n + 1) −n(n + 1)


> 🇨🇳 TODO: 待翻译


= n X k=1 k2 This is what we've accomplished: we've derived a formula for the sum of the first n square natural numbers! Of course, the expression on the left in the line above isn't particularly nice looking and we could perform some further simplification, and we will leave it to you to verify that this yields the expression below: n X k=1 k2 = 1 6n(n + 1)(2n + 1) "And so on" is not rigorous! There are a couple of "morals" that we'd like to point out, based on all of this work. The first moral is that generalizing an argument is a good method for discovering new and interesting mathematical ideas and results. Did you think about how this puzzle is related to the sums of odd natural numbers? If not, we encourage you strongly to try that now, as well as think about generalizing this even further to four or five dimensional "cubes" and so on. In addition to giving you some other interesting results, it will also be incredibly instructive for learning to think abstractly and apply inductive processes. The second moral is more like an admission: we have not technically proven the formula above for the sum of the first n square natural numbers. It seems like our derivation is valid and tells us the "correct answer" but there is a glaring issue: ellipses! In expanding the equation for (n + 1)3 and obtaining those columns of terms that we collected into particular sums, writing ... in the middle of those columns was helpful in guiding our intuition, but this is not a mathematically rigorous technique. How do we know that all of the terms in the middle are exactly what we'd expect them to be? How can we be so sure that all of our pictures of cubes translate perfectly into the mathematical expressions we wrote down? What do we really mean by "and keep going all the way down to 1"? As an example, consider this: 1, 2, 3, 4, . . . , 100 What is that list of numbers? You probably interpreted it as "all the natural numbers between 1 and 100, inclusive". That seems reasonable. But what if we actually meant this list? 1, 2, 3, 4, 7, 10, 11, 12, 14, . . . , 100 Why, of course, we meant the list of natural numbers from 1 to 100 that don't have an "i" in their English spelling! Wasn't it obvious?


> 🇨🇳 TODO: 待翻译


The point is this: when talking with a friend, and verbalizing some ideas, it might be okay to write "1, 2, 3, . . . , 100" and ensure that whoever is listening knows exactly what you mean. In general, though, we can't assume that a reader would just naturally intuit whatever we were trying to convey; we should be as explicit and rigorous as possible. It may seem to you now like we're nit-picking, but the larger point is that there is a mathematical way of making this argument more precise, so that it constitutes a completely valid proof. Everything we have done so far is useful in guiding our intuition, but we will have to do a little more work to be sure our arguments are completely convincing. There are a few other concepts required to make this type of argument rigorous, in general, and we will investigate those in the next chapter and return to this subject immediately after that. However, in the meantime, let's examine one more example to practice this intuitive argument style and recognizing when induction is an applicable technique.
### 2.2.2 Lines On The Plane Take a clean sheet of paper and a pen and a ruler. How many regions are on your sheet? Just one, right? Draw a line all the way across the paper. Now there are two regions. Draw another straight line that intersects your first line. How many regions are there? You should count four in total. Draw a third line that intersects both of the first two, but not at the point where the first two intersect. (That is, there should be three intersection points, in total.) How many regions are there? Can you predict the answer before counting? What happens when there are 4 lines? Or 5? Or 100? How do we approach this puzzle and, ultimately, solve it? Let's give a more formal statement to be sure we're thinking the same way: Consider n lines on an infinite plane (two-dimensional surface) such that no two lines are parallel and no more than two lines intersect at one point. How many distinct regions do the lines create? We can draw a few examples by hand when n is small (up to, say, n = 5 is reasonable), and let's use this to guide our intuition into making a general argument for an arbitrary value of n. (Notice that this strategy is very similar to what we did in the previous puzzle: identify a pattern with small cases, identify the relevant components of those cases that can generalize, then abstract to an aribtrary case.) Specifically, we want to attempt to identify how the number of regions in one drawing depends on the number of regions in a drawing with fewer lines. What happens when we draw a new line? Can we determine how this changes the already existing regions? Can we somehow count how many regions this creates? Do some investigation of this puzzle on your own before reading on. If you figure out some results, compare your work to the steps we follow below. Let's start with a small case, say n = 2. We know one line divides a plane into 2 regions; what happens when we add a second line? We know we get 4 regions, because we can just look and count them:


> 🇨🇳 TODO: 待翻译


However, we are only looking at one specific case of two intersecting lines. How do we know that we will always find four regions, no matter how we draw those two lines appropriately? That is, can we describe how this happens in a way that somehow incorporates the fact that the number of liens is n = 2? Think about it! Here's our approach. Notice that each of the already existing regions is split into two when we add a second line, and that this is true no matter how you choose to draw the lines; as long as we make sure the two lines aren't parallel, they will always behave this way. That is, if we take one line that splits the plane into two regions,


> 🇨🇳 TODO: 待翻译


then adding a new line will split each of those existing regions in two. This adds two new regions to the whole plane, giving four regions in total:


> 🇨🇳 TODO: 待翻译


Region 2 split Region 1 split What about when n = 3? In this case, we want to think about adding a third line to a diagram with two lines and four regions. We want to make an argument that doesn't depend on a particular arrangement of the lines, so eventually the only facts we should use are that no lines are parallel and any point of intersection only lies on two lines (not three or more). For now, though,


> 🇨🇳 TODO: 待翻译


it helps to look at a particular arrangement of lines so that we are talking about the same diagram; we can use our observations of this specific diagram to guide our general argument. Let's start with a two-line diagram, on the left below, and add a third line, but let's choose the third line so that all of the intersection points are "nearby" or within the scope of the diagram, so that we don't have to rescale the picture:


> 🇨🇳 TODO: 待翻译


Region 1 split Region 2 split Region 3 split


> 🇨🇳 TODO: 待翻译


We certainly have 7 regions now, but we made the third line a separate color so that we can identify where the "new" regions appear: one region (the lower quadrant, Region 4) remains unchanged, but the three other regions are split in two and each of those "splits" adds 1 to our count (where there was 1 region, now there are 2). What if we had placed the line differently? Region 1 split Region 2 split Region 4 split


> 🇨🇳 TODO: 待翻译


The same phenomenon occurs, where one quadrant remains untouched but the other three are split in two. (How do we know there aren't any other regions not depicted within the scale of our diagram? This is not as easy a question to answer as you might think at first blush, and it's worth thinking about.) Experiment with other arrangements of the three lines and try to convince yourself that this always happens; also, think about why this is the case and how we could explain that this must happen. Before giving a general explanation, though, let's examine another small case. When n = 4, we start with three lines and 7 regions and add a fourth line that is not parallel to any of the existing lines and doesn't pass through any existing intersection points. Again, we will want to make an argument that isn't tied to a specific arrangement of the lines, but looking at the following specific diagram will help guide our intuition into making that argument:


> 🇨🇳 TODO: 待翻译


Notice that three of the original regions remain unchanged (Regions 3 and 5 and 7), and the other four are split in two. Do you notice a pattern here? It seems like for every n we've examined, adding the n-th line leaves exactly n−1 regions unchanged while the rest are split in two. Let's try to explain why this happens. Remember that we're trying to identify how many regions appear when we draw n lines, so let's assign that value a "name" so we can refer to it; let's say R(n) represents the number of regions created by drawing n lines on the plane so that no two lines are parallel and no intersection point belongs to more than two lines. In these examples we've considered for small values of n, we've looked at what changes when we add a new line; that is, we've figured out what R(n) is by already knowing R(n −1). Let's try to adapt our observations so that they apply to any arbitrary value of n. Assume that we know R(n) already. (Why can we do this? Do we know any particular value of R(n) for sure, for some specific n? Which? How?) Say we have an arbitrary diagram of n lines on the plane that satisfy the two conditions given in the puzzle statement above. How many regions do these lines create? Yes, exactly R(n). Now, what happens when we add the (n + 1)-th line? What can we say for sure about this line and how it alters the diagram? Well, the only information we really have is that (a) this new line is not parallel to any of the existing n lines and (b) this new line does not intersect any of the already existing intersection points. Now, condition (a) tells us that this new line must intersect all of the exisiting n lines; parallel lines don't intersect, and non-parallel lines must intersect somewhere. Thus, we must create n new intersection points on the diagram. Can any of those intersection points coincide with any existing intersection points? No! This is precisely what condition (b) tells us. These two pieces of information together tell us that, no matter how we draw this new line, as long as it satisfies the requirements of the puzzle, we must be able to identify n "special" points along that line. Those special points are precisely the points where the new line intersects an existing line. We'd now like to take these special points and use them to identify new regions in the diagram. Look back to the cases we examined above: identify the new intersection points and see if you can associate them with new regions. Perhaps it would help to label those intersections with a large dot and mark the new regions with an X to make them all stand out. We'll show you one example below, where n = 4. What do you notice? Can you use these dots to


> 🇨🇳 TODO: 待翻译


help identify how many new regions are created with the addition of that n-th line? Think about this for a minute and then read on. Exactly! Between any two of the new intersection points, we have a line segment that splits a region in two! All that remains is to identify how many new such segments we've created. Since each one corresponds to exactly one existing region split in two, this will tell us exactly how many new regions we've created. We've already figured out that this (n + 1)-th line creates n new intersection points. Think about how these points are arranged on the line. Any two "consecutive" points create a segment, but the extreme points also create infinite segments (that coninue past those extreme points forever). How many are there in total? Exactly n + 1. (Look at the diagram above, for n = 3. We see that there are 3 new intersection points and 4 new segments, with two of them being infinite rays.) This means there are n + 1 line segments that split regions in two, so we have created exactly n + 1 new regions! This allows us to say that R(n + 1) = R(n) + n + 1 Phew, what an observation! It took a bit of playing around with examples and making some geometric arguments, but here we are. We've identified some inductive structure to this puzzle; we've found how one case depends on another one. That is, we've found how R(n+1) depends on R(n). This hasn't completely solved the puzzle, but we are now much closer. All that remains is to replace R(n) with a similar expression, and continually do this until we reach a value we know, R(1) = 2. Observe: R(n + 1) =  R(n) + n + 1 =  R(n −1) + n + n + 1 =  R(n −2) + (n −1) + n + n + 1 ... =  R(2) + 3 + · · · + n + n + 1 = R(1) + 2 +


> 🇨🇳 TODO: 待翻译


+ · · · + n + n + 1 Since we know R(1) = 2, we can say R(n + 1) = 2 + (2 + 3 + · · · + n + (n + 1)) = 2 + n+1 X k=1 k ! −1 = 1 + n+1 X k=1 k


> 🇨🇳 TODO: 待翻译


and this is a sum we have investigated before! (Also notice that we had to subract 1 because of the missing first term of the sum in parentheses.) Recall that Pn k=1 k = n(n+1)


> 🇨🇳 TODO: 待翻译


, and to represent the sum we have in the equation above, we just replace n with n + 1. Therefore, R(n + 1) = 1 + (n + 1)(n + 2)


> 🇨🇳 TODO: 待翻译


One final simplification we would like to make is to replace n+1 with n throughout the equation, because it makes more sense to have an expression for R(n) (For what values of n is this valid?) R(n) = 1 + n(n + 1)


> 🇨🇳 TODO: 待翻译


Finally, we have arrived at an answer to the originally-posed puzzle! In so doing, we employed an inductive technique: we explained how one "fact", namely the value of R(n + 1), depends on the value of a "previous fact", namely R(n), and used these iterative dependencies to work backwards until we reached a particular, known value, namely R(1). We want to point out, again, that the derivation we followed and the observations we made in this section have guided our intuition into an answer, but this has not rigorously proven anything. The issue is with the "· · · ", which is not a concrete, "officially" mathematical way of capturing the inductive process underlying our technique. Furthermore, our method with the "lines in the plane" problem had us starting with a diagram of n −1 lines and building a new diagram with n lines; is this okay? Why does this actually tell us anything about an arbitrary diagram of n lines? Do all such diagrams come from a smaller diagram with one fewer line? We will, in the next two chapters, learn the necessary tools to fully describe a rigorous way of doing what we have done so far, and in the chapter after that, we will employ those tools to make mathematical induction officially rigorous. For now, though, we want to give a heuristic definition of induction and continue to examine interesting puzzles and observations that rely on inductive techniques. Practicing with these types of puzzles--learning when to recognize an inductive process, how to work with it, how to use that structure to solve a problem, and so on--will be extremely helpful in the future, and we have no need to delve into technical mathematical detail. (At least, not just yet!)
### 2.2.3 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 TODO: 待翻译


(1) What properties characterize an inductive process? (2) How did we prove that n X k=1 k = n(n + 1)


> 🇨🇳 TODO: 待翻译


is correct? How was our method inductive? (Reread Section 1.4.2 if you forget!) (3) Why can we take the sum formula mentioned in the previous question and "replace" n with n+1 and know that it still holds true? Can we also replace n with n −1? (4) Work through the algebraic steps to obtain our final expression for the sum of the first n squares; that is, verify that


> 🇨🇳 TODO: 待翻译


3(n + 1)3 −1 3(n + 1) −n(n + 1)


> 🇨🇳 TODO: 待翻译


= 1 6n(n + 1)(2n + 1) (5) Try to recall the argument that adding the (n + 1)-th line on the plane created exactly n + 1 new regions. Can you work through the argument for a friend and convince him/her that it is valid? (6) To find the sum of the first n squares, why couldn't we just square the formula for the sum of the first n numbers? Why is that wrong? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Draw 5 lines on the plane (that satisfy the two conditions of the puzzle) and verify that there are 16 regions. Can you also verify that 6 lines yield 22 regions? (2) Come up with another description of a sequence that goes 1, 2, 3, 4, . . . , 100 that is not simply all of the numbers from 1 to 100. (Recall the example we gave: all the numbers from 1 to 100 with no "i" in their English spelling.) (3) Come up with an algebraic expression that relates (n + 1)4 to n4, like we did with cubes. (Challenge: Can you come up with a geometric interpretation for the expression you just derived?) (4) Challenge: Let's bump the "lines in the plane" puzzle up one dimension! Think about having n planes in three-dimensional space. How many regions are created? Assume that no two planes are parallel, and no three of them intersect in one line. (Think about how these two conditions are directly analogous to the specified conditions for the "lines" puzzle.)


> 🇨🇳 TODO: 待翻译


## 2.3 Defining Induction To properly motivate the forthcoming definition of mathematical induction as a proof technique, we want to emphasize that the above examples used some intuitive notions of the structure of the puzzle to develop a "solution", where we use quotation marks around solution to indicate that we haven't officially proven it yet. In that sense, we ask the following question: What if we had been given the formula that we derived and asked to verify it? What if we had not gone through any intuitive steps to derive the formula and someone just told us that it is correct? How could we check their claim? The reason we ask this is because we are really facing that situation now, except the person telling us the formula is . . . the very same intuitive argument we discovered above! Pretend you have a skeptical friend who says, "Hey, I heard about this formula for the sum of the first n natural numbers squared. Somebody told me that they add up to 1 6n(n+1)(2n+1). I checked the first two natural numbers, and it worked, so it's gotta be right. Pass it on!" Being a logical thinker, but also a good friend, you nod along and say, "I did hear that, but let's make sure it's correct for every number." How would you proceed? Your friend is right that the first few values "work out" nicely: 12 = 1 = 1 6(1)(2)(3) 12 + 22 = 5 = 1 6(2)(3)(5) 12 + 22 + 32 = 14 = 1 6(3)(4)(7) 12 + 22 + 32 + 42 = 30 = 1 6(4)(5)(9) and so on. We could even check, by hand, a large value of n, if we wanted to: 12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385 = 1 6(10)(11)(21) Remember, though, that this formula is claimed to be valid for any value of n. Checking individual results by hand would take forever, because there are an infinite number of natural numbers. No matter how many individual values of n we check, there will always be larger values, and how do we know that the formula doesn't break down for some large value? We need a far more efficient procedure, mathematically and temporally speaking, to somehow verify the formula for all values of n in just a few steps. We have an idea in mind, of course (it's the upcoming rigorous version of mathematical induction), and here we will explain how the procedure works, in a broad sense.
### 2.3.1 The Domino Analogy Pretend that we have a set of dominoes. This is a special set of dominoes because we have an infinite number of them (!) and we can imagine anything we want


> 🇨🇳 TODO: 待翻译


