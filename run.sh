#!/bin/bash

gunicorn --threads 10 -b "www.littledot.xyz:8000" -k gthread mysite.wsgi
