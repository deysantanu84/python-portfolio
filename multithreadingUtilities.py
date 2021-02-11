# References:
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Daemon_join_method_threads.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Event_Objects_between_Threads.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Enumerating_Active_threads.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_Timer_Object.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_RLock_Objects_ReEntrant_Locks.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Condition_Objects_Producer_Consumer.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Semaphore_Objects_Thread_Pool.php
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Thread_Local_Specific_Data.php
# https://www.geeksforgeeks.org/joining-threads-in-python/


# Multiple threads share the same data space along with the main thread within a process.
# Hence, they can easily share information or can communicate with each other unlike if they were processes.
# Also known as light weight processes, they require less memory overhead and hence are cheaper than processes.
# Multi threading is defined as the ability to execute multiple threads simultaneously or concurrently.
# More than one thread can exist in a single process where:
# The register set and local variables of each thread are stored in the stack.
# The global variables (stored in the heap) and the program codes are shared among all the threads.

import logging
import queue
from random import randint, random
from threading import (Condition,
                       current_thread,
                       currentThread,
                       enumerate,
                       Event,
                       local,
                       Lock,
                       RLock,
                       Semaphore,
                       Thread,
                       Timer)
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def n():
    logging.debug('Starting')
    logging.debug('Exiting')


def d():
    logging.debug('Starting')
    # without sleep, daemon thread exits along with __main__, as well
    time.sleep(5)
    logging.debug('Exiting')


def daemonNonDaemonThreads():
    nonDaemonThread = Thread(name='non-daemon', target=n)
    daemonThread = Thread(name='daemon', target=d)
    daemonThread.setDaemon(True)
    daemonThread.start()
    nonDaemonThread.start()
    # join() ensures both daemon and non-daemon threads exit before __main__ exits
    # join() blocks calling thread indefinitely until the thread exits -
    # either normally or through an unhandled exception -
    # or until the optional timeout occurs
    # If thread does not complete within the timeout, join() exits
    # if join() times out, call isAlive() to handle
    daemonThread.join(timeout=7)
    # daemonThread.join(timeout=3.0)
    if daemonThread.is_alive():
        print('daemon thread timed out')
    else:
        print('daemon thread did not time out')

    nonDaemonThread.join()


class connectionThreadClass(Thread):
    StopEvent = 0

    def __init__(self, args):
        Thread.__init__(self)
        self.StopEvent = args

    # The run method is overridden to define the thread body
    def run(self):
        for i in range(1, 10):
            if self.StopEvent.wait(0):
                print("Asked to stop")
                break

            print("The Child Thread sleep count is %d" % i)
            time.sleep(3)

        print("A Child Thread is exiting")


def childThreads():
    Stop: Event = Event()
    connObj = connectionThreadClass(Stop)
    connObj.start()
    print("\nMain thread is starting to wait for 5 seconds")

    connObj.join(5)
    print("Main thread says : I cannot wait for 5 seconds for the child thread;\n"
          "Will ask child thread to stop")

    # ask(signal) the child thread to stop
    Stop.set()

    # wait for the child thread to stop
    connObj.join()
    # A run time error occurs when join() method is invoked on the same thread
    # as calling join() on the same thread results in a deadlock condition.
    # If the join() method is called on a thread which is yet to be started , then a run time error is raised.

    print("Main thread says : Now I do something else to compensate the child thread task and exit")
    print("Main thread is exiting")


# Event object is one of the simplest mechanisms for communication between threads:
# one thread signals an event and other threads wait for it
# An Event manages an internal flag that callers can either set() or clear()
# Other threads can wait() for the flag to be set(). Note that the wait() method blocks until the flag is true
def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait(timeout=None)
    logging.debug('event set: %s', event_is_set)


# The wait() method takes an argument representing the number of seconds to wait for the event before timing out.
# It returns a boolean indicating whether or not the event is set, so the caller knows why wait() returned.
# The isSet() method can be used separately on the event, and it's a non-blocking call.
# The wait(timeout=None) blocks until the internal flag is true by the set() method.
# If the internal flag is true on entry, return immediately.
# Here, we're not setting it on entry but we're doing it much later.
# If not set, the wait() blocks until another thread calls set() to set the flag to true
# or until the optional timeout occurs.
# wait() returns true if and only if the internal flag has been set to true,
# either before the wait call or after the wait starts, so it will always return True
# except if a timeout is given and the operation times out.
# wait_for_event_timeout() checks the event status without blocking indefinitely since timeout is given, e.wait(t).
# However, the wait_for_event() blocks on the call to wait() does not return until the event status changes.
def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(timeout=t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other things')


def eventThreads():
    e = Event()
    t1 = Thread(name='blocking',
                target=wait_for_event,
                args=(e,))
    t1.start()

    t2 = Thread(name='non-blocking',
                target=wait_for_event_timeout,
                args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Event is set')


# It is not necessary to retain an explicit handle to all of the daemon threads in order to ensure
# they have completed before exiting the main process.
# threading.enumerate() returns a list of all Thread objects currently alive.
# The list includes daemonic threads, dummy thread objects created by current_thread(), and the main thread.
# It excludes terminated threads and threads that have not yet been started.
def f():
    # t = currentThread()
    r = randint(1, 10)
    logging.debug('sleeping %s', r)
    time.sleep(r)
    logging.debug('ending')
    return


def threadEnumeration():
    for i in range(3):
        t = Thread(target=f)
        t.setDaemon(True)
        t.start()

    main_thread = current_thread()
    for t in enumerate():
        if t is main_thread:
            continue
        logging.debug('joining %s', t.getName())
        t.join()


# Control of access to shared resources is necessary to prevent corruption of data.
# In other words, to guard against simultaneous access to an object, we need to use a Lock object.
# A primitive 'lock' is a synchronization primitive that is not owned by a particular thread when locked.
# In Python, it is currently the lowest level synchronization primitive available,
# implemented directly by the _thread extension module.
# A primitive lock is in one of two states, "locked" or "unlocked".
# It is created in the unlocked state. It has two basic methods, acquire() and release().
# When the state is unlocked, acquire() changes the state to locked and returns immediately.
# When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked,
# then the acquire() call resets it to locked and returns.
# The release() method should only be called in the locked state;
# it changes the state to unlocked and returns immediately.
# If an attempt is made to release an unlocked lock, a RuntimeError will be raised.
class threadLockClass(object):
    def __init__(self, start=0):
        self.lock = Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            self.value = self.value + 1
        finally:
            logging.debug('Released a lock')
            self.lock.release()


def lockedThreadWorker1(c):
    for i in range(2):
        r = random()
        logging.debug('Sleeping %0.02f', r)
        time.sleep(r)
        c.increment()
    logging.debug('Done')


def lockingThreadResources1():
    counter = threadLockClass()
    for i in range(2):
        t = Thread(target=lockedThreadWorker1, args=(counter,))
        t.start()

    logging.debug('Waiting for worker threads')
    main_thread = currentThread()
    for t in enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d', counter.value)


# lockedThreadWorker2() tries to acquire the lock three separate times,
# and counts how many attempts it has to make to do so. In the mean time,
# threadLocker() cycles between holding and releasing the lock,
# with short sleep in each state used to simulate load.
def threadLocker(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Locking')
            time.sleep(1.0)
        finally:
            logging.debug('Releasing')
            lock.release()
        time.sleep(1.0)


def lockedThreadWorker2(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        acquired = lock.acquire(0)
        try:
            num_tries += 1
            if acquired:
                logging.debug('Try #%d : Acquired',  num_tries)
                num_acquires += 1
            else:
                logging.debug('Try #%d : Not acquired', num_tries)
        finally:
            if acquired:
                lock.release()
    logging.debug('Done after %d tries', num_tries)


def lockingThreadResources2():
    lock = Lock()
    locker = Thread(target=threadLocker, args=(lock,), name='Locker')
    locker.setDaemon(True)
    locker.start()
    worker = Thread(target=lockedThreadWorker2, args=(lock,), name='Worker')
    worker.start()


# The Timer is a subclass of Thread. Timer class represents an action that should be run
# only after a certain amount of time has passed. A Timer starts its work after a delay,
# and can be canceled at any point within that delay time period.
# Timers are started, as with threads, by calling their start() method.
# The timer can be stopped (before its action has begun) by calling the cancel() method.
# The interval the timer will wait before executing its action may not be exactly
# the same as the interval specified by the user.
def helloTimer():
    print("hello, Timer")


def timerThreads1():
    t = Timer(interval=3.0, function=helloTimer)
    t.start()


def timerThreadFunc():
    logging.debug('thread function running')
    return


# second timer(t2) is never run because it is canceled before its wake-up
def timerThreads2():
    t1 = Timer(interval=5, function=timerThreadFunc)
    t1.setName('t1')
    t2 = Timer(interval=5, function=timerThreadFunc)
    t2.setName('t2')

    logging.debug('starting timers...')
    t1.start()
    t2.start()

    logging.debug('waiting before canceling %s', t2.getName())
    time.sleep(2)
    logging.debug('canceling %s', t2.getName())
    print('before cancel t2.is_alive() = ', t2.is_alive())
    t2.cancel()
    time.sleep(2)
    print('after cancel t2.is_alive() = ', t2.is_alive())

    t1.join()
    t2.join()

    logging.debug('done')


# A code is re-entrant if it can be safely called again.
# In other words, re-entrant code can be called more than once, even though called by different threads,
# it still works correctly. So, the re-entrant section of code usually uses local variables only
# in such a way that each and every call to the code gets its own unique copy of data.
# Re-entrant methods are more constrained than thread-safe methods.
# This is because it is safe to call re-entrant methods simultaneously from multiple threads
# only if each invocation results only in unique data being accessed, such as local variables.
"""
# Non-entrant code:
g_var = 1

def f1():
  g_var = g_var + 2;
  return g_var;

def f2():
  return f1() + 2;

# If two concurrent threads access g_var, the result depends on the time of execution of each thread.
# Re-entrant code:
def f(i): 
   return i + 2 

def h(i): 
   return f(i) + 2; 
"""


# Normal Lock objects cannot be acquired more than once, even by the same thread.
# This can introduce undesirable side-effects if a lock is accessed by more than one function
# in the same call chain
def lockingThreadConstraint1():
    lock = Lock()
    print('First try :', lock.acquire())  # Defaults: blocking=True, timeout=-1
    print('Second try:', lock.acquire(timeout=0))
    print("print this if not blocked...")


def lockingThreadConstraint2():
    lock = Lock()
    print('First try :', lock.acquire())  # Defaults: blocking=True, timeout=-1
    print('Second try:', lock.acquire())  # Defaults: blocking=True, timeout=-1
    print("print this if not blocked...")


def reEntrantThreadLocks1():
    lock = RLock()
    print('First try :', lock.acquire())  # Defaults: blocking=True, timeout=-1
    print('Second try:', lock.acquire(timeout=0))


def reEntrantThreadLocks2():
    lock = RLock()
    print('First try :', lock.acquire())  # Defaults: blocking=True, timeout=-1
    print('Second try:', lock.acquire())  # Defaults: blocking=True, timeout=-1


# All of the objects provided by a module that has acquire() and release() methods
# can be used as context managers for a with statement.
# The acquire() method will be called when the block is entered,
# and release() will be called when the block is exited
"""
with some_lock:
    # do something...

# is equivalent to:
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
"""


# Locks implement the context manager API and are compatible with the 'with' statement.
# By using locks in the 'with' statement, we do not need to explicitly acquire and release the lock
def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_not_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


def contextLocks():
    lock = Lock()
    w = Thread(target=worker_with, args=(lock,))
    nw = Thread(target=worker_not_with, args=(lock,))

    w.start()
    nw.start()


# Synchronizing threads: using a Condition object.
# Because a condition variable is always associated with some kind of lock,
# it can be tied to a shared resource.
# A lock can be passed in or one will be created by default.
# Passing one in is useful when several condition variables must share the same lock.
# The lock is part of the condition object: we don't have to track it separately.
# So, the condition object allows threads to wait for the resource to be updated.
# Here, the consumer threads wait for the 'Condition' to be set before continuing.
# The producer thread is responsible for setting the condition and
# notifying the other threads that they can continue.
# We do not use acquire() and release() methods at all since we utilized the lock object's
# context manager function. Instead, our threads used 'with' to acquire the lock associated with the 'Condition'.
# The wait() method releases the lock, and then blocks until
# another thread awakens it by calling notify() or notify_all().
# Note that the notify() and notify_all() methods don't release the lock;
# this means that the thread or threads awakened will not return from their wait() call immediately,
# but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock.
# The typical programming style using condition variables uses the lock
# to synchronize access to some shared state; threads that are interested in
# a particular change of state call wait() repeatedly until they see the desired state,
# while threads that modify the state call notify() or notify_all()
# when they change the state in such a way that it could possibly be a desired state for one of the waiters.
"""
# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()

# Produce one item
with cv:
    make_an_item_available()
    cv.notify()
"""


def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer consumed the resource')


def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()


def consumerProducerThreads1():
    condition = Condition()
    cs1 = Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = Thread(name='consumer2', target=consumer, args=(condition,))
    pd = Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()


# Here, Consumer and Producer threads runs indefinitely while checking the status of the queue.
# The Producer thread is responsible for putting items into the queue if it is not full
# while the Consumer thread consumes items if there are any
BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)


class ProducerThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        # while True:
        for i in range(3):
            if not q.full():
                item = randint(1, 10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random())


class ConsumerThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        # while True:
        for i in range(3):
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random())


# Since the Queue has a Condition and that condition has its Lock we don't need to bother about Condition and Lock.
# Producer uses Queue.put(item[, block[, timeout]]) to insert data in the queue.
# It has the logic to acquire the lock before inserting data in queue.
# If optional args block is true and timeout is None (the default),
# block if necessary until a free slot is available.
# If timeout is a positive number, it blocks at most timeout seconds and
# raises the Full exception if no free slot was available within that time.
# Otherwise (block is false), put an item on the queue if a free slot is immediately available,
# else raise the Full exception (timeout is ignored in that case).
# put() checks whether the queue is full, then it calls wait() internally and so producer starts waiting
# Consumer uses Queue.get([block[, timeout]]), and it acquires the lock before removing data from queue.
# If the queue is empty, it puts consumer in waiting state
# Queue.get() and Queue.get() has notify() method
def consumerProducerThreads2():
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)


# Semaphore objects: This is one of the oldest synchronization primitives in the history of computer science,
# invented by the early Dutch computer scientist Edsger W. Dijkstra
# (he used the names P() and V() instead of acquire() and release())
# A semaphore manages an internal counter which is decremented by each acquire() call
# and incremented by each release() call. The counter can never go below zero;
# when acquire() finds that it is zero, it blocks, waiting until some other thread calls release()
# There are many cases we may want to allow more than one worker access to a resource
# while still limiting the overall number of accesses.
# For example, we may want to use semaphore in a situation where we need to support
# concurrent connections/downloads. Semaphores are also often used to guard resources
# with limited capacity, for example, a database server
class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def semaphoreThread(semaphore, pool):
    logging.debug('Waiting to join the pool')
    with semaphore:
        name = currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.5)
        pool.makeInactive(name)


# Here, the ThreadPool class tracks which threads are able to run at a given moment.
# A real resource pool would allocate a connection or some other value to the newly active thread,
# and reclaim the value when the thread is done.
# Here it is used just to hold the names of the active threads to show that only 10 are running concurrently
def threadSemaphores():
    pool = ThreadPool()
    s = Semaphore(3)
    for i in range(10):
        t = Thread(target=semaphoreThread, name='thread_' + str(i), args=(s, pool))
        t.start()


# Thread-local data is data whose values are thread specific.
# To manage thread-local data, just create an instance of local (or a subclass) and store attributes on it
# mydata = threading.local()
# mydata.x = 1
# The instance's values will be different for separate threads
# While some resources need to be locked so multiple threads can use them,
# others need to be protected so that they are hidden from the views of threads that do not "own" them.
# The local() function creates an object capable of hiding values from view in separate threads
# local_data.value is not set for any thread until it is set in that thread
def showThreadLocalData(data):
    try:
        val = data.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def threadLocalFunc(data):
    showThreadLocalData(data)
    data.val = randint(1, 100)
    showThreadLocalData(data)


def threadLocalUsage1():
    dt = local()
    showThreadLocalData(dt)
    dt.val = 999
    showThreadLocalData(dt)

    for i in range(2):
        t = Thread(target=threadLocalFunc, args=(dt,))
        t.start()


# To initialize the settings so all threads start with the same value,
# we need to use a subclass and set the attributes in __init__()
class threadLocalClass(local):
    def __init__(self, value):
        logging.debug('Initializing %r', self)
        self.val = value


def threadLocalUsage2():
    data = threadLocalClass(999)
    showThreadLocalData(data)

    for i in range(2):
        t = Thread(target=threadLocalFunc, args=(data,))
        t.start()


if __name__ == '__main__':
    # daemonNonDaemonThreads()
    # childThreads()
    # eventThreads()
    # threadEnumeration()
    # lockingThreadResources1()
    # lockingThreadResources2()
    # timerThreads1()
    # timerThreads2()
    # lockingThreadConstraint1()
    # lockingThreadConstraint2()
    # reEntrantThreadLocks1()
    # reEntrantThreadLocks2()
    # contextLocks()
    # consumerProducerThreads1()
    # consumerProducerThreads2()
    # threadSemaphores()
    # threadLocalUsage1()
    threadLocalUsage2()
