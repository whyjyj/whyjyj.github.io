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
     The query is required, not cosmetic: the gem defines .col-sm-* only inside
     (min-width: 576px), so an unscoped override also fires on phones and squeezes
     the thumbnail into a quarter of a ~375px screen.
     Keep in sync with the copy in _pages/about.md. */
  @media (min-width: 576px) {
    .publications .col-sm-2 {
      flex: 0 0 25%;
      max-width: 25%;
    }
    .publications .col-sm-8 {
      flex: 0 0 75%;
      max-width: 75%;
    }
  }

  /* Below that breakpoint the two columns stack so the thumbnail gets the full
     content width. The gem gives the entry column no `.col` class, so set an
     explicit full-width basis on both rather than relying on flex defaults. */
  @media (max-width: 575.98px) {
    .publications .col.col-sm-2,
    .publications .col-sm-8 {
      flex: 0 0 100%;
      max-width: 100%;
    }
    .publications .col.col-sm-2 {
      margin-bottom: 0.75rem;
    }
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
