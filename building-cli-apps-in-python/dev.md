---
canonical_url: https://waylonwalker.com/building-cli-apps-in-python/
cover_image: https://images.waylonwalker.com/building-cli-apps-in-python.png
description: learning about building cli apps in python
published: true
tags:
- python
title: Building Cli apps in Python
---

## Packages

## [Click](https://click.palletsprojects.com/en/7.x/ "Click")

### Inputs

Click primarily takes two forms of inputs Options and arguments.  I think of options as keyword argument and arguments as regular positional arguments.

#### Option

* typically aliased with a shorthand ('-v', '--verbose')

---

**From the [Docs](https://click.palletsprojects.com/en/7.x/options/)

To get the Python argument name, the chosen name is converted to lower case, up to two dashes are removed as the prefix, and other dashes are converted to underscores.

``` python
@click.command()
@click.option('-s', '--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
```

``` python
@click.command()
@click.option('-s', '--string-to-echo', 'string')
def echo(string):
    click.echo(string)
```

---

#### Argument

* positional
* required
* no help text supplied by click

## [Yaspin](https://pypi.org/project/yaspin/ "Yaspin")

![Yaspin Gif](https://images.waylonwalker.com/yaspin-demo.gif)

## [Click Help Colors](https://github.com/click-contrib/click-help-colors)

## ![Click Help Colors Example](https://raw.githubusercontent.com/r-m-n/click-help-colors/master/examples/1.png)

## [Colorama](https://github.com/tartley/colorama "colorama")

[Colorama Example](https://github.com/tartley/colorama/raw/master/screenshots/ubuntu-demo.png)

### [Click DidYouMean](https://github.com/click-contrib/click-didyoumean)
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
    
    <a class='prev' href='/building-kedro-dev'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Building kedro.dev</p>
        </div>
    </a>
    
    <a class='next' href='/break-pane'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>tmux break-pane</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>