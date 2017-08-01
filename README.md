# haystack-queryparser
Converts arbitrarily complicated user entered query strings to a haystack query object. http://aplopio.github.io/haystack-queryparser

## Installation
You can install this version using:

```shell
pip install git+https://github.com/basilfx/haystack_queryparser.git
```

Alternatively, you can include it in your `requirements.txt` as

```text
-e git+https://github.com/basilfx/haystack_queryparser#egg=haystack_queryparser
```

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
