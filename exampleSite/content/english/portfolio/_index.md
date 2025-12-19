---
title: "Portfolio"
---

{{< rawhtml >}}

<style>
  .portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    padding: 40px 0;
  }

  /* Tablette */
  @media (max-width: 1024px) {
    .portfolio-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  /* Mobile */
  @media (max-width: 640px) {
    .portfolio-grid {
      grid-template-columns: 1fr;
    }
  }

  .project-card {
    text-decoration: none;
    color: inherit;
    display: block;
  }

  .image-container {
    overflow: hidden;
    border-radius: 12px;
    line-height: 0;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    background: #f4f4f4;
  }

  .project-card img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.5s ease, filter 0.5s ease;
  }

  .project-card:hover img {
    transform: scale(1.08);
    filter: brightness(1.05);
  }

  .project-card figcaption {
    margin-top: 14px;
    font-weight: 600;
    font-size: 0.95rem;
    text-align: center;
    color: #222;
  }
</style>

<div class="portfolio-grid">

  <a href="{{ "portfolio/janus/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Janus project">
      </div>
      <figcaption>Janus — Mediterranean Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/cernunnos/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Cernunnos project">
      </div>
      <figcaption>Cernunnos — PropTech Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/citrus/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Citrus project">
      </div>
      <figcaption>Citrus — Botany, Diversity & Data</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/monastic-mapping/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Monastic Mapping project">
      </div>
      <figcaption>Monastic Mapping — Middle Ages</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/urban-water/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Urban Water project">
      </div>
      <figcaption>Urban Water — Minimal Data</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/climate-tracking/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Climate Tracking project">
      </div>
      <figcaption>Global Climate Variance Study</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/supply-chain-viz/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Supply Chain project">
      </div>
      <figcaption>Logistics & Supply Chain Nodes</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/cultural-atlas/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Cultural Atlas project">
      </div>
      <figcaption>The Cultural Atlas of Migration</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/energy-transition/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img src="{{ "images/portfolio/base.png" | relURL }}" alt="Energy Transition project">
      </div>
      <figcaption>Renewable Energy Transition</figcaption>
    </figure>
  </a>

</div>

{{< /rawhtml >}}
