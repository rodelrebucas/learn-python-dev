### Couplers - excessive coupling and excessive delegation

1.  Feature Envy - a method accesses the data of another object more than its own data.

    Solution:

        a. Need to move the method? use: Move method
        b. Extract method

2.  Inappropriate Intimacy - one class uses the internal fields and methods of another class

    Solution:

        a. Move Method and Move Field
        b. Extract Class and Hide Delegate
        c. For mutually interdependent classes use: Change Bidirectional Association to Unidirectional
        d. Intimacy” is between a subclass and the superclass use: Replace Delegation with Inheritance

3.  Message Chains - series of calls: \$a->b()->c()->d()

    Solution:

        a. Hide delegate
        b. Extract Method and Move Method

4.  Middle Man - class performs only one action, delegating work to another class

    Solution:

        a. Remove Middle Man
