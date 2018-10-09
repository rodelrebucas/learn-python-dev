import asyncio

def is_prime(n):
    # range starts x - 1 (e.g x = 9, range starts 8,7,...)
    # excluding itself (x) in the range
    # also excluding 1 (2nd paramater to range)
    # starts backward,  -1, so (8,7,6..)

    # prime is only divisible by itself and 1
    # so we have excluded both of these
    # if divisible is found within the excluded range
    # then n is not prime
    return not any(n%i == 0 for i in range(n-1, 1, -1))


async def highest_prime_below(n):
    print(f"Highest prime below {n}")
    for y in range(n-1, 0, -1):
        await asyncio.sleep(0)
        if is_prime(y):
            print(f"Highest prime below {n} is {y}")
            return y
    return None



async def main():

    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ])
   


# Run the loop and pass the entry point 
# asyncio.run(main())

# or
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()