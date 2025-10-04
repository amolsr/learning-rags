# SortedSet

All objects is inserted in some sorting order.

### Methods

- Object first()
  returns the first element
- Object last()
  returns the last element
- SortedSet headSet(Object element)
  returns the set of the which is less the specified element.
- SortedSet tailSet(Object element)
  returns the set of elements which is greater than or equal to the specified element.
- SortedSet subSet(Object element, Object element)
  returns the subSet between the specified range.
- Comparator comparator()
  returns the comparator object with underlying sorted order. Returns null for default sorting order which is -
  for number Ascending
  for string alphabetical.
