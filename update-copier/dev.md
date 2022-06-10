---
canonical_url: https://waylonwalker.com/update-copier/
cover_image: https://images.waylonwalker.com/update-copier.png
description: Copier is a fantastic templating library written in python, but older
  versions I Use copier several times per day and get fantastic benefit from this
  project, h
published: true
tags:
- python
- python
- python
title: Copier < 6.0.0b0 considered dangerous
---

Copier is a fantastic templating library written in python, but older versions have a dangerous bug if you are using it inside of existing directories.

## This is a PSA

I Use copier several times per day and get fantastic benefit from this project, this post is not intended to crap all over copier in any way, but is rather a PSA for other users who do use copier like I do so that they know the dangers of using copier inside an existing directory.

## The issue

## The fix

https://github.com/copier-org/copier/pull/273

As of the time of writing this version is still in beta, if you still want to use copier with existing directtories, I'd strongly encourage you to install the `--pre` release.

``` python
pipx install copier --pip-args='--pre'
```

## confirm

``` bash
copier --version
# copier 6.0.0b0
```


## My update commit

https://github.com/WaylonWalker/devtainer/commit/a06e47462e2c6d26ad69fbdc2e7990a1a73ab4b7
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
    
    <a class='prev' href='/kedro-environment'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>kedro Virtual Environment</p>
        </div>
    </a>
    
    <a class='next' href='/docker-deep-dive'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>📝 Docker Deep Dive - Notes</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>