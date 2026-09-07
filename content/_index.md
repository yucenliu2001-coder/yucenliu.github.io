---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-01-05
type: landing

sections:
  # Developer Hero - Gradient background with name, role, social, and CTAs
  - block: dev-hero
    id: hero
    content:
      username: me
      greeting: "Hi, I'm"
      show_status: true
      show_scroll_indicator: true
      typewriter:
        enable: true
        prefix: "I like"
        strings:
          - "Computer graphics"
          - "Learning languages"
          - "Traveling"
          - "Photography"
          - "Sports"
        type_speed: 70
        delete_speed: 40
        pause_time: 2500
      cta_buttons:
        - text: View My Work
          url: "#projects"
          icon: arrow-down
        - text: Get In Touch
          url: "#contact"
          icon: envelope
    design:
      style: centered
      avatar_shape: circle
      animations: true
      background:
        color:
          light: "#fafafa"
          dark: "#0a0a0f"
      spacing:
        padding: ["6rem", "0", "4rem", "0"]
  
  # Featured Project
  - block: project-card
    id: projects
    content:
      title: "Featured Projects"
      subtitle: "Some of my past work"
    design:
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4m", "0", "4m", "0"]
  
  # Visual Tech Stack - Icons organized by category
  - block: tech-stack
    id: skills
    content:
      title: "Skills"
      subtitle: "Something I can do"
      categories:
        - name: Programming
          items:
            - name: C
              icon: devicon/c
            - name: C++
              icon: devicon/cplusplus
            - name: Python
              icon: devicon/python
            - name: Java
              icon: devicon/java
        - name: Languages
          items:
            - name: Chinese
              greeting: "你好"
            - name: English
              greeting: "Hello"
            - name: Spanish
              greeting: "Hola"
            - name: German
              greeting: "Hallo"

    design:
      style: grid
      show_levels: false
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  
  # Experience Timeline
  - block: resume-experience
    id: education
    content:
      title: Education
      date_format: Jan 2006
      items:
        - title: Senior Software Engineer
          company: Tech Corp
          company_url: ''
          company_logo: ''
          location: San Francisco, CA
          date_start: '2023-01-01'
          date_end: ''
          description: |2-
            * Lead development of microservices architecture serving 1M+ users
            * Improved API response time by 40% through optimization
            * Mentored team of 5 junior developers
            * Tech stack: React, Node.js, PostgreSQL, AWS
        - title: Full-Stack Developer
          company: Startup Inc
          company_url: ''
          company_logo: ''
          location: Remote
          date_start: '2021-06-01'
          date_end: '2022-12-31'
          description: |2-
            * Built and deployed 3 production applications from scratch
            * Implemented CI/CD pipeline reducing deployment time by 60%
            * Collaborated with design team on UI/UX improvements
            * Tech stack: Next.js, Express, MongoDB, Docker
        - title: Junior Developer
          company: Web Agency
          company_url: ''
          company_logo: ''
          location: New York, NY
          date_start: '2020-01-01'
          date_end: '2021-05-31'
          description: |2-
            * Developed client websites using modern web technologies
            * Maintained and updated legacy codebases
            * Participated in code reviews and agile ceremonies
            * Tech stack: React, WordPress, PHP, MySQL
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  
  # Photography
  - block: photo-gallery
    id: photo-gallery
    design:
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["2rem", "0", "2rem", "0"]
  
  # Contact Section
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Let's build something amazing together"
      text: |-
        I'm always interested in hearing about new projects and opportunities.
        Whether you're looking to collaborate, hagn out, or just want to play Geoguessr together, feel free to reach out!
      email: yucenliu2001@gmail.com
      autolink: true
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
---
