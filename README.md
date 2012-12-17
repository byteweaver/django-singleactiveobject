#django-singleactiveobject

Model mixin that ensures there is only one active model instance in your database. 

## What is this app good for?
This might come in handy if you store some sort of configuration in your database
but want to be sure there is only one active entry at a time.

## How it works

Upon save() this will check if the current object is active=True and will set
any other active object to active=False ensuring there is only one active.

## Download/Install

### using pip

	pip install django-singleactiveobject
	
### github

	git clone https://github.com/byteweaver/django-singleactiveobject
  
## Usage

```python
from singleactiveobject.models import SingleActiveObjectMixin

class YourModel(SingleActiveObjectMixin):
  ...your stuff
```

## Testing

Just run the makefile to set up a virtual environment for testing

	make

Start the test runner

	make test
