---
canonical_url: https://waylonwalker.com/tmux-copy-mode/
cover_image: https://images.waylonwalker.com/tmux-copy-mode.png
description: 'https://youtu.be/-ypY tmux copy-mode is a tmux mode that lets you scroll,
  search, copy, and jump your Default keybinding to get into copy mode is  If you
  are a '
published: true
tags:
- cli
- linux
- tmux
title: tmux copy-mode
---

https://youtu.be/-ypY_-VmBKk

tmux copy-mode is a tmux mode that lets you scroll, search, copy, and jump your way through a pane.  There are a ton of keybindings for copy-mode, the main ones you will need to know are `/` for searching down `?` for searching up, `n` for next item, `space` for starting a selection, and enter to copy the selection.  Arrow keys will be used for navigation unless you have specified vi mode, then it will be `hjkl`.

Default keybinding to get into copy mode is `prefix+[`.

``` bash
bind-key          [ copy-mode
```

If you are a vim user you will likely want to use vi style keys, add this to your `~/.tmux.conf` file to enable vi mode.


``` bash
setw -g mode-keys vi
```

full list of copy-mode keybindings from the man page.

``` bash
  Command                                      vi              emacs
           append-selection
           append-selection-and-cancel                  A
           back-to-indentation                          ^               M-m
           begin-selection                              Space           C-Space
           bottom-line                                  L
           cancel                                       q               Escape
           clear-selection                              Escape          C-g
           copy-end-of-line [<prefix>]                  D               C-k
           copy-line [<prefix>]
           copy-pipe [<command>] [<prefix>]
           copy-pipe-no-clear [<command>] [<prefix>]
           copy-pipe-and-cancel [<command>] [<prefix>]
           copy-selection [<prefix>]
           copy-selection-no-clear [<prefix>]
           copy-selection-and-cancel [<prefix>]         Enter           M-w
           cursor-down                                  j               Down
           cursor-down-and-cancel
           cursor-left                                  h               Left
           cursor-right                                 l               Right
           cursor-up                                    k               Up
           end-of-line                                  $               C-e
           goto-line <line>                             :               g
           halfpage-down                                C-d             M-Down
           halfpage-down-and-cancel
           halfpage-up                                  C-u             M-Up
           history-bottom                               G               M->
           history-top                                  g               M-<
           jump-again                                   ;               ;
           jump-backward <to>                           F               F
           jump-forward <to>                            f               f
           jump-reverse                                 ,               ,
           jump-to-backward <to>                        T
           jump-to-forward <to>                         t
           jump-to-mark                                 M-x             M-x
           middle-line                                  M               M-r
           next-matching-bracket                        %               M-C-f
           next-paragraph                               }               M-}
           next-space                                   W
           next-space-end                               E
           next-word                                    w
           next-word-end                                e               M-f
           other-end                                    o
           page-down                                    C-f             PageDown
           page-down-and-cancel
           page-up                                      C-b             PageUp
           pipe [<command>] [<prefix>]
           pipe-no-clear [<command>] [<prefix>]
           pipe-and-cancel [<command>] [<prefix>]
           previous-matching-bracket                                    M-C-b
           previous-paragraph                           {               M-{
           previous-space                               B
           previous-word                                b               M-b
           rectangle-on
           rectangle-off
           rectangle-toggle                             v               R
           refresh-from-pane                            r               r
           scroll-down                                  C-e             C-Down
           scroll-down-and-cancel
           scroll-up                                    C-y             C-Up
           search-again                                 n               n
           search-backward <for>                        ?
           search-backward-incremental <for>                            C-r
           search-backward-text <for>
           search-forward <for>                         /
           search-forward-incremental <for>                             C-s
           search-forward-text <for>
           search-reverse                               N               N
           select-line                                  V
           select-word
           set-mark                                     X               X
           start-of-line                                0               C-a
           stop-selection
           top-line                                     H               M-R
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
    
    <a class='prev' href='/tmux-display-message'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>tmux display-message</p>
        </div>
    </a>
    
    <a class='next' href='/tmux-command-line'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>tmux command line</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>