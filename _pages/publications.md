---
layout: page
permalink: /publications/
title: Publications
description:
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<style>
  /* Widen the thumbnail column and push the title/info block right. Overrides the
     col-sm-2 / col-sm-8 split in the gem-owned bib layout, which we cannot edit here.
     Keep in sync with the copy in _pages/about.md. */
  .publications .col-sm-2 {
    flex: 0 0 25%;
    max-width: 25%;
  }
  .publications .col-sm-8 {
    flex: 0 0 75%;
    max-width: 75%;
  }

  /* Equal-contribution note printed inline after the author list, instead of the
     hover-only info icon the gem-owned bib layout renders for `annotation`.
     Add one selector per bib key that needs it. */
  #lee2026robustness .author::after {
    content: " (*equal contribution)";
  }
</style>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
