# Tool template for python I/O Connection type. 
+ You can build your code based on the following four ways, if it is related to io connection:
  1. Functional programming
  2. Object Oriented
  3. Decorators (closures)
  4. with context management

---

- 代码示例：
  以连接AD域控为例。

- 适用场景：
  在c/s架构中，任何需要建立socket连接的部分，都可参考以上的思路来完成。如：连接db数据库等。

- 代码实现：
  - 普通的面向过程
  - 普通的面向对象
  - 使用装饰器：函数式编程（闭包的应用）
  - 使用with上下文管理：通过魔法方法
