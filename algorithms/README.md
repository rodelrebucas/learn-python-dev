### Algorithm analysis

- It tells the behaviour of an algorithm as input grows in terms of time and space complexity.

Terms:

- Asymptote - a line in a graph of a function approaches but never reaches.

- Asymptotic - an Asymptote behavior.

- Time complexity - how long does algorithm takes to finish as input grows.

- Space complexity - how much space does algorithm needed as input grows.

Big O (Upper bound) - f(n) is Big O(g(n)) when for some constank k \* g(n), f(n) is equal or no greater than k \* g(n)

- Finding the Big O (g(n))

1. Find the fastest growing variable.

2. Eliminate co-efficient and constants.

   Why?

   - we only care how the algorithm behaves in terms of bigger inputs.

   - it has minimal effect on the result.

Big Omega (lower bound) - f(n) is Big Omega(g(n)) when for some constank k \* g(n), f(n) is atleast or no lesser than k \* g(n)

Big theta (tight bound) - f(n) is Big Theta(g(n)) when for some constants k1 and k2 where f(n) => k1 _ g(n) and f(n) <= k2 _ g(n)

### Binary Tree

A. Full Tree - A node contains 0 or two children.

B. Complete Tree - Inserting nodes or children must be from left to right.

C. Perfect Tree - a full and complete tree where all leaf nodes are in the same level.
