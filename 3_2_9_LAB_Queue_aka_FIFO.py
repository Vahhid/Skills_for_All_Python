"""
3.2.9   LAB   Queue aka FIFO

Let's try something new now. A queue is a data model characterized 
    by the term FIFO: First In – Fist Out. Note: a regular queue 
    (line) you know from shops or post offices works exactly in 
    the same way – a customer who came first is served first too.

Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns 
    it as the result (the queue cannot be empty to successfully perform it.)
Follow the hints:

    use a list as your storage (just like we did with the stack)
    put() should append elements to the beginning of the list, 
        while get() should remove the elements from the end of the list;
    
    define a new exception named QueueError (choose an exception 
        to derive it from) and raise it when get() tries to operate 
        on an empty list.

Expected output
1
dog
False
Queue error

"""

class QueueError(Queue):  # Choose base class for the new exception.
    def __init__(self):
        Queue.__init__(self)
    def chk_empty(self):
        return len(self.__lst) > 0


class Queue:
    def __init__(self):
        # Write code here
        self.__lst = []

    def put(self, elem):
        # Write code here
        self.__lst.append(elem)

    def get(self):
        # Write code here
        toServe = self.__lst[0]
        del self.__lst[0]
        return toServe


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
#print(que.get())
#print(que.get())
#print(que.get())


try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    
    
