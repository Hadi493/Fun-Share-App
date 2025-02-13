# Fun-Share-App

A Django-based social media platform for sharing fun moments and connecting with friends.

## Project Status

 **This is a learning project currently under development** 
*and Complete V1.0.0*

## Features

- User authentication with GitHub OAuth
- Share posts with images and text
- Like and comment on posts
- User profiles
- Mobile-responsive design
- Dark mode support

## Technology Stack

- Django 5.1
- Python 3.x
- SQLite3
- HTML/CSS
- Social Auth Django

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Fun-Share-App.git
cd Fun-Share-App
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
- Create a `.env` file in the project root
- Add your GitHub OAuth credentials:
  ```
  SOCIAL_AUTH_GITHUB_KEY=your_github_client_id
  SOCIAL_AUTH_GITHUB_SECRET=your_github_client_secret
  ```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

## Project Structure

```
Fun-Share-App/
├── fun_app/          # Main project directory
├── sh_fun/          # Main application directory
├── static/          # Static files (CSS, JS, images)
├── media/          # User uploaded files
├── templates/      # HTML templates
└── manage.py       # Django management script
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
