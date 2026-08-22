---
layout: about
title: About
permalink: /
subtitle:

profile:
  align: right
  image: profile.jpg # file in assets/img/
  image_circular: true # crops the image to make it circular
  more_info: # text shown under the photo; left blank on purpose

# Every section below is rendered manually in the page body so the order matches
# bio -> social -> News -> Experience -> Education -> Publications -> Professional
# Services -> Honors and Awards. Keep these disabled; the layout would otherwise
# append News/posts/papers/social at the bottom in its own fixed order.
# `announcements.limit` and `announcements.scrollable` are still read by news.liquid.
selected_papers: false
social: false
latest_posts:
  enabled: false
announcements:
  enabled: false
  scrollable: true
  limit: 5
---

I'm a Master's student in the [Graduate School of Artificial Intelligence](https://ai.postech.ac.kr/) at [POSTECH](https://www.postech.ac.kr/eng/). As a member of the [Computer Vision Lab](https://cvlab.postech.ac.kr), I am conducting research under the supervision of Prof. [Suha Kwak](https://suhakwak.github.io).

My research focuses on Embodied AI and computer vision, with particular interests in Vision-Language-Action (VLA) models, their robustness and evaluation, and video understanding for intelligent agents operating in the real world.

<div class="social">
  {%- comment -%} jekyll-socials hardcodes a plain `mailto:` for the email icon, so pipe its output
  through al_email_protect_html — that rewrites the anchor into a click-to-copy element when
  `protect_email` is on, and passes it through untouched when it is off. {%- endcomment -%}
  {%- capture social_icons %}{% social_links %}{% endcapture -%}
  <div class="contact-icons">{{ social_icons | al_email_protect_html }}</div>
  <div class="contact-note">{{ site.contact_note }}</div>
</div>

<h2>News</h2>

{% include news.liquid limit=true %}

<div class="experience">
  <h2>Experience</h2>
  <!-- Add one <tr> per position, newest first. -->
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      <tr>
        <th scope="row" style="width: 20%">Feb. 2025 - Present</th>
        <td>
          <a href="https://cvlab.postech.ac.kr">Computer Vision Lab</a>, POSTECH, Pohang, South Korea<br />
          <em>Research and Teaching Assistant</em>
        </td>
      </tr>
      <tr>
        <th scope="row" style="width: 20%">Jan. 2024 - Jun. 2024</th>
        <td>
          AI &amp; Media (AIM) Lab, <a href="https://www.skku.edu/">Sungkyunkwan University</a>, Seoul, South Korea<br />
          <em>Undergraduate Research Intern</em><br />
          Advisor: Prof. <a href="https://www.csehong.com/">Sungeun Hong</a>.
        </td>
      </tr>
      <tr>
        <th scope="row" style="width: 20%">Nov. 2019 - Nov. 2020</th>
        <td>
          <a href="https://www.skku.edu/">Sungkyunkwan University</a>, Seoul, South Korea<br />
          <em>President, Student Council of the Department of Computer Education</em>
        </td>
      </tr>
    </table>
  </div>
</div>

<div class="education">
  <h2>Education</h2>
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      <tr>
        <th scope="row" style="width: 20%">Feb. 2025 - Present</th>
        <td>
          <a href="https://www.postech.ac.kr/">Pohang University of Science and Technology (POSTECH)</a>, Pohang, South Korea<br />
          M.S. Student in Graduate School of Artificial Intelligence<br />
          Advisor: Prof. <a href="https://suhakwak.github.io">Suha Kwak</a>.
        </td>
      </tr>
      <tr>
        <th scope="row" style="width: 20%">Mar. 2018 - Feb. 2025</th>
        <td>
          <a href="https://www.skku.edu/">Sungkyunkwan University (SKKU)</a>, Seoul, South Korea<br />
          B.S. in Computer Education<br />
          Advisor: Prof. <a href="https://www.csehong.com/">Sungeun Hong</a>.
        </td>
      </tr>
    </table>
  </div>
</div>

<style>
  /* Widen the thumbnail column and push the title/info block right. Overrides the
     col-sm-2 / col-sm-8 split in the gem-owned bib layout, which we cannot edit here.
     The query is required, not cosmetic: the gem defines .col-sm-* only inside
     (min-width: 576px), so an unscoped override also fires on phones and squeezes
     the thumbnail into a quarter of a ~375px screen.
     Keep in sync with the copy in _pages/publications.md. */
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

<div class="publications">
  <h2>Publications</h2>
  <!-- Entries marked `selected={true}` in _bibliography/papers.bib appear here.
       No --group_by flag, so this inherits site.scholar.group_by (year, descending)
       and prints a year heading above each group, like the publications page. -->
  {% bibliography --query @*[selected=true]* %}
</div>

<div class="honors">
  <h2>Honors and Awards</h2>
  <!-- Add one <tr> per award, newest first. -->
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      <tr>
        <td><strong>Gold Prize</strong>, 38th Workshop of Image Processing and Image Understanding (IPIU), 2026</td>
      </tr>
    </table>
  </div>
</div>
