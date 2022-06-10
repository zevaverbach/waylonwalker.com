---
cover: ''
date: 2019-02-10
datetime: 2019-02-10 00:00:00+00:00
description: How to setup a data science project in python.
edit_link: https://github.com/edit/main/pages/blog/bit-01/bit_01.md
jinja: false
long_description: 'Use  Add a minimal  consider using '
now: 2022-06-10 02:38:55.574592
path: pages/blog/bit-01/bit_01.md
slug: bit-01/bit_01
status: draft
super_description: 'Use  Add a minimal  consider using '
tags: []
templateKey: blog-post
title: Minimal Project Structure
today: 2022-06-10
year: 2019
---

## TLDR

Use **[.gitignore.io](https://www.gitignore.io)** and consider adding an alias to your terminal to quickly add a .gitignore to any project missing one.

``` bash
alias gitignore='curl https://www.gitignore.io/api/vim,emacs,python,pycharm,sublimetext,visualstudio,visualstudiocode,data > .gitignore'
```

Add a minimal **setup.py** to the root of your project, and use the following command to install it.

``` bash
pip install -e .
```

consider using **[cookiecutter](https://github.com/audreyr/cookiecutter)
<div class='prevnext'>

    <style type='text/css'>

    :root {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #ff66c4;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="light"] {
      --prevnext-color-text: #1f2022;
      --prevnext-color-angle: #ffeb00;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="dark"] {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #ff66c4;
      --prevnext-subtitle-brightness: 3;
    }
    .prevnext {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: flex-start;
    }
    .prevnext a {
      display: flex;
      align-items: center;
      width: 100%;
      text-decoration: none;
    }
    a.next {
      justify-content: flex-end;
    }
    .prevnext a:hover {
      background: #00000006;
    }
    .prevnext-subtitle {
      color: var(--prevnext-color-text);
      filter: brightness(var(--prevnext-subtitle-brightness));
      font-size: .8rem;
    }
    .prevnext-title {
      color: var(--prevnext-color-text);
      font-size: 1rem;
    }
    .prevnext-text {
      max-width: 30vw;
    }
    </style>
    
    <a class='prev' href='/newsletter/AUG2020'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Newsletter 3</p>
        </div>
    </a>
    
    <a class='next' href='/git-rewrite-history/git-rewrite-history'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Rewrite History with Git</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>