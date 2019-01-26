### Object-Orientation Abusers - incorrect application of oop principles

1.  Switch Statements - complex switch operator or sequence of if

    Solution:

        a. switch isolation use: Extract Method and Move Method
        b. switch based on type code use any:
            1. Replace Type Code with Subclasses
            2. Replace Type Code with State/Strategy
        c. Replace Conditional with Polymorphism
        d. For small amount of the same methods inside
           the switch each called with different params use:  Replace Parameter with Explicit Methods
        e. If one of the conditional options is null, use: Introduce Null Object.

2.  Temporary Field - fields that are needed only at a particular time.
    e.g variables that are need to check if something is NULL

    Solution:

        a. Extract class
        b. Introduce Null Object

3.  Refuse Bequest - subclass use only some of its parent's methods and properties

    Solution:

        a. Replace Inheritance with Delegation.
        b. If inheritance is neccessary use: Extract Superclass.

4.  Alternative Classes with Different Interfaces - Two classes perform identical
    functions but have different method names.

        a. Make the methods identical in all alternative classes and use: Rename Method
        b. Make the signature and implementation of methods the same by:
            1. Move Method
            2. Add Parameter
            3. Parameterize Method
        c. If part of functionality is duplicated use: Extract Superclass
