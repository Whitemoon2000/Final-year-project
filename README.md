# Final-year-project
Game-based learning : CS quiz
CS quiz is a multi-player GBL platform. It should also provide players with a basic understanding of computing (Data structures, Arrays, and Algorithms). The main goals of this project are to promote interest in computing science and to improve the ability to solve
problems.
## Installation
First you need to clone this project to your local server

```bash
git clone https://github.com/Whitemoon2000/Final-year-project.git
```

Second you need to create the virtual environment for install different library

For example, Using anaconda prompt to activate env

```bash
conda activate env
```

And then execute the following python command:

```python
python manage.py runserver
```

## Create Super User

If want to login to Admin page, you need to create the super user account:

```python
python manage.py createsuperuser
```
Enter your desired username and press enter.


```bash
Username: admin
```

You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```bash
Password: **********
Password (again): *********
Superuser created successfully.
```


