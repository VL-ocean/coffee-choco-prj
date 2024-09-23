# Coffee & Chocolate Blog [(*Live site*)](https://coffee-choco-blog-7ff7b0b383df.herokuapp.com/)


## Introduction 

Coffee & Chocolate blog is a blog style website for those who love coffee and chocolate. Here users can find articles and recipes as well as post their own. A comments section facilitates communication between users. Only registered users can create new posts, comment and give likes, save favourite recipes or articles to read later. 

![start screen responsive](./README-images/main-responsive.png)


## Table of contents

- [Live site](#coffee--chocolate-blog-live-site)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [UX](#ux)
    - [Target Audience](#target-audience)
    - [User Goals](#user-goals)
    - [Agile Development Tool](#agile-development-tool)
    - [User Stories](#user-stories)
  - [UX design](#ux-design)
    - [Wireframe](#wireframe)
    - [Structure \& Logical Flow](#structure--logical-flow)
    - [Colour Scheme](#colour-scheme)
    - [Fonts](#fonts)
    - [Responsiveness (media queries)](#responsiveness)
  - [Security Measures and Protective Design](#security-measures-and-protective-design)
    - [User Authentication](#user-authentication)
    - [Password Management](#password-management)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Coding languages used](#coding-languages-used)
    - [Frameworks and Libraries used](#frameworks-and-libraries-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [To deploy the project to Heroku](#to-deploy-the-project-to-heroku)
    - [To fork the project](#to-fork-the-project)
    - [To clone the project](#to-clone-the-project)
  - [Credits](#credits)
    - [Colour Theme](#colour-theme)
    - [Project](#project)
    - [Articles and Recipes](#articles--recipes)
    - [Media](#media)
    - [Tools](#tools)
  - [Acknowledgements](#acknowledgements)


## UX

### Target Audience

* People interested in reading about coffee and chocolate
* People interested in posting recipes or articles about coffee and chocolate
* People interested in finding a community to chat about a given topic (comments section)

### User Goals

**First Time User would like to**

* Find out the purpose of the site and how to use it
* Be able to easily navigate throughout the site
* See a list of posts to see if the site is something they would be interested in
* See the latest posts
* Be able to register for a user account

**Registered User would like to**

* Sign into their user account
* View posts and leave comments
* Create their own post
* Edit and delete their own posts only
* Logout of their account to keep their account secure

**Site Owner would like to**

* Restrict access to non-registered users
* Control users posts and comments for inappropriate use of the site. All posts and comments must be approved by Admin before they are live on the site

### Agile Development Tool

Agile methodology is a project management approach that emphasizes flexibility, collaboration, and iterative progress towards a well-defined goal. It is particularly effective in software development where requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. Agile methodologies aim to deliver small, incremental changes in a product to improve quality and adaptability to changing needs.

#### MoSCoW Prioritization

The MoSCoW prioritization technique is used to determine the importance of various features and tasks in a project. This method categorizes features into four groups: Must Have, Should Have, Could Have, and Won't Have. This helps in effective time management and ensures that the most critical functionalities are delivered first.

#### GitHub Projects

Using GitHub Projects, tasks are managed and progress tracked through project boards. Each board represents status of the User Story (To Do, In Progress, Done, Future features). Issue labels include the user, prioritization and iterations (milestones).

[Link to the project board](https://github.com/users/VL-ocean/projects/3/views/1) & [Link to the project table](https://github.com/users/VL-ocean/projects/3/views/2)

<details>
<summary>Iteration 1</summary>
<hr>
<b>Board</b>
<img src="./README-images/iteration-1-board.png">
<hr>
<b>Table</b>
<img src="./README-images/iteration-1-table.png">
</details>

<details>
<summary>Iteration 2</summary>
<hr>
<b>Board</b>
<img src="./README-images/iteration-2-board.png">
<hr>
<b>Table</b>
<img src="./README-images/iteration-2-table.png">
</details>

<details>
<summary>Iteration 3</summary>
<hr>
<b>Board</b>
<img src="./README-images/iteration-3-board.png">
<hr>
<b>Table</b>
<img src="./README-images/iteration-3-table.png">
</details>

<details>
<summary>Iteration 4</summary>
<hr>
<b>Board</b>
<img src="./README-images/iteration-4-board.png">
<hr>
<b>Table</b>
<img src="./README-images/iteration-4-table.png">
</details>

<details>
<summary>Milestones Progress</summary>
<hr>
<b>Overall view</b>
<img src="./README-images/milestone-progress.png">
<hr>
<b>The completed milestones are closed</b>
<img src="./README-images/1-2-milestones-closed.png">
<hr>
<b>The milestones to complete are in open status</b>
<img src="./README-images/3-4-milestones-in-progress.png">
</details>

<details>
<summary>Issue sample (iteration 2)</summary>
<hr>
<b>Issue Sample</b>
<img src="./README-images/issue-sample-iter-2.png">
</details>

### User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction. The following user stories outline the essential functionalities and the rationale behind them.

#### Developer

- As a developer I can use Agile so that I can deliver high quality product that meets the user needs
- As a developer I can plan a database schema so that I can effectively store and manage blog data, ensuring optimal perfomance and flexibility
- As a developer I can create visually engaging and responsive design so that users can easily navigate the site and access relevant information
- As a developer I can create wireframes so that I can represent the layout and structure of the site
- As a developer I can install and add basic configurations to Django so that I can create a working app
- As a developer I can deploy to Heroku so that I can verify initial set up
- As a developer I can ensure the quickly load of the platform and swifty respond to user interactions so that users can have a seamless experience
- As a developer I can ensure that all syntax errors are identified and resolved during the code validation process so that the code is free from syntax-related issues
- As a developer I can ensure that application meets performance and accessibility standards so that it provides a seamless experience for all users and performs optimally
- As a developer I can ensure that user stories are thoroughly tested so that they meet acceptance criteria and deliver the expected functionality
- As a developer I can deploy the application to Heroku so that it is accessible to users online
- As a developer I can maintain thorough documentation so that the site is maintained seamlessly in future

#### Site Visitor

- As a Site Visitor I can view the Home page once the link has loaded so that I can understand the site purpose and use
- As a Site Visitor I can sign up so that I can get access Registered User’s features
- As a Site Visitor I can click on Blog nav item so that I can view posts (articles) to choose what to read
- As a Site Visitor I can find 3 latest posts on Home page so that I can read them

#### Registered User

- As a Registered User I can log in using my username and password so that I can be authenticated in the system and use its features
- As a Registered User I can create a post so that I can share my knowledge and experience or research outcome
- As a Registered User I can update my post so that I can correct mistakes or add new information about the topic
- As a Registered User I can delete my post so that I can remove it from the website in case it is irrelevant
- As a Registered User I can click on my profile so that I can see all my posts
- As a Registered User I can fill out the profile information so that other users can get to know me better
- As a Registered User I can comment on a post so that I can join the discussion on the topic and express my opinion on the matter
- As a Registered User I can delete my comment so that I can control my engagement on the platform

#### Site Admin

- As a Site Admin I can manage posts in the admin panel so that I can enrich the content, correct mistakes, remove incorrect or outdated posts
- As a Site Admin I can ban and delete other user profile so that I can protect the site from troublemakers


## UX design

### Wireframe

The original layouts look different from the finished blog as some changes were made during the development process.

<details>
<summary>Home</summary>
<img src="./README-images/home.png">
</details>

<details>
<summary>Blog</summary>
<img src="./README-images/blog.png">
</details>

<details>
<summary>Post view</summary>
<img src="./README-images/post-view.png">
</details>

<details>
<summary>Recipes</summary>
<img src="./README-images/recipes.png">
</details>

<details>
<summary>Recipe view</summary>
<img src="./README-images/recipe-view.png">
</details>

<details>
<summary>Sign Up</summary>
<img src="./README-images/signup.png">
</details>

<details>
<summary>Login</summary>
<img src="./README-images/login.png">
</details>

<details>
<summary>Profile</summary>
<img src="./README-images/profile.png">
</details>

<details>
<summary>Logout</summary>
<img src="./README-images/logout.png">
</details>


### Structure & Logical Flow

The database schema outlines the structure and relationships between key tables for the platform. The User table stores basic user information and authentication details. The Profile table extend user details with bio and profile image. The Post table manages user-generated content with fields for title, description, content, author, and metadata. The Comment table handles comments on posts, including author information. These tables are designed to ensure efficient data management and robust user interactions on the platform.

The database model diagram was designed using Lucidchart:

![Screenshot of flowchart](./README-images/database-erd.png)

### Colour Scheme

The colours were mostly taken from bootstrap colour palette. They are:
- `#212529` - text colour for post, comment, buttons; outline and hover effects on buttons
- `#FFFFFF` - background colour for post, modal; text colour for buttons when hovered over
- `#212529BF` - text colour for secondary text in post, comment
- `#21252908` - background colour for secondary text on the post card
- `#e9ecef` - background colour for comment that is waiting for approval
- `#dc3545` - text colour for X icon used for deleting the comment; text colour and border colour for confirm button when deleting post or comment; background colour for confirm button when hovered over
- `#f6f6f6` - background colour for header, footer
- `#86b7fe` - border colour and shadow for input when focused on it
- `#f8f9fa` - background colour for text messages ("No posts yet", "No comments yet"), buttons; text colour for welcome text on the home page
- `#000000` - text colour for active navigation menu item
- `#d1e7dd` - background colour for message
- `#0a3622` - text colour for message 
- `#a3cfbb` - border colour for message
- `#00000040` - background colour for login, signup forms
- `#00000080` - background colour for welcome text on the home page

Custom colours:
- `#e99767` - border accent colour for post title; circle colour for unordered list item's marker
- `#592c12` - text colour for navigation menu items
- `#f2d9cb` - background colour for main content
- `#5f4e2a` - border colour for active navigation menu item

![Custom colour palette](./README-images/colour-palette.jpeg)

### Fonts

- 'Playfair Display' (backup 'serif') was used as a main title font. It looks nice for titles and subtitles for posts.
- 'Halant' (backup 'serif') was used as a sub-title font. It was rarely used but it also looks nice with the other two fonts.
- 'Roboto' (backup 'serif') was used as a main text font. It is easy to read even if the text is small.

![Fonts](./README-images/fonts.png)


### Responsiveness

The website is responsive to different layouts depending on the size of the viewport based on the Bootstrap media queries.

![media queries](./README-images/media-queries.png)


## Security Measures and Protective Design

### User Authentication

- Django's LoginRequiredMixin is used to ensure that any requests to access secure pages by non-authenticated users are redirected to the login page.
- Django's UserPassesTestMixin is used to limit access based on certain permissions, ensuring users can only edit/delete content they authored. If the user doesn't pass the test, they are shown an HTTP 403 Forbidden error.

### Password Management

- Use Django's built-in password management tools to ensure passwords are hashed and stored securely.
- Enforce strong password policies to enhance user account security.

### Form Validation

- If incorrect or empty data is added to a form, the form won't submit, and a warning will appear to the user informing them which field raised the error.

### Database Security

- The database URL and secret key are stored in the env.py file to prevent unwanted connections to the database. This setup was implemented before the first push to GitHub.
- Cross-Site Request Forgery (CSRF) tokens are used on all forms throughout the site to enhance security.


## Features

### Existing Features


### Future Features


## Technologies Used

### Coding languages used

* HTML
* CSS
* Python
* JavaScript

### Frameworks and Libraries used

**Django**
* Framework used to build this project. Provides a built in admin panel and includes many helper template tags that make writing code quick and efficient.

**Django-Allauth**
* Used for User authenticaion (register, login and logout).

**Django Crispy Forms**
* Used to control rendering of Django forms.

**PostgreSQL**
* The database used by the deployed project on Heroku.
  
**psycopg2**
* PostgreSQL database adapter for the Python programming language.

**Gunicorn**
* Python HTTP server for WSGI applications.

**WhiteNoise**
* Designed to serve static files for Django applications.

**Django RichTextField**
* A Django model field and widget that renders a customizable rich text/WYSIWYG widget.

**Django Resized**
* Resizes image origin to specified size.

**Cloudinary**
* The cloud platform used to store static media files.

**Balsamic**
* Used for the wireframes

**Git**
* Used for version control.

**GitHub**
* Used to store the project's code after being pushed from Git.

**GitPod**
* Used as a platform to develop code in a ready-to-code developer environment.

**Heroku**
* The cloud platform used to deploy the project in the live environment.

**Bootstrap**
* The front end development framework used for styling along with custom CSS.
  
**Lucidchart**
* Used for the entity relationship diagram


## Testing

The website underwent an extensive testing process to ensure its functionality, accessibility, and performance. This involved validating the code, assessing accessibility, conducting performance tests, performing cross-device testing, verifying browser compatibility, evaluating user stories, and incorporating user feedback to improve the overall user experience. 

Testing summary and results can be found in [TESTING.md](TESTING.md) file.


## Deployment

### To deploy the project to Heroku

Follow these steps to deploy your Django project to Heroku from VS Code:
| |
| --- |
| **Step 1** Create a New Heroku App |
| - Access the Heroku Dashboard: Log in to your Heroku account and access the dashboard. |
| - Create a New App: Click on the New button in the top-right corner of the dashboard and select Create new app from the dropdown menu. |
| - App Name and Region: Enter a unique name for your app and choose a region closest to you (EU or USA). Click Create App to create the app. |
| **Step 2** Configure Environment Variables |
| - Reveal Config Vars: From the new app Settings, click Reveal Config Vars. |
| - Set Environment Variables: Set your environment variables as follows: |
|   - `CLOUDINARY_URL`: Insert your own Cloudinary API key here. |
|   - `DATABASE_URL`: Insert your own ElephantSQL database URL here. |
|   - `DISABLE_COLLECTSTATIC`: Set to 1 for temporary purposes, and remove it for the final deployment. |
|   - `SECRET_KEY`: This can be any random secret key. |
| **Step 3** Prepare the Project for Deployment |
| - Create a `requirements.txt` File: This file lists all the dependencies required by your project. You can install the project's requirements using `pip3 install -r requirements.txt`. If you have your own packages installed, update the `requirements.txt` file using `pip3 freeze --local > requirements.txt`. |
| - Create a `Procfile`: This file specifies the commands Heroku should run to start your app. Create the Procfile using `echo web: gunicorn app_name.wsgi > Procfile`. Replace `app_name` with the name of your primary Django app, which is the folder where `settings.py` is located. |
| **Step 4** Connect Your GitHub Repository to Heroku |
| - Automatic Deployment: Select Automatic Deployment from the Heroku app settings to automatically deploy your app whenever you push changes to your GitHub repository. |
| - Manual Deployment: Alternatively, you can connect your GitHub repository to Heroku manually using the Terminal/CLI: |
|   - Login to Heroku: Run `heroku login -i` to log in to your Heroku account. |
|   - Set the Remote for Heroku: Run `heroku git:remote -a app_name` to set the remote for Heroku. Replace `app_name` with your app name. |
|   - Push to Heroku: After performing the standard Git add, commit, and push to GitHub, you can now type `git push heroku main` to deploy your app. |
| **Step 5**  Verify Your Deployment |
| - Open App: Once your app is deployed, you can open it by clicking on the Open App button in the Heroku dashboard. This will open your app in a web browser. |
| - Verify App: Verify that your app is running correctly by checking for any errors or issues. |

### To fork the project

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.

- Log in to **GitHub**.
- Locate the repository.
- Click to open it.
- The fork button is located on the right side of the repository menu.
- To copy the repository to your **GitHub** account, click the button.

### To clone the project

- Log in to **GitHub**.
- Navigate to the main page of the repository and click **Code**.
- Copy the **URL** for the repository.
- Open your local **IDE**.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the **URL** you copied earlier.
- Press **Enter** to create your local clone.


## Credits

### Colour Theme

- [Brown coffee chocolate beige theme by Elisa Cazzulo](https://color.adobe.com/de09e28a57de007f885d0c16d3e3-color-theme-12966174/)

### Project

- [Blossom-Therapy-Insights blog](https://github.com/Indre-V/blossom-therapy)

### Articles & Recipes

- [Chocolate Orange and Lemon Mousse Dessert Cups](https://lilyobriens.ie/blog/post/chocolate-orange-and-lemon-mousse-dessert-cups)
- [Frozen Hot Chocolate](https://www.tasteofhome.com/recipes/frozen-hot-chocolate/)
- [Salted Caramel and Chocolate Chunk Cookies](https://lilyobriens.ie/blog/post/salted-caramel-and-chocolate-chunk-cookies)
- [Creamy Caramel Chocolate Mini Cakes](https://lilyobriens.ie/blog/post/creamy-caramel-chocolate-mini-cakes)
- [Belgian Chocolate Lava Puddings](https://lilyobriens.ie/blog/post/belgian-chocolate-lava-puddings)
- [Chocolate Valentine’s Truffles](https://lilyobriens.ie/blog/post/chocolate-valentine%E2%80%99s-truffles-2023)
- [Your Ultimate Guide to Different Types of Coffee](https://www.tasteofhome.com/article/types-of-coffee/)

### Media

- [Coffee and Chocolate photo](https://www.pexels.com/photo/white-printer-paper-on-brown-textile-10254303/)
- [Blog Letters on Brown Wood](https://www.pexels.com/photo/blog-letters-on-brown-wood-262508/)
- [error 404](https://www.pexels.com/photo/error-404-27968632/)

### Tools

- [Abobe Colour](https://color.adobe.com/create/color-wheel)
- [FontJoy](https://fontjoy.com/)


## Acknowledgements

  - [Cohort Facilitator - Marko Tot](https://github.com/tmarkec) for support in the classroom and guidance through the course.
  - [Mentor - Dick Vlaanderen](https://github.com/dickvla) for support throughout the project, ideas and advice.