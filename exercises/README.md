---
title: Uppgifter
layout: page
toc: true
permalink: /exercises/
---

Här är uppgifterna vi börjat jobba på hittils. De kommer i blandad ordning så använd taggarna som står vid sidan om varje uppgift för att hitta rätt!

<ul>
{% assign sitepages = site.pages | sort: 'title' %}
{% for sitepage in sitepages %}
  {% if sitepage.type == 'exercise' %}
    <li>
    <a href="{{ site.baseurl }}{{ sitepage.url }}">{{ sitepage.title }}</a>

    {% if sitepage.tags %}
        ({{ sitepage.tags | join: ', '}})
    {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>
