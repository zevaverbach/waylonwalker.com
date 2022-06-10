---
cover: ''
date: 2022-01-16
datetime: 2022-01-16 00:00:00+00:00
description: I don I first tried the nvim lsp rename, and it failed, Then I pip installed
  Once you have rope installed you can call rename on the variable.
edit_link: https://github.com/edit/main/pages/til/nvim-rename-python.md
jinja: false
long_description: I don I first tried the nvim lsp rename, and it failed, Then I pip
  installed Once you have rope installed you can call rename on the variable.
now: 2022-06-10 02:38:55.574868
path: pages/til/nvim-rename-python.md
slug: til/nvim-rename-python
status: published
super_description: I don I first tried the nvim lsp rename, and it failed, Then I
  pip installed Once you have rope installed you can call rename on the variable.
tags:
- python
- vim
- vim
templateKey: til
title: Rename Python Variables with nvim
today: 2022-06-10
year: 2022
---

I don't use refactoring tools as much as I probably should.  mostly
because I work with small functions with unique names, but I recently
had a case where a variable name `m` was everywhere and I wanted it
named better.  This was not possible with find and replace, because
there were other `m`'s in this region.


I first tried the nvim lsp rename, and it failed, Then I pip installed
rope, a refactoring tool for python, and it just worked!

```bash
pip install rope
```

Once you have rope installed you can call rename on the variable.

```vim
:lua vim.lsp.buf.rename()
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
    
    <a class='prev' href='/til/nvim-telescope-custom-command'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Opening files in vim from output of command</p>
        </div>
    </a>
    
    <a class='next' href='/til/nixery-versions-by-commit-count'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Nix Versions By Commit Count</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>