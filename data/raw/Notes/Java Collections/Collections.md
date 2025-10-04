# Collections Class

### Methods

- `boolean addAll(Collection c, T... elements)`  
  Add all the elements to a collection, e.g., `Collections.addAll(fruits, "Apples", "Oranges", "Banana")`.

- `void sort(List list)`  
  Sorts the specified List into ascending order, according to the natural ordering of its elements.

- `int frequency(Collection c, Object o)`  
  Returns the frequency of an object in a collection of objects.

- `void shuffle(List list)`  
  Randomly permutes the specified list using a default source of randomness.

- `int binarySearch(List list, Object key)`  
  Searches the specified List for the specified Object using the binary search algorithm.

- `void copy(List dest, List src)`  
  Copies all of the elements from one List into another.

- `void fill(List list, Object o)`  
  Replaces all of the elements of the specified List with the specified element.

- `Object max(Collection coll)`  
  Returns the maximum element of the given Collection, according to the natural ordering of its elements.

- `Object min(Collection coll)`  
  Returns the minimum element of the given Collection, according to the natural ordering of its elements.

- `List nCopies(int n, Object o)`  
  Returns an immutable List consisting of `n` copies of the specified Object.

- `void reverse(List l)`  
  Reverses the order of the elements in the specified List.

- `Queue asLifoQueue(Deque deque)`  
  Returns a view of Deque as a Last-in-first-out (LIFO) Queue.

- `Comparator reverseOrder()`  
  Returns a Comparator that imposes the reverse of the natural ordering on a collection of Comparable objects.

- `boolean disjoint(Collection c1, Collection c2)`  
  Returns true if the two specified collections have no elements in common.

- `Collection checkedCollection(Collection c, Class type)`  
  Provides a dynamically typesafe view of the provided collection, e.g., `Collection checkedList = Collections.checkedCollection(list, String.class)`.

- `int indexOfSubList(List source, List target)`  
  Returns the starting position of the first occurrence of the specified target list within the specified source list, or -1 if there is no such occurrence.

- `void sort(List list, Comparator c)`  
  Sorts the specified List according to the order induced by the specified Comparator.

- `int binarySearch(List list, Object key, Comparator c)`  
  Searches the specified List for the specified Object using the binary search algorithm.

- `Object max(Collection coll, Comparator comp)`  
  Returns the maximum element of the given Collection, according to the order induced by the specified Comparator.

- `Object min(Collection coll, Comparator comp)`  
  Returns the minimum element of the given Collection, according to the order induced by the specified Comparator.
