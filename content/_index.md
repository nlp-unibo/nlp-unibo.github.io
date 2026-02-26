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
      link:
          icon: graduation-cap
          icon_pack: fas
          text: Join Us
          url: ../contact/  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
