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
        {% if event.url %}
        <a href="{{ event.url }}" class="event-link" target="_blank" rel="noopener noreferrer">
          <div class="event-item card-clickable">
            <span class="event-date">{{ event.date }}</span>
            <div class="event-title">{{ event.title }}</div>
            {% if event.description %}
              {{ event.description | markdownify }}
            {% endif %}
          </div>
        </a>
        {% else %}
        <div class="event-item">
          <span class="event-date">{{ event.date }}</span>
          <div class="event-title">{{ event.title }}</div>
          {% if event.description %}
            {{ event.description | markdownify }}
          {% endif %}
        </div>
        {% endif %}
        {% endfor %}
      {% else %}
        <p class="event-placeholder">{{ site.data.news.events_placeholder }}</p>
      {% endif %}
    </div>
  </section>

</div>
