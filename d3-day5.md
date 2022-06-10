---
cover: ''
date: 2018-05-08
datetime: 2018-05-08 00:00:00+00:00
description: For what we are creating in these posts d3 is way overkill and very verbose,
  but I need to start somewhere
edit_link: https://github.com/edit/main/pages/blog/d3-day5.md
jinja: false
long_description: For what we are creating in these posts d3 is way overkill and very
  verbose, but I need to start somewhere
now: 2022-06-10 02:38:55.573197
path: pages/blog/d3-day5.md
slug: d3-day-5
status: published
super_description: For what we are creating in these posts d3 is way overkill and
  very verbose, but I need to start somewhere
tags:
- webdev
templateKey: blog-post
title: D3 Day 5
today: 2022-06-10
year: 2018
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/4.13.0/d3.min.js'></script>
<style>
    #content{
        max-width: 800px;
        margin: 0 auto;
    }
    .chart {
        display: block;
        padding: 10px;
        background: peachpuff;
    }

    .bar {
        height: 30px;
        margin: 5px;
        background: teal;
    }
    .bar:hover{
        background: #444;
        }
    button {
        background: rgb(240, 196, 211);
        border: none;
        font-size: 1.3rem;
        border-radius: 5px;
        padding: .2rem 1rem;
        margin-bottom: 1rem
    }
    .on {
        background: palevioletred;
    }
    .big {
    width: 100%
    }
    .small {
    width: 50%
    }
</style>


## Learn D3 in 5 days

For what we are creating in these posts d3 is way overkill and very verbose, but I need to start somewhere!  These are just stepping stones into real custom visualizations that cannot be done in any other tool today.  I still cannot explain how excited I am to say **"I created that in d3!!!"**
### Todays Result

## Recall Example 3 from yesterday

<div id='buttons'>
    <h3>Subject</h3>
    <div id='subjects'>
        <button class='math' onclick="render4('math')">Math</button>
        <button class='science' onclick="render4('science')">Science</button>
    </div>
    <h3>Chart Size</h3>
    <div id='sizes'>
        <button class='chart4-big-btn' onclick='chart4_size("big")')>Large</button>
        <button class='chart4-small-btn' onclick='chart4_size("small")'>Small</button>
    </div>
</div>

<div id="chart4" class='chart'></div>



<script>
    const data4 = [
        { name: 'Alice', math: 93, science: 84},
        { name: 'Bob', math: 73, science: 82 },
        { name: 'James', math: 92, science: 78},
        { name: 'Steve', math: 77, science: 93 },
        { name: 'Jordan', math: 80, science: 68 },
    ]

    chart4 = document.getElementById('chart4')


    let width = function() {
        return chart4.getBoundingClientRect().width
        }
    let height = function() {
        return chart4.getBoundingClientRect().height
        }
    let barHeight = function() {
        height() /  data4.length + 'px'
        }

    function chart4_size(size) {
        d3.select('#sizes')
            .selectAll('button')
            .classed('on', false)
        d3.select('#sizes')
            .select('.chart4-' + size + '-btn')
            .classed('on', true)
        d3.select('#chart4')
            .attr('class', 'chart ' + size)
        subject = document
            .getElementById('subjects')
            .querySelector('.on')
            .classList[0]
        render4(subject)
    }

    function render4(subject) {

        d3.select('#subjects')
            .selectAll('button')
            .classed('on', false);

        d3.select('#subjects')
            .select('.' + subject)
            .attr('class', subject + ' on');

        let xScale = d3.scaleLinear()
            .domain([50, 100])
            .range([0, width()]);

        const bars5 = d3.select('#chart4')
            .selectAll('div')
            .data(data4, function(d) {
                return d.name
            })
        const newBars = bars5.enter()
            .append('div')
                .attr('class', 'bar')
                .style('width', 0)

        newBars.merge(bars5)
            .transition()
            .style('width', function(d) {
                return xScale(d[subject]) + 'px'
            })
            .style('height', barHeight())
    }
    render4('math')
    chart4_size('big')
</script>


## Final Result

<div id='buttons5'>
    <h3>Subject</h3>
    <div id='subjects5'>
        <button class='math' onclick="render5('math')">Math</button>
        <button class='science' onclick="render5('science')">Science</button>
    </div>
    <h3>Chart Size</h3>
    <div id='sizes5'>
        <button class='chart5-big-btn' onclick='chart5_size("big")')>Large</button>
        <button class='chart5-small-btn' onclick='chart5_size("small")'>Small</button>
    </div>
</div>

<div id="chart5" class='chart'></div>



<script>
    const data5 = [
        { name: 'Alice', math: 93, science: 84},
        { name: 'Bob', math: 73, science: 82 },
        { name: 'James', math: 92, science: 78},
        { name: 'Steve', math: 77, science: 93 },
        { name: 'Jordan', math: 80, science: 68 },
    ]

    chart5 = document.getElementById('chart5')


    let width5 = function() {
        return chart5.getBoundingClientRect().width
        }
    let height5 = function() {
        return chart5.getBoundingClientRect().height
        }
    let barHeight5 = function() {
        height5() /  data5.length + 'px'
        }


    function chart5_size(size) {
        d3.select('#sizes5')
            .selectAll('button')
            .classed('on', false)
        d3.select('#sizes5')
            .select('.chart5-' + size + '-btn')
            .classed('on', true)
        d3.select('#chart5')
            .attr('class', 'chart ' + size)
        subject = document
            .getElementById('subjects5')
            .querySelector('.on')
            .classList[0]
        console.log(subject)
        render5(subject)
    }

    function render5(subject) {

        d3.select('#subjects5')
            .selectAll('button')
            .classed('on', false);

        d3.select('#subjects5')
            .select('.' + subject)
            .attr('class', subject + ' on');

        let xScale = d3
            .scaleLinear()
            .domain([50, 100])
            .range([0, width5()]);


        const bars5 = d3.select('#chart5')
            .selectAll('div')
            .data(data5, function(d) {
                return d.name
            })
        const newBars = bars5
            .enter()
            .append('div')
                .attr('class', 'bar')
                .style('width', 0)

        newBars.merge(bars5)
            .transition()
            .style('width', function(d) {
                return xScale(d[subject]) + 'px'
            })
            .style('height', barHeight5())

        d3
         .select('#chart5')
         .select('svg')
         .remove()

        const svg5 = d3
            .select('#chart5')
            .append('svg')
            .attr('width', width5())
            .attr('height', height5())
            .style('position', 'relative')
            .append('g')
            .call(d3.axisBottom(xScale))
    }
    render5('math')
    chart5_size('big')
</script>
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
    
    <a class='prev' href='/data-scientist-advice'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>What is YOUR Advice for New Data Scientists</p>
        </div>
    </a>
    
    <a class='next' href='/custom-scrollbar-design'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Custom Scrollbar Design</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>