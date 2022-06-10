---
cover: ''
date: 2100-03-20
datetime: 2100-03-20 00:00:00+00:00
description: prev Unzip minecraft mods to their directory from the command line next
  Upcoming Stream
edit_link: https://github.com/edit/main/pages/til/python-web-conf-snippet.md
jinja: false
long_description: ''
now: 2022-06-10 02:38:55.574825
path: pages/til/python-web-conf-snippet.md
slug: til/python-web-conf-snippet
status: draft
super_description: ''
tags:
- python
templateKey: til
title: python web conf snippet
today: 2022-06-10
year: 2100
---

## From my terminal

``` bash
pipx run \
 --spec git+https://github.com/waylonwalker/lookatme \
 lookatme {filepath} \
 --live-reload \
 --style gruvbox-dark
```

## From Neovim

``` vim
nnoremap <leader><leader>s <cmd>lua require'telegraph'.telegraph({cmd='pipx run --spec git+https://github.com/waylonwalker/lookatme lookatme {filepath} --live-reload --style gruvbox-dark', how='tmux'})<CR>
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
    
    <a class='prev' href='/til/linux-unzip-directory'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Unzip minecraft mods to their directory from the command line</p>
        </div>
    </a>
    
    <a class='next' href='/upcoming-streams'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Upcoming Stream</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>