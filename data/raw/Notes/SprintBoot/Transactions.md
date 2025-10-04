# Transactions

Transactions are used to maintain the **ACID** properties of the database.

### ACID Properties
- **Atomicity**: Every transaction is atomic. It either executes completely or does not execute at all.  
- **Consistency**: After a transaction, the database must transition from one valid state to another, preserving integrity constraints.  
- **Isolation**: Concurrent transactions must not interfere with each other, and the final outcome should be as if they executed sequentially.  
- **Durability**: Once a transaction is committed, its results are permanently recorded in non-volatile storage and survive system crashes.  

---

## Transactions in Spring Boot

In Spring Boot, transactions are achieved by using the `@Transactional` annotation.  
It allows us to configure:
- Propagation  
- Isolation  
- Timeout  
- Read-only behavior  
- Rollback conditions  
- Transaction manager  

---

## Transaction Propagation

- **REQUIRED (default)**  
  - If there’s an active transaction, it joins it.  
  - If not, Spring creates a new one.  

- **SUPPORTS**  
  - Uses the current transaction if it exists.  
  - Otherwise, executes non-transactionally.  

- **MANDATORY**  
  - Requires an active transaction.  
  - If none exists, Spring throws an exception.  

- **NEVER**  
  - Must not run in a transaction.  
  - Throws an exception if a transaction exists.  

- **NOT_SUPPORTED**  
  - Suspends the current transaction (if any).  
  - Executes non-transactionally.  

- **REQUIRES_NEW**  
  - Suspends the current transaction (if any).  
  - Always creates a new transaction.  

- **NESTED**  
  - If a transaction exists, sets a savepoint.  
  - On rollback, only rolls back to the savepoint.  
  - If no transaction exists, behaves like REQUIRED.  

---

## Transaction Isolation

Transactions should be **isolated** to prevent concurrency issues. Without proper isolation, the following anomalies may occur:

- **Dirty Read**  
  Reading uncommitted changes of a concurrent transaction.  

- **Non-repeatable Read**  
  Getting different values when re-reading the same row after another transaction updates and commits it.  

- **Phantom Read**  
  Re-executing a range query returns different rows if another transaction adds/removes rows in that range and commits.  

### Spring Isolation Levels
Spring provides multiple isolation levels to handle the above issues:
- **READ_UNCOMMITTED**  
- **READ_COMMITTED**  
- **REPEATABLE_READ**  
- **SERIALIZABLE**  

---
