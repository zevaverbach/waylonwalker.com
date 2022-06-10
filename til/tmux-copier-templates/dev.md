---
canonical_url: https://waylonwalker.com/til/tmux-copier-templates/
cover_image: https://images.waylonwalker.com/til/tmux-copier-templates.png
description: I have added a hotkey to my copier template setup to quickly access all
  my I
published: true
tags:
- python
- linux
- tmux
title: Tmux hotkey for copier templates
---

I have added a hotkey to my copier template setup to quickly access all my templates at any time from tmux.  At any point I can hit `<c-b><c-b>`, thats holding control and hitting `bb`, and I will get a popup list of all of my templates directory names.  Its an fzf list, which means that I can fuzzy search through it for the template I want, or arrow key to the one I want if I am feeling insane.  I even setup it up so that the preview is a list of the files that come with the template in tree view.

``` bash
bind-key c-b popup -E -w 80% -d '#{pane_current_path}' "\
    pipx run copier copy ~/.copier-templates/`ls ~/.copier-templates |\
    fzf --header $(pwd) --preview='tree ~/.copier-templates/{} |\
    lolcat'` . \
    "
```

I've had this on my systems for a few weeks now and I am constantly using it for my [tils](https://waylonwalker.com/til/), [blogs](https://waylonwalker.com/archive), and my .envrc file that goes into all of my projects to make sure that I have a virtual environment installed and running any time I open it.

![this is what it looks like when I open my copier templates popup](https://images.waylonwalker.com/copier-templates-tmux-popup.png)
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
    
    <a class='prev' href='/til/tmux-copy-mode-binding'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>A better copy-mode bind for Tmux</p>
        </div>
    </a>
    
    <a class='next' href='/til/textual-popup-hack'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Textual Popup Hack</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>