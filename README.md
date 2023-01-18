# Freelance Developer Portfolio Website

This is a freelance developer portfolio website built using **Django 4**, **HTML 5**, **CSS 3**, **Bootstrap 5**, and **Sass**.

![plot](https://github.com/BobsProgrammingAcademy/portfolio-website-django4-bootstrap-5/blob/master/static/images/portfolio.png?raw=true)


## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the application](#run-the-application)
- [Adding data to the application](#add-data-to-the-application)
- [Customizing the application](#customize-the-application)
- [Copyright and License](#copyright-and-license)


## Prerequisites

Install the following prerequisites:

1. [Python 3.10.8 or higher](https://www.python.org/downloads/)
2. [Node.js 19.1.0 or higher](https://nodejs.org/en/)
3. [Visual Studio Code](https://code.visualstudio.com/download)


## Installation

### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

From the **root** directory run:

```bash
cd static
```
```bash
npm install
```

### 4. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 5. Create an admin user to access the Django Admin interface

From the **root** directory run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

## Run the application

From the **root** directory run:

```bash
python manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.


## Add data to the application

Add data through Django Admin.

Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.


## Customize the application

This section describes how to customize the application. 

### Changing Section Titles and Subtitles 

#### 1. About

To modify the title and subtitle of the **About** section, make changes in the ```templates/index.html``` file.

#### 2. Projects

To modify the title and subtitle of the **Projects** section, make changes in the ```templates/index.html``` file.

### Changing Colors

To modify the colors in the application, make changes in the ```static/sass/styles.scss``` file and compile the file using the **Live Sass Compiler**, which is a Visual Studio Code Extension. Remember to set the **savePath** option in the **settings.json** file (**liveSassCompile.settings.formats** section) to **static/css** so that the generated CSS file is stored in the static/css directory. 

### Changing Logo

To modify the logo in the application, make changes in the ```templates/index.html``` file.


## Copyright and License

Copyright © 2022 Bob's Programming Academy. Code released under the MIT license.
