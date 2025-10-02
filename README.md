# LIM Lab Website

This is the official website for the Learning, Inference & Memory (LIM) Lab, led by Dr. Athena Akrami at the Sainsbury Wellcome Centre, UCL, London.

## 🚀 Built with Jekyll

This website is built using [Jekyll](https://jekyllrb.com/), a static site generator that's natively supported by GitHub Pages. This provides:

- **Template System**: One layout file controls all pages
- **Data-Driven Content**: People and publications managed in YAML files
- **Automatic Builds**: GitHub Pages builds automatically on push
- **Easy Maintenance**: Add new content without touching HTML

## 📁 Site Structure

```
├── _config.yml          # Site configuration
├── _layouts/
│   └── default.html     # Main layout template
├── _includes/
│   ├── header.html      # Header partial
│   └── footer.html      # Footer partial
├── _data/
│   ├── people.yml       # Lab members data
│   └── publications.yml # Publications data
├── index.md             # Home page
├── research/
│   └── index.md         # Research page
├── people/
│   └── index.md         # People page
├── publications/
│   └── index.md         # Publications page
├── labnews/
│   └── index.md         # Lab news page
├── join/
│   └── index.md         # Join page
└── assets/
    ├── css/
    │   └── style.css    # All styling
    └── img/             # Images and photos
```

## 🛠️ Local Development

### Prerequisites
- Ruby 2.7 or higher
- Bundler gem

### Setup
```bash
# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

## 📝 Adding Content

### Adding Lab Members
Edit `_data/people.yml` and add new members to the appropriate section:

```yaml
research_fellows:
  - name: "New Person"
    title: "Research Fellow"
    photo: "photo.jpg"  # or null for no photo
    description: "Research description..."
```

### Adding Publications
Edit `_data/publications.yml` and add new publications:

```yaml
published:
  - authors: "Author Names"
    title: "Paper Title"
    journal: "Journal Name"
    year: 2024
    status: "In press"  # optional
    note: "Additional note"  # optional
```

### Adding News
Edit `labnews/index.md` and add new news items in the Recent News section.

## 🎨 Making Design Changes

### Global Changes
- **Header/Footer**: Edit `_includes/header.html` or `_includes/footer.html`
- **Layout**: Edit `_layouts/default.html`
- **Styling**: Edit `assets/css/style.css`

### Page-Specific Changes
- **Content**: Edit the respective `.md` file in each directory
- **Page Title/Description**: Edit the front matter at the top of each `.md` file

## 🚀 Deployment

This site is automatically deployed to GitHub Pages when you push to the `main` branch. No manual deployment needed!

## 📋 Features

- ✅ **Responsive Design**: Works on all devices
- ✅ **SEO Optimized**: Proper meta tags and structure
- ✅ **Fast Loading**: Static files, optimized for speed
- ✅ **Easy Updates**: Data-driven content management
- ✅ **Professional Design**: Clean, academic aesthetic
- ✅ **Accessibility**: Proper semantic HTML and alt tags

## 🔧 Technical Details

- **Jekyll Version**: 4.3.4
- **Ruby Version**: 2.7+
- **CSS**: Custom stylesheet with responsive design
- **Images**: Optimized for web with proper alt tags
- **Navigation**: Automatic active state highlighting

## 📞 Contact

For questions about the website or lab, contact:
- **Email**: a.akrami@ucl.ac.uk
- **Institution**: Sainsbury Wellcome Centre, UCL
- **Location**: London, UK

---

*This website showcases the research and people of the LIM Lab, contributing to our understanding of learning, inference, and memory in the brain.*