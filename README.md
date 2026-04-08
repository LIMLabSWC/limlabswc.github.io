# LIM Lab Website

This is the official website for the Learning, Inference & Memory (LIM) Lab, at the Sainsbury Wellcome Centre, UCL, London.

🌐 **Live at**: [https://lim.bio](https://lim.bio)

## 🚀 Built with Jekyll

This website is built using [Jekyll](https://jekyllrb.com/) with the `github-pages` gem, ensuring full compatibility with GitHub Pages. This provides:

- **Template System**: One layout file controls all pages
- **Data-Driven Content**: People, publications, and lab news managed in YAML files
- **Automatic Builds**: GitHub Pages builds automatically on push
- **Easy Maintenance**: Add new content without touching HTML

## 📁 Site Structure

```
├── 404.html             # Custom 404 error page
├── _config.yml          # Site configuration
├── _layouts/
│   └── default.html     # Main layout template
├── _includes/
│   ├── header.html      # Header partial
│   └── footer.html      # Footer partial
├── _data/
│   ├── people.yml       # Lab members data
│   ├── publications.yml # Publications data
│   └── news.yml         # Lab news entries
├── CNAME                # Custom domain (lim.bio)
├── Gemfile              # Ruby dependencies
├── Gemfile.lock         # Locked dependency versions
├── .gitignore           # Git ignore rules
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
        ├── athena1b.jpg
        ├── erc.png
        ├── swc.png
        ├── ucl.png
        └── [other member photos and logos]
```

## 🛠️ Local Development

### Prerequisites

- Ruby 2.7 or higher
- Bundler

On Ubuntu/Debian, also install:

```bash
sudo apt update
sudo apt install ruby-full ruby-all-dev build-essential zlib1g-dev
````

### Setup

Install dependencies locally (avoids permission issues):

```bash
bundle config set --local path vendor/bundle
bundle install
```

If there is a Bundler version mismatch:

```bash
gem install --user-install bundler -v 2.7.2
bundle _2.7.2_ install
```

### Build and serve

```bash
bundle exec jekyll build
bundle exec jekyll serve
```

The site will be available at [http://localhost:4000](http://localhost:4000)

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
    url: "https://doi.org/..."  # optional, makes the card clickable on the Publications page
```

### Adding Lab News

Edit `_data/news.yml` and add new entries under `recent_news`. Each item has a `date`, `title`, and `paragraphs` list. Paragraphs support **markdown** (bold, links, lists).

```yaml
recent_news:
  - date: "2025"
    title: "Your headline"
    paragraphs:
      - "First paragraph."
      - "Second paragraph. Use **bold** or [links](/join/) in markdown."
      - |
        - List item one
        - List item two
```

Add new items at the top of the list so the latest news appears first.

### Upcoming Events (Lab News page)

The lab news page has an **Upcoming Events** section. Edit `_data/news.yml`:

- **Placeholder message** (when there are no events): change `events_placeholder`.
- **Add events**: set `upcoming_events` to a list of items (or `[]` when none), each with `date`, `title`, optional `description` (markdown), and optional `url` (for clickable cards):

```yaml
upcoming_events:
  - date: "2025-03-15"
    title: "Lab meeting"
    description: "Weekly lab meeting, Room 123."
    url: "https://example-conference.org"  # optional
```

## 🎨 Making Design Changes

### Global Changes

- **Header/Footer**: Edit `_includes/header.html` or `_includes/footer.html`
- **Layout**: Edit `_layouts/default.html`
- **Styling**: Edit `assets/css/style.css`

### Page-Specific Changes

- **Content**: Edit the respective `.md` file in each directory (People, Publications, and Lab News content live in `_data/people.yml`, `_data/publications.yml`, and `_data/news.yml`)
- **Page Title/Description**: Edit the front matter at the top of each `.md` file

## 🌐 Custom Domain Configuration

This site uses the custom domain `lim.bio`.

- `CNAME` is configured for the custom domain
- `_config.yml` is set to use the production site URL
- DNS is managed through Cloudflare
- The site is deployed via GitHub Pages with HTTPS enabled

## 🚀 Deployment

This site is automatically deployed to GitHub Pages when you push to the `main` branch. No manual deployment needed!

The site is live at [https://lim.bio](https://lim.bio) with HTTPS automatically enforced.

## 📋 Features

- ✅ **Custom Domain**: Professional `lim.bio` domain with HTTPS
- ✅ **CDN Performance**: Cloudflare proxy for global fast loading
- ✅ **Responsive Design**: Works on all devices
- ✅ **SEO Optimized**: Proper meta tags and structure
- ✅ **Fast Loading**: Static files, optimized for speed
- ✅ **Easy Updates**: Data-driven content management
- ✅ **Professional Design**: Clean, academic aesthetic
- ✅ **Accessibility**: Proper semantic HTML and alt tags
- ✅ **DDoS Protection**: Cloudflare security features

## 🔧 Technical Details

- **Domain**: `lim.bio` (custom domain via Cloudflare DNS)
- **Hosting**: GitHub Pages with Jekyll
- **CDN**: Cloudflare proxy for global performance
- **SSL**: Automatic HTTPS enforcement
- **Jekyll Version**: 3.10.0 (GitHub Pages compatible)
- **Ruby Version**: 2.7+
- **CSS**: Custom stylesheet with responsive design
- **Images**: Optimized for web with proper alt tags
- **Navigation**: Automatic active state highlighting
- **DNS**: 4 A records for redundancy + CNAME for www subdomain
- **GitHub Pages**: Fully compatible with automatic deployment

## 🤝 How to Contribute

We welcome contributions to improve the website! Here's how you can help:

1. **Update Your Profile**:
   - Edit `_data/people.yml` to update your information
   - Add or update your photo in `assets/img/`
   - Include your latest research interests and publications

2. **Add Publications**:
   - Edit `_data/publications.yml`
   - Follow the existing format for consistency
   - Include DOI links when available

3. **Share News**:
   - Edit `_data/news.yml` and add a new entry under `recent_news`
   - Use `date`, `title`, and `paragraphs` (list of strings; markdown supported)
   - Add new items at the top so the latest news appears first
   - To add or edit **Upcoming Events**, edit `upcoming_events` in `_data/news.yml`

### Development Workflow

```bash
# Fork and clone the repository
git clone https://github.com/YOUR-USERNAME/limlabswc.github.io.git
cd limlabswc.github.io

# Install dependencies
bundle install

# Make your changes
# Edit files as needed

# Test locally
bundle exec jekyll serve

# Check at http://localhost:4000

# Commit and push
git add .
git commit -m "Description of changes"
git push origin your-branch

# Create pull request on GitHub
```

### Contribution Guidelines

- **Images**: Optimize images for web (compress, use appropriate formats)
- **Code**: Follow existing patterns and structure
- **Testing**: Always test changes locally before submitting
- **Documentation**: Update README if you add new features

### Types of Contributions Welcome

- ✅ Content updates (people, publications, news)
- ✅ Bug fixes and broken link repairs
- ✅ Accessibility improvements
- ✅ Performance optimizations
- ✅ Mobile responsiveness fixes
- ✅ SEO improvements
- ✅ New features (with discussion first)
