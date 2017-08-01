# haystack-queryparser
Converts arbitrarily complicated user entered query strings to a haystack query object. http://aplopio.github.io/haystack-queryparser

## Usage
```python
from haystack_queryparser import ParseSQ
```

Also provides or_parser and and_parser which can be directly used with a query.

```python
parser = ParseSQ()
sq_object = parser.parse(query)
```

It optionally takes `AND` or `OR` operators.

### Input
Input should be a string. This the query.

### Output
Output is a `SQ(haystack.query.SQ)` object. This can be passed to `SearchQuerySet.filter` and the	query will be applied.

## Test
Nosetests is used as the test runner. You can invoke the tests from the root folder using:

```shell
DJANGO_SETTINGS_MODULE=tests.settings python setup.py test
```
