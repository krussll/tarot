# Tarot & Cartomancy (`tarot`) — Project Overview & Architecture Guide

**Repository**: `krussll/tarot`  
**Active Production Branch**: `gh-pages`  
**Hosting Platform**: GitHub Pages  
**Engine**: Jekyll 4.4.x (Ruby Static Site Generator)  
**Primary Author/Persona**: Reece Williams (`reece`)  
**Site Topic**: Playing Card Divination (Cartomancy), Tarot Parallels, and Card Combination Interpretations  

---

## 1. Executive Summary & Site Concept

The **Tarot & Cartomancy** project is an editorial and programmatic content website designed to be the definitive digital reference for cartomancy—specifically reading standard 52-card playing decks for divination, fortune-telling, and personal insight, alongside their relationships to traditional 78-card Tarot (Minor Arcana).

### Core Concept & Mission
- **Demystifying Cartomancy**: Provide accessible, practical, and grounded interpretations for reading standard playing cards as a divination tool.
- **Pairwise Combinations Engine (1,326 Pairs)**: Systematically interpret all 1,326 unique two-card combinations from a 52-card deck ($\binom{52}{2} = 1,326$), complete with dedicated custom illustration assets already prepared in the codebase.
- **Suit & Numerology Foundations**: Deep-dive into the four suits (Hearts, Diamonds, Clubs, Spades) and their elemental connections (Water, Earth, Fire, Air) matching the Tarot suits (Cups, Pentacles, Wands, Swords).
- **Spreads & Practical Divination**: Guide users through spread layouts (single-card draws, 3-card past/present/future, 9-card box spreads, and modified Celtic Cross spreads) for love, career, finances, and personal growth.

### Repository Origin & Current Transition State
The codebase was cloned and adapted from Reece's custom Jekyll publishing ecosystem (originating from WowThemes' "Affiliates" theme and shared with sister projects `zoonearme`, `howtoplaysport`, and `riverpairs`). 

Currently, the site is in a **scaffolding transition phase**:
- **Assets Present**: The repository contains the complete asset set of **1,326 pairwise cartomancy combination illustrations** under `assets/images/cartomancy/`.
- **Boilerplate Remnants**: Several configuration and layout files still hold placeholder copy and settings from earlier projects (such as "Zoo Near Me", "Jack High Bowls", and "How To Play Sport") in `_config.yml`, `_layouts/`, `about-me.md`, and `contact.md`.
- **Target Objective**: Complete the transition into a fully rebranded, high-authority Tarot and Cartomancy destination.

---

## 2. Technical Stack & Architecture

```
                               +-----------------------------+
                               |     Markdown & Assets       |
                               |  - Cartomancy Combinations  |
                               |  - Single Card Guides       |
                               |  - 1,326 Pair Images        |
                               +--------------+--------------+
                                              |
                                              v
+--------------------------+   +--------------+--------------+   +---------------------------+
|         Layouts          |-->|     Jekyll 4.4.x Engine      |<--|    Includes & Partials    |
| default, post, page,     |   |   (GitHub Pages Builder)    |   | postbox, featuredbox,     |
| post-left-sidebar        |   +--------------+--------------+   | sidebar, pagination       |
+--------------------------+                  |                  +---------------------------+
                                              v
                               +--------------+--------------+
                               |   Compiled Static HTML/CSS  |
                               |   Served via GitHub Pages   |
                               |   Branch: gh-pages          |
                               +-----------------------------+
```

### Technical Specifications
| Layer | Technology | Details / Configuration |
| :--- | :--- | :--- |
| **Static Site Generator** | Jekyll 4.4.1 | Liquid templating, SCSS preprocessing, Kramdown Markdown parser |
| **Hosting & Deployment** | GitHub Pages | Automatically compiled and deployed from the `gh-pages` branch |
| **CSS Framework** | Bootstrap 4.0.0-alpha.6 | Responsive grid, utility classes, card components |
| **Custom Styling** | `assets/css/theme.css`, `_sass/config.scss`, `assets/css/custom.scss` | Adapted from WowThemes Affiliates; customized palette of dark teal (`#277c80`), cyan (`#00B2D8`), and lime accent (`#6FD350`) |
| **Typography & Icons** | Google Fonts ("Rubik") & FontAwesome 5.8.1 | Rubik weights 400, 500, 700; FontAwesome and Casper font icons for UI |
| **Client-Side Scripts** | jQuery 3.x, Masonry, Lazysizes | Dynamic masonry grid for post cards, lazy image loading for optimal Core Web Vitals |
| **Monetization Stack** | AdSense, Ezoic, Amazon Affiliates | `ads.txt` (publisher `pub-8543572621618524`), Ezoic placeholders (`103`, `104`, video), Amazon Associates disclaimer |
| **Analytics & Verification** | Google Tag Manager / GA4 | Integrated via `gtag.js` in `_layouts/default.html` |

---

## 3. Main Content Clusters

The content architecture is structured around five strategic pillars, blending programmatic combinatorial coverage with high-intent editorial guidance:

```
                                  +-----------------------------+
                                  |     Tarot & Cartomancy      |
                                  |      Content Universe       |
                                  +--------------+--------------+
                                                 |
         +-----------------------+---------------+-----------------------+
         |                       |                                       |
         v                       v                                       v
+------------------+   +--------------------+                 +--------------------+
|  1. Pairwise     |   |  2. Single Card    |                 |  3. Spreads &      |
|  Combinations    |   |  & Suit Profiles   |                 |  Divination Method |
|  (1,326 Matchups)|   |  (52 Cards + Suits)|                 |  (Spreads Library) |
+------------------+   +--------------------+                 +--------------------+
         |                       |                                       |
         +-----------------------+---------------+-----------------------+
                                                 |
                                 +---------------+---------------+
                                 |                               |
                                 v                               v
                       +--------------------+          +--------------------+
                       |  4. Cartomancy vs  |          |  5. Trust, Legal & |
                       |  Tarot Theory      |          |  Author Authority  |
                       |  (Comparative SEO) |          |  (E-E-A-T Pages)   |
                       +--------------------+          +--------------------+
```

### Cluster 1: Cartomancy Pairwise Combinations (The 1,326 Pairs Engine)
The programmatic backbone of the site. In cartomancy, two cards drawn together create a distinct, combined narrative that modifies their individual meanings.
- **Total Universe**: Exactly 1,326 unique combinations ($\frac{52 \times 51}{2} = 1,326$).
- **Visual Asset Pairing**: Every pair has a dedicated illustration in `assets/images/cartomancy/`:
  - Filename format: `Drawing-[Card1]-And-[Card2]-Together.jpg` (e.g., `Drawing-10-of-Clubs-And-Ace-of-Hearts-Together.jpg`).
- **Standardized Combinatorial Page Schema**:
  1. **Quick Meaning / Summary Box**: High-level verdict when both cards appear together.
  2. **Card Visual**: High-resolution image of the two cards drawn side-by-side.
  3. **General / Life Theme**: Overarching energetic dynamic (e.g., career breakthrough, emotional tension).
  4. **Love & Relationships**: Interpretation when asking about romantic or interpersonal questions.
  5. **Career, Wealth & Finances**: Practical insights for professional life and money matters.
  6. **Reversed / Shadow Aspect**: Nuances if surrounding cards are negative or challenging.
  7. **Advice / Actionable Step**: Concrete guidance for the querent.

### Cluster 2: Single Card & Suit Profiles (The 52 Cards)
Detailed foundational guides for each of the 52 playing cards and the 4 suits:
- **Suit Foundations & Tarot Equivalents**:
  - **Hearts** (Water / Cups): Emotions, romantic love, friendships, domestic life, healing, vulnerability.
  - **Diamonds** (Earth / Pentacles): Finances, career, business ventures, tangible goals, practical realities, energy exchange.
  - **Clubs** (Fire / Wands): Ambition, enterprise, creative projects, passion, drive, education, willpower.
  - **Spades** (Air / Swords): Intellect, mental challenges, conflict, communication, difficult choices, transformations, warnings.
- **Rank Progression (Numerology)**:
  - **Aces**: Seeds, beginnings, major opportunities, breakthroughs.
  - **Twos to Tens**: Progression from polarity/choice (2), expansion (3), stability/foundations (4), conflict/change (5), harmony (6), spirituality/tests (7), movement/power (8), culmination (9), to endings and cycles (10).
  - **Court Cards (Jacks, Queens, Kings)**: Personalities, visitors, maturity levels, archetypal influences (Jack = Youth/Messenger, Queen = Nurturing/Intuitive Authority, King = Mastery/External Leadership).

### Cluster 3: Divination Spreads & Reading Techniques
Practical instructions for executing readings using a regular deck:
- **Single-Card Daily Oracle**: Morning guidance and daily meditation focus.
- **Three-Card Spreads**:
  - Past / Present / Future
  - Mind / Body / Spirit
  - Situation / Challenge / Advice
- **Five-Card & Nine-Card Box Spreads**: Comprehensive situation assessment, cross-influences, and root causes.
- **The Cartomancy Horseshoe & Grand Tableau**: Traditional European cartomancy layouts for advanced practitioners.

### Cluster 4: Cartomancy vs. Tarot Theory (Comparative SEO)
Educational, high-intent informational content targeting searchers comparing playing card divination to Tarot:
- Can you read regular playing cards as Tarot cards?
- What are the missing Major Arcana and Knight cards, and how does cartomancy compensate?
- How to prepare, consecrate, and shuffle your cartomancy deck.
- Reading reversed playing cards (identifying subtle asymmetrical indices).

### Cluster 5: Trust, Legal & Author Authority (E-E-A-T)
- **About Reece**: Cartomancy practitioner, intuitive reader, and student of historical card divination traditions.
- **Reading Ethics & Philosophy**: Empowering, non-fatalistic approach focusing on agency and self-reflection.
- **Legal & Compliance**: Clear disclaimers for entertainment/guidance purposes, Privacy Policy, Terms, and Affiliate disclosures.

---

## 4. Brand Colours & Visual Guidelines

The site leverages a balanced palette blending mystical elegance with modern, clean, and high-readability design. It steers clear of cluttered, hard-to-read gothic tropes in favor of an approachable editorial style.

### Complete Color Palette
| Color Name | Hex Code | Usage & Placement | CSS Selector / Variable |
| :--- | :--- | :--- | :--- |
| **Theme Primary / Navigation Teal** | `#277c80` | Header navigation background, primary CTA buttons, headings | `.mediumnavigation`, `.btn-primary` |
| **Secondary Bright Teal / Cyan** | `#00B2D8` | SCSS theme accent, footer background default | `_sass/config.scss`: `$nav-background`, `$footer-background` |
| **Accent Lime Green** | `#6FD350` | Hyperlinks, link hover states, featured badges | `a`, `a:hover`, `.author-description a` |
| **Secondary Accent Indigo / Purple** | `#675bff` | Interactive hover states, mystical highlights, tags | Tag badges, secondary button hover |
| **Accent Yellow** | `#fff100` | Alert banners, highlight tags, notification callouts | `.alert-highlight`, featured pill |
| **Dark Slate / Primary Text** | `#24292e` | Body text, high-contrast headings, secondary footer | `$content-font`, `$footer-secondary-background`, `body` |
| **Charcoal Headings** | `#171e27` / `#333333` | Post titles, card headers, section titles | `h1`, `h2`, `h3`, `.posttitle` |
| **Border & Divider Gray** | `#E3EDF3` | Code borders, card borders, subtle separators | `pre`, `.card`, `.border` |
| **Light Gray Code / Card BG** | `#F7FAFB` | Code blocks, callout quote backgrounds | `pre`, `.highlight` |
| **Soft Page Backgrounds** | `#ECEEEF` / `#f6f6f4` | Jumbotron backgrounds, intro section styling | `$jumbotron-background`, `$secondary-jumbotron-background` |
| **Card White** | `#ffffff` | Post cards, reading layout tiles, main container | `.card`, `.bg-white` |

### Suit-Specific Visual Styling
When formatting card combinations and meanings in articles, use consistent suit cues:
- **Hearts (♥)** & **Diamonds (♦)**: Crimson red accent (`#c0392b` or `#d63031`).
- **Clubs (♣)** & **Spades (♠)**: Deep charcoal / midnight slate (`#2c3e50` or `#171e27`).

### Typography Standards
- **Primary Body & Headings**: `"Rubik", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;`
  - Loaded via Google Fonts with weights: `400` (Regular), `400i` (Italic), `500` (Medium), `700` (Bold).
- **Code & Monospace**: `monospace, sans-serif;`
- **Iconography**: FontAwesome 5.8.1 (`use.fontawesome.com/releases/v5.8.1/css/all.css`) and Casper web icons (`assets/fonts/casper-icons.*`).

### Editorial Voice & Tone
- **Tone**: Wise, compassionate, analytical, and grounded. Never fear-inducing or superstitious.
- **Empowerment Focus**: Cards reveal prevailing energies and psychological reflections; the querent always holds free will.
- **Format**: Scannable, structured Markdown with bulleted takeaways, bold highlights, and clean comparison tables.

---

## 5. Project Setup, Directory Structure & Build Guide

### Directory & File Structure

```
tarot/
├── .git/                        # Git version control directory (branch: gh-pages)
├── _config.yml                  # Jekyll global configuration
├── index.html                   # Homepage template (Hero, featured posts, recent posts)
├── about-me.md                  # Author biography page
├── contact.md                   # Contact page
├── all-posts.md                 # Complete archive page using masonry grid
├── privacy.md                   # Privacy Policy
├── terms.md                     # Terms and Conditions
├── affiliate-disclaimer.md      # Amazon Associates & monetization disclaimer
├── ads.txt                      # AdSense publisher authorization file
├── robots.txt                   # Search crawler directives
├── feed.xml                     # RSS syndication feed
├── sitemap.xml                  # XML sitemap generator
├── favicon.ico                  # Site favicon
│
├── _layouts/                    # Liquid page layout templates
│   ├── default.html             # Base HTML wrapper (head, nav, footer, scripts)
│   ├── post.html                # Standard single-post layout (article + author + prev/next)
│   ├── post-left-sidebar.html   # 2-column post layout with sidebar
│   ├── page.html                # Standard page layout
│   └── archive.html             # Category/archive listing layout
│
├── _includes/                   # Reusable Liquid template components
│   ├── postbox.html             # Post card item for grid feeds
│   ├── featuredbox.html         # Featured post highlight card
│   ├── sidebar.html             # Sidebar wrapper
│   ├── recommended.html         # Recommended post links
│   ├── useful.html              # Useful resources partial
│   ├── pagination.html          # Pagination controls
│   ├── newsletter.html          # Email newsletter signup block
│   ├── newsletter-signup.html   # Sendinblue / Brevo newsletter form
│   ├── search-form.html         # Search input partial
│   └── all-posts.html           # Archive loop partial
│
├── _posts/                      # Published Jekyll blog posts (YYYY-MM-DD-title.md)
├── _drafts/                     # Unpublished draft articles
│
├── _sass/                       # SCSS stylesheets
│   ├── config.scss              # SCSS variables for nav, footer, and jumbotron
│   └── _syntax.scss             # Rouge/Pygments code syntax highlighting styles
│
├── assets/                      # Static assets
│   ├── css/
│   │   ├── theme.css            # Compiled core theme styling (Affiliates theme)
│   │   └── custom.scss          # SCSS compiler entry point importing _sass/
│   ├── fonts/                   # Casper icon web fonts (.eot, .svg, .ttf, .woff)
│   ├── js/                      # JavaScript libraries
│   │   ├── jquery.min.js        # jQuery 3.x
│   │   ├── masonry.pkgd.min.js  # Masonry grid layout engine
│   │   ├── lazysizes.min.js     # Responsive image lazyloader
│   │   ├── theme.js             # Navigation behavior & animations
│   │   └── ie10-viewport-bug-workaround.js
│   └── images/
│       ├── cartomancy/          # 1,326 pairwise card combination images (150MB+)
│       └── zoonearme.png        # Legacy logo asset (to be replaced)
│
└── agents/                      # Agent instruction and project documentation
    ├── overview.md              # This single source of truth document
    └── project_overview.md      # Symlink to overview.md for tool compatibility
```

### Local Development & Build Commands

The site uses standard Jekyll on Ruby. Because Jekyll is installed globally (`jekyll 4.4.1`, `ruby 2.7.4p191`), no complex container or Node build step is necessary.

#### 1. Running the Local Dev Server
```bash
# Serve locally with root baseurl (essential for local links and asset paths)
jekyll serve --baseurl ""

# Serve including unpublished drafts in _drafts/
jekyll serve --baseurl "" --drafts

# Serve with live reloading on file changes
jekyll serve --baseurl "" --livereload
```
> [!IMPORTANT]
> Because production `_config.yml` sets `baseurl`, running `jekyll serve` without `--baseurl ""` will cause assets and links to point to production URLs. Always include `--baseurl ""` for local previews.

#### 2. Building Static Output
```bash
# Compile site into _site/ directory
jekyll build

# Production build with production environment flag
JEKYLL_ENV=production jekyll build
```

#### 3. Git & GitHub Pages Deployment
- Pushing to the `gh-pages` branch triggers the GitHub Pages Jekyll build automatically.
- Ensure `_site/` and `.jekyll-cache/` are **never committed** to git.

---

## 6. Frontmatter Data Model & Post Archetypes

### Post Frontmatter Schema
Each cartomancy post must follow standard Jekyll YAML frontmatter:

```yaml
---
layout: post
title: "10 of Clubs and Ace of Hearts Cartomancy Meaning"
description: "Discover what it means when the 10 of Clubs and Ace of Hearts appear together in a cartomancy reading. Explore love, career, and wealth interpretations."
first_paragraph: "When the ambitious 10 of Clubs meets the emotionally rich Ace of Hearts, practical effort yields joyful domestic and creative fulfillment."
image: "assets/images/cartomancy/Drawing-10-of-Clubs-And-Ace-of-Hearts-Together.jpg"
author: reece
categories: [ cartomancy, combinations ]
tags: [ "10 of clubs", "ace of hearts", "love", "career", "combinations" ]
featured: false
comments: false
date: 2026-11-09 10:00:00 +0000
last_modified_at: 2026-11-09
---
```

### Key Frontmatter Properties
- `layout`: Always `post` (or `post-left-sidebar` if a dedicated table of contents / spread widget is used).
- `title`: High-intent search title including both card names and "Cartomancy Meaning" or "Together".
- `first_paragraph`: Summarizes the reading verdict in 1-2 sentences. Crucial because `_includes/postbox.html` extracts `{{ post.first_paragraph | strip_html | truncatewords:15 }}` for homepage and archive card previews.
- `image`: Relative path to the image. `post.html` renders `<img class="featured-image img-fluid" src="{{ site.baseurl }}/{{ page.image }}">`.
- `categories`: Primary taxonomy buckets (e.g., `combinations`, `suits`, `spreads`, `theory`).
- `featured`: Set to `true` to display in the homepage hero carousel/grid (`_includes/featuredbox.html`).

---

## 7. Audit of Legacy Debt & Rebranding Checklist

To transition the site from its inherited boilerplate into the definitive Tarot/Cartomancy destination, agents should address the following items:

| Priority | Item | Current State | Required Fix |
| :---: | :--- | :--- | :--- |
| **High** | `_config.yml` Branding | Displays `Zoo Near Me` and `zoonear.me` URLs | Update `name`, `title`, `description`, `meta_description`, `url`, and `baseurl` to Tarot/Cartomancy branding |
| **High** | Navigation & Header | Links to `/zoos-by-states` and has `zoonearme.png` logo | Update `_layouts/default.html` navigation links to: Home, Card Combinations, Single Cards, Spreads, and About; replace logo |
| **High** | Add `.gitignore` | No `.gitignore` exists; riesgo of committing `_site/` | Create `.gitignore` ignoring `_site/`, `.jekyll-cache/`, `.sass-cache/`, `.jekyll-metadata` |
| **High** | Untracked Images | 1,326 images in `assets/images/cartomancy/` are untracked | Verify, stage, or configure LFS / tracking for cartomancy images as needed |
| **Medium** | `about-me.md` | Zoo enthusiast bio | Replace with Reece's cartomancy and tarot reading background, ethics, and site mission |
| **Medium** | `index.html` Copy | Mentions "Unleashing America's Wildlife Wonders" | Rewrite hero section and intro for playing card divination and tarot mastery |
| **Medium** | `_layouts/post.html` | Schema publisher says `How To Play Sport` | Change publisher `<span itemprop="name">` to `{{ site.name }}` |
| **Medium** | `contact.md` | Lists `reece@jackhighbowls.com` | Update contact email address to match site domain |
| **Low** | Search Form | Search form points to `/search` which has no template | Implement search template or remove search link from includes |

---

## 8. Strategic Roadmap for Future Agent Work

1. **Phase 1: Foundation & Rebranding**
   - Clean up `_config.yml`, `index.html`, `about-me.md`, and default layouts.
   - Add `.gitignore` to prevent repository pollution.
   - Establish dedicated Tarot logo / icon in `assets/images/`.

2. **Phase 2: Programmatic Combinations Engine**
   - Create post templates / generators for the 1,326 cartomancy pairwise combinations.
   - Ensure every combination post links directly to its existing illustration in `assets/images/cartomancy/`.
   - Organize internal cross-linking between individual card profiles and their pairwise combinations.

3. **Phase 3: Pillar Content & Spreads Library**
   - Author foundational suit guides (Hearts, Diamonds, Clubs, Spades).
   - Write practical spread tutorials (3-card spreads, Celtic Cross adaptation).
   - Create category landing pages for `combinations`, `suits`, and `spreads`.

4. **Phase 4: SEO, Schema & Monetization Polish**
   - Implement `Article` / `HowTo` Schema structured data on post templates.
   - Audit sitemap, robots.txt, and canonical URLs.
   - Refine internal linking hubs to distribute page authority across the 1,326 combination pages.

