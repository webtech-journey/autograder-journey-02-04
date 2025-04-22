import os
from bs4 import BeautifulSoup

# Helper function to load the HTML content
def load_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")

# Test 1: Correct Bootstrap CSS link
def test_bootstrap_css_included():
    html_content = load_html()
    bootstrap_css = html_content.find("link", {"rel": "stylesheet", "href": lambda x: x and "bootstrap" in x})
    assert bootstrap_css is not None, "Bootstrap CSS is missing"

# Test 2: Correct Bootstrap JS link
def test_bootstrap_js_included():
    html_content = load_html()
    bootstrap_js = html_content.find("script", {"src": lambda x: x and "bootstrap" in x})
    assert bootstrap_js is not None, "Bootstrap JS is missing"

# Test 3: Profile card with class 'card'
def test_profile_card_class():
    html_content = load_html()
    card = html_content.find("div", {"class": "card"})
    assert card is not None, "Profile card with class 'card' is missing"

# Test 4: Profile image with class 'rounded-circle'
def test_profile_image_class():
    html_content = load_html()
    img = html_content.find("img", {"class": "rounded-circle"})
    assert img is not None, "Profile image with class 'rounded-circle' is missing"

# Test 5: User's name in title (h1, h2, or h3)
def test_user_name_title():
    html_content = load_html()
    title = html_content.find(["h1", "h2", "h3","h4","h5"], string=lambda x: x and len(x.strip()) > 0)
    assert title is not None, "User's name title (h1, h2, or h3) is missing or empty"



# Test 7: Button with class 'btn'
def test_button_class():
    html_content = load_html()
    button = html_content.find("button", {"class": "btn"})
    assert button is not None, "Button with class 'btn' is missing"

# Test 8: 'd-flex' class for layout
def test_d_flex_class_usage():
    html_content = load_html()
    flex_element = html_content.find("div", {"class": "d-flex"})
    assert flex_element is not None, "'d-flex' class for flexible layout is missing"

# Test 9: Proper <html> tag in structure
def test_html_tag_exists():
    html_content = load_html()
    assert html_content.find("html") is not None, "<html> tag is missing"

# Test 10: Proper <head> tag in structure
def test_head_tag_exists():
    html_content = load_html()
    assert html_content.find("head") is not None, "<head> tag is missing"

# Test 11: Proper <body> tag in structure
def test_body_tag_exists():
    html_content = load_html()
    assert html_content.find("body") is not None, "<body> tag is missing"


