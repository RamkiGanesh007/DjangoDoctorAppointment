# Django Doctor Appointment

A Minimalistic Django Doctor Appointment App.

## Installation 

This Project assumes that the python 3.X is pre-installed.
 
The Script the root folder will install all the requirements and runs the server on [Address](https://127.0.0.5:80) .
### Linux and Windows (Script)
```
./start.sh
```
### Linux (Manual)
```
sudo apt-get -y install build-essential
sudo apt-get -y install libsqlite3-dev
sudo apt-get -y install sqlite3
sudo apt-get -y install bzip2 libbz2-dev
sudo apt-get -y install python3-pip
sudo pip3 install -r requirements.txt
```
### Windows(Manual)
```
pip3 install -r requirements.txt
```

## Usage

### Linux

```
cd polyclinic/
python3 manage.py makemigrations
python3 manage.py migrate
sudo python3 manage.py runserver 127.0.0.5:80;

```
### Windows

```
cd polyclinic/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.5:80;
```

## Contributions

When contributing to this repository, please first discuss the change you wish to make via issue, email and directly submit a PR.


