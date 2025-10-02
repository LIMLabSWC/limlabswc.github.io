# LIM Lab Website Template System

## Overview
This website uses a simple template system to maintain consistency across all pages. When you need to make design changes to headers, footers, or navigation, you can update all pages at once using the provided script.

## Files Structure
- `update_template.py` - Script to update all pages with common templates
- `includes/` - Directory containing template components (for reference)
- Individual HTML pages - Each page has its own content but uses common header/footer

## How to Make Design Changes

### 1. Update the Template Script
Edit `update_template.py` and modify the `HEADER_TEMPLATE` or `FOOTER_TEMPLATE` variables with your changes.

### 2. Run the Update Script
```bash
python3 update_template.py
```

This will update all pages (index.html, research.html, people.html, publications.html, labnews.html, join.html) with the new template.

### 3. Verify Changes
Check that all pages have been updated correctly and the navigation active states are working.

## Current Template Features
- **Header**: IM Lab logo, navigation menu with active state highlighting
- **Footer**: LIM Lab branding, official SWC and UCL logos
- **Navigation**: Automatic active state based on current page
- **Responsive**: Mobile-friendly design

## Adding New Pages
1. Create your new HTML page
2. Add it to the `pages` list in `update_template.py`
3. Run the script to apply the template
4. Add your page-specific content

## Notes
- The script automatically sets the active navigation state for each page
- All pages use the same CSS file (`assets/css/style.css`)
- Logos are loaded from official institutional URLs to ensure they're always up-to-date
