---
canonical_url: https://waylonwalker.com/tmux-status-bar/
cover_image: https://images.waylonwalker.com/tmux-status-bar.png
description: 'https://youtu.be/mvgM8UH11 The tmux status bar can be a handy tool to
  remind yourself where you are within You can set a hotkey to show or hide the status
  bar. '
published: true
tags: []
title: tmux status-bar
---

https://youtu.be/mvgM8UH11_U

The tmux status bar can be a handy tool to remind yourself where you are within tmux.  It can also include a bunch of system information like battery status, cpu, mem, whatever you can get from the command  line.  Honestly I like to keep it minimal, and actually keep it turned off most of the time.  I find that it helps a little bit for others to follow along if I keep it on in certain circumstances.

##  show the status bar

You can set a hotkey to show or hide the status bar.

``` bash
bind s set-option -g status bind C-s set-option -g status
```

## setting the background transparent

I really want a minimal status bar with very little bling, I want it to get out of the way an not draw too much attention, so step one is to set the background to transparent.

``` bash
# default statusbar colors
#――――――――――――――――――――――――――――――――
set-option -g status-bg default set-option -g status-fg colour240
```

## setting default colors

I want my status bar to somewhat match the rest of my theme, so I set the default foreground as magenta and the default background as transparent.

``` bash
# default window title colors
#―――――――――――――――――――――――――――――――
set-window-option -g window-status-style fg=magenta set-window-option -g window-status-style bg=default
```

## my status bar

Honestly I set this up quite awhile ago, and it does everything I need it to for now.  It shows me the current session that I am in on the left and lists out the windows for the session in the middle.

``` bash
set -g status-left-length 85 set -g status-left "working on#[fg=colour135] #S" set -g window-status-current-format "#[fg=black,bold bg=default]│#[fg=white bg=cyan]#W#[fg=black,bold bg=default]│" set -g window-status-current-format "#[fg=black,bold bg=default]│#[fg=colour135 bg=black]#W#[fg=black,bold bg=default]│" set -g status-style bg=default set -g status-right "#[fg=magenta] #[bg=gray] %b %d %Y %l:%M %p" set -g status-right '#(gitmux "#{pane_current_path}")' set -g status-justify centre
```

For more format options search for FORMATS in the tmux manpage.



  <div class="onelinelink-wrapper">
      <a class="onelinelink" href="https://waylonwalker.com/tmux-nav-2021/">
          <img style="float: right;" align='right' src="https://images.waylonwalker.com/tmux-nav-2021-og_250x140.png" alt="article cover for 
 How I navigate tmux in 2021
"/>
          <p><strong>
 How I navigate tmux in 2021
</strong></p>
      </a>
  </div>


> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube [tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr) to see all of the videos in this series.
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
    
    <a class='prev' href='/tmux-ta'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>tmux ta</p>
        </div>
    </a>
    
    <a class='next' href='/tmux-start-application'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>tmux start application</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>