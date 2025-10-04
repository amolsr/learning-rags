# Collection interface

implements serializable and clonable interface

### Methods

- boolean add(Object o)
- boolean addAll(Collection c)
- boolean remove(Object o)
- boolean removeAll(Collection c)
- boolean retainAll(Collection c)
- void clear()
- boolean contains(Object o)
- boolean containsAll(Collection c)
- boolean isEmpty()
- int size()
- Object[] toArray();
- Iterator iterator()

### equals() Vs hashCode()

- In java equals() method is used to compare equality of two Objects.
- hashCode() returns the hashcode value as an Integer. Hashcode value is mostly used in hashing based collections like HashMap, HashSet, HashTable….etc. This method must be overridden in every class which overrides equals() method.
- If two Objects are equal, according to the equals(Object) method, then hashCode() method must produce the same Integer on each of the two Objects.
- If two Objects are unequal, according to the equals(Object) method, It is not necessary the Integer value produced by hashCode() method on each of the two Objects will be distinct. It can be same but producing the distinct Integer on each of the two Objects is better for improving the performance of hashing based Collections like HashMap, HashTable…etc.
