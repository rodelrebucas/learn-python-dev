# [WIP] clean-code-python

## Table of Contents

1. [Variables](#variables)
2. [Functions](#functions)
3. [Comments](#comments)

### TODOS

[ ] Functions should only be one level of abstraction

[ ] Remove duplicate code

[ ] Don't use flags as function parameters

[ ] Avoid Side Effects

[ ] Favor functional programming over imperative programming

[ ] Encapsulate conditionals

[ ] Avoid negative conditionals

[ ] Avoid conditionals

[ ] Don't over-optimize

[ ] Remove dead code

[ ] Objects and Data Structures

[ ] Classes

[ ] Prefer composition over inheritance

[ ] Single concept per test

[ ] Don't ignore caught errors

[ ] Use consistent capitalization

### Mirror guide for python from [clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript)

#### Variables

- Use meaningful and pronounceable variable names

  Bad:

      dt = datetime.datetime.now()

  Good

      today = datetime.datetime.now()

- Use the same vocabulary for the same type of variable

  Bad:

      get_user_info()

      get_client_data()

  Good:

      get_user_info()

      get_user_data()

- Use searchable names

  Bad:

      time.sleep(86400)

  Good:

      SECONDS_IN_A_DAY = 60 * 60 * 24

      time.sleep(ONE_SECOND)

- Use explanatory variables

  Bad:

      address = 'One Infinite Loop, Cupertino 95014'

      city_zip_code_regex = r'^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$'

      matches = re.match(city_zip_code_regex, address)

      save_city_zip_code(matches[1], matches[2]) <-- matches what?

  Good:

  Decrease dependence on regex by naming subpatterns.

      address = 'One Infinite Loop, Cupertino 95014'

      city_zip_code_regex = r'^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$' <-- Using named capture groups

      matches = re.match(city_zip_code_regex, address)

  save_city_zip_code(matches['city'], matches['zip_code']) <-- Now we know what are those

- Avoid mental mapping

  Don’t force the reader of your code to translate what the variable means. Explicit is better than implicit.

  Bad:

      seq = ('Austin', 'New York', 'San Francisco')

      for item in seq:
        do_stuff()
        do_some_other_stuff()
        # ...
        # Wait, what's `item` for again?
        dispatch(item)

  Good:

      locations = ('Austin', 'New York', 'San Francisco')

      for location in locations:
        do_stuff()
        do_some_other_stuff()
        # ...
        dispatch(location)

- Don't add unneeded context

  If your class/object name tells you something, don't repeat that in your variable name.

  Bad:

      class Car:
          car_make: str
          car_model: str
          car_color: str

  Good:

      class Car:
          make: str
          model: str
          color: str

- Use default arguments instead of short circuiting or conditionals

  Default arguments are often cleaner than short circuiting. Be aware that if you use them, your function will only provide default values. Other "falsy" values such as '', "", false, null, 0, and NaN, will not be replaced by a default value.

  Bad:

      def create_micro_brewery(name):
        name = "Hipster Brew Co." if name is None else name
        slug = hashlib.sha1(name.encode()).hexdigest()
        # etc.

  Good:

      def create_micro_brewery(name: str="Hipster Brew Co."):
        slug = hashlib.sha1(name.encode()).hexdigest() # etc.

### Functions

Function arguments (2 or fewer ideally)

- testing is easier

- more than 2 arguments should lead to a refactoring or creation of another object that holds the variables

  Bad:

  def create_menu(title, body, button_text, cancellable): # ...

  Good:

      class Menu:
        def **init**(self, config: dict):
          title = config["title"]
          body = config["body"] # ...

      menu = Menu(
        {
        "title": "My Menu",
        "body": "Something about my menu",
        "button_text": "OK",
        "cancellable": False
        }
      )

* Functions should do one thing

  This is by far the most important rule in software engineering. When functions do more than one thing, they are harder to compose, test, and reason about. When you can isolate a function to just one action, they can be refactored easily and your code will read much cleaner. If you take nothing else away from this guide other than this, you'll be ahead of many developers.

  Bad:

      def email_clients(clients: List[Client]):
        """Filter active clients and send them an email.
        """
        for client in clients:
          if client.active:
            email(client)

  Good:

      def get_active_clients(clients: List[Client]) -> List[Client]:
          """Filter active clients.
          """
        return [client for client in clients if client.active]

      def email_clients(clients: List[Client, ...]) -> None:
        """Send an email to a given list of clients.
        """
        for client in clients:
          email(client)

- Function names should say what they do

  Bad:

      class Email:
        def handle(self) -> None: # Do something...

        message = Email()

      # What is this supposed to do again?

      message.handle()

  Good:

      class Email:
        def send(self) -> None:
          """Send this message.
          """

      message = Email()
      message.send()

### Comments

- Only comment things that have business logic complexity.
  Comments are an apology, not a requirement. Good code mostly documents itself.

  Bad:

      # sums a and b
      def sum(a,b):
        return a + b

  Good:

      def sum(a,b): <-- No need for comment =)
        return a + b

- Don't leave commented out code in your codebase
  Version control exists for a reason. Leave old code in your history.

  Bad:

      doStuff();
      // doOtherStuff();
      // doSomeMoreStuff();
      // doSoMuchStuff();

  Good:

      doStuff();

- Don't have journal comments

  Remember, use version control! There's no need for dead code, commented code, and especially journal comments. Use git log to get history!

  Bad:

      /\*

          - 2016-12-20: Removed monads, didn't understand them (RM)
          - 2016-10-01: Improved using special monads (JP)
          - 2016-02-03: Removed type-checking (LI)
          - 2015-03-14: Added combine with type-checking (JR)

      \*/

      def combine(a, b):
        return a + b;

  Good:

      def combine(a, b):
        return a + b;

- Avoid positional markers

  They usually just add noise. Let the functions and variable names along with the proper indentation and formatting give the visual structure to your code.

  Bad:

      ////////////////////////////////////////////////////////////////////////////////
      // variable instantiation
      ////////////////////////////////////////////////////////////////////////////////

      name = ""
      lastname = ""

  Good:

      name = ""
      lastname = ""
