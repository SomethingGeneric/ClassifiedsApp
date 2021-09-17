#!/bin/bash

cat >> classified.service << EOF
[Unit]
Description=Gunicorn instance to serve ClassifiedsApp
After=network.target

[Service]
User=${USER}
Group=www-data
WorkingDirectory=/home/${USER}/ClassifiedsApp
Environment="PATH=/home/${USER}/.local/bin"
ExecStart=/home/${USER}/.local/bin/gunicorn --workers 3 --bind unix:classifieds.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
EOF

cat >> nginx.site << EOF
server {
    listen 80;
    server_name your_domain www.your_domain;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/${USER}/ClassifiedsApp/classifieds.sock;
    }
}
EOF