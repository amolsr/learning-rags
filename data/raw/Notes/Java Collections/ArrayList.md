# ArrayList Class

(ArrayList and Vector implements RandomAccess interface for same access time for every element. ArrayList is worst for insertion or removal due to shifting)

### Constructors

- ArrayList l = new ArrayList(); (default size is 10 afterwards x\*3/2 +1)
- ArrayList l = new ArrayList(int initialcapacity);
- ArrayList l = new ArrayList(Collection c);

### ArrayList Vs Vector

- ArrayList is non synchronised so multiple threads are allowed to operate in ArrayList Object and hence ArrayList is not thread safe also performance is high.
- Vector is synchronised so only one thread is allowed to operate on Vector Object hence it is thread safe but performance is low.
- For synchornised version of ArrayList:- List l = Collections.synchronisedList(new ArrayList()) (or any other list) similarly for map and set method is also avalaible in Collections
