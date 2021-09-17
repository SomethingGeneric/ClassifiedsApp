python:
	pip3 install -r requirements.txt

apt:
	sudo apt update
	sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools nginx
	make python

deploy: apt
	bash util.sh
	sudo cp deployment/classified.service /etc/systemd/system/classified.service
	sudo systemctl daemon-reload
	sudo systemctl enable --now classified
	sudo cp deployment/nginx.site /etc/nginx/sites-enabled/classified.site
	sudo systemctl restart nginx

undeploy:
	sudo systemctl stop classified
	sudo systemctl disable classified
	sudo rm /etc/systemd/system/classified.service
	sudo rm /etc/nginx/sites-enabled/classified.site
	sudo systemctl daemon-reload
	
run:
	gunicorn --bind 0.0.0.0:5000 wsgi:app

test:
	python3 main.py

reset:
	rm -rf db/