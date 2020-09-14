---
title: Uppdrag
layout: page
toc: true
permalink: /exercises/
---

<style>
.card {
    background: #EEE;
    margin: 1%;
    border: 1px solid #DDD;
    border-radius: 0.25em;
    float: left;
    width: 47%;
    height: 5em;
}

.card > div {
    padding: 0.5em;
}

a > .card {
    color: #000 !important;
}

a > .card > div > small {
    color: #666 !important;
}
</style>

Här är uppgifterna vi börjat jobba på hittils. De kommer i blandad ordning så använd taggarna som står vid sidan om varje uppgift för att hitta rätt!

<div>
{% assign sitepages = site.pages | sort: 'title' %}
{% for sitepage in sitepages %}
    {% if sitepage.type == 'exercise' %}
        <a href="{{ site.baseurl }}{{ sitepage.url }}">
            <div class="card">
                <div>
                <b>{{ sitepage.title }}</b>
                <br>
                <small>
                    <i>
                    {% if sitepage.tags %}
                        {{ sitepage.tags | sort | join: ', '}}
                    {% endif %}
                    </i>
                </small>
                </div>
            </div>
        </a>
    {% endif %}
{% endfor %}
</div>
