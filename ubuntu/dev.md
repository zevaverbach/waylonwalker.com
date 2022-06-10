---
canonical_url: https://waylonwalker.com/ubuntu/
cover_image: https://images.waylonwalker.com/ubuntu.png
description: I ran this, but have no idea if it had any effect as the theme did What
  I think actuagnome terminal showing scrollbar in tmuxlly worked was One thing that
  I rea
published: true
tags:
- linux
title: Ubuntu
---

## gnome-tweaks

``` bash
sudo apt install gnome-tweaks

```

## nordix gtk theme

I ran this, but have no idea if it had any effect as the theme did not show up until I relogged.

```
gsettings set org.gnome.desktop.wm.preferences theme Nordic
```

What I think actuagnome terminal showing scrollbar in tmuxlly worked was 


## emoji support

One thing that I really missed quite early from windows was the emoji virtual keyboard.  I like being able to quickly toss in those emoji that give just a bit of a visual cue 🔥, ⚠️,, 🎉, 🦄, 💜. 


### installation

I found an application called emote. that seems to do everything I need it to in the snap store.  Installation is a typicall snap install.

```
sudo snap install emote
```


### default keybinding


The application came with a default keybinding `ctrl+alt+e`, but I could never remember it.

```
ctrl+alt+e
```

### Windows keybinding

Old habits are hard to break, I opened up the gnome settings and set a hotkey to `super+;` to run the command emote.

```
Super+;
```

### How it works



## Get that dock outta here

I tried to disable the dock and it didn't immediately work for me, likely because I needed to relog.  I really have no use for the dock though as I will always open applications with a hotkey or super + search.

``` bash
sudo apt remove gnome-shell-extension-ubuntu-dock
```

## Terminal One Dark Theme

I don't stress too hard on themes, I just want something halfway consistent and just works.  I typically have just used a semi-popular theme "one-dark" everywhere.  This was the default theme in GitHub's Atom text editor that I never used.  I only care that it looks good and is popular enought that it just exists everywhere.

``` bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/denysdovhan/gnome-terminal-one/master/one-dark.sh)"
```

## Terminal menu and scrollbar

I found these to be ugly ans unnecessary so I turned them off.  You can access all the menu items by right clicking on the terminal anyways, so there is no reason to let it take up any screen real estate.

### Hiding the scrollbar

![hide the scrollbar](https://images.waylonwalker.com/gnome-terminal-hide-scrollbar)

### Hiding the menubar

![hide the menubar](https://images.waylonwalker.com/gnome-terminal-hide-menubar)

## vim clipboard

``` bash
sudo apt install xsel
```

``` vim
set clipboard+=unnamedplus
```

## tmux clipboard

``` bash
# Copy and Paste on Linux
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard" set-option -s set-clipboard off bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -selection clipboard -i"
```

## Hotkeys

| Key | Desc | 
| --- | ---- |
| super+j | move to workspace below |
| super+k | move to workspace above |
| super+shift+j | move window one workspace down |
| super+shift+k | move window one workspace up |


| Key | Command | Desc | 
| --- | ------- | ---- |
| Super+e | nautilus | File Browser|
| Super+Shift+p | Area Screenshot | gnome-screenshot -a |
| Super+Alt+p | Area Screenshot to clipboard | gnome-screenshot -ac |
| Super+e | nautilus | File Browser|

### screenshots

I am constantly taking screenshots for my daily workflow, on Windows I had it setup to both send to the clipboard and store in a screenshots directory.

``` bash
# take a screenshot and Store it as a file.
gnome-screenshot -a

# take a screenshot and send it to the clipboard
gnome-screenshot -ac
```

### obs

As od Jun 2021 the version of obs-studio installed using the instructions in their wiki is out of date.  I had success getting the latest version, which supports virtual webcams, using snap.

``` bash
sudo snap install obs-studio
```

### virtual webcam

After getting the latest version of obs-studio whixh supports virtual webcam it still did not start.  After some searching I found that updating v4l2loopback resolved the issue.

``` bash
sudo apt purge v4l2loopback-dkms git clone https://github.com/umlaeute/v4l2loopback.git ~/git/v4l2loopback/ cd ~/git/v4l2loopback/ make sudo make install

sudo modprobe v4l2loopback devices=1 exclusive_caps=1
```


``` bash
sudo depmod -a sudo modprobe v4l2loopback video_nr=10 card_label="OBS Video Source" exclusive_caps=1
```

## i3

I decided to give i3 a try, simply apt install it, then it shows up under the gear icon at the login screen after a reboot.  At this point I don't think I am ready for i3.  I have just changed a bunch of stuff in my workflow and honestly I got a decent gnome config setup in like 10 minutes.

``` bash
sudo apt install i3
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
    
    <a class='prev' href='/locked_diskcache'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Python Diskcahe is locked</p>
        </div>
    </a>
    
    <a class='next' href='/kedro-git-init'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Kedro Git Init</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>