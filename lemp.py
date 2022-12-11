# Import the subprocess module to run system commands
import subprocess

# Create the Docker Compose configuration file
with open("docker-compose.yml", "w") as f:
    f.write("""
version: '3'

services:
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - ./nginx/log:/var/log/nginx
      - ./nginx/html:/usr/share/nginx/html
    depends_on:
      - php
    networks:
      - web
  php:
    build: ./php
    volumes:
      - ./php/app:/app
    networks:
      - web
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_DATABASE: app
      MYSQL_ROOT_PASSWORD: root
    volumes:
      - ./mysql/data:/var/lib/mysql
    networks:
      - web

networks:
  web:
    driver: bridge
""")

# Build and start the LEMP stack using Docker Compose
subprocess.run(["docker-compose", "build"])
subprocess.run(["docker-compose", "up", "-d"])
