all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

test: clean
	popularshots/manage.py collectstatic --noinput
	popularshots/manage.py test test

