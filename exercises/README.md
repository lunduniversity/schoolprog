---
title: Exercises
layout: page
toc: true
permalink: /exercises/
---

Here are the exercises we've written so far, in no particular order.

<ul>
{% assign sitepages = site.pages | sort: 'order' %}
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
