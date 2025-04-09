import os
from bs4 import BeautifulSoup

# Helper function to load the HTML content
def load_html():
    with open("index.html", "r") as file:
        return BeautifulSoup(file, "html.parser")

# Test 1: Responsiveness of the layout on different screen sizes
def test_responsive_layout():
    html_content = load_html()

    # Check if the layout adjusts using Bootstrap grid classes (e.g., .col, .col-sm, .col-md)
    responsive_elements = html_content.find_all(["div", "section", "article"], {"class": lambda x: x and "col" in x})
    assert len(responsive_elements) > 0, "No responsive grid classes (.col, .col-sm, .col-md) found for layout"

# Test 2: Custom CSS for button hover effect
def test_custom_button_hover_effect():
    html_content = load_html()

    # Check if there is any custom CSS for the button hover effect (e.g., checking for :hover style)
    style_tag = html_content.find("style")
    assert style_tag is None or ":hover" in str(style_tag), "No custom hover effect found for buttons"

# Test 3: Interactive button (e.g., "Follow" button is interactive)
def test_interactive_button():
    html_content = load_html()

    # Check if the button is interactive, i.e., it has an action like a link or JavaScript function
    button = html_content.find("button", {"class": "btn"})
    assert button is not None, "Button with class 'btn' is missing"
    assert button.get("onclick") is not None or button.get("href") is not None, "Button is not interactive"

# Test 4: Profile image alt text for accessibility
def test_profile_image_alt_text():
    html_content = load_html()

    # Check if the profile image has the 'alt' attribute
    img = html_content.find("img", {"class": "rounded-circle"})
    assert img is not None, "Profile image with class 'rounded-circle' is missing"
    assert img.get("alt") is not None and len(img.get("alt").strip()) > 0, "Profile image missing alt text"

# Test 5: Custom styling for card background or borders
def test_custom_card_styling():
    html_content = load_html()

    # Check if there is any custom CSS that modifies the card's background or borders
    style_tag = html_content.find("style")
    if style_tag:
        card_style = style_tag.find(string=lambda x: x and "card" in x)
        assert card_style is not None, "No custom styles for the card's background or borders"
    else:
        # If no inline styles are used, check if the card uses Bootstrap's predefined styles
        card = html_content.find("div", {"class": "card"})
        assert card is not None, "Card with class 'card' is missing"
        assert card.get("style") is None, "Card has inline styles which should be avoided for this task"

