### Change Preventers - changing something results in a lot of changes in other places

1.  Divergent Change - changes in a class result in changes in many of its methods

    Solution:

        a.  Split class via: Extract Class
        b.  Or combine same behavior with: Extract Superclass and Extract Subclass

2.  Shotgun Surgery - making modifications result in many changes in other classes

    Solution:

        a. Moving existing class behaviors in into single class with:
                1. Move Method
                2. Move Field
        b. Refactor almost empty class after refactoring with *a use: Inline class

3.  Parallel Inheritance Hierarchies - creating a subclass for a class
    result in creating subclass for another class

    Solution:

        a. Remove the hierarchy of one of the subclass, make this subclass refer to the other one
            use:
                1. Move Method
                2. Move Field
