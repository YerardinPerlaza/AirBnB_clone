## AirBnB_clone

### Description
This is the first step towards our first full web application: the AirBnB clone.
We've developed a command interpreter that can be activated and perform certain tasks on object instances of different classes, according to user input.

### Installation
```
git clone git@github.com:YerardinPerlaza/AirBnB_clone.git
```
### Command interpreter usage
Interactive mode
```
$ ./console.py
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) quit
```

Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
$ echo "create User" | ./console.py
(hbnb) 1688806b-ba54-4a86-aed7-5e24a07f5bf4
(hbnb)
$ echo "create BaseModel" | ./console.py
(hbnb) 4a130742-b6a2-4e55-b6ba-a00830a1f637
(hbnb)
$
```

### Command interpreter commands

| Commands | Usage | Function |
| :---: | :---: | :---: |
| `help` | help | displays all commands available |
| `create` | create \<class> | creates a new instance |
| `destroy` | destroy \<class> | deletes an existing instance |
| `update` | placeholder text | updates an attribute of an existing instance |
| `all` | all | prints a string representation of all instances |
| `show` | placeholder text | prints a string representation of an instance |
| `quit` | quit | exits the command interpreter |
  
### Existing classes
* Basemodel
* User
* State
* City
* Amenity
* Place
* Review

### Authors

[![name](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/YerardinPerlaza) Yerardin Perlaza
[![name](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/SantiagoHolber) Santiago Cano
