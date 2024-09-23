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
| **Blog App** |  |  |  |  |
|  |  |  |  | ✅ |

</details><br/>