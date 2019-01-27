1.  Renaming methods

    from:

        getfn()

    to:

        getFirstName()

2.  Removing Unused params

3.  Separate query from modifier

    from:

        getTotalAndSetPayment()

    to:

        getTotal()
        setPayment()

4.  Parameterize method - for methods with same actions

    from:

        calculateFivePercentDiscount()
        calculateTenPercentDiscount()

    to:

        calculateDiscount(discount_rate)

5.  Introduce Parameter Object

    from:

        class Vacation:
            def __init__(dateStart, dateEnd):
                pass

    to:

        class Vacation:
            def __init__(schedule:Date):
                pass

6.  Hide methods - for methods not used outside the class

7.  Create factory method - for constructors that do more than setting its fields, replace constructor calls with this

        E.g. (Java)

            class Employee {
                Employee(int type) {
                    this.type = type;
                }
                //...
            }

        change to:

            class Employee {
                static Employee create(int type) {
                    employee = new Employee(type);
                    // do some heavy lifting.
                    return employee;
                }
                //...
            }
