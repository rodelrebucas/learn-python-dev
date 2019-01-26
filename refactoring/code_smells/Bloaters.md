### Bloaters - large no. of methods and classes

1.  Long method - a method that has too many lines

    Solutions:

        a. Use Extract Method to shorthen length of body
        b. If local variables and parameters interfere with extracting a method, use any:
            1. Replace Temp with Query
            2. Introduce Parameter Object
            3. Preserve Whole Object.
        c. Replace Method with Method Object.
        d. For conditionals use Decompose Conditional
        e. For loops use: Extract Method.

2.  Large class - a class that also has many lines of code/methods/fields

    Solutions:

        a. A part can be extracted as a separate component use: Extract Class
        b. A part can be separate as a subclass use: Extract Subclass
        c. For extracting behaviors and operations use: Extract Interface
        d. For graphical interface - separating data and behavior use:  Duplicate Observed Data

3.  Primitive obsession - use of primitive types instead of objects

    Solutions:

        a. If primitive fields are used in method parameters use any:
            1. Introduce Parameter Object
            2. Preserve Whole Object
        b. For complicated data is coded variables use any:
            1. Replace Type Code with Class
            2. Replace Type Code with Subclasses
            3. Replace Type Code with State/Strategy
        c. Replace array with object use: Replace Array with Object.

4.  Long Parameter List - More than three or four parameters for a method.

    Solutions:

        a. If arguments are results of method call use: Replace Parameter with Method Call.
        b. Passing a group of data from an object use: Preserve Whole Object.
        c. Several unrelated data use: Introduce Parameter Object.

5.  Data Clumps - handling identical groups of variables in the code (database configs...)

    Solutions:

        a. Repeating data comprises the fields of a class use: Extract Class
        b. Same data clumps are passed in the parameters of methods use:  Introduce Parameter Object
        c. some data is passed to other methods use:  Preserve Whole Object
