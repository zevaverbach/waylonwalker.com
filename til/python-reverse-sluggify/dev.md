---
canonical_url: https://waylonwalker.com/til/python-reverse-sluggify/
cover_image: https://images.waylonwalker.com/til/python-reverse-sluggify.png
description: In order to make an auto title plugin for markata I needed to come up
  ! Here I have  a  To turn this into a markata plugin I put it into a pre
published: true
tags:
- python
title: Python Reverse Sluggify
---

In order to make an auto title plugin for markata I needed to come up with a way to reverse the slug of a post to create a title for one that does not explicitly have a title.

!!! Note "slugs"
   a slug is generally all lowercase and free of spaces, and is a way to
   make website routes (urls)


Here I have  a `path` available that gives me the articles path, ex.
`python-reverse-sluggify.md`.  An easy way to get rid of the file
extension, is to pass it into pathlib.Path and ask for the stem, which returns `python-reverse-sluggify`.  Then from There I chose to replace
`-` and `_` with a space.

``` python
article["title"] = (
    Path(article["path"]).stem.replace("-", " ").replace("_", " ").title()
)
```



To turn this into a markata plugin I put it into a pre_render hook.

``` python
from pathlib import Path

from markata.hookspec import hook_impl, register_attr


@hook_impl
@register_attr("articles")
def pre_render(markata) -> None:
    for article in markata.filter('title==""'):
        article["title"] = (
            Path(article["path"]).stem.replace("-", " ").replace("_", " ").title()
        )
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
    
    <a class='prev' href='/til/python-string-is-string'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Python string of letters is a string of letters, but not with special</p>
        </div>
    </a>
    
    <a class='next' href='/til/python-requests-get'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Get Webpage with python requests</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>