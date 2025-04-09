import os
from bs4 import BeautifulSoup


# Helper function to load the HTML content
def load_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")


# Helper function to check for the existence of style.css
def check_style_css():
    return os.path.exists("style.css")


# Test 1: Use of inline styles (Penalize)
def test_inline_styles():
    html_content = load_html()

    # Check if there are any inline styles used
    inline_styles = html_content.find_all(style=True)
    assert len(inline_styles) > 0, "Inline styles are not used, good."



# Test 2: Missing or incorrect 'alt' attribute in the profile image (Penalize)
def test_missing_or_incorrect_alt_text():
    html_content = load_html()

    # Check if the profile image is missing the 'alt' attribute
    img = html_content.find("img", {"class": "rounded-circle"})
    assert img is None or img.get("alt") is None, "Profile image is not missing 'alt' text"


# Test 3: Unnecessary custom JavaScript (Penalize)
def test_unnecessary_custom_javascript():
    html_content = load_html()

    # Check if there is any unnecessary custom JavaScript for simple tasks
    script_tags = html_content.find_all("script")
    for script in script_tags:
        assert "bootstrap"  in script.get("src",
                                             ""), "Code does not use unnecessary custom JavaScript"



