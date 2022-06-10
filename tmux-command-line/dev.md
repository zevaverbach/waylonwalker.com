---
canonical_url: https://waylonwalker.com/tmux-command-line/
cover_image: https://images.waylonwalker.com/tmux-command-line.png
description: https://youtu.be/SNu-4IrkjAs So far we have covered a lot of tmux commands
  and how they map to keybindings Let Or we can open the tmux command line and run
  it f
published: true
tags:
- cli
- linux
- tmux
title: tmux command line
---

https://youtu.be/SNu-4IrkjAs

So far we have covered a lot of tmux commands and how they map to keybindings but these same commands can be executed at the command line.

## From the command line

Let's make a popup that displays our git status for 5s or until we close it manually.  We can run the following command at the command line, in a split.

``` bash
tmux display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```

## From the tmux command line

Or we can open the tmux command line and run it from tmux's built in command line, which is very similar to bim EX mode. By default the tmux command line can be opened with `prefix+[`.

``` bash
display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```
> 🗒️ note that the tmux command is called by default when inside of tmux.

## Make it a keybinding

Finally we can make it a keybinding by adding a bind command ahead of our tmux command, then we can execute this in the tmux command line or add it to our
`~/.tmux.conf`.

``` bash
bind s display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```


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
    
    <a class='prev' href='/tmux-copy-mode'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>tmux copy-mode</p>
        </div>
    </a>
    
    <a class='next' href='/tmux-choose-tree'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>tmux choose-tree</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>