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

<div class="row align-items-center mb-4">
  <div class="col-md-3 col-sm-4 col-6 mb-3 mb-md-0">
    <img src="{{ '/assets/img/team/yongkeun-park.jpg' | relative_url }}" alt="YongKeun (Paul) Park" style="width:100%; border-radius:8px; box-shadow:0 1px 6px rgba(0,0,0,.14);">
  </div>
  <div class="col-md-9 col-sm-8">
    <p style="font-weight:600; font-size:.95rem; line-height:1.2; margin:0 0 .5rem;">YongKeun (Paul) Park</p>
    <p style="font-size:.8rem; opacity:.65; margin:0; line-height:1.6;">
      Endowed Chair Professor, Department of Physics, KAIST<br>
      Director, Virtual 3D Biology Center, KAIST<br>
      Optica Fellow, SPIE Fellow, NAEK Member, YKAST Member<br>
      Cofounder and CEO, Tomocube<br>
      Cofounder and Advisor, TheWaveTalk
    </p>
    <p style="font-size:.8rem; opacity:.65; margin:.5rem 0 0;">
      <strong>O</strong>&nbsp;+82.42.350.2514 &nbsp;|&nbsp; <strong>E</strong>&nbsp;yk.park at kaist.ac.kr &nbsp;|&nbsp; <a href="https://www.dropbox.com/scl/fi/fj1sidzwd1a750kfygx9w/resume-ykpark-online-posting.pdf?rlkey=c8j94h77lgvo84s8zsxnrnhgh&amp;st=h9k7di9a&amp;dl=0" target="_blank" rel="noopener">CV</a>
    </p>
  </div>
</div>

## Postdoctoral Associates

<div class="row">
{% for m in site.data.members.postdocs %}
  <div class="col-md-3 col-6 bmol-person">
    <img src="{{ '/assets/img/team/' | append: m.image | relative_url }}" alt="{{ m.name }}">
    <p class="name">{{ m.name }}</p>
    <p class="meta">{{ m.email }}</p>
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
    <p class="meta">{{ m.email }}</p>
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
    <p class="meta">{{ m.email }}</p>
  </div>
{% endfor %}
</div>

## Administrative Staff

- **Hyun-Ju Park** — Administrative Assistant · <span class="meta">hyunju90 at kaist.ac.kr</span>

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
