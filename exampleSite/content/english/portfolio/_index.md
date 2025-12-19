---
title: "Portfolio"
body_class: "page-portfolio"
---

<style>
  /* Grille portfolio */
  .portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    width: 100%;
    margin: 0 auto;
  }

  .project-card { 
    text-decoration: none; 
    color: black; 
    display: block;
  }

  .img-box { 
    overflow: hidden; 
    border-radius: 5px; 
    aspect-ratio: 4/3; 
  }

  .img-box img { 
    width: 100%; 
    height: 100%; 
    object-fit: cover; 
    transition: transform 0.4s; 
  }

  .project-card:hover img { 
    transform: scale(1.1); 
  }

  @media (max-width: 1024px) {
    .portfolio-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 640px) {
    .portfolio-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<section class="portfolio-grid" aria-label="Selected projects">

  {{ $projects := slice
    (dict "url" "portfolio/janus/" "img" "images/portfolio/base.png" "title" "Janus — Mediterranean Investment Analytics" "alt" "Janus — Mediterranean investment analytics project")
    (dict "url" "portfolio/cernunnos/" "img" "images/portfolio/base.png" "title" "Cernunnos — PropTech Investment Analytics" "alt" "Cernunnos — PropTech investment analytics project")
    (dict "url" "portfolio/citrus/" "img" "images/portfolio/base.png" "title" "Citrus — Botany, Diversity & Data" "alt" "Citrus — botany, diversity and data project")
    (dict "url" "portfolio/monastic-mapping/" "img" "images/portfolio/base.png" "title" "Monastic Mapping — Middle Ages" "alt" "Monastic Mapping — medieval data cartography project")
    (dict "url" "portfolio/urban-water/" "img" "images/portfolio/base.png" "title" "Urban Water — Minimal Data" "alt" "Urban Water — minimal data visualization project")
    (dict "url" "portfolio/climate-tracking/" "img" "images/portfolio/base.png" "title" "Global Climate Variance Study" "alt" "Global climate variance tracking project")
    (dict "url" "portfolio/supply-chain-viz/" "img" "images/portfolio/base.png" "title" "Logistics & Supply Chain Nodes" "alt" "Logistics and supply chain nodes visualization project")
    (dict "url" "portfolio/cultural-atlas/" "img" "images/portfolio/base.png" "title" "The Cultural Atlas of Migration" "alt" "Cultural atlas of migration project")
    (dict "url" "portfolio/energy-transition/" "img" "images/portfolio/base.png" "title" "Renewable Energy Transition" "alt" "Renewable energy transition analysis project")
  }}

  {{ range $projects }}
    <a href="{{ .url | relURL }}" class="project-card">
      <figure>
        <div class="img-box">
          <img src="{{ .img | relURL }}" alt="{{ .alt }}" loading="lazy">
        </div>
        <figcaption>{{ .title }}</figcaption>
      </figure>
    </a>
  {{ end }}

</section>

