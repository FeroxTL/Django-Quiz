Для критических секций в django предусмотрены атомарные транзакции (https://docs.djangoproject.com/en/1.11/topics/db/transactions/#controlling-transactions-explicitly)

```python
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
```
