课程主页：https://courses.d2l.ai/zh-v2/
教材：https://zh-v2.d2l.ai/

# 引言
## 机器学习中的关键组件
### 数据
 每个数据集由一个个**样本**（example, sample）组成，大多时候，它们遵循独立同分布(independently and identically distributed, i.i.d.)。 样本有时也叫做数据点（data point）或者数据实例（data instance），通常每个样本由一组称为**特征**（features，或协变量（covariates））的属性组成。 机器学习模型会根据这些属性进行预测。 在上面的监督学习问题中，要预测的是一个特殊的属性，它被称为**标签**（label，或目标（target））。

当每个样本的特征类别数量都是相同的时候，其特征向量是固定长度的，这个长度被称为数据的**维数**（dimensionality）。 固定长度的特征向量是一个方便的属性，它可以用来量化学习大量样本。然而，并不是所有的数据都可以用“固定长度”的向量表示。如图像的分辨率或形状，文本数据。

拥有海量的数据是不够的，我们还需要正确的数据。 如果数据中充满了错误，或者如果数据的特征不能预测任务目标，那么模型很可能无效。一种常见的问题来自不均衡的数据集，比如在一个有关医疗的训练数据集中，某些人群没有样本表示。

### 模型及损失函数
在机器学习中，我们需要定义模型的优劣程度的度量，这个度量在大多数情况是“可优化”的，这被称之为**目标函数**（objective function）。 我们通常定义一个目标函数，并希望优化它到最低点。 因为越低越好，所以这些函数有时被称为**损失函数**（loss function，或cost function）。 但这只是一个惯例，我们也可以取一个新的函数，优化到它的最高点。 这两个函数本质上是相同的，只是翻转一下符号。

当任务在试图预测数值时，最常见的损失函数是**平方误差**（squared error），即预测值与实际值之差的平方。 当试图解决分类问题时，最常见的目标函数是最小化错误率，即预测与实际情况不符的样本比例。 有些目标函数（如平方误差）很容易被优化，有些目标（如错误率）由于不可微性或其他复杂性难以直接优化。 在这些情况下，通常会优化替代目标。

通常，损失函数是根据模型参数定义的，并取决于数据集。 在一个数据集上，我们可以通过最小化总损失来学习模型参数的最佳值。 该数据集由一些为训练而收集的样本组成，称为**训练数据集**（training dataset，或称为训练集（training set））。 然而，在训练数据上表现良好的模型，并不一定在“新数据集”上有同样的性能，这里的“新数据集”通常称为**测试数据集**（test dataset，或称为测试集（test set））。

### 优化算法
当我们获得了一些数据源及其表示、一个模型和一个合适的损失函数，接下来就需要一种算法，它能够搜索出最佳参数，以最小化损失函数。 深度学习中，大多流行的优化算法通常基于一种基本方法–**梯度下降**（gradient descent）。 简而言之，在每个步骤中，梯度下降法都会检查每个参数，看看如果仅对该参数进行少量变动，训练集损失会朝哪个方向移动。 然后，它在可以减少损失的方向上优化参数。

## 机器学习类别
### 监督学习
监督学习（supervised learning）擅长在“给定输入特征”的情况下预测标签。 每个“特征-标签”对都称为一个样本（example）。 有时，即使标签是未知的，样本也可以指代输入特征。 我们的目标是生成一个模型，能够将任何输入特征映射到标签（即预测）。

监督学习的学习过程一般可以分为三大步骤：
1.  从已知大量数据样本中随机选取一个子集，为每个样本获取真实标签。有时，这些样本已有标签（例如，患者是否在下一年内康复？）；有时，这些样本可能需要被人工标记（例如，图像分类）。这些输入和相应的标签一起构成了训练数据集；
2.  选择有监督的学习算法，它将训练数据集作为输入，并输出一个“已完成学习的模型”；
3.  将之前没有见过的样本特征放到这个“已完成学习的模型”中，使用模型的输出作为相应标签的预测。

#### 回归
回归（regression）是最简单的监督学习任务之一。 其分析输入变量（自变量）和输出变量（因变量）之间的关系，来预测一个或多个连续值结果的问题。与分类问题主要预测离散标签不同，回归问题的输出是连续的数值。

#### 分类
分类问题希望模型能够预测样本属于哪个类别（category，正式称为类（class））。 例如，手写数字可能有10类，标签被设置为数字0～9。 最简单的分类问题是只有两类，这被称之为二项分类（binomial classification）。 例如，数据集可能由动物图像组成，标签可能是猫狗
两类。 回归是训练一个回归函数来输出一个数值； 分类是训练一个分类器来输出预测的类别。

当有两个以上的类别时，我们把这个问题称为多项分类（multiclass classification）问题。 常见的例子包括手写字符识别 
。 与解决回归问题不同，分类问题的常见损失函数被称为交叉熵（cross-entropy）。

#### 标记问题
有些分类问题很适合于二项分类或多项分类。 例如，我们可以训练一个普通的二项分类器来区分猫和狗。 运用最前沿的计算机视觉的算法，这个模型可以很轻松地被训练。 尽管如此，无论模型有多精确，当分类器遇到新的动物时可能会束手无策。 比如下图所示的这张“不来梅的城市音乐家”的图像 （这是一个流行的德国童话故事），图中有一只猫、一只公鸡、一只狗、一头驴，背景是一些树。 取决于我们最终想用模型做什么，将其视为二项分类问题可能没有多大意义。 取而代之，我们可能想让模型描绘输入图像的内容，一只猫、一只公鸡、一只狗，还有一头驴。

![img](https://zh-v2.d2l.ai/_images/stackedanimals.png)

####  搜索

有时，我们不仅仅希望输出一个类别或一个实值。 在信息检索领域，我们希望对一组项目进行排序。 以网络搜索为例，目标不是简单的“查询（query）-网页（page）”分类，而是在海量搜索结果中找到用户最需要的那部分。 搜索结果的排序也十分重要，学习算法需要输出有序的元素子集。 换句话说，如果要求我们输出字母表中的前5个字母，返回“A、B、C、D、E”和“C、A、B、E、D”是不同的。 即使结果集是相同的，集内的顺序有时却很重要。

该问题的一种可能的解决方案：首先为集合中的每个元素分配相应的相关性分数，然后检索评级最高的元素。[PageRank](https://en.wikipedia.org/wiki/PageRank)，谷歌搜索引擎背后最初的秘密武器就是这种评分系统的早期例子，但它的奇特之处在于它不依赖于实际的查询。 在这里，他们依靠一个简单的相关性过滤来识别一组相关条目，然后根据PageRank对包含查询条件的结果进行排序。 如今，搜索引擎使用机器学习和用户行为模型来获取网页相关性得分，很多学术会议也致力于这一主题。

####  推荐系统

另一类与搜索和排名相关的问题是*推荐系统*（recommender system），它的目标是向特定用户进行“个性化”推荐。 例如，对于电影推荐，科幻迷和喜剧爱好者的推荐结果页面可能会有很大不同。 类似的应用也会出现在零售产品、音乐和新闻推荐等等。

尽管推荐系统具有巨大的应用价值，但单纯用它作为预测模型仍存在一些缺陷。 首先，我们的数据只包含“审查后的反馈”：用户更倾向于给他们感觉强烈的事物打分。 例如，在五分制电影评分中，会有许多五星级和一星级评分，但三星级却明显很少。 此外，推荐系统有可能形成反馈循环：推荐系统首先会优先推送一个购买量较大（可能被认为更好）的商品，然而目前用户的购买习惯往往是遵循推荐算法，但学习算法并不总是考虑到这一细节，进而更频繁地被推荐。 综上所述，关于如何处理审查、激励和反馈循环的许多问题，都是重要的开放性研究问题。

#### 序列学习

如果输入是连续的，模型可能就需要拥有“记忆”功能。 比如，我们该如何处理视频片段呢？ 在这种情况下，每个视频片段可能由不同数量的帧组成。 通过前一帧的图像，我们可能对后一帧中发生的事情更有把握。 语言也是如此，机器翻译的输入和输出都为文字序列。

再比如，在医学上序列输入和输出就更为重要。 设想一下，假设一个模型被用来监控重症监护病人，如果他们在未来24小时内死亡的风险超过某个阈值，这个模型就会发出警报。 我们绝不希望抛弃过去每小时有关病人病史的所有信息，而仅根据最近的测量结果做出预测。

这些问题是序列学习的实例，是机器学习最令人兴奋的应用之一。 序列学习需要摄取输入序列或预测输出序列，或两者兼而有之。 具体来说，输入和输出都是可变长度的序列，例如机器翻译和从语音中转录文本。 虽然不可能考虑所有类型的序列转换，但以下特殊情况值得一提。

### 无监督学习

相反，如果工作没有十分具体的目标，就需要“自发”地去学习了。 比如，老板可能会给我们一大堆数据，然后要求用它做一些数据科学研究，却没有对结果有要求。 这类数据中不含有“目标”的机器学习问题通常被为*无监督学习*（unsupervised learning）

- *聚类*（clustering）问题：没有标签的情况下，我们是否能给数据分类呢？比如，给定一组照片，我们能把它们分成风景照片、狗、婴儿、猫和山峰的照片吗？同样，给定一组用户的网页浏览记录，我们能否将具有相似行为的用户聚类呢？
- *主成分分析*（principal component analysis）问题：我们能否找到少量的参数来准确地捕捉数据的线性相关属性？比如，一个球的运动轨迹可以用球的速度、直径和质量来描述。再比如，裁缝们已经开发出了一小部分参数，这些参数相当准确地描述了人体的形状，以适应衣服的需要。另一个例子：在欧几里得空间中是否存在一种（任意结构的）对象的表示，使其符号属性能够很好地匹配?这可以用来描述实体及其关系，例如“罗马” − “意大利” + “法国” = “巴黎”。
- *因果关系*（causality）和*概率图模型*（probabilistic graphical models）问题：我们能否描述观察到的许多数据的根本原因？例如，如果我们有关于房价、污染、犯罪、地理位置、教育和工资的人口统计数据，我们能否简单地根据经验数据发现它们之间的关系？
- *生成对抗性网络*（generative adversarial networks）：为我们提供一种合成数据的方法，甚至像图像和音频这样复杂的非结构化数据。潜在的统计机制是检查真实和虚假数据是否相同的测试，它是无监督学习的另一个重要而令人兴奋的领域。

### 与环境互动

有人一直心存疑虑：机器学习的输入（数据）来自哪里？机器学习的输出又将去往何方？ 到目前为止，不管是监督学习还是无监督学习，我们都会预先获取大量数据，然后启动模型，不再与环境交互。 这里所有学习都是在算法与环境断开后进行的，被称为*离线学习*（offline learning）。

这种简单的离线学习有它的魅力。 好的一面是，我们可以孤立地进行模式识别，而不必分心于其他问题。 但缺点是，解决的问题相当有限。 这时我们可能会期望人工智能不仅能够做出预测，而且能够与真实环境互动。 与预测不同，“与真实环境互动”实际上会影响环境。 这里的人工智能是“智能代理”，而不仅是“预测模型”。 因此，我们必须考虑到它的行为可能会影响未来的观察结果。

考虑“与真实环境互动”将打开一整套新的建模问题。以下只是几个例子。

- 环境还记得我们以前做过什么吗？
- 环境是否有助于我们建模？例如，用户将文本读入语音识别器。
- 环境是否想要打败模型？例如，一个对抗性的设置，如垃圾邮件过滤或玩游戏？
- 环境是否重要？
- 环境是否变化？例如，未来的数据是否总是与过去相似，还是随着时间的推移会发生变化？是自然变化还是响应我们的自动化工具而发生变化？

当训练和测试数据不同时，最后一个问题提出了*分布偏移*（distribution shift）的问题。 接下来的内容将简要描述强化学习问题，这是一类明确考虑与环境交互的问题。

### 强化学习

在强化学习问题中，智能体（agent）在一系列的时间步骤上与环境交互。 在每个特定时间点，智能体从环境接收一些*观察*（observation），并且必须选择一个*动作*（action），然后通过某种机制（有时称为执行器）将其传输回环境，最后智能体从环境中获得*奖励*（reward）。 此后新一轮循环开始，智能体接收后续观察，并选择后续操作，依此类推。 强化学习的过程在下图中进行了说明。 请注意，强化学习的目标是产生一个好的*策略*（policy）。 强化学习智能体选择的“动作”受策略控制，即一个从环境观察映射到行动的功能。

![image-20240207184420302](learning.assets/image-20240207184420302.png)

强化学习框架的通用性十分强大。 例如，我们可以将任何监督学习问题转化为强化学习问题。 假设我们有一个分类问题，可以创建一个强化学习智能体，每个分类对应一个“动作”。 然后，我们可以创建一个环境，该环境给予智能体的奖励。 这个奖励与原始监督学习问题的损失函数是一致的。

当然，强化学习还可以解决许多监督学习无法解决的问题。 例如，在监督学习中，我们总是希望输入与正确的标签相关联。 但在强化学习中，我们并不假设环境告诉智能体每个观测的最优动作。 一般来说，智能体只是得到一些奖励。 此外，环境甚至可能不会告诉是哪些行为导致了奖励。

以强化学习在国际象棋的应用为例。 唯一真正的奖励信号出现在游戏结束时：当智能体获胜时，智能体可以得到奖励1；当智能体失败时，智能体将得到奖励-1。 因此，强化学习者必须处理*学分分配*（credit assignment）问题：决定哪些行为是值得奖励的，哪些行为是需要惩罚的。 就像一个员工升职一样，这次升职很可能反映了前一年的大量的行动。 要想在未来获得更多的晋升，就需要弄清楚这一过程中哪些行为导致了晋升。

强化学习可能还必须处理部分可观测性问题。 也就是说，当前的观察结果可能无法阐述有关当前状态的所有信息。 比方说，一个清洁机器人发现自己被困在一个许多相同的壁橱的房子里。 推断机器人的精确位置（从而推断其状态），需要在进入壁橱之前考虑它之前的观察结果。

最后，在任何时间点上，强化学习智能体可能知道一个好的策略，但可能有许多更好的策略从未尝试过的。 强化学习智能体必须不断地做出选择：是应该利用当前最好的策略，还是探索新的策略空间（放弃一些短期回报来换取知识）。

当环境可被完全观察到时，强化学习问题被称为*马尔可夫决策过程*（markov decision process）。 当状态不依赖于之前的操作时，我们称该问题为*上下文赌博机*（contextual bandit problem）。 当没有状态，只有一组最初未知回报的可用动作时，这个问题就是经典的*多臂赌博机*（multi-armed bandit problem）。

# 预备知识

## 数据操作

## 数据预处理

## 线性代数

## 微积分

### 导数和微分

![image-20240210115237716](learning.assets/image-20240210115237716.png)

### 偏导数

![image-20240210115320642](learning.assets/image-20240210115320642.png)

### 梯度

![image-20240210115406049](learning.assets/image-20240210115406049.png)

![image-20240210120034172](learning.assets/image-20240210120034172.png)

![image-20240210120326805](learning.assets/image-20240210120326805.png)

![image-20240210120544650](learning.assets/image-20240210120544650.png)

###  链式法则

![image-20240210115526850](learning.assets/image-20240210115526850.png)

## 概率

![image-20240221180105205](learning.assets/image-20240221180105205.png)

![image-20240221180348925](learning.assets/image-20240221180348925.png)

![image-20240221180815911](learning.assets/image-20240221180815911.png)

![image-20240221183351115](learning.assets/image-20240221183351115.png)

# 线性神经网络

## 线性回归

![image-20240221214350612](learning.assets/image-20240221214350612.png)

![image-20240221214808749](learning.assets/image-20240221214808749.png)

![image-20240221214913668](learning.assets/image-20240221214913668.png)

![image-20240221220021166](learning.assets/image-20240221220021166.png)

![image-20240221223355962](learning.assets/image-20240221223355962.png)

##  softmax回归

![image-20240222215348605](learning.assets/image-20240222215348605.png)

![image-20240222215606706](learning.assets/image-20240222215606706.png)

![image-20240222225800781](learning.assets/image-20240222225800781.png)

![image-20240222225930911](learning.assets/image-20240222225930911.png)

![image-20240222233448407](learning.assets/image-20240222233448407.png)

![image-20240222233507666](learning.assets/image-20240222233507666.png)
