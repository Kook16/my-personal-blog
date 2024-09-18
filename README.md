# Django Blog Project

This is a Django-based blog application that allows users to view blog posts, leave comments, and save posts for later reading. It includes features like a homepage with recent posts, a detailed post view with comments, and a session-based "Read Later" functionality.

## Features

- **Homepage (Starting Page):** Displays the three most recent blog posts.
- **All Posts Page:** Shows a list of all blog posts, ordered by the date they were published.
- **Single Post View:** Allows users to read a full post, view associated tags, and leave comments.
- **Comments:** Users can submit comments on blog posts. Comments are displayed in reverse chronological order (newest first).
- **Read Later:** Users can save blog posts for later reading, and their selections are stored in the session.

## Project Structure

.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       ├── css
│   │       └── images
│   ├── templates
│   │   └── blog
│   │       ├── all-posts.html
│   │       ├── index.html
│   │       ├── post-detail.html
│   │       └── stored-posts.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── README.md
├── requirements.txt
└── db.sqlite3


### Important Files:

- **`views.py`:** Contains the class-based views for handling the logic behind displaying posts, comments, and saved posts.
- **`models.py`:** Defines the models for `Post`, `Author`, `Tag`, and `Comment`.
- **`forms.py`:** Contains the `CommentForm` used for handling comment submissions.
- **`urls.py`:** Defines the URL patterns for the blog, linking them to their respective views.

## URL Routes

- `/`: The homepage showing the three most recent posts.
- `/post/`: Displays all posts in reverse chronological order.
- `/post/<slug>/`: Displays a single post, allowing users to read it and leave comments.
- `/read-later/`: Shows posts that the user has saved for later reading.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kook16/my-personal-blog.git

2. Navigate into the project directory:
    cd django-blog
3. Install the required dependencies:
    pip install -r requirements.txt
4. Run migrations:
    python manage.py migrate
5. Create a superuser (optional, for accessing the Django admin panel):
    python manage.py createsuperuser
6. Start the development server:
    python manage.py runserver

## Usage
- Homepage (Starting Page): Displays the three most recent blog posts.
- All Posts: Lists all posts in reverse chronological order.
- Single Post View: View a detailed post, comment on it, and view the post's tags.
- Read Later: Save posts to the session and access them later from the "Read     
  Later" page.

## How to Add Comments
1. Navigate to any post detail page (e.g., /post/<slug>/).
2. Scroll to the bottom to find the comment form.
3. Submit your comment, and it will appear below the post.


## Read Later Functionality
The "Read Later" feature allows users to save posts to their session. Posts saved for later can be accessed via the /read-later/ route.

  - Saving a Post: On the post detail page, click "Save for Later". This will     
    store the post ID in the session.
  - Removing a Post: Clicking the "Remove from Saved" button will remove the post 
   from the saved list.

## Models
1. Post:
    - Represents a blog post.
    - Fields: title, excerpt, content, date, author, tags, etc.
2. Author:
    - Represents the author of a post.
    - Fields: name, email.
3.Tag:
    - Represents a tag associated with a post.
    - Field: name.
4. Comment:
    - Represents a comment left by a user on a post.
    - Fields: user_name, user_email, text, post.
## Author
- Email: kookcalvinayen@gmail.com


### Key Sections:
- **Introduction**: Overview of the project.
- **Features**: What the project offers.
- **Installation**: Steps to set up the project locally.
- **Usage**: How to interact with the website.
- **Read Later**: Explanation of how the "Read Later" functionality works.
- **Models**: Overview of the Django models used in the project.

