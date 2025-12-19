---
title: "Portfolio"
---

<style>
  .portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 40px;
    padding: 20px 0;
  }
  .project-card {
    text-decoration: none;
    color: inherit;
    transition: transform 0.3s ease;
  }
  .image-container {
    overflow: hidden;
    border-radius: 8px;
    line-height: 0;
  }
  .project-card img {
    width: 100%;
    transition: transform 0.5s ease, filter 0.5s ease;
  }
  .project-card:hover img {
    transform: scale(1.05); /* The Zoom effect */
    filter: brightness(1.1);
  }
  .project-card figcaption {
    margin-top: 15px;
    font-family: sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
  }
</style>

<div class="portfolio-grid">

  <a href="/portfolio/janus/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Janus"></div>
      <figcaption>Janus Mediterranean Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="/portfolio/cernunnos/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Cernunnos"></div>
      <figcaption>Cernunnos PropTech Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="/portfolio/citrus/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Citrus"></div>
      <figcaption>Citrus — Botany, Diversity & Data</figcaption>
    </figure>
  </a>

  <a href="/portfolio/monastic-mapping/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Monastic"></div>
      <figcaption>Monastic Mapping — Middle Ages</figcaption>
    </figure>
  </a>

  <a href="/portfolio/urban-water/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Water"></div>
      <figcaption>Urban Water — Minimal Data</figcaption>
    </figure>
  </a>

  <a href="/portfolio/climate-tracking/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Climate"></div>
      <figcaption>Global Climate Variance Study</figcaption>
    </figure>
  </a>

  <a href="/portfolio/supply-chain-viz/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Supply"></div>
      <figcaption>Logistics & Supply Chain Nodes</figcaption>
    </figure>
  </a>

  <a href="/portfolio/cultural-atlas/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Atlas"></div>
      <figcaption>The Cultural Atlas of Migration</figcaption>
    </figure>
  </a>

  <a href="/portfolio/energy-transition/" class="project-card">
    <figure>
      <div class="image-container"><img src="/images/portfolio/base.png" alt="Energy"></div>
      <figcaption>Renewable Energy Transition</figcaption>
    </figure>
  </a>

</div>