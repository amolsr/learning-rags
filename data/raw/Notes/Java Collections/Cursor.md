# Cursor

Cursors are only interface hence enumeration, iterator, and listiterator doesnt have any constructor hence we can not have object directly or indirectly. interanly the corresponding method returns the annomyous inner class object.

## Enumeration

> #### Enumeration e = v.elements();
>
> _v is vector_

- boolean hasMoreElements();
- Object nextElement();
  Applicable for only legacy classes. And only retrive operation is possible.

## Iterator

Universal cursor. Read and remove is possible.
collection interface contains public Iterator iterator();

> #### Iterator itr = c.iterator;
>
> _c is any Collection Object_

- boolean hasNext();
- Object next();
- void remove();

##### Limitations

1. its a single director cursor.(forward direction)
2. read and remove is only possible while replace, add is not possible.

## ListIterator

Its a bidirectional cursor. Read, Remove, Replacement, and addition of new objects is possible.
public ListIterator listIterator() in List interface. It is child interface of ListIterator.

> #### ListIterator ltr = l.listIterator();
>
> _l is any list object_

- public boolean hasNext();
- public Object next();
- public int nextIndex();
- public boolean hasPrevious();
- public Object previous();
- public int previousIndex();
- public void remove();
- public void set(Object new);
- public void add(Object new);

##### Limitations

1. Applicable for only list objects.
