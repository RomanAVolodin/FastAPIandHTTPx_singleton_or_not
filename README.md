# FastAPIandHTTPx_singleton_or_not


1. http://localhost:8000/

Выдача будет всегда одинаковая

```bash
{
  "client_id": 4434343824,
  "result": "",
  "status": 302
}
```

2. http://localhost:8000/sing

Так же как и в п.1, но лишаем себя магии Depends, которая иногда полезна.

[Здесь](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times) сказано о кешировании, но случай когда кеширование происходит довольно специфичный -

> If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.

> And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.
если у Вас получается в одном path декораторе получилось так что Вы вызвали несколько Dependency а у них общие subDependency так вот об этом шла речь, что они кешируются

3. http://localhost:8000/mul

Тут при каждом запросе будет создаваться новый инстанс AsyncClient