'''
    What is a coroutine?
        Coroutine is a just like a simple function that can pause to allow other block of codes or
        a other function to execute then resume its execution once the other block of codes is done.        

    Examples are taken from:
        From https://docs.python.org/3/library/asyncio-task.html    

'''

import asyncio
import time

# To make a function asynchronous
# async keyword is required at the start
# of the function

# Waiting for other function to finish
# then execute back the remaining lines of code
async def say_after(delay, what):
    # wait for this function to finish
    # this is a sleep function
    # will pause for delay duration
    await asyncio.sleep(delay)

    # run this after waiting
    print(what)

# main will serve as the main entry point
async def main():

    print('started at', time.strftime('%X'))

    # await this function
    # simply executing this function
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print('finished at', time.strftime('%X'))

# run the loop
asyncio.run(main())

# output
''' 
started at 16:49:54
hello
world
finished at 16:49:57
'''
# task hello execution time 1 second
# task world execution time 2 seconds

## Executing the codes in concurrent manner
## meaning it starts at the same time or exists at the same time


# main will serve as the main entry point
async def main():

    # asyncio.create_task makes the functions
    # runs in concurrent manner
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print('started at', time.strftime('%X'))

    await task1
    await task2

    print('finished at', time.strftime('%X'))


# output
'''
started at 17:33:30
hello
world
finished at 17:33:33
'''

# both started at 17:33:30
# @31 , task 1 has 1/1 second delay done, prints hello
# @31, task 2 has 1/2 second delay started

# @32, task 1 done execution
# @32, task 2  2/2 second delay done, prints world
