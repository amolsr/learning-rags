# Vector

ResizableArray or growable array. Duplication is allowed. Insertion order is presearved. null insertion is possible. Hetrogenous object is allowed. Implements RandomAccess, seriablisable and clonable interface. Most methods is synchronised and vector is thread safe. Suited if frequent operation is retrival.

### Methods

- void addElement(Object o)
- void removeElement(Object o)
- void removeElementAt(int index)
- void removeAllElement()
- Object elementAt(int index)
- Object firstElement()
- Object lastElement()
- int size(); current size
- int capacity(); total size
- Enumeration elements();

### Constructors

- Vector v = new Vector(); //default size is 10 then 2 \* current capacity
- Vector v = new Vector(int initialCapacity);
- Vector v = new Vector(int initialcapacity, int incrementalCapacity);
- Vector v = new Vector(Collection c);
