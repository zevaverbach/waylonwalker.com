---
canonical_url: https://waylonwalker.com/if-tmux/
cover_image: https://images.waylonwalker.com/if-tmux.png
description: 'I do much of my work from tmux, I love it so much that I want to setup
  some Bash function to check if the shell is in a tmux session. I often open up vim
  to do '
published: true
tags:
- bash
- tmux
title: If Tmux
---

I do much of my work from tmux, I love it so much that I want to setup some functionality that puts me in tmux even if I didn't ask for it.


## Bash Function

Bash function to check if the shell is in a tmux session.

``` bash
in_tmux () {
  if [ -n "$TMUX" ]; then
    return 0
  else
    return 1
  fi
  }
```

## Using the bash function

I often open up vim to do some quite edits, but before I know it I have several splits open and I need access to another shell utility, but I forgot to start in tmux.  This function makes sure tht I start in tmux everytime.

Using `if_tmux` to ensure vim is opened in tmux.

``` bash
vim () { 
  in_tmux \
    && nvim \
    || bash -c "\
    tmux new-session -d;\
    tmux send-keys nvim Space +GFiles C-m;\
    tmux -2 attach-session -d;
    "
  }
```


I am not quite sure if this is proper use of the `&&` and `||`, let me know if you have a better way to do one thing if `in_tmux` returns true and another if it returns faslse.
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
    
    <a class='prev' href='/if_name_main'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>What is if __name__ == "__main___", and how do I use it.</p>
        </div>
    </a>
    
    <a class='next' href='/how-python-tools-config'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>How python tools configure</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>