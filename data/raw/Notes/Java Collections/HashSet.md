# HashSet

- Implementatted class of hashTable
- Duplicates are not allowed and the add method returns false
- Insertion order not preserved
- Order is according to hashcode of object
- Null insertion is possible
- Heterogeneous objects are alowed
- Implements serializale and clonable but not randomAccess
- Recommended for search operations
  _Fill ratio is after filling that ratio a new HashSet is going to be created_

### Constructors of HashSet (Same as the Hashed Data Structure)

- HashSet h = new HashSet(); (Default capacity- 16, Default fill ratio 0:75)
- HashSet h = new HashSet(int size);
- HashSet h = new HashSet(int size, float fillRatio);
- HashSet h = new HashSet(Collection c);

_Methods related to HashSet is same as Collections._
