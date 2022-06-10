---
canonical_url: https://waylonwalker.com/til/pip-require-virtualenv/
cover_image: https://images.waylonwalker.com/til/pip-require-virtualenv.png
description: Whenever you are installing python packages, you should always use a
  virtual Pip is the pacakage tool for python.  It installs third-party packages and
  is pytho
published: true
tags:
- python
title: pip require-virtualenv
---

Whenever you are installing python packages, you should always use a virtual environment.  pip makes this easy to follow by adding some configuration to pip.

## require-virtualenv

Pip is the pacakage tool for python.  It installs third-party packages and is configurable.  One of the configuration settings that I highly reccommend everyone to add is `require-virtualenv`.  This will stop pip from installing any packages if you have not activated a virtualenv.

## why

python packages often require many different dependencies, sometimes packages are up to date and sometimes they require different versions of dependencies. If you install everything in one environment its easy to end up with version conflict issues that are really hard to resolve, especially since your system environment cannot easily be restarted.

## PIPX my one exception

My one exception that I put in my system level packages is `pipx`.  `pipx` is very handy as it manages virtual environments for you and is intended for command line utilities that would end up in your system env or require you to manually manage virtual environments without it.

## pip config

Your pip config might be found in either `~/.pip/pip.conf` or
`~/.config/pip/pip.conf`.  You can either use the `pip config set` command or
edit one of these files manually.

```bash
pip config set global.require-virtualenv True
```

Now you sould see this in your `~/.config/pip/pip.conf`

``` toml
[global] require-virtualenv = True
```

## pip config debug

If you want to know where pip is looking for configuration on your system, and what files are setting a certain config you can use `pip config debug` to find it.

``` bash
❯ pip config debug

env_var: env: global:
  /etc/xdg/xdg-awesome/pip/pip.conf, exists: False
  /etc/xdg/pip/pip.conf, exists: False
  /etc/pip.conf, exists: False
site:
  /home/waylon/git/waylonwalker.com/.venv/pip.conf, exists: False
user:
  /home/waylon/.pip/pip.conf, exists: False
  /home/waylon/.config/pip/pip.conf, exists: True
    global.require-virtualenv: True
```

## saved my bacon

This setting recently saved me when I modified my `.envrc` file my virtual environment deactivated, so when I went to pip install something it gave me an error that it was not active.  Situations like this are an easy way to pollute your system with packages that it does not need installed.

![pip-require-virtualenv-direnv-error](https://screenshots.waylonwalker.com/pip-require-virtualenv-direnv-error.webp)

## TLDR

Run this at your command line to avoid polluting your system environment by mistake before running any pip command.

```bash
pip config set global.require-virtualenv True
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
    
    <a class='prev' href='/til/pipx-on-windows'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>pipx on windows</p>
        </div>
    </a>
    
    <a class='next' href='/til/pathlib-read-text'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>How I read Files in Python</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>