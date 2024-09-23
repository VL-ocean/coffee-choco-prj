# Testing

![Main Image]()

# Contents

- [Responsiveness Tests](#responsiveness-tests)
- [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Python (Unit Testing)](#python--unit-testing-)
- [Manual Testing](#manual-testing)
- [Role-based Restrictions](#role-based-restrictions)
- [Bugs](#bugs)
- [Browser Compatibility](#browser-compatibility)
- [User Story Testing](#user-story-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Accessibility Testing](#accessibility-testing)


## Responsiveness Tests


## Code Validation

### HTML

The HTML files were validated using the recommended [HTML W3C Validator](https://validator.w3.org/#validate_by_input).

The process of HTML file validation by direct input:

1. Access the Validator: Visit the W3C Markup Validation Service.
2. Choose Direct Input: Select the "Validate by Direct Input" tab.
3. Paste Your HTML Code: Copy HTML code of the page from deployed website and paste it into the text box.
4. Validate: Click the "Check" button to validate HTML.

Notes:
- The source code for validation has been copied from the deployed version of the website, using "View source code" option.
- Every page extends from base.html and includes header.html and footer.html
- The 403.html page has not been checked, since the user is right away redirected to the Login page.


<details>
<summary>HTML Validation Results</summary>

| **File name** | **Pass** | **Notes** | **Result** |
| --- | --- | --- | --- |
| **Blog App** |  |  |  |
| add_post.html | ✅ | No errors or warnings to show | ![add_post](./README-images/add-post.png) |
| comment_confirm_delete.html | ✅ | No errors or warnings to show | ![comment_confirm_delete](./README-images/comment-confirm-delete.png) |
| edit_post.html | ✅ | No errors or warnings to show | ![edit_post](./README-images/edit-post.png) |
| post_confirm_delete.html | ✅ | No errors or warnings to show | ![post_confirm_delete](./README-images/post-confirm-delete.png) |
| post_detail.html ("Types of Coffee Drinks") | ✅ | No errors or warnings to show | ![post_detail](./README-images/post-detail.png) |
| post_detail.html ("Creamy Caramel Chocolate Mini Cakes") | ✅ | No errors or warnings to show. Except "Info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values". The widget renders post content using \<br/> | ![post_detail_info](./README-images/post-detail-info.png) |
| posts.html | ✅ | No errors or warnings to show | ![posts](./README-images/posts.png) |
| posts.html | ✅ | No errors or warnings to show | ![posts](./README-images/posts.png) |
| **Home App** |  |  |  |
| index.html | ✅ | No errors or warnings to show | ![index](./README-images/index.png) |
| **Profiles App** |  |  |  |
| profile.html | ✅ | No errors or warnings to show | ![profile](./README-images/profile-html-validation.png) |
| **AllAuth templates** |  |  |  |
| login.html | ✅ | No errors or warnings to show | ![login](./README-images/login-html-validation.png) |
| logout.html | ✅ | No errors or warnings to show | ![logout](./README-images/logout-html-validation.png) |
| signup.html | ✅ | No errors or warnings to show | ![signup](./README-images/signup-html-validation.png) |
| **Error templates** |  |  |  |
| 404.html | ✅ | No errors or warnings to show | ![404](./README-images/404-page-html-validation.png) |
| 500.html | ✅ | No errors or warnings to show | ![500](./README-images/500-page-html-validation.png) |

</details>

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) tool, provided by the W3C, enables to validate and verify the correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and accessibility.


| **File name** | **Pass** | **Notes** | **Result** |
| --- | --- | --- | --- |
| base.css | ✅ | No errors. Two warnings. First, due to imported Google Fonts: "Imported style sheets are not checked in direct input and file upload modes". Second, due to variables used to assign some fonts and colours: "Due to their dynamic nature, CSS variables are currently not statically checked" | ![css](./README-images/css-validation.png) |

### JavaScript

No major errors were found when validating JavaScript through [Jshint](https://jshint.com/).

Jshint noted that bootstrap and tooltipList variables are undefined. This can be ignored because they rely on bootstrap javascript.

![jshint](./README-images/jshint-validation.png)

### Python

The python files have all been passed through [CI Python Linter](https://pep8ci.herokuapp.com/)

<details><summary><b>Test Results</b></summary>

| **File name** | **Pass** | **Result** |
| --- | --- | --- |
|  |  | **Blog App** |
| admin.py | ✅ | ![Result](./README-images/blog-admin-py.png) |
| apps.py | ✅ | ![Result](./README-images/blog-apps-py.png) |
| forms.py | ✅ | ![Result](./README-images/blog-forms-py.png) |
| models.py | ✅ | ![Result](./README-images/blog-models-py.png) |
| urls.py | ✅ | ![Result](./README-images/blog-urls-py.png) |
| views.py | ✅ | ![Result](./README-images/blog-views-py.png) |
|  |  | **Coffee_Choco App** |
| asgi.py | ✅ | ![Result](./README-images/main-asgi-py.png) |
| settings.py | ✅ | ![Result](./README-images/main-settings-py.png) |
| urls.py | ✅ | ![Result](./README-images/main-urls-py.png) |
| wsgi.py | ✅ | ![Result](./README-images/main-wsgi-py.png) |
|  |  | **Home App** |
| apps.py | ✅ | ![Result](./README-images/home-apps-py.png) |
| urls.py | ✅ | ![Result](./README-images/home-urls-py.png) |
| views.py | ✅ | ![Result](./README-images/home-views-py.png) |
|  |  | **Profiles App** |
| admin.py | ✅ | ![Result](./README-images/profiles-admin-py.png) |
| apps.py | ✅ | ![Result](./README-images/profiles-apps-py.png) |
| forms.py | ✅ | ![Result](./README-images/profiles-forms-py.png) |
| models.py | ✅ | ![Result](./README-images/profiles-models-py.png) |
| urls.py | ✅ | ![Result](./README-images/profiles-urls-py.png) |
| views.py | ✅ | ![Result](./README-images/profiles-views-py.png) |

</details><br/>


## Manual Testing

Extensive manual testing was performed on the application. Each feature was verified against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to assess the application's robustness in handling errors and exceptions.

<details><summary><b>Manual Testing Results</b></summary>

| **Test Case** | **Element** | **Action** | **Success Criteria** | **Result** |
| --- | --- | --- | --- | --- |
| **Header** |  |  |  |  |
| Logo link | Logo image | Click on the Logo | The user is navigated to the home page | ✅ |
| Home link | Home navigation item | Click on 'Home' | The user is navigated to the Home page | ✅ |
| Blog link | Blog navigation item | Click on 'Blog' | The user is navigated to the Blog page | ✅ |
| Add Post link | Add Post navigation item | Click on 'Add Post' | The logged in user is navigated to the Add Post page. While the visitor is asked to log in first, or sign up | ✅ |
| Register link | Register navigation item | Click on 'Register' | The user is navigated to the Signup page | ✅ |
| Login link | Login navigation item | Click on 'Login' | The user is navigated to the Login page | ✅ |
| Profile link | Profile navigation item | Click on 'Profile' | The user is navigated to his Profile page. The link is only available for registered users. Registered users can see each other's profiles. It is not restricted. More details in Feature Features section | ✅ |
| Logout link | Logout navigation item | Click on 'Logout' | The user is navigated to the Logout confirmation page. Only registered users can access Logout link | ✅ |
| **Search bar** |  |  |  |  |
| Empty search | Search button | Click on 'Search' button | The user is navigated to the Blog page. Since the input was empty, all posts are displayed on the page | ✅ |
| Search available keyword | Search bar | Enter 'coffee', click on 'Search' button | The user is navigated to the Blog page. The posts, which include the keyword 'coffee' in either title, description or content are displayed on the page | ✅ |
| Search unavailable keyword | Search bar | Enter 'ndkghf', click on 'Search' button | The user is navigated to the Blog page. The message 'No matching results' is displayed on the page | ✅ |
| **Footer** |  |  |  |  |
| LinkedIn link | LinkedIn icon | Click on 'LinkedIn' icon | The LinkedIn website is opened in a separate tab | ✅ |
| Facebook link | Facebook icon | Click on 'Facebook' icon | The Facebook website is opened in a separate tab | ✅ |
| Instagram link | Instagram icon | Click on 'Instagram' icon | The Instagram website is opened in a separate tab | ✅ |
| Twitter link | Twitter icon | Click on 'Twitter' icon | The Twitter website is opened in a separate tab | ✅ |
| YouTube link | YouTube icon | Click on 'YouTube' icon | The YouTube website is opened in a separate tab | ✅ |
| **Home App** |  |  |  |  |
| Display hero image and welcome text | Home page | Navigate through Logo or 'Home' navigation item | The Home page displays the hero image with welcome text on it. The purpose of the website is clearly visible and the text is easy to read | ✅ |
| Display the latest posts (3) | 'Latest Posts' section | Navigate through Logo or 'Home' navigation item | Beneath the hero image the user can find three latest posts (published and approved posts only) | ✅ |
| View any latest post to read | Latest Post card | Click on the post card on the Home page | The user is navigated to the post detail view | ✅ |
| **Blog App** |  |  |  |  |
| View paginated list of posts | Blog page | Navigate through 'Blog' navigation item | The approved and published posts are displayed by 6, with pagination. Sorted by the date | ✅ |
| View next page of posts | 'Next' button | Click on 'Next' button | The user is navigated to the next page | ✅ |
| View previous page of posts | 'Previous' button | Click on 'Previous' button | The user is navigated to the previous page | ✅ |
| View first page of posts | 'First' button | Click on 'First' button | The user is navigated to the first page | ✅ |
| View last page of posts | 'Last' button | Click on 'Last' button | The user is navigated to the last page | ✅ |
| View 2-nd page of posts | '2' page button | Click on '2' page button | The user is navigated to the 2-nd page | ✅ |
| View a post to read | Post card | Click on the post card | The user is navigated to the post detail view | ✅ |
| **Post CRUD** |  |  |  |  |
| 'Add Post' link | 'Add Post' navigation item | Click on 'Add Post' | The user is navigated to the Add Post page with the form. Only registered users have access to the form | ✅ |
| 'Add Post' Form validation | 'Add Post' Form | Leave some fields empty | The error message is displayed. The user is asked to fill in the empty fields | ✅ |
| 'Create Post' Form action | 'Create Post' button in 'Add Post' Form | After filling out all the fields correctly, click on 'Create Post' button under the form | The user is navigated to the Blog page. The post has been created. If the Post status is 'published', then it is awaiting approval. The user can find it in his profile with the message 'awaiting approval' displayed. If the Post status is 'draft', it can be found in user profile for further editing | ✅ |
| 'Edit' link | 'Edit' button under the post | Click on 'Edit' button under your post | The user is navigated to the edit post view. Only the post owner has access to the button and the form to edit the post | ✅ |
| 'Edit Post' Form validation | 'Edit Post' Form | Remove the text and leave some fields empty | The error message is displayed. The user is asked to fill in the empty fields | ✅ |
| 'Edit Post' Form action | 'Edit Post' button in 'Edit Post' Form | After editing the fields, click on 'Edit Post' button under the form | The user is navigated to the Blog page. The post has been updated. If the Post has been published and approved before, then it will be displayed on the Blog page with all other posts. If the Post status is 'published' but it was not previously approved, then it is awaiting approval. The user can find it in his profile with the message 'awaiting approval' displayed. If the Post status is 'draft', it can be found in user profile for further editing | ✅ |
| 'Delete' link | 'Delete' button under the post | Click on 'Delete' button under your post | The user is navigated to the delete post confirmation. Only the post owner has access to the button and can confirm deletion | ✅ |
| Deletion confirmation | 'Confirm' button on delete post confirmation view | Click on 'Confirm' button | The user is navigated to the Blog page. The post has been deleted from the database and is no longer displayed | ✅ |
| **Comment CRUD** |  |  |  |  |
| View post comments | Comments section | Click on post card, scroll down to the comments section | The comments are displayed. Only approved comments are visible for all users. Not approved comments are visible to the comment author | ✅ |
| 'Add Comment' link | 'Add Comment' button in comments section | Click on 'Add Comment' | The modal with form is displayed to the user. Only registered users have access to the button and form | ✅ |
| 'Save changes' Form validation | 'Add Post' Form | Leave some fields empty | The error message is displayed. The user is asked to fill in the empty fields | ✅ |




</details><br/>