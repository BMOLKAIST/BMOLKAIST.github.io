---
layout: page
title: people
permalink: /people/
nav: true
nav_order: 2
description: Members of the Biomedical Optics Laboratory at KAIST.
---

<style>
.bmol-person { text-align: center; margin-bottom: 1.5rem; }
.bmol-person img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,.12); }
.bmol-person .name { font-weight: 600; margin: .5rem 0 0; font-size: .95rem; line-height: 1.2; }
.bmol-person .meta { font-size: .8rem; margin: 0; opacity: .65; }
.bmol-alumni li { margin-bottom: .25rem; }
</style>

## Principal Investigator

<div class="row">
  <div class="col-md-3 col-6 bmol-person">
    <img src="{{ '/assets/img/team/yongkeun-park.png' | relative_url }}" alt="YongKeun (Paul) Park">
    <p class="name">YongKeun (Paul) Park</p>
    <p class="meta">Professor of Physics · Director</p>
  </div>
</div>

## Postdoctoral Associates

<div class="row">
{% for m in site.data.members.postdocs %}
  <div class="col-md-3 col-6 bmol-person">
    <img src="{{ '/assets/img/team/' | append: m.image | relative_url }}" alt="{{ m.name }}">
    <p class="name">{{ m.name }}</p>
    <p class="meta">Since {{ m.since }}</p>
  </div>
{% endfor %}
</div>

## Graduate Students

<div class="row">
{% for m in site.data.members.grads %}
  <div class="col-md-3 col-6 bmol-person">
    <img src="{{ '/assets/img/team/' | append: m.image | relative_url }}" alt="{{ m.name }}">
    <p class="name">{{ m.name }}</p>
    <p class="meta">Since {{ m.since }}</p>
  </div>
{% endfor %}
</div>

## Undergraduate Students

<div class="row">
{% for m in site.data.members.undergrads %}
  <div class="col-md-3 col-6 bmol-person">
    <img src="{{ '/assets/img/team/' | append: m.image | relative_url }}" alt="{{ m.name }}">
    <p class="name">{{ m.name }}</p>
  </div>
{% endfor %}
</div>

## Administrative Staff

- **Hyun-Ju Park** — Administrative Assistant

---

## Alumni

<div class="bmol-alumni" markdown="1">

**Research Professors**
{% for m in site.data.members.alumni_research_prof %}
- {{ m.name }} <span class="meta">({{ m.note }})</span>
{% endfor %}

**Postdoctoral Associates**
{% for m in site.data.members.alumni_postdocs %}
- {{ m.name }} — {{ m.note }}
{% endfor %}

**Graduate Students**
{% for m in site.data.members.alumni_grads %}
- {{ m.name }} — {{ m.note }}
{% endfor %}

**Research Assistants**
{% for m in site.data.members.alumni_research_assistant %}
- {{ m.name }} — {{ m.note }}
{% endfor %}

**Undergraduate Students**
{% for m in site.data.members.alumni_undergrads %}
- {{ m.name }} — {{ m.note }}
{% endfor %}

</div>
