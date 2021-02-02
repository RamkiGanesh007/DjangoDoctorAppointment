#!/bin/bash
case "$OSTYPE" in
  solaris*) echo "UnSupported Operating System" ;;
  darwin*)  echo "UnSupported Operating System" ;; 
  linux*)   echo "Updating the apt...."
sudo apt-get update
sudo apt-get -y install build-essential
sudo apt-get -y install libsqlite3-dev
sudo apt-get -y install sqlite3
sudo apt-get -y install bzip2 libbz2-dev
sudo apt-get -y install python3-pip
sudo pip3 install -r requirements.txt
cd polyclinic/
python3 manage.py makemigrations
python3 manage.py migrate
sudo python3 manage.py runserver 127.0.0.5:80;;
  bsd*)     echo "UnSupported Operating System" ;;
  msys*)
  pip3 install -r requirements.txt
  cd polyclinic/
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver 127.0.0.5:80;;
  *)        echo "unknown: $OSTYPE" ;;
esac
