---
layout: default
title: "Publications"
description: "Publications from LIM Lab (Learning, Inference & Memory), Athena Akrami's group at Sainsbury Wellcome Centre, UCL, London"
---

<div class="page-header">
  <h1>Publications</h1>
  <p class="page-subtitle">Research output from LIM Lab</p>
</div>

<div class="publications-content">
  <section class="publications-section">
    <h2>Preprints</h2>
    <div class="publication-list">
      {% for pub in site.data.publications.preprints %}
      <div class="publication-item">
        <p><strong>{{ pub.authors }}</strong>, "{{ pub.title }}" <em>({{ pub.journal }} {{ pub.year }})</em></p>
      </div>
      {% endfor %}
    </div>
  </section>
  
  <section class="publications-section">
    <h2>Published Papers</h2>
    
    {% assign published_by_year = site.data.publications.published | group_by: "year" | sort: "name" | reverse %}
    {% for year_group in published_by_year %}
    <div class="publication-year">
      <h3>{{ year_group.name }}</h3>
      <div class="publication-list">
        {% for pub in year_group.items %}
        <div class="publication-item">
          <p><strong>{{ pub.authors }}</strong>, "{{ pub.title }}" <em>({{ pub.journal }} {{ pub.year }}{% if pub.status %}, {{ pub.status }}{% endif %}{% if pub.note %}, {{ pub.note }}{% endif %})</em></p>
        </div>
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </section>
  
 </div>
