# AccuKnox Django Trainee Assignment

## Question 1: Are Django Signals Synchronous?

### Conclusion

Yes, Django signals execute synchronously by default.

### Proof

A delay of 5 seconds was introduced inside the signal handler using `time.sleep(5)`. The browser response was delayed until the signal completed execution, demonstrating that Django waits for the signal handler to finish before continuing.

---

## Question 2: Do Django Signals Run in the Same Thread?

### Conclusion

Yes, Django signals run in the same thread as the caller by default.

### Proof

The thread ID printed inside the view and inside the signal handler were identical.

Example:

Thread inside view: 17032

Thread inside signal: 17032

This confirms that both execute in the same thread.

---

## Question 3: Do Django Signals Run in the Same Database Transaction?

### Conclusion

Yes, Django signals run in the same database transaction as the caller by default.

### Proof

A transaction was created using `transaction.atomic()`. After creating a model instance and triggering the signal, an exception was raised to force a rollback. After execution, both the main model and the signal-created model had zero records, proving that both operations were rolled back together.

---

## Rectangle Class Task

The Rectangle class accepts length and width during initialization and supports iteration.

Example Output:

{'length': 10}

{'width': 5}

Implementation uses Python's `__iter__()` method and generators (`yield`) to return the required values.
