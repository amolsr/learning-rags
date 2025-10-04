
# Volatile vs Synchronized in Java Multithreading

This document explains the differences between **`volatile`** and **`synchronized`** in Java multithreading.

---

## 🔹 1. `volatile`

- **What it is**:  
  A **field modifier** (applied to variables). Ensures that **reads and writes go directly to main memory**, not cached in CPU registers or thread-local memory.  

- **Guarantees**:  
  - **Visibility**: ✅ A thread reading a volatile variable sees the most recent write by another thread.  
  - **Atomicity**: ❌ Not guaranteed (except for reads/writes of primitives, including `long` and `double` since Java 5).  
  - **Ordering**: ✅ Prevents instruction reordering involving the volatile variable.  

- **When to use**:  
  - When multiple threads read/write a variable, but operations are **independent**.  
  - Useful for **flags** (e.g., stopping threads).  

- **Example**:
  ```java
  class SharedResource {
      volatile boolean flag = true;

      void runTask() {
          while (flag) {
              // do work
          }
          System.out.println("Stopped!");
      }

      void stopTask() {
          flag = false; // visible immediately to other threads
      }
  }
  ```

---

## 🔹 2. `synchronized`

- **What it is**:  
  A **keyword** applied to methods or blocks. Ensures **mutual exclusion (atomicity)** and **visibility**.  

- **Guarantees**:  
  - **Atomicity**: ✅ Only one thread can execute a synchronized block/method at a time for the same monitor.  
  - **Visibility**: ✅ Changes made by one thread are visible to others once the lock is released.  
  - **Ordering**: ✅ Locks enforce happens-before relationships.  

- **When to use**:  
  - When multiple threads modify shared state.  
  - For compound actions (read-modify-write, like `x++`, `list.add()`).  

- **Example**:
  ```java
  class Counter {
      private int count = 0;

      public synchronized void increment() {
          count++; // atomic now
      }

      public synchronized int getCount() {
          return count;
      }
  }
  ```

---

## ⚡ Key Differences

| Aspect         | `volatile`                           | `synchronized`                        |
|----------------|--------------------------------------|----------------------------------------|
| Type           | Variable modifier                    | Block/method modifier                  |
| Scope          | One variable only                    | Group of statements (critical section) |
| Visibility     | ✅ Ensures visibility                | ✅ Ensures visibility                  |
| Atomicity      | ❌ Not guaranteed (except reads/writes) | ✅ Guaranteed                          |
| Locking        | ❌ No locking (non-blocking)         | ✅ Uses lock (monitor)                 |
| Performance    | ✅ Faster (no lock overhead)         | ❌ Slower (locking overhead)           |
| Use Case       | Status flags, config values          | Counters, collections, shared state    |

---

## 👉 Summary
- Use **`volatile`** → when you only need **visibility** for simple variables (e.g., flags).  
- Use **`synchronized`** → when you need **atomicity + visibility** (for compound operations on shared state).  


# Difference Between HashMap, Hashtable, and ConcurrentHashMap

This document explains the differences between **HashMap**, **Hashtable**, and **ConcurrentHashMap** in Java.

---

## 🔹 1. HashMap
- **Thread Safety**: ❌ Not synchronized, not thread-safe. Multiple threads can cause data inconsistency.  
- **Performance**: ✅ Faster than `Hashtable` and `ConcurrentHashMap` in **single-threaded** applications.  
- **Nulls**: ✅ Allows **one null key** and **multiple null values**.  
- **Iteration**: Uses **fail-fast iterator** (throws `ConcurrentModificationException` if the map is modified while iterating).  
- **Use Case**: Best for **non-threaded applications** where speed matters.  

---

## 🔹 2. Hashtable
- **Thread Safety**: ✅ **Synchronized** → every method is synchronized. Thread-safe, but blocks entire table for every operation.  
- **Performance**: ❌ Slower than `HashMap` because of **synchronization overhead**.  
- **Nulls**: ❌ **No null key, no null values** allowed.  
- **Iteration**: Uses **enumerator** (legacy) and also **fail-fast iterators** when using `entrySet`/`keySet`.  
- **Legacy**: Considered **obsolete**, kept for backward compatibility.  
- **Use Case**: Rarely used today; replaced by `ConcurrentHashMap` for multi-threaded environments.  

---

## 🔹 3. ConcurrentHashMap
- **Thread Safety**: ✅ Thread-safe with **better concurrency** than `Hashtable`.  
   - Instead of locking the whole map, it uses **segment-based locking** (Java 7) or **bucket-level CAS-based updates** (Java 8).  
- **Performance**: ✅ Much faster than `Hashtable` in multi-threaded environments.  
- **Nulls**: ❌ **No null keys and no null values** allowed (to avoid ambiguity in concurrent settings).  
- **Iteration**: Uses **fail-safe iterators** (does not throw `ConcurrentModificationException` while iterating, but may not reflect the most recent updates).  
- **Use Case**: Best for **highly concurrent, multi-threaded applications**.  

---

## ⚡ Quick Comparison Table

| Feature               | HashMap              | Hashtable            | ConcurrentHashMap    |
|------------------------|----------------------|----------------------|----------------------|
| Thread-Safe            | ❌ No               | ✅ Yes (synchronized) | ✅ Yes (fine-grained locking / CAS) |
| Performance            | ✅ Fastest (single-threaded) | ❌ Slow (full map lock) | ✅ High concurrency |
| Null Key               | ✅ 1 allowed        | ❌ Not allowed        | ❌ Not allowed        |
| Null Values            | ✅ Multiple allowed | ❌ Not allowed        | ❌ Not allowed        |
| Iterator               | Fail-fast           | Fail-fast / Enumerator | Fail-safe           |
| Legacy or Modern       | Modern (Java 1.2+) | Legacy (Java 1.0)    | Modern (Java 5+)     |

---

## 👉 Summary
- Use **HashMap** → For single-threaded applications.  
- Use **ConcurrentHashMap** → For multi-threaded applications.  
- Avoid **Hashtable** → It’s legacy and less efficient.  
