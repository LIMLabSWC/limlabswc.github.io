---
layout: default
title: "People"
description: "People at LIM Lab (Learning, Inference & Memory), Athena Akrami's group at Sainsbury Wellcome Centre, UCL, London"
---

<div class="page-header">
  <h1>People</h1>
  <p class="page-subtitle">Meet the team at LIM Lab</p>
</div>

<div class="people-content">
  <section class="principal-investigator">
    <h2>Principal Investigator</h2>
    {% for person in site.data.people.principal_investigator %}
    <div class="person-card{% if person.url %} person-card-linked{% endif %}">
      <div class="person-photo">
        <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="person-image">
      </div>
      <div class="person-info">
        <h3>
          {% if person.url %}
            <a href="{{ person.url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>
          {% else %}
            {{ person.name }}
          {% endif %}
        </h3>
        <p class="person-title">{{ person.title }}</p>
        <p class="person-affiliation">{{ person.affiliation }}</p>
        <p>{{ person.description }}</p>
        <div class="person-links">
          {% if person.email %}
            <a href="mailto:{{ person.email }}">Email</a>
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
  </section>

  <section class="lab-members">
    <h2>Lab Members</h2>

    <div class="members-section">
      <h3>Senior Research Fellows</h3>
      <div class="members-grid">
        {% for person in site.data.people.senior_research_fellows %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>

    <div class="members-section">
      <h3>Research Fellows</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_fellows %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>

    <div class="members-section">
      <h3>PhD Students</h3>
      <div class="members-grid">
        {% for person in site.data.people.phd_students %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>

    <div class="members-section">
      <h3>Research Technicians</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_technicians %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>

    <div class="members-section">
      <h3>Research Assistants</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_assistants %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>

    <div class="members-section">
      <h3>Alumni</h3>
      <div class="members-grid">
        {% for person in site.data.people.alumni %}
          {% include member-card.html person=person %}
        {% endfor %}
      </div>
    </div>
  </section>
</div>
