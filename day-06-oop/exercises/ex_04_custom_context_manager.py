"""Exercise 4: Custom Context Manager — HTML Builder

Create a context manager that builds an HTML document.

Usage:
    with HTMLBuilder() as html:
        html.h1("Hello")
        html.p("This is a paragraph")

Expected output:
    <html>
      <h1>Hello</h1>
      <p>This is a paragraph</p>
    </html>

Support at least: html, h1-h6, p, div, ul/li, a

Hint: Track an indentation level and a list of output lines.
Make __enter__ return self. In __exit__, print the built HTML.
"""
