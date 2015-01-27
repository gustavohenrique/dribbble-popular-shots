all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

test: clean
	popularshots/manage.py collectstatic --noinput
	popularshots/manage.py test test

database:
	popularshots/manage.py migrate
	popularshots/manage.py syncdb

run: clean
	popularshots/manage.py runserver

