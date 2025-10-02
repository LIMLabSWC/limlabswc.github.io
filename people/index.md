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
    <div class="person-card">
      <div class="person-photo">
        <img src="{{ '/assets/img/athena1b.jpg' | relative_url }}" alt="Dr. Athena Akrami" class="person-image">
      </div>
      <div class="person-info">
        <h3>Dr. Athena Akrami</h3>
        <p class="person-title">Principal Investigator</p>
        <p class="person-affiliation">Sainsbury Wellcome Centre, UCL</p>
        <p>Athena Akrami leads the Learning, Inference & Memory Lab at the Sainsbury Wellcome Centre, UCL. Her research focuses on understanding the neural mechanisms underlying learning, memory, and inference in both humans and animals.</p>
        <div class="person-links">
          <a href="mailto:a.akrami@ucl.ac.uk">Email</a>
          <a href="https://www.ucl.ac.uk/swc/people/athena-akrami" target="_blank" rel="noreferrer">SWC Profile</a>
        </div>
      </div>
    </div>
  </section>
  
  <section class="lab-members">
    <h2>Lab Members</h2>
    
    <div class="members-section">
      <h3>Senior Research Fellows</h3>
      <div class="members-grid">
        {% for person in site.data.people.senior_research_fellows %}
        <div class="member-card">
          <div class="member-photo">
            {% if person.photo %}
              <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="member-image">
            {% else %}
              <div class="member-placeholder">No Photo</div>
            {% endif %}
          </div>
          <div class="member-info">
            <h4>{{ person.name }}</h4>
            <p class="member-title">{{ person.title }}</p>
            <p class="member-description">{{ person.description }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    
    <div class="members-section">
      <h3>Research Fellows</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_fellows %}
        <div class="member-card">
          <div class="member-photo">
            {% if person.photo %}
              <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="member-image">
            {% else %}
              <div class="member-placeholder">No Photo</div>
            {% endif %}
          </div>
          <div class="member-info">
            <h4>{{ person.name }}</h4>
            <p class="member-title">{{ person.title }}</p>
            <p class="member-description">{{ person.description }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    
    <div class="members-section">
      <h3>PhD Students</h3>
      <div class="members-grid">
        {% for person in site.data.people.phd_students %}
        <div class="member-card">
          <div class="member-photo">
            {% if person.photo %}
              <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="member-image">
            {% else %}
              <div class="member-placeholder">No Photo</div>
            {% endif %}
          </div>
          <div class="member-info">
            <h4>{{ person.name }}</h4>
            <p class="member-title">{{ person.title }}</p>
            <p class="member-description">{{ person.description }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    
    <div class="members-section">
      <h3>Research Technicians</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_technicians %}
        <div class="member-card">
          <div class="member-photo">
            {% if person.photo %}
              <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="member-image">
            {% else %}
              <div class="member-placeholder">No Photo</div>
            {% endif %}
          </div>
          <div class="member-info">
            <h4>{{ person.name }}</h4>
            <p class="member-title">{{ person.title }}</p>
            <p class="member-description">{{ person.description }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    
    <div class="members-section">
      <h3>Research Assistants</h3>
      <div class="members-grid">
        {% for person in site.data.people.research_assistants %}
        <div class="member-card">
          <div class="member-photo">
            {% if person.photo %}
              <img src="{{ '/assets/img/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="member-image">
            {% else %}
              <div class="member-placeholder">No Photo</div>
            {% endif %}
          </div>
          <div class="member-info">
            <h4>{{ person.name }}</h4>
            <p class="member-title">{{ person.title }}</p>
            <p class="member-description">{{ person.description }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>
  
  <section class="alumni">
    <h2>Alumni</h2>
    <p>Information about former lab members will be updated here as the lab grows.</p>
  </section>
</div>
