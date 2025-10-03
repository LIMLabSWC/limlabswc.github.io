# LIM Lab Website

This is the official website for the Learning, Inference & Memory (LIM) Lab, led by Dr. Athena Akrami at the Sainsbury Wellcome Centre, UCL, London.

🌐 **Live at**: [https://lim.bio](https://lim.bio)

## 🚀 Built with Jekyll

This website is built using [Jekyll](https://jekyllrb.com/) with the `github-pages` gem, ensuring full compatibility with GitHub Pages. This provides:

- **Template System**: One layout file controls all pages
- **Data-Driven Content**: People and publications managed in YAML files
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
│   └── publications.yml # Publications data
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
        ├── European_Research_Council_logo-01.webp
        ├── sainsbury.png
        ├── ucl.png
        └── [other member photos and logos]
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

## 🌐 Custom Domain Configuration

This site uses a custom domain `lim.bio` instead of the default `limlabswc.github.io`:

- **CNAME file**: Contains `lim.bio` to configure the custom domain
- **Jekyll config**: `_config.yml` updated with the custom domain URL
- **DNS records**: Configured in Cloudflare with GitHub Pages IPs
- **HTTPS**: Automatically enforced through GitHub Pages

### DNS Configuration (Cloudflare)

- **A records**: 4 GitHub Pages IP addresses (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`)
- **CNAME**: `www` subdomain pointing to `limlabswc.github.io`
- **Proxy status**: All records are proxied through Cloudflare for performance and security
- **Subdomains**: `bcontrol.lim.bio` and `dosing.lim.bio` also point to the GitHub Pages site

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

## 📞 Contact

For questions about the website or lab, contact:

- **Email**: <a.akrami@ucl.ac.uk>
- **Institution**: Sainsbury Wellcome Centre, UCL
- **Location**: London, UK

---

*This website showcases the research and people of the LIM Lab, contributing to our understanding of learning, inference, and memory in the brain.*
