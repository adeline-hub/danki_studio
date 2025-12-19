---
title: "Portfolio"
---

<style>
  .portfolio-grid {
    display: grid;
    /* Force 3 colonnes sur ordinateur, 1 sur mobile */
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    padding: 20px 0;
  }

  @media (max-width: 768px) {
    .portfolio-grid {
      grid-template-columns: 1fr;
    }
  }

  .project-card {
    text-decoration: none !important;
    color: inherit;
    display: block;
  }

  .image-container {
    overflow: hidden;
    border-radius: 8px;
    line-height: 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  }

  .project-card img {
    width: 100%;
    height: auto;
    transition: transform 0.5s ease, filter 0.5s ease;
  }

  .project-card:hover img {
    transform: scale(1.08);
    filter: brightness(1.1);
  }

  .project-card figcaption {
    margin-top: 15px;
    font-family: sans-serif;
    font-weight: 600;
    font-size: 1rem;
    text-align: center;
    color: #333;
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