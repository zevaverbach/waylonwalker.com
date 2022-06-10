---
cover: ''
date: 2022-02-08
datetime: 2022-02-08 00:00:00+00:00
description: A super useful tool when doing PR It
edit_link: https://github.com/edit/main/pages/til/ag-ahead.md
jinja: false
long_description: A super useful tool when doing PR It
now: 2022-06-10 02:38:55.575301
path: pages/til/ag-ahead.md
slug: til/ag-ahead
status: published
super_description: A super useful tool when doing PR It
tags:
- cli
- bash
- linux
templateKey: til
title: ag silver searcher look ahead and look behind
today: 2022-06-10
year: 2022
---

A super useful tool when doing PR's or checking your own work during a big
refactor is the silver searcher.  Its a super fast command line based searching
tool. You just run `ag "<search term>"` to search for your search term.  This
will list out every line of every file in any directory under your current
working directory that contains a match.

## Ahead/Behind

It's often useful to need some extra context around the change.  I recently
reviewed a bunch of PR's that moved schema from `save_args` to the root of the
dataset in all yaml configs.  To ensure they all made it to the top level
DataSet configuraion, and not underneath save_args.  I can do a search for all
the schemas, and ensure that none of them are under `save_args` anymore.

``` bash
ag "schema: " -A 12 -B 12
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
    
    <a class='prev' href='/til/ansible_install_fonts'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Installing system nerd-fonts with ansible</p>
        </div>
    </a>
    
    <a class='next' href='/til/2-minutes-to-stow'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>2 minutes to stow</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>