---
canonical_url: https://waylonwalker.com/til/git-recover-checkout/
cover_image: https://images.waylonwalker.com/til/git-recover-checkout.png
description: Once you give a branch the big D ( Checkout is your savior, all you need
  is the commit hash. We have all done this, you give  branch the big D only to realize
  i
published: true
tags:
- git
- linux
- cli
title: Recover a lost git branch with checkout
---

Once you give a branch the big D (`git branch -D mybranch`) its gone, its lost from your history.  It's completely removed from your log. There will be no reference to these commits, or will there?

## TLDR

Checkout is your savior, all you need is the commit hash.

## Immediate Regret
_your terminal is still open_

We have all done this, you give  branch the big D only to realize it was the wrong one.  Don't worry, not all is lost, this is the easiest to recover from.  When you run the delete command you will see something like this.


``` bash
❯ git branch -D new
Deleted branch new (was bc02a64).
```

Notice the hash is right there is the hash of your commit.  You can use that to get your content back.

``` bash
git checkout -b bc02a64 git branch new

# or in one swoop checkout your new branch at the `start-point` you want
git checkout -b new bc02a64
```

## Delayed reaction
_you have closed your terminal_

If you have closed your terminal, or have deleted with a gui or something that does not tell you the hash as you run it, don't fret, all your work is still there (as long as you have commited).  You just have to dig it out.  The reflog contains a list of all git operations that have occurred on your git repo, and can be incredibly helpful with this.

### Kinda Recent

If your botched delete operation was recent just diving right into the reflog will show it.

``` bash
❯ git reflog
03a3338 (main) HEAD@{0}: checkout: moving from new to main
bc02a64 (HEAD -> another, new) HEAD@{4}: commit: newfile
03a3338 (main) HEAD@{2}: checkout: moving from main to new
```

> In this example, I checked out a branch called new, commited a new
> file, then switched back to main and deleted new.

Now That I have the commit hash I can use the same solution to get my branch back.

``` bash
git checkout -b bc02a64 git branch new

# or in one swoop checkout your new branch at the `start-point` you want
git checkout -b new bc02a64
```

### A lot has happened since then

If a lot has happened since then, you are going to need to pull out some more tool to sift through that `reflog`, especially if its a big one. The first suggestion that I have is to pipe into grep and look for commit messages, or the name of the branch.


``` bash
❯ git reflog | grep "moving from"
03a3338 HEAD@{1}: checkout: moving from main to branch/oops
03a3338 HEAD@{2}: checkout: moving from oops to main
03a3338 HEAD@{4}: checkout: moving from main to oops
03a3338 HEAD@{5}: checkout: moving from another to main
bc02a64 HEAD@{6}: checkout: moving from main to another
03a3338 HEAD@{7}: checkout: moving from another to main
bc02a64 HEAD@{8}: checkout: moving from new to another bc02a64 HEAD@{9}: checkout: moving from bc02a64bbe5683d905e333e8dfcbbb91a5e77549 to new bc02a64 HEAD@{10}: checkout: moving from main to bc02a64bbe56
03a3338 HEAD@{11}: checkout: moving from new to main
03a3338 HEAD@{13}: checkout: moving from main to new
03a3338 HEAD@{14}: checkout: moving from other to main
03a3338 HEAD@{18}: checkout: moving from main to other
```

git has a built in `--grep` flag, but I don't think there is a way to filter by branch name, regardless it still is helpful.

``` bash
❯ git reflog --grep new
bc02a64 (HEAD -> another, new) HEAD@{4}: commit: newfile
```

Maybe if you can remember a filename you can pass in `-- <filename>`.

``` bash
git reflog -- readme.md
```

## RTFM

There are many other ways to slice up a git log, and reflog alike. check out `man git log` for some more flags.
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
    
    <a class='prev' href='/til/git-reflog-is-an-alias'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Git reflog is an alias for git log -g</p>
        </div>
    </a>
    
    <a class='next' href='/til/git-rebase-root'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Git rebase to the beginning of time</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>