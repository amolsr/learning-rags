# Comparator

(Used for customized sorting order)
_It is present in java.util package. It contains two methods compare() and equals() method._

`public int compare(Object obj1, Object obj2)`

- returns negative iff obj1 has to come before obj2
- returns positive iff obj1 has to come after obj2
- returns zero if both are equal.

`public boolean equals()`

- It is optionable to implement as if already implemented in java.lang.Object class.

Example->
```
class Job 
{ 
    int start, finish, profit; 
  
    // Constructor 
    Job(int start, int finish, int profit) 
    { 
        this.start = start; 
        this.finish = finish; 
        this.profit = profit; 
    } 
} 
  
// Used to sort job according to finish times 
class JobComparator implements Comparator<Job> 
{ 
    public int compare(Job a, Job b) 
    { 
        return a.finish < b.finish ? -1 : a.finish == b.finish ? 0 : 1; 
    } 
}
```
