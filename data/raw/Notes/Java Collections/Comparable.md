# Comparable Interface.

(It is for default sorting order)

_It is present in java.lang.package. It contains only one method. Obj1.compareTo(Object obj2)_

````public int compareTo(Object obj)
	returns -ve iff obj1 has to come before obj2.
	returns +ve iff obj1 has to come after obj2.
	returns zero if both are equal.```
````


Example -> 

```
class Job implements Comparable<Job> {
    int start, finish, profit;

    Job(int start, int finish, int profit) {
        this.start = start;
        this.finish = finish;
        this.profit = profit;
    }

    public int compareTo(Job b) {
        return finish < b.finish ? -1 : finish == b.finish ? 0 : 1;
    }
}
```
