# catalog
Udacity - item catalog app


## Description
This app is meant to collect food menu items. A 3rd party authentication system (Google and Facebook) is implemented to let users add, update and delete food items. Also, this app implements API endpoints, where the response format can be JSON .
This app is based upon the Flask Python framework for the back end.

## Requirements
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Python ~2.7](https://www.python.org/)


## Set Up

For an initial set up please follow these 2 steps:

1. Download or clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Find the *catalog* folder and replace it with the content of this current repository.


## Usage

Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

`vagrant ssh`

Then move inside the catalog folder:

`cd /vagrant/catalog`

Then lift the application:

`python application.py`

After the last command you are able to browse the application at this URL:

`http://localhost:8000/`

It is important you use *localhost* instead of *0.0.0.0* inside the URL address. That will prevent OAuth from failing.


## API endpoints 


Endpoints:

| Request | What you get | 
| ------------- |:-------------:|
| /restaurant/JSON | Get all restaurants |
| /restaurant/*restaurant id*/recipe/JSON	|Get menu of that restaurant|
| /restaurant/*restaurant id*/recipe/*recipe id*/JSON		|Get detail of that specific menu item from restaurant mentioned with id|
| /users | Get all registered users |



Note::
This app is not intended for commercial use. It's just for educational purpose.
