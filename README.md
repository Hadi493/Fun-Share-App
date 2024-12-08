# Fun Share App

A Django-based social sharing application where users can share fun moments with others.

## Project Status

 **This is a learning project currently under development** 
 *Complete V1.0.0*

## Features

- User Authentication (Login/Register)
- Create, Read, Update, Delete fun posts
- Image upload support
- Mobile-friendly design
- Dark mode support

## Tech Stack

- Python 3.12
- Django
- Bootstrap 5
- SQLite3

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

```
fun_app/
├── manage.py
├── templates/
│   └── index.html
├── sh_fun/
│   ├── templates/
│   │   ├── fun_list.html
│   │   ├── fun_detail.html
│   │   ├── create_fun.html
│   │   ├── fun_edit.html
│   │   └── fun_delete.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── static/
    └── style.css
```

## Contributing

This is a personal learning project, but suggestions and feedback are welcome!
