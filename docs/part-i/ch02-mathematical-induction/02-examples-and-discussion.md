---
title: Examples and Discussion
---

# Examples and Discussion

it is a mathematically elegant and simple explanation. Start with the 1-cube positioned as it is above and "enlarge" the 3 exposed faces by the appropriate amount, in this case by one block. This accounts for 3 of the 7 blocks, thus far: 23 = 13 + 3 +. Where are there "holes" now? The blocks we just added have created "gaps" between each pair of them, and each of those "gaps" can be filled with one block. This accounts for 3 more of the 7 total blocks: 23 = 13 + 3 + 3 +. Now what? There is just one block left to be filled, and it's the very top corner. Adding this block completes the 2-cube and tells us how to mathematically describe our construction process with the following picture and equation: 23 = 1 + 3 + 3 + 1 2-Cube into a 3-Cube Okay, we might now have a better idea of how to describe this process in general, but let's examine another case or two just to make sure we have the full idea.


> 🇨🇳 这是一个数学上优雅而简洁的解释。从一个1阶立方体开始，将其3个暴露面"扩大"适当的量——在本例中即一个方块。这到目前为止占了7个方块中的3个：$2^3 = 1^3 + 3 + \ldots$。现在"洞"在哪里？我们刚加的方块在每对之间创建了"间隙"，每个间隙都可以用一个方块来填充。这占了7个总方块中的另外3个：$2^3 = 1^3 + 3 + 3 + \ldots$。现在呢？只剩下一个方块要填充，就是最上面的角。加上这个方块就完成了2阶立方体的构建，对应的等式为：$2^3 = 1 + 3 + 3 + 1$。**从2阶立方体构建3阶立方体** 好了，我们现在可能对如何一般性地描述这个过程有了更好的想法，但让我们再考察一两个案例以确保完全理解。


Let's start with a 2-cube and construct a 3-cube from it. (You can even try this out by hand if you happen to own various sizes of Rubik's Cubes!) We can follow a process similar to the steps we used in the previous case and just change the numbers appropriately. Starting with a similar picture we see that we need to "enlarge" the three exposed faces of the 2-cube but, in this case, the amount by which we need to enlarge them is different than before (with the 1-cube) since we are working with a larger initial cube. Specifically, each face must be enlarged by a 2 $	imes$ 2 square of blocks (whereas, in the previous case, we added a 1 	imes 1 square of blocks). Thus, an equation to account for this addition is 33 = 23 + 3 \cdot 22 + After we do this, we see that we need to fill in the gaps between those enlarged faces with 2 	imes 1 of blocks (whereas, in the previous case, we added 1 	imes 1 rows of blocks). An equation to account for the additions thus far is 33 = 23 + 3 \cdot 22 + 3 $\cdot$ 2 +


> 🇨🇳 让我们从一个2阶立方体出发，从中构建一个3阶立方体。（如果你碰巧拥有各种尺寸的魔方，甚至可以亲手试试！）我们可以遵循与前一种情况类似的步骤，只需适当更改数字。从类似的图示开始，我们看到需要"扩大"2阶立方体的三个暴露面，但在本例中，扩大的量与之前（1阶立方体）不同，因为我们的初始立方体更大。具体来说，每个面需要扩大一个 $2 \times 2$ 的方块阵列（而之前加了 1 \times 1 的方块）。因此，记录这一增加的等式为 $3^3 = 2^3 + 3 \cdot 2^2 + \ldots$。完成之后，我们看到需要用 2 \times 1 的行来填充那些扩大面之间的间隙。至此的等式为 $3^3 = 2^3 + 3 \cdot 2^2 + 3 \cdot 2 + \ldots$。


After we do this, we see that there is only the top corner left to fill in. Accordingly, we can depict our construction process and its corresponding equation: 33 = 23 + 3 $\cdot 22 + 3 \cdot$ 2 + 1 n-Cube into an (n + 1)-Cube Do you see now how this process will generalize? What if we started with an n-cube? How could we construct an (n + 1)-cube? Let's follow the same steps we used in the previous two cases. First, we would enlarge the three exposed faces by adding three squares of blocks. How big is each square? Well, we want each square to be the same size as the exposed faces, so they will be n $	imes$ n squares, accounting for n2 blocks for each face:


> 🇨🇳 完成之后，只剩最上面的角需要填充。因此，我们可以描绘构建过程及其对应等式：$3^3 = 2^3 + 3 \cdot 2^2 + 3 \cdot 2 + 1$。**从n阶立方体到(n+1)阶立方体** 你看到这个过程如何一般化了吗？如果我们从一个n阶立方体出发呢？如何构建一个(n+1)阶立方体？让我们遵循与前两种情况相同的步骤。首先，我们需要扩大三个暴露面，添加三个方块阵列。每个阵列有多大？我们希望每个阵列与暴露面同大，因此它们是 n \times n 的阵列，每个面占 $n^2$ 个方块：$(n+1)^3 = n^3 + 3n^2 + \ldots$。


(n + 1)3 = n3 + 3n2 + Next, we would fill in the gaps between these enlarged faces with rows of blocks. How long are those rows? Well, they each lie along the edges of the squares of blocks we just added, so they will each be of size n $	imes$ 1, accounting for n blocks for each gap: (n + 1)3 = n3 + 3n2 + 3n + Finally, there will only be the top corner left to fill in! Therefore, (n + 1)3 = n3 + 3n2 + 3n + 1 "Wait a minute!" you might say, abruptly. "We already knew that, right?" In a way, yes; the equation above is an algebraic identity that we can also easily see by just expanding the product on the left and collecting terms: (n + 1)3 = (n + 1) \cdot (n + 1)2 = (n + 1) $\cdot$ (n2 + 2n + 1) = (n3 + 2n2 + n) + (n2 + 2n + 1) = n3 + 3n2 + 3n + 1 So what have we really accomplished? Well, the main point behind deriving this identity in this geometric and visual way is that it exhibits how this identity represents some kind of inductive process. We sought to explain how to derive one "fact" (a cubic number, (n + 1)3) from a previously known "fact" (the next smallest cubic number, n3) and properly explained how to do just that. Compare this to one of the methods we used to investigate the fact that the sums of odd integers yield perfect squares, too. That observation also belies an


> 🇨🇳 接下来，我们用行的方块来填充这些扩大面之间的间隙。这些行有多长？它们沿着我们刚加的方块阵列的边排列，因此每行的大小为 $n \times 1$，每个间隙占 $n$ 个方块：$(n+1)^3 = n^3 + 3n^2 + 3n + \ldots$。最后，只剩最上面的角要填充！因此，$(n+1)^3 = n^3 + 3n^2 + 3n + 1$。

>
> "等等！"你可能会突然说，"我们不是已经知道这个了吗？"某种程度上是的；上面的等式是一个代数恒等式，我们也可以通过展开左边的乘积并合并同类项来轻松验证。那么我们究竟获得了什么？以这种几何和可视化的方式推导恒等式的主要意义在于，它展示了这个恒等式代表某种归纳过程。我们试图解释如何从一个已知的"事实"（较小的立方数 $n^3$）推导出另一个"事实"（立方数 $(n+1)^3$），并正确地解释了如何做到这一点。

>
> 这也与奇数之和得到完全平方数的观察类似——那也隐含着一个归纳过程。回顾我们的讨论，试着写出如何通过方块阵列从 $n^2$ 得到 $(n+1)^2$。它看起来像不像一个"显然的"代数恒等式？（如果你有雄心，想想 $(n+1)^4$ 用 $n^4$ 表示会怎样。这背后有没有几何直觉？更高次幂呢？）


inductive process and, although we didn't describe it as such at the time, we encourage you to think about that now. Look back at our discussion and try to write out how you could write (n + 1)2 in terms of n2 by looking at squares of blocks. Does it look anything like an "obvious" algebraic identity? (If you're feeling ambitious, think about what happens with writing (n + 1)4 in terms of n4. Is there any geometric intuition behind this? What about higher powers?) The benefit of the method we've used is that we now know how to describe cubic numbers in terms of smaller cubic numbers, all the way down to 1; that is, any time we see a cubic number in an expression, we know precisely how to write that value in terms of a smaller cubic number and some leftover terms. Furthermore, each of those expressions and leftover terms have an inherent structure to them that depends on the cubic number in question. Thus, by iteratively replacing any cubic number, like (n + 1)3, with an expression like the one we derived above, and continuing until we can't replace any more, should produce an equation that has some built in symmetry. This idea is best illustrated by actually doing it, so let's see what happens. Let's start with the expression we derived, for some arbitrary value of n, (n + 1)3 = n3 + 3n2 + 3n + 1 and then recognize that we now know a similar expression n3 = (n -1)3 + 3(n -1)2 + 3(n -1) + 1 We proved that this equation holds when we gave a general argument for the expression above for n3, since that only relied on the fact that n $\geq$1. We can follow the same logical steps, throughout replacing n with n -1, and end up with the second expression above, for (n -1)3. (Does this keep going, for any value of n? Think about this for a minute. Does our argument make any sense when n \leq0? Would it make physical sense to talk about, say, constructing a (-2) 	imes (-2) $	imes$ (-2) cube from a different cube?) Therefore, we can replace the n3 term in the line above (n + 1)3 = (( n3 + 3n2 + 3n +


> 🇨🇳 这种方法的好处在于，我们现在知道如何用更小的立方数来描述立方数，一直到1。每当我们在表达式中看到一个立方数，就能精确地用更小的立方数和剩余项来表示它。此外，这些表达式和剩余项都有取决于所涉立方数的固有结构。因此，通过迭代替换任何立方数（如 $(n+1)^3$），不断用我们推导的表达式代入，直到无法替换为止，应该会产生一个具有内在对称性的等式。

>
> 让我们从推导的表达式开始，对于某个任意的 $n$ 值：$(n+1)^3 = n^3 + 3n^2 + 3n + 1$，然后注意到我们同样知道：$n^3 = (n-1)^3 + 3(n-1)^2 + 3(n-1) + 1$。由于上面的论证仅依赖于 n \geq 1，将 n 替换为 n-1 就得到关于 $(n-1)^3$ 的第二个表达式。（这对任何 n 值都成立吗？当 n \leq 0 时，论证还有意义吗？构造一个 $(-2) \times (-2) \times (-2)$ 的立方体有物理意义吗？）因此，我们可以替换上面等式中的 $n^3$ 项：$(n+1)^3 = n^3 + 3n^2 + 3n + 1 = (n-1)^3 + 3(n-1)^2 + 3(n-1) + 1 + 3n^2 + 3n + 1$。


+ (n -1)3 + 3(n -1)2 + 3(n -1) +


> 🇨🇳 这也是一个代数恒等式，但它绝不是仅通过展开左边乘积并合并项就能轻易想到写出的。在这里，我们利用结果的结构反复应用它，得到了本不会想到的新表达式。让我们继续这个代入过程，看看会走向何方！


This is also an algebraic identity, but it's certainly not one that we would easily think to write down just by expanding the product on the left-hand side and grouping terms. Here, we are taking advantage of the structure of our result to apply it over and over and obtain new expressions that we wouldn't have otherwise thought to write down. Let's continue with this substitution process and see where it takes us! Next, we replace (n -1)3 with the corresponding expression and find (n + 1)3 = 3n2 + 3n +

 (n -1)3 + 3(n -1)2 + 3(n -1) +


> 🇨🇳 下一步，我们将 $(n-1)^3$ 替换为对应的表达式，得到：$(n+1)^3 = 3n^2 + 3n + 1 + 3(n-1)^2 + 3(n-1) + 1 + (n-2)^3 + 3(n-2)^2 + 3(n-2) + 1$。


+ (n -2)3 + 3(n -2)2 + 3(n -2) +


> 🇨🇳 也许你已经看出规律了？我们可以反复执行这个代入过程，上面排列的各列会不断增长，表明这里有某种深层且具有数学对称性的东西。但这个过程在哪里停止？我们需要写下这个迭代过程的简洁版本，并能够解释出现的所有项，所以我们需要知道它在哪里结束。还记得我们对立方数调查的第一步吗？我们弄清了如何写出 $2^3 = 1^3 + 3 + 3 + 1$。既然这是建立此归纳过程的第一步，它应该是我们现在反向构建时应用的最后一步。因此，我们可以写出：


Perhaps you see where this is going? We can do this subsitution process over and over, and the columns that we've arranged above will continue to grow, showing us that there is something deep and mathematically symmetric going on here. But where does this process stop? We want to write down a concise version of this iterative process and be able to explain all of the terms that arise, so we need to know where it ends. Remember the very first step in our investigation of the cubic numbers? We figured out how to write 23 = 13 + 3 + 3 + 1. Since this was our first step in building this inductive process, it should be the last step we apply when building backwards, as we are now. Accordingly, we can write (n + 1)3 = 3n2 + 3n +


> 🇨🇳 也许你已看出方向？我们可以反复执行这个代入过程。但我们还需要知道它何时终止。回想我们调查的第一步：$2^3 = 1^3 + 3 + 3 + 1$。既然这是归纳过程的起点，反向构建时应是最后一步。


+ 3(n -1)2 + 3(n -1) +


> 🇨🇳 $+ 3(n-1)^2 + 3(n-1) + 1$


+ 3(n -2)2 + 3(n -2) +


> 🇨🇳 $+ 3(n-2)^2 + 3(n-2) + 1$


+ 3(n -3)2 + 3(n -3) +


> 🇨🇳 $+ 3(n-3)^2 + 3(n-3) + 1$


... +... +... + 3 $\cdot 22 + 3 \cdot$ 2 +


> 🇨🇳 $\ldots + \ldots + \ldots + 3 \cdot 2^2 + 3 \cdot 2 + 1$


+ 3 $\cdot 12 + 3 \cdot$ 1 +


> 🇨🇳 $+ 3 \cdot 1^2 + 3 \cdot 1 + 1$


This is definitely an identity we wouldn't have come up with offthe top of our heads! In addition to being relatively pretty-looking on the page like this, it also allows us to apply some of our previous knowledge and simplify the expression. To see how we can do that, let's apply summation notation to the columns above and collect a bunch of terms into some simple expressions: (n + 1)3 = 13 + 3 $\cdot$ n X k=1 k2 + 3 $\cdot$ n X k=1 k + n X k=1


> 🇨🇳 这绝对是一个我们凭空想不出来的恒等式！除了在页面上看起来相当美观之外，它还让我们能够应用已有知识来简化表达式。为此，我们将求和符号应用于上面的各列，将许多项合并为简洁的表达式：$(n+1)^3 = 1^3 + 3 \cdot \sum_{k=1}^{n} k^2 + 3 \cdot \sum_{k=1}^{n} k + \sum_{k=1}^{n} 1$。


In the last chapter, we saw a couple of different proofs that told us n X k=1 k = n(n + 1)


> 🇨🇳 在上一章中，我们看到了几种不同的证明告诉我们 $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$。


Let's use that fact in the line above, and also simplify the term on the far right, to write (n + 1)3 = 1 + 3 $\cdot$ n X k=1 k2 + 3n(n + 1)


> 🇨🇳 将这个事实代入上面的等式，并简化最右边的项，得到：$(n+1)^3 = 1 + 3 \cdot \sum_{k=1}^{n} k^2 + \frac{3n(n+1)}{2} + n$。


+ n What does this tell us? What have we accomplished after all this algebraic manipulation? Well, we previously proved a result about the sum of the first n natural numbers, so a natural question to ask after that is: What is the sum of the first n natural numbers squared? How could we begin to answer that? That's a trick question, because we already have! Let's do one or two more algebraic steps with the equation above by isolating the summation term and


> 🇨🇳 $+ n$。这告诉了我们什么？经过所有这些代数运算，我们得到了什么？之前我们证明了前 n 个自然数之和的结果，那么自然的问题是：前 $n$ 个自然数的平方和是多少？我们该如何回答？这是一个巧妙的问题，因为我们已经有了答案！让我们再做一些代数步骤，将求和项单独提取出来——


then dividing: (n + 1)3 -1 -n -3n(n + 1)


> 🇨🇳 然后作除法：$(n+1)^3 - 1 - n - \frac{3n(n+1)}{2}$


= 3 $\cdot$ n X k=1 k2


> 🇨🇳 $= 3 \cdot \sum_{k=1}^{n} k^2$


3(n + 1)3 -1 3(n + 1) -n(n + 1)


> 🇨🇳 $\frac{3(n+1)^3 - 1}{3(n+1)} - n(n+1)$ 整理后得到：$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$


= n X k=1 k2 This is what we've accomplished: we've derived a formula for the sum of the first n square natural numbers! Of course, the expression on the left in the line above isn't particularly nice looking and we could perform some further simplification, and we will leave it to you to verify that this yields the expression below: n X k=1 k2 = 1 6n(n + 1)(2n + 1) "And so on" is not rigorous! There are a couple of "morals" that we'd like to point out, based on all of this work. The first moral is that generalizing an argument is a good method for discovering new and interesting mathematical ideas and results. Did you think about how this puzzle is related to the sums of odd natural numbers? If not, we encourage you strongly to try that now, as well as think about generalizing this even further to four or five dimensional "cubes" and so on. In addition to giving you some other interesting results, it will also be incredibly instructive for learning to think abstractly and apply inductive processes. The second moral is more like an admission: we have not technically proven the formula above for the sum of the first n square natural numbers. It seems like our derivation is valid and tells us the "correct answer" but there is a glaring issue: ellipses! In expanding the equation for (n + 1)3 and obtaining those columns of terms that we collected into particular sums, writing... in the middle of those columns was helpful in guiding our intuition, but this is not a mathematically rigorous technique. How do we know that all of the terms in the middle are exactly what we'd expect them to be? How can we be so sure that all of our pictures of cubes translate perfectly into the mathematical expressions we wrote down? What do we really mean by "and keep going all the way down to 1"? As an example, consider this: 1, 2, 3, 4,..., 100 What is that list of numbers? You probably interpreted it as "all the natural numbers between 1 and 100, inclusive". That seems reasonable. But what if we actually meant this list? 1, 2, 3, 4, 7, 10, 11, 12, 14,..., 100 Why, of course, we meant the list of natural numbers from 1 to 100 that don't have an "i" in their English spelling! Wasn't it obvious?


> 🇨🇳 "以此类推"不够严谨！基于以上所有工作，我们想指出几点"寓意"。第一点是，推广论证是发现新而有趣的数学思想和结果的好方法。你是否想过这个谜题与奇数自然数之和的关系？如果没有，我们强烈建议你现在尝试，并思考将其进一步推广到四维或五维"立方体"等。第二点更像是一种承认：我们并没有从技术上证明前 $n$ 个自然数平方和的公式。我们的推导似乎有效且给出了"正确答案"，但有一个明显的问题：省略号！在展开 $(n+1)^3$ 的等式并得到我们收集为特定求和的那些列时，在列中间写"..."有助于引导直觉，但这不是数学上严谨的技巧。我们如何知道中间的所有项恰好如我们所期望的？我们怎么能如此确定立方体的图片完美地转化为我们写下的数学表达式？我们说"一直向下到1"到底是什么意思？举个例子：$1, 2, 3, 4, \ldots, 100$——这个数列是什么？你可能把它解释为"1到100之间的所有自然数"。这似乎合理。但如果我们实际上指的是：$1, 2, 3, 4, 7, 10, 11, 12, 14, \ldots, 100$——即1到100中英文拼法不含字母"i"的自然数！不是很明显吗？


The point is this: when talking with a friend, and verbalizing some ideas, it might be okay to write "1, 2, 3,..., 100" and ensure that whoever is listening knows exactly what you mean. In general, though, we can't assume that a reader would just naturally intuit whatever we were trying to convey; we should be as explicit and rigorous as possible. It may seem to you now like we're nit-picking, but the larger point is that there is a mathematical way of making this argument more precise, so that it constitutes a completely valid proof. Everything we have done so far is useful in guiding our intuition, but we will have to do a little more work to be sure our arguments are completely convincing. There are a few other concepts required to make this type of argument rigorous, in general, and we will investigate those in the next chapter and return to this subject immediately after that. However, in the meantime, let's examine one more example to practice this intuitive argument style and recognizing when induction is an applicable technique.
### 2.2.2 Lines On The Plane Take a clean sheet of paper and a pen and a ruler. How many regions are on your sheet? Just one, right? Draw a line all the way across the paper. Now there are two regions. Draw another straight line that intersects your first line. How many regions are there? You should count four in total. Draw a third line that intersects both of the first two, but not at the point where the first two intersect. (That is, there should be three intersection points, in total.) How many regions are there? Can you predict the answer before counting? What happens when there are 4 lines? Or 5? Or 100? How do we approach this puzzle and, ultimately, solve it? Let's give a more formal statement to be sure we're thinking the same way: Consider n lines on an infinite plane (two-dimensional surface) such that no two lines are parallel and no more than two lines intersect at one point. How many distinct regions do the lines create? We can draw a few examples by hand when n is small (up to, say, n = 5 is reasonable), and let's use this to guide our intuition into making a general argument for an arbitrary value of n. (Notice that this strategy is very similar to what we did in the previous puzzle: identify a pattern with small cases, identify the relevant components of those cases that can generalize, then abstract to an aribtrary case.) Specifically, we want to attempt to identify how the number of regions in one drawing depends on the number of regions in a drawing with fewer lines. What happens when we draw a new line? Can we determine how this changes the already existing regions? Can we somehow count how many regions this creates? Do some investigation of this puzzle on your own before reading on. If you figure out some results, compare your work to the steps we follow below. Let's start with a small case, say n = 2. We know one line divides a plane into 2 regions; what happens when we add a second line? We know we get 4 regions, because we can just look and count them:


> 🇨🇳 关键在于：和朋友交谈、口头表达想法时，写"1, 2, 3,..., 100"并确保听者理解你的意思可能没问题。但一般来说，我们不能假设读者会自然而然地理解我们要传达的内容；我们应该尽可能明确和严谨。现在这看起来可能像吹毛求疵，但更大的意义在于：有一种数学方法可以让这种论证更精确，从而构成完全有效的证明。我们目前所做的一切有助于引导直觉，但要做完全令人信服的论证还需要额外的工作。这将在下一章研究并紧接着回到这个主题。不过，现在让我们再考察一个例子来练习这种直觉论证风格，并识别何时归纳法是适用的技巧。

> **2.2.2 平面上的直线** 拿一张白纸、一支笔和一把尺子。纸上有几个区域？只有一个，对吧？画一条横穿纸面的线，现在有两个区域。再画一条与第一条相交的直线。有几个区域？你应该数出4个。画第三条与前两条都相交、但不通过前两条交点的直线。有几个区域？在数之前你能预测答案吗？4条线时呢？5条？100条？我们该如何解决这个谜题？让我们给出更正式的陈述：考虑无限平面上的 $n$ 条直线，其中没有两条平行，也没有三条以上交于一点。这些直线创建了多少个不同的区域？当 $n$ 较小时我们可以手动画几个例子，用此引导直觉做出一般性论证。具体来说，我们想尝试确定一幅画中的区域数如何依赖于较少直线的画中的区域数。


However, we are only looking at one specific case of two intersecting lines. How do we know that we will always find four regions, no matter how we draw those two lines appropriately? That is, can we describe how this happens in a way that somehow incorporates the fact that the number of liens is n = 2? Think about it! Here's our approach. Notice that each of the already existing regions is split into two when we add a second line, and that this is true no matter how you choose to draw the lines; as long as we make sure the two lines aren't parallel, they will always behave this way. That is, if we take one line that splits the plane into two regions,


> 🇨🇳 然而，我们只是在看两条相交直线的一个具体情况。我们如何确定无论怎样画都能得到4个区域？能否以一种某种方式融合"线数 $n = 2$"的方式来描述这个过程？我们的方法是：注意到当我们添加第二条直线时，每个已有区域都被分成两半，且无论你怎样画线这都是正确的——只要两条线不平行，它们就会总是如此。即，如果我们取一条将平面分成两个区域的直线——


then adding a new line will split each of those existing regions in two. This adds two new regions to the whole plane, giving four regions in total:


> 🇨🇳 那么添加新线会将每个已有区域分成两半。这给整个平面新增了两个区域，总共得到四个区域。


Region 2 split Region 1 split What about when n = 3? In this case, we want to think about adding a third line to a diagram with two lines and four regions. We want to make an argument that doesn't depend on a particular arrangement of the lines, so eventually the only facts we should use are that no lines are parallel and any point of intersection only lies on two lines (not three or more). For now, though,


> 🇨🇳 区域2被分割、区域1被分割。$n = 3$ 的情况呢？这时，我们想在有两条线和四个区域的图上添加第三条线。我们希望做出不依赖于特定线排列的论证，因此最终我们只用到的条件是：没有线平行、每个交点只属于两条线。不过眼下——


it helps to look at a particular arrangement of lines so that we are talking about the same diagram; we can use our observations of this specific diagram to guide our general argument. Let's start with a two-line diagram, on the left below, and add a third line, but let's choose the third line so that all of the intersection points are "nearby" or within the scope of the diagram, so that we don't have to rescale the picture:


> 🇨🇳 看一个特定的线排列有助于我们讨论同一幅图；我们可以利用对具体图的观察来引导一般性论证。让我们从两条线的图出发（下面左图），添加第三条线，并选择使所有交点都在图的"附近"或范围内。


Region 1 split Region 2 split Region 3 split


> 🇨🇳 区域1被分割、区域2被分割、区域3被分割。


We certainly have 7 regions now, but we made the third line a separate color so that we can identify where the "new" regions appear: one region (the lower quadrant, Region 4) remains unchanged, but the three other regions are split in two and each of those "splits" adds 1 to our count (where there was 1 region, now there are 2). What if we had placed the line differently? Region 1 split Region 2 split Region 4 split


> 🇨🇳 我们现在确实有7个区域。我们用不同颜色画了第三条线，以便识别"新"区域出现在哪里：一个区域（下象限，区域4）保持不变，但另外三个区域各被分成两半，每次"分割"使计数加1。如果线的位置不同呢？同样的现象发生：一个象限保持不变，其他三个被分成两半。


The same phenomenon occurs, where one quadrant remains untouched but the other three are split in two. (How do we know there aren't any other regions not depicted within the scale of our diagram? This is not as easy a question to answer as you might think at first blush, and it's worth thinking about.) Experiment with other arrangements of the three lines and try to convince yourself that this always happens; also, think about why this is the case and how we could explain that this must happen. Before giving a general explanation, though, let's examine another small case. When n = 4, we start with three lines and 7 regions and add a fourth line that is not parallel to any of the existing lines and doesn't pass through any existing intersection points. Again, we will want to make an argument that isn't tied to a specific arrangement of the lines, but looking at the following specific diagram will help guide our intuition into making that argument:


> 🇨🇳 同样的现象出现：一个象限未受影响，其他三个被分成两半。（我们怎么确定图的范围内没有其他未显示的区域？这个问题初看不难，实则值得深思。）试试三条线的其他排列方式，让自己确信这总是成立的；同时想想为什么会这样，以及如何解释这必然发生。在进行一般性解释之前，让我们看看另一个小案例。当 $n = 4$ 时，我们从三条线和7个区域开始，添加不平行于任何现有线且不通过任何已有交点的第四条线。


Notice that three of the original regions remain unchanged (Regions 3 and 5 and 7), and the other four are split in two. Do you notice a pattern here? It seems like for every n we've examined, adding the $n$-th line leaves exactly n-1 regions unchanged while the rest are split in two. Let's try to explain why this happens. Remember that we're trying to identify how many regions appear when we draw n lines, so let's assign that value a "name" so we can refer to it; let's say R(n) represents the number of regions created by drawing n lines on the plane so that no two lines are parallel and no intersection point belongs to more than two lines. In these examples we've considered for small values of n, we've looked at what changes when we add a new line; that is, we've figured out what R(n) is by already knowing R(n -1). Let's try to adapt our observations so that they apply to any arbitrary value of n. Assume that we know R(n) already. (Why can we do this? Do we know any particular value of R(n) for sure, for some specific n? Which? How?) Say we have an arbitrary diagram of n lines on the plane that satisfy the two conditions given in the puzzle statement above. How many regions do these lines create? Yes, exactly R(n). Now, what happens when we add the (n + 1)-th line? What can we say for sure about this line and how it alters the diagram? Well, the only information we really have is that (a) this new line is not parallel to any of the existing n lines and (b) this new line does not intersect any of the already existing intersection points. Now, condition (a) tells us that this new line must intersect all of the exisiting n lines; parallel lines don't intersect, and non-parallel lines must intersect somewhere. Thus, we must create n new intersection points on the diagram. Can any of those intersection points coincide with any existing intersection points? No! This is precisely what condition (b) tells us. These two pieces of information together tell us that, no matter how we draw this new line, as long as it satisfies the requirements of the puzzle, we must be able to identify n "special" points along that line. Those special points are precisely the points where the new line intersects an existing line. We'd now like to take these special points and use them to identify new regions in the diagram. Look back to the cases we examined above: identify the new intersection points and see if you can associate them with new regions. Perhaps it would help to label those intersections with a large dot and mark the new regions with an X to make them all stand out. We'll show you one example below, where n = 4. What do you notice? Can you use these dots to


> 🇨🇳 注意到三个原有区域保持不变（区域3、5和7），其他四个被分成两半。你注意到规律了吗？对于我们检查的每个 $n$，添加第 $n$ 条线时恰好留下 $n-1$ 个区域不变，其余的被分成两半。让我们尝试解释为什么会这样。设 R(n) 表示满足条件的 n 条线在平面上创建的区域数。在我们考虑的小 n 值的例子中，我们观察了添加新线时的变化——即利用已知的 R(n-1) 来确定 R(n)。现在，当我们添加第 (n+1) 条线时能说什么？条件(a)告诉我们新线必须与所有现有的 n 条线相交——平行线不相交，非平行线必相交。因此产生了 n 个新交点。这些交点会不会与已有交点重合？不会！这恰好是条件(b)告诉我们的。因此，不管新线怎样画，只要满足条件，我们就能在新线上识别 $n$ 个"特殊"点——就是新线与已有线的交点。


help identify how many new regions are created with the addition of that $n$-th line? Think about this for a minute and then read on. Exactly! Between any two of the new intersection points, we have a line segment that splits a region in two! All that remains is to identify how many new such segments we've created. Since each one corresponds to exactly one existing region split in two, this will tell us exactly how many new regions we've created. We've already figured out that this (n + 1)-th line creates n new intersection points. Think about how these points are arranged on the line. Any two "consecutive" points create a segment, but the extreme points also create infinite segments (that coninue past those extreme points forever). How many are there in total? Exactly n + 1. (Look at the diagram above, for n = 3. We see that there are 3 new intersection points and 4 new segments, with two of them being infinite rays.) This means there are n + 1 line segments that split regions in two, so we have created exactly n + 1 new regions! This allows us to say that R(n + 1) = R(n) + n + 1 Phew, what an observation! It took a bit of playing around with examples and making some geometric arguments, but here we are. We've identified some inductive structure to this puzzle; we've found how one case depends on another one. That is, we've found how R(n+1) depends on R(n). This hasn't completely solved the puzzle, but we are now much closer. All that remains is to replace R(n) with a similar expression, and continually do this until we reach a value we know, R(1) = 2. Observe: R(n + 1) = R(n) + n + 1 = R(n -1) + n + n + 1 = R(n -2) + (n -1) + n + n + 1... = R(2) + 3 + \cdot \cdot $\cdot$ + n + n + 1 = R(1) + 2 +


> 🇨🇳 正是这样！任意两个新交点之间有一段线段将一个区域分成两半！我们已确定新线产生了 $n$ 个新交点。考虑这些点在线上的排列方式。任意两个"相邻"点形成一段线段，而两端的超出的点还形成无限射线段。总共有多少段？恰好 n+1 段。这意味着恰好有 n+1 条线段将区域分成两半，因此恰好创建了 n+1 个新区域！于是 $R(n+1) = R(n) + n + 1$。这是一个了不起的观察！通过在例子中摸索并做几何论证，我们找到了这个谜题的归纳结构：R(n+1) 如何依赖于 R(n)。剩下的就是不断替换 R(n) 直到已知值 R(1) = 2：$R(n+1) = R(n) + n + 1 = R(n-1) + (n-1) + n + 1 = \cdots = R(1) + 2 + 3 + \cdots + n + (n+1)$


+ $\cdot \cdot \cdot$ + n + n + 1 Since we know R(1) = 2, we can say R(n + 1) = 2 + (2 + 3 + \cdot \cdot $\cdot$ + n + (n + 1)) = 2 + n+1 X k=1 k ! -1 = 1 + n+1 X k=1 k


> 🇨🇳 因为 $R(1) = 2$，可得 $R(n+1) = 2 + (2 + 3 + \cdots + n + (n+1)) = 2 + \sum_{k=1}^{n+1} k - 1 = 1 + \sum_{k=1}^{n+1} k$


and this is a sum we have investigated before! (Also notice that we had to subract 1 because of the missing first term of the sum in parentheses.) Recall that Pn k=1 k = n(n+1)


> 🇨🇳 这正是我们之前研究过的求和！（注意我们减去了1，因为括号中的求和缺少首项。）回忆 $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$


, and to represent the sum we have in the equation above, we just replace n with n + 1. Therefore, R(n + 1) = 1 + (n + 1)(n + 2)


> 🇨🇳 ，要用上面的等式中的求和表示，只需将 $n$ 替换为 $n+1$。因此，$R(n+1) = 1 + \frac{(n+1)(n+2)}{2}$。


One final simplification we would like to make is to replace n+1 with n throughout the equation, because it makes more sense to have an expression for R(n) (For what values of n is this valid?) R(n) = 1 + n(n + 1)


> 🇨🇳 最后一个化简：将等式中的 $n+1$ 替换为 $n$，因为直接给出 $R(n)$ 的表达式更自然。（这对哪些 n 值成立？）$R(n) = 1 + \frac{n(n+1)}{2}$


Finally, we have arrived at an answer to the originally-posed puzzle! In so doing, we employed an inductive technique: we explained how one "fact", namely the value of R(n + 1), depends on the value of a "previous fact", namely R(n), and used these iterative dependencies to work backwards until we reached a particular, known value, namely R(1). We want to point out, again, that the derivation we followed and the observations we made in this section have guided our intuition into an answer, but this has not rigorously proven anything. The issue is with the " $\cdot \cdot \cdot$ ", which is not a concrete, "officially" mathematical way of capturing the inductive process underlying our technique. Furthermore, our method with the "lines in the plane" problem had us starting with a diagram of n -1 lines and building a new diagram with n lines; is this okay? Why does this actually tell us anything about an arbitrary diagram of n lines? Do all such diagrams come from a smaller diagram with one fewer line? We will, in the next two chapters, learn the necessary tools to fully describe a rigorous way of doing what we have done so far, and in the chapter after that, we will employ those tools to make mathematical induction officially rigorous. For now, though, we want to give a heuristic definition of induction and continue to examine interesting puzzles and observations that rely on inductive techniques. Practicing with these types of puzzles--learning when to recognize an inductive process, how to work with it, how to use that structure to solve a problem, and so on--will be extremely helpful in the future, and we have no need to delve into technical mathematical detail. (At least, not just yet!)
### 2.2.3 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 最终我们得到了谜题的答案！在此过程中，我们使用了归纳技巧：解释了一个"事实"（$R(n+1)$ 的值）如何依赖于"前一个事实"（R(n)），并利用这些迭代依赖关系反向工作直到已知值 $R(1)$。再次强调：我们的推导引导直觉得到了答案，但没有严格证明任何东西。问题在于省略号——它不是捕捉底层归纳过程的严谨数学方式。我们将在接下来的两章中学习使这种论证形式严谨化的工具，然后在下一章中用这些工具使数学归纳法正式严谨化。现在，让我们给出归纳法的启发式定义，并继续考察依赖归纳技巧的有趣谜题。

> **2.2.3 问题与练习** 自我提醒：简要回答以下问题。这些都是基于你刚读到的内容，所以如果不能回忆某个定义或概念，请回去重读。


(1) What properties characterize an inductive process? (2) How did we prove that n X k=1 k = n(n + 1)


> 🇨🇳 (1) 什么性质表征了一个归纳过程？(2) 我们如何证明 $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$？


is correct? How was our method inductive? (Reread Section 1.4.2 if you forget!) (3) Why can we take the sum formula mentioned in the previous question and "replace" n with n+1 and know that it still holds true? Can we also replace n with n -1? (4) Work through the algebraic steps to obtain our final expression for the sum of the first n squares; that is, verify that


> 🇨🇳 是正确的？我们的方法为何是归纳的？（如果忘了请重读1.4.2节！）(3) 为什么我们可以将求和公式中的 $n$ "替换"为 $n+1$ 并知道它仍然成立？也可以将 $n$ 替换为 $n-1$ 吗？(4) 请逐步验证代数步骤以得到前 $n$ 个平方和的最终表达式，即验证


3(n + 1)3 -1 3(n + 1) -n(n + 1)


> 🇨🇳 $\frac{3(n+1)^3 - 1}{3(n+1)} - n(n+1)$


= 1 6n(n + 1)(2n + 1) (5) Try to recall the argument that adding the (n + 1)-th line on the plane created exactly n + 1 new regions. Can you work through the argument for a friend and convince him/her that it is valid? (6) To find the sum of the first n squares, why couldn't we just square the formula for the sum of the first n numbers? Why is that wrong? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Draw 5 lines on the plane (that satisfy the two conditions of the puzzle) and verify that there are 16 regions. Can you also verify that 6 lines yield 22 regions? (2) Come up with another description of a sequence that goes 1, 2, 3, 4,..., 100 that is not simply all of the numbers from 1 to 100. (Recall the example we gave: all the numbers from 1 to 100 with no "i" in their English spelling.) (3) Come up with an algebraic expression that relates (n + 1)4 to n4, like we did with cubes. (Challenge: Can you come up with a geometric interpretation for the expression you just derived?) (4) Challenge: Let's bump the "lines in the plane" puzzle up one dimension! Think about having n planes in three-dimensional space. How many regions are created? Assume that no two planes are parallel, and no three of them intersect in one line. (Think about how these two conditions are directly analogous to the specified conditions for the "lines" puzzle.)


> 🇨🇳 $= \frac{n(n+1)(2n+1)}{6}$ (5) 回忆添加第 $(n+1)$ 条线恰好创建 $n+1$ 个新区域的论证。你能向朋友解释并让他/她相信它是有效的吗？(6) 要求前 n 个平方和，为什么不能直接对前 $n$ 个数之和的公式取平方？为什么那是错误的？

> **动手试试** (1) 在平面上画5条线（满足谜题的两个条件），验证有16个区域。你能验证6条线产生22个区域吗？(2) 构造一个形如 $1, 2, 3, 4, \ldots, 100$ 但并非简单列出1到100所有数的序列描述。(3) 找出将 $(n+1)^4$ 与 $n^4$ 关联的代数表达式，如同我们对立方体所做的那样。（挑战：能给出几何解释吗？）(4) 挑战：将"平面上的直线"谜题提升一维！考虑三维空间中的 $n$ 个平面。创建了多少个区域？假设没有两个平面平行，也没有三个平面交于一线。


## 2.3 Defining Induction To properly motivate the forthcoming definition of mathematical induction as a proof technique, we want to emphasize that the above examples used some intuitive notions of the structure of the puzzle to develop a "solution", where we use quotation marks around solution to indicate that we haven't officially proven it yet. In that sense, we ask the following question: What if we had been given the formula that we derived and asked to verify it? What if we had not gone through any intuitive steps to derive the formula and someone just told us that it is correct? How could we check their claim? The reason we ask this is because we are really facing that situation now, except the person telling us the formula is... the very same intuitive argument we discovered above! Pretend you have a skeptical friend who says, "Hey, I heard about this formula for the sum of the first n natural numbers squared. Somebody told me that they add up to 1 6n(n+1)(2n+1). I checked the first two natural numbers, and it worked, so it's gotta be right. Pass it on!" Being a logical thinker, but also a good friend, you nod along and say, "I did hear that, but let's make sure it's correct for every number." How would you proceed? Your friend is right that the first few values "work out" nicely: 12 = 1 = 1 6(1)(2)(3) 12 + 22 = 5 = 1 6(2)(3)(5) 12 + 22 + 32 = 14 = 1 6(3)(4)(7) 12 + 22 + 32 + 42 = 30 = 1 6(4)(5)(9) and so on. We could even check, by hand, a large value of n, if we wanted to: 12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385 = 1 6(10)(11)(21) Remember, though, that this formula is claimed to be valid for any value of n. Checking individual results by hand would take forever, because there are an infinite number of natural numbers. No matter how many individual values of n we check, there will always be larger values, and how do we know that the formula doesn't break down for some large value? We need a far more efficient procedure, mathematically and temporally speaking, to somehow verify the formula for all values of n in just a few steps. We have an idea in mind, of course (it's the upcoming rigorous version of mathematical induction), and here we will explain how the procedure works, in a broad sense.
### 2.3.1 The Domino Analogy Pretend that we have a set of dominoes. This is a special set of dominoes because we have an infinite number of them (!) and we can imagine anything we want


> 🇨🇳 **2.3 定义归纳法** 为了适当地引出即将给出的数学归纳法定义，我们要强调，上面的例子使用了对谜题结构的直觉概念来发展"解"——我们用引号是因为还没有正式证明它。从这个角度看，我们面临的问题是：如果有人给了我们推导出的公式并要求验证呢？如果有人直接告诉我们公式是正确的呢？我们如何验证他们的说法？

> 假装你有一个持怀疑态度的朋友说："嘿，我听说了一个前 $n$ 个自然数平方和的公式，加起来等于 $\frac{n(n+1)(2n+1)}{6}$。我验证了前两个自然数，算对了，所以它一定是对的。传播开去吧！"作为一个既讲逻辑又是好朋友的人，你说："我确实听说了，但让我们确保它对每个数都正确。"你该怎么验证？

> 记住，这个公式据称对任何 $n$ 值成立。逐个手工验证会永无止境，因为自然数有无限个。无论我们检查多少个 n 值，总有更大的值，我们怎么知道公式不会在某个大值处失效？我们需要一种远更高效的程序，以仅几步验证公式对所有 $n$ 值成立。

> **2.3.1 多米诺骨牌类比** 假设我们有一组多米诺骨牌。这是一组特殊的骨牌，因为我们有无限多个！我们可以想象任何我们想要的排列方式……
