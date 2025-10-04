# TreeSet implements BalancedTree

- Duplicates are not allowed
- Insertion order is not preserved.
- Sorting Order is preserved.
- Heterogeneous is not allowed (Run time Exception)
- Homogeneous and Comparable objects should be there
- Null is allowed but only once.

_Null Acceptance - If we want to insert null for non-empty TreeSet then compulsory Comparator is required as the TreeSet compares the object._
_Comparable is ment for default sorting order. Comparator is for user defined object._

obj1.compareTo(Obj2); (obj1 with we are trying to insert and obj2 is element already present)

### Constructors

- TreeSet t = new TreeSet(); (Elements is inserted into with default sorting order)
- TreeSet t = new TreeSet(Comparator c); (Elements are inserted as per specified comparator
- TreeSet t = new TreeSet(Collection c);
- TreeSet t = new TreeSet(SortedSet s);

### Methods for TreeSet
