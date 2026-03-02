---
# Leave the homepage title empty to use the site title
title:
date: 2026-02-26
type: landing

sections:
  - block: hero
    content:
      title: |
        Language Technologies (LT) 
        Lab
      image:
        filename: ltlab.png
      text: |
        <br>
        
        We are a research group of the Department of Computer Science and Engineering of the University of Bologna.
        
        Our **focus** is natural language processing research and application. We contribute to several national and international research projects and offer a variety of NLP learning activities at the international masters degree in Artificial Intelligence and elsewhere.
        
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
      button:
        text: test
        url: /people
      primary_action:
        text: Get Started
        url: /about/
      secondary_action:
        text: Learn More
        url: /docs/
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        folders:
          - news
      offset: 0
      order: desc
      page_type: news
    design:
      view: card
      columns: '1'
  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 2
      filters:
        folders:
          - publication_preprints
    design:
      view: citation
      columns: '1'
---
