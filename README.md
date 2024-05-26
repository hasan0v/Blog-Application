# Blog Application

This is a Django-based blog application that allows users to create, read, update, and delete blog posts. The application also includes features for categorizing posts, liking posts, and viewing detailed information about each post.

## Features

- **Home Page**: Displays a list of all blog posts ordered by the post date.
- **Post Detail Page**: Displays detailed information about a specific post, including who liked the post.
- **Like Post**: Allows authenticated users to like and unlike posts.
- **Categories**: Users can view posts filtered by categories.
- **Create, Update, Delete Posts**: Authenticated users can create new posts, update existing posts, and delete posts.
- **Create Categories**: Admins can create new categories.

## Technologies Used

- **Django**: Web framework used to build the application.
- **SQLite**: Default database used for development.
- **HTML/CSS**: For the front-end templates.
- **Bootstrap**: For responsive design and UI components.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hasan0v/blog-application.git
cd blog-application
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

### Home Page

The home page lists all blog posts with the newest posts first. Each post displays a title, author, and the date it was created. 

### Post Detail Page

Clicking on a post title will take you to the post detail page. Here, you can see the full content of the post, the number of likes it has received, and who has liked it.

### Liking a Post

Authenticated users can like or unlike a post by clicking the like button on the post detail page.

### Categories

You can view posts by categories by selecting a category from the category menu.

### Creating, Updating, and Deleting Posts

Authenticated users can create new posts by clicking on the "New Post" button. Posts can be edited or deleted from their respective detail pages.

### Admin Panel

Admins can create new categories and manage posts and categories through the Django admin panel, accessible at `http://127.0.0.1:8000/admin`.

## Code Overview

### Views

- **HomeView**: Lists all posts on the home page.
- **PostDetailView**: Shows detailed information about a specific post.
- **LikeView**: Handles the logic for liking and unliking a post.
- **CategoryView**: Filters posts by category.
- **PostCreateView**: Allows users to create a new post.
- **CategoryCreateView**: Allows admins to create a new category.
- **PostUpdateView**: Allows users to update an existing post.
- **PostDeleteView**: Allows users to delete a post.

### Models

- **Post**: Represents a blog post.
- **Categorie**: Represents a category that posts can belong to.

### Forms

- **PostForm**: Form for creating and updating posts.
- **EditForm**: Form for editing posts.

### Templates

- **home.html**: Template for the home page.
- **post_detail.html**: Template for the post detail page.
- **post_new.html**: Template for creating a new post.
- **category_new.html**: Template for creating a new category.
- **update_post.html**: Template for updating a post.
- **delete_post.html**: Template for deleting a post.
- **categories.html**: Template for viewing posts by category.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or inquiries, please contact me at [hasan0v](alihasanov.m@gmail.com).
