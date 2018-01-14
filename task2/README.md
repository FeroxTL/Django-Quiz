2. Как вывести на экран последнюю выполненную процедуру определенным сотрудником?

```python
user = User.objects.first()

last_procedure = None
last_execution = user.procedure_executions.order_by('-datetime_create').first()

# order_by в этом случае можно опустить т.к. в модели уже определён нужный порядок

if last_execution:
    last_procedure = last_execution.procedure

print(last_procedure)
```


3. Получить количество выполнений каждой процедуры за все время.

```python
from django.db.models import Count

annotated_list = Procedure.objects.all().annotate(total=Count('executions')).values('name', 'total')
# values только для демонстрации, создаётся атрибут у каждой модели

print(annotated_list)
```

4. Вывести на экран (print) все выполнения процедур отсортированные в обратном хронологическом порядке.

```python
qs = ProcedureExecution.objects.all().order_by('-datetime_create')
print(qs)
```

5. Количество выполнений процедур за последние 2 дня.

```python
from django.utils.timezone import now

total_executions = ProcedureExecution.objects.all().filter(datetime_create__gte=now() - timedelta(days=2)).count()
print(total_executions)
```

6. Суммарное кол-во выполнений процедур procedure1 и procedure2.

```python
total_executions = ProcedureExecution.objects.filter(procedure__in=[procedure1, procedure2]).count()
print(total_executions)
```

7. Суммарное кол-во выполнений всех процедур за любой день за исключением определенного.
Непонятно за любой выбранный день или всё же все кроме выбранного
upd: Суммарное кол-во выполнений всех процедур за ВСЕ дни за исключением определенного.

```python
exclude_day = now()

total_executions = ProcedureExecution.objects.exclude(date_create=exclude_day).count()
print(total_executions)
```
