# Testing

![Main Image](./README-images/main-responsive.png)

# Contents

- [Responsiveness Tests](#responsiveness-tests)
- [Browser Compatibility](#browser-compatibility)
- [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Python (Unit Testing)](#python--unit-testing-)
- [Lighthouse Testing](#lighthouse-testing)
- [Accessibility Testing](#accessibility-testing)
- [Manual Testing](#manual-testing)
- [Role-based Restrictions](#role-based-restrictions)
- [User Story Testing](#user-story-testing)
- [Bugs](#bugs)


## Responsiveness Tests

The mobile-first strategy was used when developing the website. The project has been deployed at early stage to ensure best layout and effective testing. The DevTools were used during development and [Responsive Design Checker](https://responsivedesignchecker.com/ "Responsive Design Checker") along with [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive") for testing.

| **Size** | **Device** | **Screenshot** | **Result** |
| --- | --- | --- | --- |
| 360 x 740  | Samsung Galaxy S8+ | <details><summary>View</summary>![screenshot](./README-images/samsung-galaxy-s8.png)</details> | ✅ |
| 414 x 896  | iPhone XR | <details><summary>View</summary>![screenshot](./README-images/iphone-xr.png)</details> | ✅ |
| 430 x 932  | iPhone 14 Pro Max | <details><summary>View</summary>![screenshot](./README-images/iphone-14.png)</details> | ✅ |
| 768 x 1024  | iPad Mini | <details><summary>View</summary>![screenshot](./README-images/ipad-mini.png)</details> | ✅ |
| 853 x 1280  | Asus Zenbook Fold | <details><summary>View</summary>![screenshot](./README-images/asus-zenbook.png)</details> | ✅ |
| 912 x 1368  | Surface Pro 7 | <details><summary>View</summary>![screenshot](./README-images/surface-pro-7.png)</details> | ✅ |
| 1024 x 1366  | iPad Pro | <details><summary>View</summary>![screenshot](./README-images/ipad-pro.png)</details> | ✅ |
| 1440 x 900  | Desktop | <details><summary>View</summary>![screenshot](./README-images/1440-sample.png)</details> | ✅ |
| 1680 x 1050  | Desktop | <details><summary>View</summary>![screenshot](./README-images/1680-sample.png)</details> | ✅ |
| 1920 x 1080  | Desktop | <details><summary>View</summary>![screenshot](./README-images/1920-sample.png)</details> | ✅ |


## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.

| Browser | Notes | Result |
| --- | --- | --- |
| Chrome | No issues identified | ✅ |
| Opera | No issues identified | ✅ |
| Firefox | No issues identified | ✅ |
| Microsoft Edge | No issues identified | ✅ |


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
| urls.py | ✅ | ![Result](./README-images/home-urls-py.png) |
| views.py | ✅ | ![Result](./README-images/home-views-py.png) |
|  |  | **Profiles App** |
| admin.py | ✅ | ![Result](./README-images/profiles-admin-py.png) |
| forms.py | ✅ | ![Result](./README-images/profiles-forms-py.png) |
| models.py | ✅ | ![Result](./README-images/profiles-models-py.png) |
| urls.py | ✅ | ![Result](./README-images/profiles-urls-py.png) |
| views.py | ✅ | ![Result](./README-images/profiles-views-py.png) |

</details><br/>

## Lighthouse Testing

The website was tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

<details><summary><b>Desktop Test Results</b></summary>

| **Page** | **Role** | **Result** |
| --- | --- | --- |
| Home | Visitor | ![Result](./README-images/home-visitor-desktop.png) |
| Home | Registered User | ![Result](./README-images/home-user-desktop.png) |
| Blog | Visitor | ![Result](./README-images/blog-visitor-desktop.png) |
| Blog | Registered User | ![Result](./README-images/blog-user-desktop.png) |
| Search results (Blog) | Visitor | ![Result](./README-images/search-visitor-desktop.png) |
| Search results (Blog) | Registered User | ![Result](./README-images/search-user-desktop.png) |
| Post Detail | Visitor | ![Result](./README-images/post-visitor-desktop.png) |
| Post Detail | Registered User | ![Result](./README-images/post-user-desktop.png) |
| Add Post | Registered User | ![Result](./README-images/add-post-user-desktop.png) |
| Edit Post | Registered User | ![Result](./README-images/edit-post-user-desktop.png) |
| Delete Post | Registered User | ![Result](./README-images/delete-post-user-desktop.png) |
| Register | Visitor | ![Result](./README-images/register-visitor-desktop.png) |
| Profile | Registered User | ![Result](./README-images/profile-user-desktop.png) |
| Login | Visitor | ![Result](./README-images/login-visitor-desktop.png) |
| Logout | Registered User | ![Result](./README-images/logout-user-desktop.png) |

</details>

<details><summary><b>Mobile Test Results</b></summary>

| **Page** | **Role** | **Result** |
| --- | --- | --- |
| Home | Visitor | ![Result](./README-images/home-visitor-mobile.png) |
| Home | Registered User | ![Result](./README-images/home-user-mobile.png) |
| Blog | Visitor | ![Result](./README-images/blog-visitor-mobile.png) |
| Blog | Registered User | ![Result](./README-images/blog-user-mobile.png) |
| Search results (Blog) | Visitor | ![Result](./README-images/search-visitor-mobile.png) |
| Search results (Blog) | Registered User | ![Result](./README-images/search-user-mobile.png) |
| Post Detail | Visitor | ![Result](./README-images/post-visitor-mobile.png) |
| Post Detail | Registered User | ![Result](./README-images/post-user-mobile.png) |
| Add Post | Registered User | ![Result](./README-images/add-post-user-mobile.png) |
| Edit Post | Registered User | ![Result](./README-images/edit-post-user-mobile.png) |
| Delete Post | Registered User | ![Result](./README-images/delete-post-user-mobile.png) |
| Register | Visitor | ![Result](./README-images/register-visitor-mobile.png) |
| Profile | Registered User | ![Result](./README-images/profile-user-mobile.png) |
| Login | Visitor | ![Result](./README-images/login-visitor-mobile.png) |
| Logout | Registered User | ![Result](./README-images/logout-user-mobile.png) |

</details><br/>


## Accessibility Testing

Besides Lighthouse accessibility testing, the website was also tested using the [WAVE](https://wave.webaim.org/) tool. No errors identified. 
Unfortunately, it cannot evaluate the website from the registered user's view, due to login issues. Heroku app refused to connect.

| **Page** | **Notes** | **Result** |
| --- | --- | --- |
| Home | No errors were detected | <details><summary>View</summary>![result](./README-images/wave-home.png)</details> |
| Blog | No errors were detected | <details><summary>View</summary>![result](./README-images/wave-blog.png)</details> |
| Register | No errors were detected | <details><summary>View</summary>![result](./README-images/wave-register.png)</details> |
| Login | No errors were detected | <details><summary>View</summary>![result](./README-images/wave-login.png)</details> |


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
| 'Edit' link | 'Edit' button under the post | Click on 'Edit' button under your post | The user is navigated to the edit post view. Only the post author has access to the button and the form to edit the post | ✅ |
| 'Edit Post' Form validation | 'Edit Post' Form | Remove the text and leave some fields empty | The error message is displayed. The user is asked to fill in the empty fields | ✅ |
| 'Edit Post' Form action | 'Edit Post' button in 'Edit Post' Form | After editing the fields, click on 'Edit Post' button under the form | The user is navigated to the Blog page. The post has been updated. If the Post has been published and approved before, then it will be displayed on the Blog page with all other posts. If the Post status is 'published' but it was not previously approved, then it is awaiting approval. The user can find it in his profile with the message 'awaiting approval' displayed. If the Post status is 'draft', it can be found in user profile for further editing | ✅ |
| 'Delete' link | 'Delete' button under the post | Click on 'Delete' button under your post | The user is navigated to the delete post confirmation. Only the post author has access to the button and can confirm deletion | ✅ |
| Deletion confirmation | 'Confirm' button on delete post confirmation view | Click on 'Confirm' button | The user is navigated to the Blog page. The post has been successfully deleted from the database and is no longer displayed. Only the post author can confirm deletion | ✅ |
| Cancel post deletion | 'Cancel' button on delete post confirmation view | Click on 'Cancel' button | The user is navigated back to the post detail page. The post has not been deleted | ✅ |
| **Comments section** |  |  |  |  |
| View post comments | Comments section | Click on post card, scroll down to the comments section | The comments are displayed. Only approved comments are visible for all users. Not approved comments are visible to the comment author | ✅ |
| 'Add Comment' link | 'Add Comment' button in comments section | Click on 'Add Comment' | The modal with form is displayed to the user. Only registered users have access to the button and form | ✅ |
| 'Add Comment' Form validation | 'Add Comment' Form | Leave empty | The error message is displayed. The user is asked to fill in the empty field | ✅ |
| 'Add Comment' Form action | 'Save changes' button in 'Add Comment' Form | After inputting some text, click on 'Save changes' button | The user is navigated to the post detail page he commented. The comment has been created. It is awaiting approval. The proper message is displayed | ✅ |
| 'Delete' link | 'Delete' icon at top right corner of the comment | Click on 'Delete' icon on your comment | The user is navigated to the delete comment confirmation. Only the comment author has access to the button | ✅ |
| Deletion confirmation | 'Confirm' button on delete comment confirmation view | Click on 'Confirm' button | The user is navigated to the Blog page. The comment has been successfully deleted from the database and is no longer displayed. Only the comment author can confirm deletion | ✅ |
| Cancel comment deletion | 'Cancel' button on delete comment confirmation view | Click on 'Cancel' button | The user is navigated back to the post detail page. The comment has not been deleted | ✅ |
| **Profile App** |  |  |  |  |
| View my profile | Profile page | Navigate through 'Profile' navigation item | The profile is displayed with picture, username, date joined, amount of posts and bio if available. Only registered users can view each other's profile | ✅ |
| 'Edit' profile | 'Edit' button under the profile | Click on 'Edit' button under your profile | The modal is displayed with a form to update a profile picture and bio. The bio can be left blank. The avatar can be either changed or unchanged (the default image will be displayed). Only the profile's owner has access to the button and the form to edit it | ✅ |
| 'Edit profile' Form action | 'Save changes' button in 'Edit profile' Form | After updating bio or changing the picture, click on 'Save changes' button under the form | The user is navigated to his profile. The profile has been successfully updated. Only the profile's owner can update his profile | ✅ |
| Cancel the editing | 'Close' button in 'Edit profile' form | Click on 'Close' button | The user is navigated back to the profile. The profile has not been updated | ✅ |
| View my posts | Profile page | Navigate through 'Profile' navigation item | Beneath the profile, the user's posts can be found, including the title, description and creation date. Only the post author can see drafts and unapproved posts. Other registered users can see only approved and published posts | ✅ |
| View my post to edit or delete it | Post card in profile | Click on post card in your profile | The user is navigated to the post detail view. The post author can access edit and delete buttons to work on the post.  | ✅ |

</details><br/>


## Role-based Restrictions

The user role based restrictions were tested to ensure that view and functionality reflects the scope of the project.

- ### **Admin**

| **Functionality** | **Result** |
| --- | --- |
| Full access to all resources and features | ✅ |
| CRUD on all elements | ✅ |
| Manage user roles and restrictions | ✅ |
| Access to admin dashboard and settings | ✅ |

- ### **Registered User**

| **Functionality** | **Result** |
| --- | --- |
| CRUD on their own content (post) | ✅ |
| No access to change another user's content | ✅ |
| Create and delete comments | ✅ |
| Update profile | ✅ |
| Read all published and approved posts | ✅ |
| Read all approved comments | ✅ |
| View another user's profile (if shared a link) | ✅ |

- ### **Visitor**

| **Functionality** | **Result** |
| --- | --- |
| View published and approved content (post) | ✅ |
| No CRUD on any elements | ✅ |
| No access to view another user's profile | ✅ |


## User Story Testing




## Bugs

| **Description** | **Solution** | **Status** | **Notes** |
| --- | --- | --- | --- |
| 'Profile' navigation item does not become active when the Profile page is opened | In header.html use 'request.resolver_match.url_name' to compare the opened url with the url name in [profiles/urls.py]. Once it matches, the active class is applied to the navigation item | ✅ | Resolved with git commit beb22da |
| When searching a word that is not found in any blog posts, the posts.html renders the title 'Newst Posts' with no posts in it. It does not indicate that the match was not found | In posts.html added if statement to check whether 'posts' variable has anything inside. If it is empty, then the message 'No matching results' is displayed to the user | ✅ | Resolved with git commit beb22da |
| 'Add Comment' Form can be submitted empty | In post_detail.html add 'required' attribute to the textarea of the comment body. So that the form cannot be submitted empty on the frontend | ✅ | Resolved with git commit ff9ee1b |
| Console error displayed by CKE Editor. Due to it being no longer supported by the developers |The solution is to buy and use their secured and supported 5-th version of the Editor. Or replace it with another free editor | ❌ | Due to resolve in future fixes |
| Modal popup displayed by CKE Editor in the forms where the widget was used. Due to it being no longer supported by the developers |The solution is to buy and use their secured and supported 5-th version of the Editor. Or replace it with another free editor | ✅ | Temporary fix by setting display to none using custom JavaScript |