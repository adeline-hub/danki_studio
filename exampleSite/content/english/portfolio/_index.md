---
title: "Portfolio"
body_class: "page-portfolio"
---


<style>
  /* On force la grille à ignorer les limites du thème */
  .portfolio-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 20px !important;
    width: 100%;
    margin: 0 auto;
  }

  .project-card { text-decoration: none !important; color: black !important; }
  .img-box { overflow: hidden; border-radius: 5px; aspect-ratio: 4/3; }
  .img-box img { width: 100%; height: 100%; object-fit: cover; transition: 0.4s; }
  .project-card:hover img { transform: scale(1.1); }
  
  @media (max-width: 768px) {
    .portfolio-grid { grid-template-columns: 1fr !important; }
  }
</style>

<section class="portfolio-grid" aria-label="Selected projects">

  <a href="{{ "portfolio/janus/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Janus — Mediterranean investment analytics project"
          loading="lazy">
      </div>
      <figcaption>Janus — Mediterranean Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/cernunnos/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Cernunnos — PropTech investment analytics project"
          loading="lazy">
      </div>
      <figcaption>Cernunnos — PropTech Investment Analytics</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/citrus/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Citrus — botany, diversity and data project"
          loading="lazy">
      </div>
      <figcaption>Citrus — Botany, Diversity & Data</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/monastic-mapping/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Monastic Mapping — medieval data cartography project"
          loading="lazy">
      </div>
      <figcaption>Monastic Mapping — Middle Ages</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/urban-water/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Urban Water — minimal data visualization project"
          loading="lazy">
      </div>
      <figcaption>Urban Water — Minimal Data</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/climate-tracking/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Global climate variance tracking project"
          loading="lazy">
      </div>
      <figcaption>Global Climate Variance Study</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/supply-chain-viz/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Logistics and supply chain nodes visualization project"
          loading="lazy">
      </div>
      <figcaption>Logistics & Supply Chain Nodes</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/cultural-atlas/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Cultural atlas of migration project"
          loading="lazy">
      </div>
      <figcaption>The Cultural Atlas of Migration</figcaption>
    </figure>
  </a>

  <a href="{{ "portfolio/energy-transition/" | relURL }}" class="project-card">
    <figure>
      <div class="image-container">
        <img
          src="{{ "images/portfolio/base.png" | relURL }}"
          alt="Renewable energy transition analysis project"
          loading="lazy">
      </div>
      <figcaption>Renewable Energy Transition</figcaption>
    </figure>
  </a>

</section>
