---
layout: default
title: "Lab News"
description: "Latest news from LIM Lab (Learning, Inference & Memory), Athena Akrami's group at Sainsbury Wellcome Centre, UCL, London"
---

<div class="page-header">
  <h1>Lab News</h1>
  <p class="page-subtitle">Latest updates from LIM Lab</p>
</div>

<div class="news-content">
  <section class="news-section">
    <h2>Recent News</h2>

    {% for item in site.data.news.recent_news %}
    <article class="news-item">
      <div class="news-date">{{ item.date }}</div>
      <div class="news-item-content">
        <h3>{{ item.title }}</h3>
        {% for p in item.paragraphs %}
          {{ p | markdownify }}
        {% endfor %}
      </div>
    </article>
    {% endfor %}
  </section>

  <section class="news-section">
    <h2>Upcoming Events</h2>
    <div class="events-list">
      {% if site.data.news.upcoming_events.size > 0 %}
        {% for event in site.data.news.upcoming_events %}
        <div class="event-item">
          <span class="event-date">{{ event.date }}</span>
          <div class="event-title">{{ event.title | markdownify }}</div>
          {% if event.description %}
            {{ event.description | markdownify }}
          {% endif %}
        </div>
        {% endfor %}
      {% else %}
        <p class="event-placeholder">{{ site.data.news.events_placeholder }}</p>
      {% endif %}
    </div>
  </section>

  <section class="news-section">
    <h2>Lab Highlights</h2>
    <div class="highlights-grid">
      <div class="highlight-item">
        <h4>Research Focus</h4>
        <p>Our lab investigates the fundamental principles of learning, inference, and memory using a combination of theoretical and experimental approaches.</p>
      </div>
      <div class="highlight-item">
        <h4>Collaborations</h4>
        <p>We collaborate with researchers across UCL and internationally to advance our understanding of neural computation.</p>
      </div>
      <div class="highlight-item">
        <h4>Training</h4>
        <p>We provide comprehensive training in cutting-edge neuroscience techniques and computational methods.</p>
      </div>
    </div>
  </section>
</div>
