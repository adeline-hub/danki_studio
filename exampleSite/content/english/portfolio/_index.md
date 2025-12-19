---
title: "Portfolio"
body_class: "page-portfolio"
---

<section class="container mx-auto py-12" aria-label="Selected projects">
  <div class="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">

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
      <a href="{{ .url | relURL }}" class="group block overflow-hidden rounded-lg shadow-lg bg-white dark:bg-gray-800 transition-transform transform hover:scale-105">
        <div class="aspect-w-4 aspect-h-3">
          <img src="{{ .img | relURL }}" alt="{{ .alt }}" loading="lazy" class="object-cover w-full h-full transition-transform duration-300 group-hover:scale-110">
        </div>
        <figcaption class="mt-3 text-center text-lg font-semibold text-gray-900 dark:text-gray-100 px-2">
          {{ .title }}
        </figcaption>
      </a>
    {{ end }}

  </div>
</section>

