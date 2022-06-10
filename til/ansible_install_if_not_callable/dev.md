---
canonical_url: https://waylonwalker.com/til/ansible_install_if_not_callable/
cover_image: https://images.waylonwalker.com/til/ansible_install_if_not_callable.png
description: Part of my neovim setup requires having the  re-installing a bunch of
  things that are already installed can be quite check if the command is installed
  with  reg
published: true
tags:
- python
- ansible
title: Installing packages with ansible only if they do not exist
---

Part of my neovim setup requires having the `black` python formatter installed and callable.  I install it with `pipx` so that I don't have to manage a virtual environment and have it available everywhere.  So far this works well for me, if there are ever breaking changes I may need to rethink this.

re-installing a bunch of things that are already installed can be quite a waste and really add up to my ansible run time, so for most of my ansible tasks that install a command like this I have been following this pattern.

1. check if the command is installed with `command -v <command>`
2. register that step
3. ignore if that step fails
4. add a `when: <xxx>_exists is failed` condition to the step that
   installs that command.

``` yaml
- name: check is black installed
  shell: command -v black
  register: black_exists
  ignore_errors: yes

- name: install black
  when: black_exists is failed
  shell: pipx install black
```

https://www.youtube.com/watch?v=MCFg6-W5SBI

> I made a video based on this post, check it out if its your thing
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
    
    <a class='prev' href='/til/aws-eventbridge-visidata'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>View AWS event bridge rules with visidata</p>
        </div>
    </a>
    
    <a class='next' href='/til/ansible_install_fonts'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Installing system nerd-fonts with ansible</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>