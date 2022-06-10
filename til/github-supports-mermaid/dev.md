---
canonical_url: https://waylonwalker.com/til/github-supports-mermaid/
cover_image: https://images.waylonwalker.com/til/github-supports-mermaid.png
description: Mermaid diagrams provide a way to display graphs defined as plain text.
  You can define nodes like this in mermaid, and GitHub will now render
published: true
tags:
- python
- python
- python
title: GitHub Markdown now Supports Mermaid Diagrams
---

Mermaid diagrams provide a way to display graphs defined as plain text. Some markdown renderers support this as a plugin.  GitHub now supports it.

## example

You can define nodes like this in mermaid, and GitHub will now render them as a pretty graph diagram.  Its rendered in svg, so its searchable with `control f` and everything.

```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D-->OUT;
      E-->F-->G-->OUT
```

![Here is what the example looks like on GitHub](https://images.waylonwalker.com/example-gh-mermaid.png)

## Links

* [GitHub support announcement](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
* [mermaid docs](https://mermaid-js.github.io/mermaid/#/)
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
    
    <a class='prev' href='/til/gitignore-python'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Python Respect the .gitignore</p>
        </div>
    </a>
    
    <a class='next' href='/til/git-revive-dead-files'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Revive files from the dead with git</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>