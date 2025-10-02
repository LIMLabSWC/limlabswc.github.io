#!/usr/bin/env python3
"""
Simple template updater for LIM Lab website.
This script helps maintain consistency across all pages.
"""

import os
import re

# Common header template
HEADER_TEMPLATE = '''  <header class="site-header">
    <div class="header-container">
      <div class="brand">
        <div class="logo-container">
          <div class="logo-text">
            <div class="logo-main">IM</div>
            <div class="logo-sub">Lab</div>
          </div>
          <div class="logo-full">Learning Inference Memory</div>
        </div>
      </div>
      <nav class="nav">
        <a href="/">HOME</a>
        <a href="/research">RESEARCH</a>
        <a href="/people">PEOPLE</a>
        <a href="/publications">PUBLICATIONS</a>
        <a href="/labnews">LAB NEWS</a>
        <a href="/join">JOIN</a>
      </nav>
    </div>
  </header>'''

# Common footer template
FOOTER_TEMPLATE = '''  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-brand">LIM Lab</div>
      <div class="footer-logos">
        <a href="https://www.ucl.ac.uk/swc" target="_blank" rel="noreferrer">
          <img src="https://www.sainsburywellcome.org/sites/default/files/2021-05/swc-logo.png" alt="Sainsbury Wellcome Centre logo">
        </a>
        <a href="https://www.ucl.ac.uk" target="_blank" rel="noreferrer">
          <img src="https://www.ucl.ac.uk/sites/default/files/ucl-logo.png" alt="UCL logo">
        </a>
      </div>
    </div>
  </footer>'''

def update_page(page_path, active_nav):
    """Update a single page with the common template."""
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header
    header_pattern = r'<header class="site-header">.*?</header>'
    content = re.sub(header_pattern, HEADER_TEMPLATE, content, flags=re.DOTALL)
    
    # Replace footer
    footer_pattern = r'<footer class="site-footer">.*?</footer>'
    content = re.sub(footer_pattern, FOOTER_TEMPLATE, content, flags=re.DOTALL)
    
    # Set active navigation
    if active_nav:
        content = content.replace(f'href="{active_nav}"', f'href="{active_nav}" class="active"')
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {page_path}")

def main():
    """Update all pages with the common template."""
    pages = [
        ('index.html', '/'),
        ('research.html', '/research'),
        ('people.html', '/people'),
        ('publications.html', '/publications'),
        ('labnews.html', '/labnews'),
        ('join.html', '/join'),
    ]
    
    for page_path, active_nav in pages:
        if os.path.exists(page_path):
            update_page(page_path, active_nav)
        else:
            print(f"Warning: {page_path} not found")

if __name__ == "__main__":
    main()
