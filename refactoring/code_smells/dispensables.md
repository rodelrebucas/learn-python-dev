### Dispensables - something unneccessary and pointless

1.  Comments - explanatory commends in methods, comment only if:

    1. the whys of an implementation
    2. explaining a still complex algo after doing refactor to simplify

    Solution:

         a. explaination on complex expression use: Extract Variable
         b. explaination of sectionof code use: Extract Method
         c. Rename method
         d. For asserting rules use: Introduce Assertion

2.  Duplicates - identical code fragments

    Solution:

        a. Duplicate code in methods use: Extract Method
        b. Duplicate code in two subclasses with the same level:
                b1. For methods use:
                    1. Extract Method
                    2. Pull Up Field
                b2. Duplicaate codes in constructor use: Pull Up Constructor Body
                b3. For similiraties use: Form Template Method.
                b4. Same functionality diff algo choose one and use: Substitute Algorithm.
        c. Duplicate in 2 classes:
                1. If not in hierarchy use: Extract Superclass
                2. else, hard to create Superclass use: Extract class
        d. Large the same conditional statements which differ in conditions use:
                1. Consolidate Conditional Expression
                2. Extract Method
        e. Same code performed inside conditions use: Consolidate Duplicate Conditional Fragments

3.  Lazy classes - classes that nearly does nothing

    Solution:

        a. Components that are near-useless use: Inline Class treatment.
        b. Subclasses with few functions use: Collapse Hierarchy

4.  Data Class - class that refers to a class that contains only fields and crude methods for accessing them (getters and setters)

    Solution:

        a. Encapsulate Fields
        b. For data stored in collections use: Encapsulate Collection
        c. Move method and Extract method if beneficial
        d. Remove Setting Method and Hide Method

5.  Dead Code - unused: variable, parameter, field, method or class

    Solution:

        a. Delete them!
        b. Unnecessary classes use any:
            1. Inline Class
            2. Collapse Hierarchy
        c. Remove unused params

6.  Speculative Generality - unused class, method, field or parameter only for future use or with the intention that in can be useful some other times.


    Solution:

        a. Removing abstract class use: Collapse Hierarchy
        b. Unnecesary class use: Inline Class
        c. Methods: Inline Method
        d. Removing unused params
        e. Delete unused fields
