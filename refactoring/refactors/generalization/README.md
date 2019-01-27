1.  Pull Up Field - If two subclasses have same field move it to Superclass.

2.  Pull Up Method - If two subclasses have same methods who do similar function move it to Superclass.

3.  Push Down Method - move a method from a superclass to the only subclass using the method.

4.  Push Down Field - move a field from a superclass to the only subclass using the field.

5.  Extract Subclass - for features in a class that is used in only some cases, extract this feature in a Subclass

6.  Extract SuperClass - for classes with common fields and methods, create a SuperClass

7.  Extract Interface - extracting same features as an Interface

8.  Collapse Hierarchy - merge into one class, for Superclass and subclass that are identical

9.  Form Template Method - for subclasses who implements algorithm with similar steps:
    1.  extract these similar steps
    2.  subclass now needs to implement their additional steps
