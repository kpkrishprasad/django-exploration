SHELL=bash
# run:
# 	source venv/bin/activate; \
# 		cd tutorial; \
# 		python3 manage.py runserver

	
setup: 
	python3 -m venv venv
	source venv/bin/activate; \
		pip install -r requirements.txt; \



clean:
	rm -rf venv
	 	
freeze:
	source venv/bin/activate; \
		pip freeze > requirements.txt

tutorial-bootstrap:
	source venv/bin/activate; \
		django-admin startproject todo; \
		cd todo; \
		django-admin startapp todo_api; \
			python3 manage.py migrate; 
	

