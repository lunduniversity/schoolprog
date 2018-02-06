---
title: Exercises
layout: page
toc: true
permalink: /exercises/
---

Here our proposed exercises will go!

<ul>
{% assign sitepages = site.pages | sort: 'order' %}
{% for sitepage in sitepages %}
  {% if sitepage.type == 'exercise' %}
    <li>
      <a href="{{ site.baseurl }}{{ sitepage.url }}">{{ sitepage.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>
