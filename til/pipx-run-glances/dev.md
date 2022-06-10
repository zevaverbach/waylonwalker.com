---
canonical_url: https://waylonwalker.com/til/pipx-run-glances/
cover_image: https://images.waylonwalker.com/til/pipx-run-glances.png
description: Glances is a fully featured system monitoring tool written in python.  Out
  of Once you run this you will be in a tui application similar to htop.  You can
published: true
tags:
- python
title: Run glances without install with pipx
---

Glances is a fully featured system monitoring tool written in python.  Out of the box it's quite similar to htop, but has quite a few more features, and can be ran without installing anything other than `pipx`, which you should already have installed if you do anything with python.


``` bash
pipx run glances
```

Once you run this you will be in a tui application similar to htop.  You can kill processes with k, use left and right arrows to change the sorting column, and up and down to select different processes.

![running pipx run glances on my ubuntu 21.10 machine inside the kitty terminal](https://images.waylonwalker.com/pipx-run-glances.png)

## Links

* [pipx](https://pypa.github.io/pipx/)
* [website](https://nicolargo.github.io/glances/)
* [docs](https://glances.readthedocs.io/en/latest/index.html)
* [github](https://github.com/nicolargo/glances)
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
    
    <a class='prev' href='/til/pipx-w'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Glances webui with pipx</p>
        </div>
    </a>
    
    <a class='next' href='/til/pipx-on-windows'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>pipx on windows</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>