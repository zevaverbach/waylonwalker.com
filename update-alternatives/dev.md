---
canonical_url: https://waylonwalker.com/update-alternatives/
cover_image: https://images.waylonwalker.com/update-alternatives.png
description: prev cmd.exe tips next https://waylonwalker.com/how-i-deploy-2022
published: true
tags:
- linux
- bash
title: Update Alternatives in Linux
---

``` bash
update-alternatives --query python
```

``` bash
update-alternatives: error: no alternatives for python
```

``` bash
sudo update-alternatives --install /usr/local/bin/python python `which python3.8` 2
# update-alternatives: using /usr/bin/python3.8 to provide /usr/local/bin/python (python) in auto mode

sudo update-alternatives --install /usr/local/bin/python python `which python2.7` 5
# update-alternatives: using /usr/bin/python2.7 to provide /usr/local/bin/python (python) in auto mode

update-alternatives --query python
# Name: python
# Link: /usr/local/bin/python
# Status: auto
# Best: /usr/bin/python2.7
# Value: /usr/bin/python2.7
# 
# Alternative: /usr/bin/python2.7
# Priority: 5
# 
# Alternative: /usr/bin/python3.8
# Priority: 2

sudo update-alternatives --install /usr/local/bin/python python `which python3.8` 20
# update-alternatives: using /usr/bin/python3.8 to provide /usr/local/bin/python (python) in auto mode
```
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
    
    <a class='prev' href='/cmd-exe-tips'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>cmd.exe tips</p>
        </div>
    </a>
    
    <a class='next' href='/how-i-deploy-2021'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>https://waylonwalker.com/how-i-deploy-2022</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>