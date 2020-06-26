# 数据结构与算法
## 数据结构
### 一维
#### 数组array
##### O(1) 随机访问
##### 平均O(n) 插入和删除
##### 可被缓存加速访问
#### 链表list
##### 单向链表
###### value   .next
###### 不支持随机访问
###### O（1）插入和删除
###### O(n) 访问某个元素
###### 比数组占用更多存储空间
##### 双向链表
###### .next   .prev   .value
###### 每个节点多了一个指向前一节点的指针
##### 循环链表
###### 尾节点指针指向头节点
##### 静态链表
###### 用数组描述的链表
##### 特殊：跳表skip list
###### 只能用于元素有序的情况O(Logn)
###### 对标平衡树或二分法
#### 栈stack
##### 先入后出
##### 添加删除皆为O(1)
##### 查询O(n)
##### push(). top(). pop(). getMin()
#### 队列queue
    deque模块是python标准库collections中的一项，它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作。
    
    1.创建deque序列：
    
    from collections import deque
    
    q = deque(maxlen =3)
    q.appendleft(1)
    q.popleft()
    
    
    

##### 先入先出
##### 添加删除皆为O(1)
##### 查询O(n)
##### 双边队列：入口和出口都可以入队和出队
##### 优先队列：根据优先级出队
###### 插入O(1)
###### 取出:O(logn)
#### 哈希表hash table
##### 也叫散列表
##### 查询删除插入均O(1)
##### 根据关键码值(key value)访问
##### 集合set
##### 映射map
### 二维
#### 树tr ee O(n)
##### 二叉树
###### 前序遍历pre-order：根-左-右
###### 中序遍历：左-根-右
###### 后序遍历左-右-根
###### 递归解法
###### 示例代码
     示例代码
    def preorder(self, root):
         if root: 
               self.traverse_path.append(root.val) 
               self.preorder(root.left)     
               self.preorder(root.right)
    
    def inorder(self, root):
         if root:
               self.inorder(root.left) 
               self.traverse_path.append(root.val) 
               self.inorder(root.right)
    
    def postorder(self, root):
         if root:
               self.postorder(root.left) 
               self.postorder(root.right) 
               self.traverse_path.append(root.val)

#### 图graph
##### 有环二叉树
###### 
#### 二叉搜索树AVL. O(logn)
##### 二叉排序树
##### 左子树所有节点均小于根节点值
##### 右子树所有节点均大于根节点值
#### 堆heap(以二叉堆为例）
    模块heapq中一些重要的函数
              函 数                                                                           heappush(heap, x)                                 将x压入堆中
     heappop(heap)                                      从堆中弹出最小的元素
     heapify(heap)                                         让列表具备堆特征
     heapreplace(heap, x)                       弹出最小的元素，并将x压入堆中
     nlargest(n, iter)                                       返回iter中n个最大的元素
    nsmallest(n, iter)                                   返回iter中n个最小的元素
    
    

##### 可以迅速找最大或最小值
##### 根节点最大：大顶堆、大根堆
##### 根节点最小：小顶堆、小根堆
##### find-max、find-min：O(1)
##### delete-max,delete-min：O(logn):先删堆顶元素，再将堆尾元素挪到堆顶再调整交换
##### insert: O(logn) or O(1)：先插入到最后再调整交换(heapifyDown)
##### 通过完全二叉树来实现
##### 索引为i的左、右孩子的索引为：2i+1、2i+2，父节点：floor((i-1)/2)
##### 常见：二叉堆、斐波那契堆
#### 并查集disjoint set
#### 字典树tr ie
### 特殊
#### 位运算Bitwise
#### 布隆过滤器BloomFilter
#### LRU Cache
## 算法
### if-else，switch
### for、while循环
### 递归Recursion
    def recursion(level, param1, param2, ...): 
         # recursion terminator
         if level > MAX_LEVEL:
               process_result
               return
         # process logic in current level
         process(level, data...)
         # drill down
         self.recursion(level + 1, p1, ...)
         # reverse the current level status if needed

#### 递归终结条件->处理当前层逻辑->下探到下一层->清理当前层
#### 分治Divide&Conquer
##### 代码模版
    def divide_conquer(problem, param1, param2, ...): 
        # recursion terminator
        if problem is None:
             print_result
             return
        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)
        # conquer subproblems
        subresult1 = self.divide_conquer(subproblems[0], p1, ...)  
        subresult2 = self.divide_conquer(subproblems[1], p1, ...)
        subresult3 = self.divide_conquer(subproblems[2], p1, ...)
        ...
        # process and generate the final result
        result = process_result(subresult1, subresult2, subresult3, ...)
        # revert the current level states

##### 分成子问题求解再合并结果
#### 回溯Backtracking
##### 采用试错思想，尝试分布解决一个问题，采用最简单递归来实现
### 搜索Search
#### 深度优先
#### 广度优先
### 动态规划
### 二分查找
### 贪心
### 数学、几何
## 排序
### O(n^2)
#### 冒泡排序
#### 选择排序
#### 插入排序
#### 希尔排序
### O(nlogn)
#### 归并排序
#### 快速排序
#### 希尔排序
### O(n)
#### 基数排序
#### 计数排序
#### 桶排序
## 算法复杂度分析
### 时间
#### 常见时间复杂度
##### 散列表O(1）
##### 二分查找、二叉搜索树O(Logan)
##### 大多数遍历O(n)
##### 双重循环O(n^2)
##### 递归O(2^n)
### 空间
#### 数组的长度
#### 递归的深度
## 分支主题 4
## 
