# Fun Share App

A social platform built with Django where users can share their fun moments through text and photos.

## About

Fun Share is a web application that allows users to:
- Share fun moments with text and photos
- View other users' shared moments
- Edit and delete their own posts
- Interact with a clean, responsive interface

## Features

- 📝 Text posts with photo uploads
- 👤 User authentication
- 🖼️ Image handling
- 📱 Responsive design
- ⚡ Fast and intuitive interface
- 🔒 Secure user content management

## Tech Stack

- **Backend**: Django 4+
- **Frontend**: Bootstrap 5
- **Database**: SQLite3
- **Image Storage**: Django's Media Handler
- **Authentication**: Django Auth

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fun_app.git
   cd fun_app
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/funs/` to start sharing fun moments!

## Project Structure

```
fun_app/
├── sh_fun/              # Main app directory
│   ├── templates/       # HTML templates
│   ├── models.py        # Data models
│   ├── views.py         # View logic
│   └── urls.py          # URL patterns
├── media/               # User uploads
├── static/              # Static files
└── manage.py           # Django management
```

## Usage

1. Register or log in to your account
2. Click "Share Your Fun" to create a new post
3. Add text and optionally upload a photo
4. View all posts on the home page
5. Edit or delete your own posts using the buttons provided

## Development

Want to contribute? Great! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---
Made with ❤️ using Django
