---
title: Defining Induction
tags:
  - 数学归纳法
  - 归纳原理
---

# Defining Induction

written on them, instead of the standard array of dots. Let's also pretend that they are set up in an infinite line along an infinite tabletop, and we are viewing the dominos from the side and we can see a label under each one so that we know where we are in the line: n = 1 n = 2 n = 3 n = 4 n = 5 For this particular example, to verify the formula n X k=1 k2 = 1 6n(n + 1)(2n + 1) we will imagine a particular "fact" written on each domino. Specifically, we will imagine that the 1st domino has the expression


> 🇨🇳 我们设想多米诺骨牌上写有"事实"而非标准点数。假设它们在无限长的桌面上排成一行，我们从侧面观看，每块骨牌下方有标签标明序号：$n=1 n=2 n=3 n=4 n=5$。对于这个特例，为验证公式 $\sum_{k=1}^{n} k^2 = \frac{1}{6}n(n+1)(2n+1)$，我们在每块骨牌上写一个"事实"。具体来说，第 1 块骨牌上写着


X k=1 k2 = 1 6(1)(2)(3) written on it, and the 2nd domino has the expression


> 🇨🇳 $\sum_{k=1}^{1} k^2 = \frac{1}{6}(1)(2)(3)$，第 2 块骨牌上写着


X k=1 k2 = 1 6(2)(3)(5) written on it. In general, we imagine that the $n$-th domino in the infinite line has the following "fact" written on it: n X k=1 k2 = 1 6n(n + 1)(2n + 1) Since we're dealing with dominos that are meant to fall into each other and knock each other over, let's pretend that whenever a domino falls, that means the corresponding "fact" written on it is a true statement. This is how we will relate our physical interpretation of the dominos to the mathematical interpretation of the validity of the formula we derived. We did check the sum for n = 1 by hand: 12 = 1 6(1)(2)(3). Thus, the fact written on the first domino is a true statement, so we know that the first domino will, indeed, fall over. We also checked the sum for n = 2 by hand, so we know that the second domino will fall over:


> 🇨🇳 $\sum_{k=1}^{2} k^2 = \frac{1}{6}(2)(3)(5)$。一般地，第 $n$ 块骨牌上写：$\sum_{k=1}^{n} k^2 = \frac{1}{6}n(n+1)(2n+1)$。骨牌倒下意味着其上的"事实"为真。我们验证了 n=1：$1^2 = \frac{1}{6}(1)(2)(3)$，所以第 1 块骨牌确实会倒下。我们也验证了 $n=2$，所以第 2 块骨牌也会倒下：


n = 1 n = 2 n = 3 n = 4 n = 5 However, continuing like this brings us back to the same problem as before: we don't want to check every individual domino to make sure it falls. We would really like to encapsulate our physical notion of the line of dominos---namely, that when a domino falls it will topple into the next one and knock that over, and so on---and somehow relate the "facts" that are written on adjacent dominos. Let's look at this situation for the first two dominos. Knowing that Domino 1 falls, can we guarantee that Domino 2 falls without rewriting all of the terms of the sum? How are the statements written on the two dominos related? Each statement is a sum of squared natural numbers, and the one on the second domino has exactly one more term. Thus, knowing already that Domino 1 has fallen, we can use the true statement written on Domino 1 to verify the truth of the statement written on Domino 2:


> 🇨🇳 然而逐个检查每块骨牌又回到了之前的问题。我们真正想做的是将骨牌倒下推倒下一块的物理直觉数学化——将相邻骨牌上"事实"的推导关系形式化。来看前两块骨牌：已知骨牌 1 倒下，能否不重新求和就保证骨牌 2 倒下？两块骨牌上的陈述有何联系？每条陈述都是自然数平方和，第 2 块骨牌上恰好多一项。因此，已知骨牌 1 倒下，我们可以利用骨牌 1 上的真命题来验证骨牌 2 上的命题：


X k=1 k2 = 12 + 22 = 1 + 22 = 5 = 1 6(2)(3)(5) Now, this may seem a little silly because the only "work" we have saved is not having to "do the arithmetic" to write 12 = 1. Let's use this procedure on a case with larger numbers so we can more convincingly illustrate the benefit of this method. Let's assume that Domino 10 has fallen. (In case you are worried about this assumption, we wrote the full sum a few paragraphs ago and you can verify it there.) This means we know that


> 🇨🇳 这似乎有点简单——我们只省略了计算 $1^2 = 1$ 的"运算"。让我们用更大的数来说明方法的优势。假设骨牌 10 已倒下（你可以在前面找到完整和验证），这意味着我们知道


X k=1 k2 = 1 6(10)(11)(21) = 385 is a true statement. Let's use this to verify the statement written on Domino 11, which is


> 🇨🇳 $\sum_{k=1}^{10} k^2 = \frac{1}{6}(10)(11)(21) = 385$ 是真命题。用此验证骨牌 11 上的命题：


X k=1 k2 = 1 6(11)(12)(23) The sum written on Domino 11 has 11 terms, and the first 10 are exactly the sum written on Domino 10! Since we know something about that sum, let's just separate that 11th term from the sum and apply our knowledge of the other


> 🇨🇳 $\sum_{k=1}^{11} k^2 = \frac{1}{6}(11)(12)(23)$。骨牌 11 上的和有 11 项，前 10 项恰好就是骨牌 10 上的和！既然我们已知该和的信息，将第 11 项分离出来并利用已知：


X k=1 k2 = {12 + 22 + $\cdot \cdot \cdot$ + 102} + 112 = 10 X k=1 k2 ! + 112 = 385 + 121 = 506 = 1 63036 = 1 6(11)(12)(23) Look at all of the effort we saved! Why bother reading the first 10 terms of the sum if we know something about them already? Now, imagine if we could do this procedure for all values of n, simultaneously! That is, imagine that we could prove that any time Domino n falls, we are guaranteed that Domino (n + 1) falls. What would this tell us? Well, think about the infinite line of dominos again. We know Domino 1 will fall, because we checked that value by hand. Then, because we verified the "Domino n knocks over Domino (n + 1)" step for all values of n, we know Domino 1 will fall into Domino 2, which in turn falls into Domino 3, which in turns falls into Domino 4, which... The entire line of dominos will fall! In essence, we could collapse the whole line of dominos falling down into just two steps: (a) Make sure the first domino topples; (b) Make sure every domino knocks over the one immediately after it in line. With only these two steps, we can guarantee every domino falls and, therefore, prove that all of the facts written on them are true. This will prove that the formula we derived is valid for every natural number n. We have already accomplished step (a), so now we have to complete step (b). We have done this for specific cases in the previous paragraphs (Domino 1 topples Domino 2, and Domino 10 topples Domino 11), so let's try to follow along with the steps of those cases and generalize to an arbitrary value of n. We assume, for some specific but arbitrary value of n, that Domino n falls, which tells us that the equation n X k=1 k2 = 1 6n(n + 1)(2n + 1) is a true statement. Now, we want to relate this to the statement written on Domino (n + 1) and apply the knowledge given in the equation above. Let's do what we did before and write a sum of n + 1 terms as a sum of n terms plus the last term: n+1 X k=1 k2 = 12 + 22 + $\cdot$ $\cdot$ $\cdot$ + n2 + (n + 1)2 = n X k=1 k2 ! + (n + 1)2


> 🇨🇳 省了好大力气！既然已知前 10 项，何必重新加一遍呢？如果我们对所有 $n$ 的值都能做同样的操作——即证明一旦骨牌 n 倒下，骨牌 n+1 也必然倒下——那会怎样？回头看那条无限的骨牌线：我们知道骨牌 1 会倒，因为手算验证了；然后，因为验证了所有 n 的"骨牌 n 推倒骨牌 n+1"步骤，骨牌 1 倒\to推倒骨牌 2\to推倒骨牌 3\to……整条骨牌线都会倒！本质上，只需两步：(a) 确保第一块骨牌倒下；(b) 确保每块骨牌都能推倒紧邻的下一块。仅这两步就能保证每块骨牌倒下，从而证明骨牌上的所有命题为真。步骤 (a) 已完成，接下来完成步骤 (b)。前面已对特例完成（骨牌 1 推倒骨牌 2，骨牌 10 推倒骨牌 11），现在推广到任意 n。对某个特定但任意的 n，假设骨牌 n 倒下，即方程 $\sum_{k=1}^{n} k^2 = \frac{1}{6}n(n+1)(2n+1)$ 是真命题。将其与骨牌 n+1 上的命题关联，像之前一样将 n+1 项的和写成 $n$ 项的和加上最后一项：


Next, we can apply our assumption that Domino n has fallen (which tells us that the fact written on it is true) and write n+1 X k=1 k2 = 1 6n(n + 1)(2n + 1) + (n + 1)2 Is this the same as the fact written on Domino (n + 1)? Let's look at what that is, first, and then compare. The "fact" on Domino (n + 1) is similar to the fact on Domino n, except everywhere we see "n" we replace it with "n + 1": n+1 X k=1 k2 = 1 6(n + 1)((n + 1) + 1)(2(n + 1) + 1) = 1 6(n + 1)(n + 2)(2n + 3) It is not clear yet whether the expression we have derived thus far is actually equal to this. We could attempt to simplify the expression we've derived and factor it to make it "look like" this new expression, but it might be easier to just expand both expressions and compare all the terms. (This is motivated by the general idea that expanding a factored polynomial is far easier than recognizing a polynomial can be factored.) For the first expression, we get


> 🇨🇳 接下来利用骨牌 $n$ 倒下这一假设（即其上的命题为真），写出 $\sum_{k=1}^{n+1} k^2 = \frac{1}{6}n(n+1)(2n+1) + (n+1)^2$。这与骨牌 $n+1$ 上的命题相同吗？先看骨牌 $n+1$ 上的命题——将 $n$ 替换为 $n+1$：$\sum_{k=1}^{n+1} k^2 = \frac{1}{6}(n+1)((n+1)+1)(2(n+1)+1) = \frac{1}{6}(n+1)(n+2)(2n+3)$。目前尚不清楚推导出的表达式是否与此相等。展开比较（因展开因式比识别因式容易）：


6n(n + 1)(2n + 1) + (n + 1)2 = 1 6n(2n2 + 3n + 1) + (n2 + 2n + 1) = 1 3n3 + 1 2n2 + 1 6n + n2 + 2n + 1 = 1 3n3 + 3 2n2 + 13 6 n + 1 and for the second expression, we get


> 🇨🇳 第一个表达式展开：$\frac{1}{6}n(n+1)(2n+1) + (n+1)^2 = \frac{1}{6}n(2n^2+3n+1) + (n^2+2n+1) = \frac{1}{3}n^3 + \frac{1}{2}n^2 + \frac{1}{6}n + n^2 + 2n + 1 = \frac{1}{3}n^3 + \frac{3}{2}n^2 + \frac{13}{6}n + 1$。


6(n + 1)(n + 2)(2n + 3) = 1 6(n + 1)(2n2 + 7n + 6) = 1


> 🇨🇳 第二个表达式展开：$\frac{1}{6}(n+1)(n+2)(2n+3) = \frac{1}{6}(n+1)(2n^2+7n+6)$。


| (2n3 + 7n2 + 6n) + (2n2 + 7n + 6) | = 1 3n3 + 3 2n2 + 13 6 n + 1 Look at that; they're identical! Also, notice how much easier this was than trying to rearrange one of the expressions and "morph" it into the other. We proved they were identical by manipulating them both and finding the same expression, ultimately. Now, let's look back and assess what we have accomplished: 1. We likened proving the validity of the formula n X k=1 k2 = 1 6n(n + 1)(2n + 1) for all values of n to knocking over an infinite line of dominos.


> 🇨🇳 $= \frac{1}{6}[(2n^3+7n^2+6n)+(2n^2+7n+6)] = \frac{1}{3}n^3 + \frac{3}{2}n^2 + \frac{13}{6}n + 1$。它们完全相同！注意，这比试图将一个表达式"变形"为另一个容易多了。我们通过分别化简两个表达式找到相同结果来证明它们相等。回顾我们完成的工作：


2. We verified that Domino 1 will fall by checking the formula corresponding to that case by hand. 3. We proved that Domino n will fall into Domino (n+1) and knock it over by assuming the fact written on Domino n is true and using that knowledge to show that the fact written on Domino (n + 1) must also be true. 4. This guarantees that all dominos will fall, so the formula is true for all values of n! Are you convinced by this technique? Do you think we've rigorously proven that the formula is valid for all natural numbers n? What if there were a value of n for which the formula didn't hold? What would that mean in terms of our domino scheme? Remember that this domino analogy is a good intuitive guide for how induction works, but it is not built on mathematically rigorous foundations. That will be the goal of the next couple of chapters. For now, let's revisit the other example we've examined in this section: lines in the plane. Again, the use of ellipses in our derivation of the formula R(n) is troublesome and we want to avoid it. Let's try to follow along with the domino scheme in the context of this puzzle. Imagine that we have defined the expression R(n) to represent the number of distinct regions in the plane created by n lines, where no two lines are parallel and no three intersect at one point. Also, imagine that on Domino n we have written the "fact" that "R(n) = 1 + n(n+1)


> 🇨🇳 1. 我们将证明公式 $\sum_{k=1}^{n} k^2 = \frac{1}{6}n(n+1)(2n+1)$ 对所有 $n$ 成立，类比为推倒一条无限长的骨牌线。2. 手算验证了骨牌 1 对应的公式。3. 假设骨牌 $n$ 上的命题为真，以此为前提证明骨牌 n+1 上的命题也必为真——即骨牌 n 推倒骨牌 n+1。4. 这保证所有骨牌倒下，从而公式对所有 $n$ 成立！


". Can we follow the same steps as above and verify that all the dominos will fall? First, we need to check that Domino 1 does, indeed fall. This amounts to verifying the statement: "R(1) = 1+ 1(2)


> 🇨🇳 你被这个技巧说服了吗？你认为我们严谨地证明了公式对所有自然数 $n$ 成立吗？如果某个 $n$ 使公式不成立会怎样？在我们的骨牌类比中意味着什么？记住骨牌类比只是归纳法的直觉引导，尚未建立在数学严谨的基础上——那是接下来几章的目标。现在回到平面直线问题：推导中使用了省略号，我们要避免它。按照骨牌方案，设 $R(n)$ 表示 $n$ 条直线（无两线平行、无三线共点）将平面分成的区域数，骨牌 $n$ 上写有"$R(n) = 1 + \frac{n(n+1)}{2}$"。


= 1+1 = 2". Is this a true statement? Yes, of course, we saw this before; one line divides the plane into two regions. Second, we need to prove that Domino n will topple into Domino (n + 1) for any arbitrary value of n. That is, let's assume that "R(n) = 1 + n(n+1)


> 🇨🇳 能按相同步骤验证所有骨牌倒下吗？首先验证骨牌 1 倒下，即验证：$R(1) = 1 + \frac{1 \cdot 2}{2} = 1 + 1 = 2$。这是真命题——一条直线将平面分为两个区域。


" is a true statement for some value of n and show that "R(n + 1) = 1 + (n+1)(n+2)


> 🇨🇳 其次，证明骨牌 $n$ 推倒骨牌 $n+1$，即假设 "$R(n) = 1 + \frac{n(n+1)}{2}$" 为真，证明 "$R(n+1) = 1 + \frac{(n+1)(n+2)}{2}$" 也必为真。如何做到？利用之前导出的关系 $R(n+1) = R(n) + n + 1$。结合骨牌 $n$ 倒下的假设：


" must also be a true statement. How can we do this? Well, let's follow along with the argument we used before to relate R(n + 1) to $\mathbb{R}$(n). By considering the geometric consequences of adding an extra line to any diagram with n lines (that also fit our rules about the lines) we proved that R(n +1) = R(n)+n +1. Using this knowledge and our assumption about Domino n falling, we can say that R(n + 1) = R(n) + n + 1 = 1 + n(n + 1)


> 🇨🇳 $R(n+1) = R(n) + n + 1 = 1 + \frac{n(n+1)}{2} + n + 1$。这与骨牌 $n+1$ 上的表达式相同吗？化简两边验证。左边：


+ n + 1 Is this the same expression as what is written on Domino (n + 1)? Again, let's simplify both expressions to verify they are the same. We have 1 + n(n + 1)


> 🇨🇳 $1 + \frac{n(n+1)}{2} + n + 1 = 2 + n + \frac{n^2+n}{2} = \frac{1}{2}n^2 + \frac{3}{2}n + 2$。


+ n + 1 = 2 + n + n2 + n


> 🇨🇳 $1 + \frac{(n+1)(n+2)}{2} = 1 + \frac{n^2+3n+2}{2} = \frac{1}{2}n^2 + \frac{3}{2}n + 2$。


= 1 2n2 + 3 2n + 2 and 1 + (n + 1)(n + 2)


> 🇨🇳 它们完全相同！因此我们证明了骨牌 $n$ 保证推倒骨牌 $n+1$，对所有 $n$ 成立。于是可以宣布所有骨牌都会倒下！思考：用这种方法证明与我们之前推导公式有何不同？我们用了省略号吗？为什么用这种方式证明更好？能否用骨牌归纳法来推导公式本身？


= 1 + n2 + 3n + 2


> 🇨🇳 **其他类比** 骨牌类比很流行，但不是唯一描述归纳法的方式。这里介绍几个。**魔法猴子 Mojo**：想象一架通向天空的无限长梯子，阶梯编号 1, 2, 3,...。Mojo 是一只既聪明又有魔力的猴子，能爬上无限长梯子！到达某级即对应命题为真。如何保证他爬遍整架梯子？仅确认两点：(1) 好是否会起步——到达第 1 级？(2) 梯级间距是否足够近够到下一级？这与骨牌类比的条件完全一致。**归纳鸭 Doug**：Doug 是只爱面包的鸭子，沿归纳街挨家找面包，房子编号 1, 2, 3,...。#1 找不到就去 #2，还找不到就去 #3……若事先知道没人有面包，则他在每一家都找不到，必去下一家，因此一定到过每一家！


= 1 2n2 + 3 2n + 2


> 🇨🇳 **一个担忧：梯子的"顶"在哪？** 你可能担心："Mojo 确实在爬梯子，但他怎么可能到达顶？梯子是无限的，他永远到不了……"在某种程度上你说得对——无限长梯确实没有尽头，Mojo 不会"到达那里"。但这不是目标——我们不需要他站在梯子顶端，只需要他到达每一个可能的梯级。假设你关心第 18,458,789,572,311,000,574,003 号命题——对应梯级远在上方，而 Mojo 一定会到达！也许需要很长时间，但在这魔法世界谁在乎？他终将到达，这就够了。每个命题都有人关心，Mojo 终将到达他们的梯级——每个人都会满意。整个无限攀登过程浓缩为两个步骤——仅靠这两步确信每个梯级都会被触及。每个编号命题都是真的。骨牌类比亦然——我们不关心"终点"，骨牌线无限延伸，每块终将倒下。Doug 终将到达每个院子——不在乎"何时"，只在乎"全都到过"。


Look at that; they're identical! Thus, we have shown that Domino n is guaranteed to fall into Domino (n+1), for any value of n. Accordingly, we can declare that all dominos will fall! Think about the differences between what we have done with this "domino technique" and what we did before to derive the expressions we just proved. Did we use any ellipses in this section? Why is it better to prove a formula this way? Could we have used the domino induction technique to derive the formulas themselves?
### 2.3.2 Other Analogies The Domino Analogy is quite popular, but it's not the only description of how induction works. Depending on what you read, or who you talk to, you might learn of a different analogy, or some other kind of description altogether. Here, we'll describe a couple that we've heard of before. It will help solidify your understanding of induction (at least as far as we've developed it) to think about how these analogies are all equivalent, fundamentally. Mojo the Magical, Mathematical Monkey Imagine an infinite ladder, heading straight upwards into the sky. There are infinitely-many rungs on this ladder, numbered in order: 1, 2, 3, and so on going upwards. Our friend Mojo happens to be standing next to this ladder. He is an intelligent monkey, very interested in mathematics but also a little bit magical, because he can actually climb up this infinite ladder! If Mojo makes it to a certain rung on the ladder, that means the fact corresponding to that number is True. How can we make sure he climbs up the entire ladder? It would be inefficient to check each rung individually. Imagine that: we would have to stand on the ground and make sure he got to Rung 1, then we would have to look up a bit and make sure he got to Rung 2, and then Rung 3, and so on... Instead, let's just confirm two details with Mojo before he starts climbing. Is he going to start climbing? That is, is he going to make it to Rung 1? If so, great! Also, are the rungs close enough together so that he can always reach the next one, no matter where he is? If so, even greater! These are exactly like the conditions established in our Domino Analogy. To ensure that Mojo gets to every rung, we just need to know he gets to the first one and that he can always get to the next one. Doug the Induction Duck Meet Doug. He's a duck. He also loves bread, and he's going to go searching through everyone's yards to find more bread. These yards are all along Induction Street in Math Town, where the houses are numbered 1, 2, 3, and so on, all in a row. Doug starts in the yard of house #1, looking for bread. He doesn't find any, so he's still hungry. Where else can he look? The house next door, #2, has a


> 🇨🇳 **### 2.3.4 问题与练习** **回顾** (1) 骨牌、Mojo、Doug 三个类比有何等价关系？能否找出一个"函数"描述它们之间的转换？(2) 找一个未学过数学归纳法的朋友，试着向他描述。你是否用到了某个类比？有帮助吗？


backyard, too! Doug heads that way, his tummy rumbling. He doesn't find any bread there, either, so he has to keep looking. He already knows house #1 has no bread, so the only place to go is next door to house #3. We think you see where this is going... If we were keeping track of Doug's progress, we might wonder whether he eventually gets to every yard. Let's say we also knew ahead of time that nobody has any bread. This means that whenever he's in someone's yard, he will definitely go to the next house, still searching for a meal. This means that he will definitely get to every house! That is, no matter which house we live in, no matter how large the number on our front door might be, at some point we will see Doug wandering around our backyard. (Unfortunately, he will go hungry all this time, though! Poor Doug.)
### 2.3.3 Summary Let's reconsider what we've accomplished with the two example puzzles we've seen thus far, and the analogies we've given. In our initial consideration of each puzzle, we identified some aspect of the structure of the puzzle where a "fact" depended on a "previous fact". In the case of the cubic numbers, we found a way to express (n + 1)3 in terms of n3; in the case of the lines in the plane, we described how many regions were added when an extra line was added to a diagram with n lines. From these observations, we applied this encapsulated knowledge over and over until we arrived at a "fact" that we knew, for a "small" value of n (in both cases, here, n = 1). This allowed us to derive a formula or equation or expression for a general fact that should hold for any value of n. This work was interesting and essential for deriving these expressions, but it was not enough to prove the validity of the expressions. In doing the work described above, we identified the presence of an inductive process and utilized its structure to derive the expressions in question. This was beneficial in two ways, really; we actually found the expressions we wanted to prove and, by recognizing the inductive behavior of the puzzle, we realized that proving the expressions by mathematical induction would be prudent and efficient. For the actual "proof by induction", we followed two main steps. First, we identified a "starting value" for which we could check the formula/equation by hand. Second, we assumed that one particular value of n made the corresponding formula hold true, and then used this knowledge to show that the corresponding formula for the value n + 1 must also hold true. Between those two steps, we could rest assured that "all dominos will fall" and, therefore, the formulas would hold true for all relevant values of n. One Concern: What's at the "top" of the ladder? You might be worried about something, and we'll try to anticipate your question here. (We only bring this up because it's a not uncommon observation to make. If you weren't thinking about this, try to imagine where the idea would come from.) You might say, "Hey now, I think I see how Mojo is climbing the ladder,


> 🇨🇳 (3) 为什么仅做了立方数的工作还不能证明求和公式？为什么还要再做那些工作？(4) 想想骨牌类比——骨牌线无限延伸是问题吗？是否意味着某些骨牌永远不会倒？试在类比范围内描述。


but how can he actually get all the way to the top? It's an infinite ladder, right? And he never gets there... right?" In a way, you would be right. Since this magical ladder really does go on forever, then there is truly no end to it and Mojo will never get "there". However, that isn't the point; we don't care about any "end" of the ladder (and not just because there isn't one). We just need to know that Mojo actually gets to every possible rung. He doesn't have to surpass all of them and stand at the top of the ladder, looking down at where he came from. That wasn't the goal! Think of it this way: pretend you have a vested interest in some particular fact that we're proving. Let's say it's Fact #18,458,789,572,311,000,574,003. (Some huge number. It doesn't matter, really.) Its corresponding rung is waaayyyyyy up there on the ladder, and all you care about is whether or not Mojo gets there on his journey. Does he?... You bet he does! It might take a long time (how many steps will it take?), but in this magical world of monkeys and ladders, who cares about time anyway! You know that he'll eventually get there, and that makes you happy. Now, just imagine that for each fact, there's somebody out there in that magical world that cares about only that fact. Surely, everyone will be happy with the knowledge that Mojo will get to their rung on his journey. Nobody cares about whether he gets to the top; that isn't their concern. Meanwhile, out here in our regular, non-magical world, we are extremely happy with the fact that everyone in that world will eventually be happy. That entire infinite process of ladder-climbing was condensed into just two steps, and with only those two steps, we can rest assured that every rung on that ladder will be touched. Every numbered fact is true. Think about this in terms of the Domino Analogy, as well. Do we care whether or not there is some "ending point" of the line of dominoes, so that they all fall into a wall somewhere? Of course not; the line goes on forever. Every domino will eventually fall over, and we don't even care how "long" that takes. Likewise, we know Doug will get to everyone's yard; we don't care "when" he gets to any individual yard, just that he gets to all of them.
### 2.3.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) How are the Domino, Mojo, and Doug analogies all equivalent? Can you come up with some "function" that describes their relationship, that converts one analogy into another? (2) Find a friend who hasn't studied mathematical induction before, and try to describe it. Do you find yourself using one of the analogies? Was it helpful?


> 🇨🇳 **动手试试** (1) 完成归纳步骤，证明公式 $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$。


(3) Why is it the case that our work with the cubes didn't prove the summation formula? Why did we still need to go through all that work? (4) Think about the Domino Analogy. Is it a problem that the line of dominoes goes on forever? Does this mean that there are some dominoes that will never fall down? Try to describe what this means in terms of the analogy. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Work through the inductive steps to prove the formula n X k=1 k = n(n + 1)


> 🇨🇳 (2) 完成归纳步骤，证明公式 $\sum_{k=1}^{n} (2k-1) = n^2$。 (3) 完成归纳步骤，证明公式 $\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2$。


(2) Work through the inductive steps to prove the formula n X k=1 (2k -1) = n2 (3) Work through the inductive steps to prove the formula n X k=1 k3 = (n(n + 1)


> 🇨🇳 (4) 设有一系列用自然数索引的命题，用 $P(n)$ 表示第 $n$ 个命题。(a) 若要证明每个 $n$ 都使命题为真，如何做？(b) 若要证明只有偶数 n 使命题为真，能做吗？如何修改类比描述你的方法？(c) 若要证明只有 $n \geq 4$ 使命题为真，能做吗？如何修改类比？


)2 (4) Suppose we have a series of facts that are indexed by natural numbers. Let's use the expression "P(n)" to represent the $n$-th fact. (a) If we want to prove every instance is True, for every natural number n, how can we do this? (b) What if we want to prove that only every even value of n makes a True statement? Can we do this? Can you come up with a modification of one of the analogies we gave that would describe your method? (c) What if we want to prove that only every value of n greater than or equal to 4 makes a True statement? Can we do this? Can you come up with a modification of one of the analogies we gave that would describe your method?


> 🇨🇳 **2.4 两个更多（不同的）示例** 本节有几个目的：一是不要让你产生归纳法只适用于数值公式和多项式的印象——归纳法远比那有用！后面的例子将证明某个抽象性质对任意"规模"的情形成立，你会看到它仍属于归纳法范畴，但与之前的例子有所不同。此外，这些例子将展示有时我们需要知道"更多信息"才能推倒骨牌——之前只需知道骨牌 $n$ 倒下即可保证骨牌 $n+1$ 倒下，但现在可能需要知道前面好几块骨牌的情况。


2.4. TWO MORE (DIFFERENT) EXAMPLES


> 🇨🇳 **2.4.1 骨牌与铺砖** 这个例子比前两个更复杂。我们仍然要证明一个数值公式，但问题更具几何直观性。此外，我们会注意到起始步骤中有一个有趣的"弯折"——需要先解决几个"小情形"才能推广方法。这将是我们首次考虑归纳法的推广与适应。问题是：给定一个 $2 \times n$ 的方格阵列，有多少种不同的方式用骨牌铺满？铺砖必须使每个方格恰好被一块骨牌覆盖。


## 2.4 Two More (Different) Examples This short section serves a few purposes. For one, we don't want you to get the idea, right away, that induction is all about proving a numerical formula with numbers and polynomials. Induction is so much more useful than that! One of the following examples, in particular, will be about proving some abstract property is true for any "size" of the given situation. You will see how it still falls under the umbrella of "induction", but you will also notice how it is different from the previous examples. Furthermore, these examples will illustrate that sometimes we need to know "more information" to knock over some dominoes. In the previous examples, we only needed to know that Domino n fell to guarantee that Domino n + 1 will fall. Here, though, we might have to know about several previous dominoes. After these two examples, we will summarize how this differs from the domino definition given above, and preview a broader definition of the technique of induction, as it applies to these examples.
### 2.4.1 Dominos and Tilings This next example is a little more complicated than the first two. We will still end up proving a certain numerical formula, but the problem is decidedly more visual than just manipulating algebraic expressions. Furthermore, we'll notice an interesting "kink" in the starting steps, where we have to solve a couple of "small cases" before being able to generalize our approach. This will be our first consideration of how the technique of induction can be generalized and adapted to other situations. The question we want to answer is nicely stated as follows: $Given a 2 \times n array of squares, how many different ways can we tile the array with dominoes$? A tiling must have every square covered by one--and only one--domino. For example, the following are proper tilings whereas the following are not proper tilings


> 🇨🇳 （铺砖示例——本书原配有插图，展示 $2 \times n$ 方格的正确与不正确铺法。）


