# MicroBlog

MicroBlog is a simple Flask-based web application that allows users to create and view short blog entries. It uses MongoDB for data storage and provides a clean, minimalistic interface for users to interact with their microblog entries.

## Features

- Create new blog entries
- View all entries with formatted dates
- MongoDB integration for data persistence
- Environment variable support for secure configuration
- Responsive design with custom CSS

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package manager)
- MongoDB instance (local or cloud-based)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sachinsharmak/Micro-Blog.git
    cd Micro-Blog
    ```

2. Install the required dependencies:
    ```bash
    pip install flask
    pip install pymongo[srv]
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    Create a `.env` file in the root directory and add your MongoDB URI:
    ```env
    MONGO_URI=your_mongodb_uri_here
    ```

## Usage

To run the application:

1. Ensure your MongoDB instance is running.
2. From the project root directory, run:
    ```bash
    python app.py
    ```
3. Open a web browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main application file containing Flask routes and MongoDB connection
- `templates/home.html`: Main template for the application
- `static/css/styles.css`: Custom styles for the application
- `.env`: Environment variables file (not tracked in git)

## Frontend

The frontend of MicroBlog is built with HTML and CSS:

- **HTML**: The `home.html` template in the `templates/` directory structures the content of the web page.
- **CSS**: The `styles.css` file in the `static/css/` directory provides custom styling for a responsive and user-friendly interface. It includes:
    - A color scheme defined with CSS variables
    - Responsive layout using flexbox
    - Custom styles for the header, form inputs, and blog entries
    - Media queries for different screen sizes

## Contributing

Contributions to MicroBlog are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
