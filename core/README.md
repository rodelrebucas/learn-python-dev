### Notes:

### Concurrency

    - looks like happening simultaneously on a single core, it has cooperative scheduling on python (programmer decides when to stop).

    - mainly used for I/O bound tasks since it reduces waiting time by switching to another process/task instead of waiting.

### Parallelism

    - for Cpu bound tasks. (Computations, etc..)

    - performing multiple operation at the same time.

    - Can also show concurrency by performing tasks at same time on a multi core

### Threading

    - also for I/O bound tasks

    - a unit of process or subprocess, handled by the cpu which is a pre-emptive scheduling that can be stopped anytime/anywhere as oppose to cooperative scheduling.

####

    Single core:

         - Single thread

         - Multi thread - with pre-emptive scheduling

         - Concurrency - with cooperative scheduling

    Multi core: (GIL limit)

        - Multiple threads

        - Multiple processes
