<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of appindicator/createappindicator.py at revision 100</title>
<link href="/static/css/global.css" rel="stylesheet" />
<link href="/static/images/favicon.png" rel="shortcut icon" />

<script type="text/javascript">
var global_path = '/~akkzilla/python-snippets/maintrunk/';
var collapsed_icon_path = '/static/images/treeCollapsed.png';
var expanded_icon_path = '/static/images/treeExpanded.png';
</script>
<script src="/static/javascript/yui/build/yui/yui-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/oop/oop-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/event/event-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/attribute/attribute-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/base/base-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/dom/dom-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/node/node-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/anim/anim-min.js" type="text/javascript"></script>
<script src="/static/javascript/yui/build/io/io-base-min.js" type="text/javascript"></script>
<script src="/static/javascript/custom.js" type="text/javascript"></script>

<link href="/static/css/view.css" media="all" type="text/css" rel="stylesheet" />
<link href="/static/css/highlight.css" media="all" type="text/css" rel="stylesheet" />

</head>
<body class="public">



<div class="black-link">
<a href="https://code.launchpad.net/~akkzilla/python-snippets/maintrunk">
← Back to branch summary
</a>
</div>


<h1 class="branch-name">
~akkzilla/python-snippets/maintrunk
</h1>

<ul id="menuTabs">


<li><a href="/~akkzilla/python-snippets/maintrunk/changes" title="Changes">Changes</a></li>
<li><a href="/~akkzilla/python-snippets/maintrunk/files" title="Files" id="on">Files</a></li>

</ul>

<div id="loggerheadCont">
<div id="search_terms"></div>

<div id="breadcrumbs">

<a href="https://code.launchpad.net/~akkzilla/python-snippets/maintrunk">~akkzilla/python-snippets/maintrunk</a>


<span>: <span class="breadcrumb">
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/appindicator">appindicator</a>/createappindicator.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/appindicator/createappindicator.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=createappindicator.p-20100114210631-7gtc355kc0mjp64l-2">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/createappindicator.p-20100114210631-7gtc355kc0mjp64l-2/createappindicator.py">download file</a>
</li>
</ul>
<div class="view">
<table id="logentries">

<tr>
<td class="viewLine">
<pre><a id="L1" href="#L1">1</a>
<a id="L2" href="#L2">2</a>
<a id="L3" href="#L3">3</a>
<a id="L4" href="#L4">4</a>
<a id="L5" href="#L5">5</a>
<a id="L6" href="#L6">6</a>
<a id="L7" href="#L7">7</a>
<a id="L8" href="#L8">8</a>
<a id="L9" href="#L9">9</a>
<a id="L10" href="#L10">10</a>
<a id="L11" href="#L11">11</a>
<a id="L12" href="#L12">12</a>
<a id="L13" href="#L13">13</a>
<a id="L14" href="#L14">14</a>
<a id="L15" href="#L15">15</a>
<a id="L16" href="#L16">16</a>
<a id="L17" href="#L17">17</a>
<a id="L18" href="#L18">18</a>
<a id="L19" href="#L19">19</a>
<a id="L20" href="#L20">20</a>
<a id="L21" href="#L21">21</a>
<a id="L22" href="#L22">22</a>
<a id="L23" href="#L23">23</a>
<a id="L24" href="#L24">24</a>
<a id="L25" href="#L25">25</a>
<a id="L26" href="#L26">26</a>
<a id="L27" href="#L27">27</a>
<a id="L28" href="#L28">28</a>
<a id="L29" href="#L29">29</a>
<a id="L30" href="#L30">30</a>
<a id="L31" href="#L31">31</a>
<a id="L32" href="#L32">32</a>
<a id="L33" href="#L33">33</a>
<a id="L34" href="#L34">34</a>
<a id="L35" href="#L35">35</a>
<a id="L36" href="#L36">36</a>
<a id="L37" href="#L37">37</a>
<a id="L38" href="#L38">38</a>
<a id="L39" href="#L39">39</a>
<a id="L40" href="#L40">40</a>
<a id="L41" href="#L41">41</a>
<a id="L42" href="#L42">42</a>
<a id="L43" href="#L43">43</a>
<a id="L44" href="#L44">44</a>
<a id="L45" href="#L45">45</a>
<a id="L46" href="#L46">46</a>
<a id="L47" href="#L47">47</a>
<a id="L48" href="#L48">48</a>
<a id="L49" href="#L49">49</a>
<a id="L50" href="#L50">50</a>
<a id="L51" href="#L51">51</a>
<a id="L52" href="#L52">52</a>
<a id="L53" href="#L53">53</a>
<a id="L54" href="#L54">54</a>
<a id="L55" href="#L55">55</a>
<a id="L56" href="#L56">56</a>
<a id="L57" href="#L57">57</a>
<a id="L58" href="#L58">58</a>
<a id="L59" href="#L59">59</a>
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-c">#!/usr/bin/env python</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># [SNIPPET_NAME: Create an Application Indicator]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: Application Indicator]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: How to create an application indicator and add items to it]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: Jono Bacon &lt;jono@ubuntu.com&gt;]</span>
<span class="pyg-c"># [SNIPPET_DOCS: https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>

<span class="pyg-kn">import</span> <span class="pyg-nn">pygtk</span>
<span class="pyg-n">pygtk</span><span class="pyg-o">.</span><span class="pyg-n">require</span><span class="pyg-p">(</span><span class="pyg-s">&#39;2.0&#39;</span><span class="pyg-p">)</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">gtk</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">appindicator</span>

<span class="pyg-k">class</span> <span class="pyg-nc">AppIndicatorExample</span><span class="pyg-p">:</span>
    <span class="pyg-k">def</span> <span class="pyg-nf">__init__</span><span class="pyg-p">(</span><span class="pyg-bp">self</span><span class="pyg-p">):</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">ind</span> <span class="pyg-o">=</span> <span class="pyg-n">appindicator</span><span class="pyg-o">.</span><span class="pyg-n">Indicator</span> <span class="pyg-p">(</span><span class="pyg-s">&quot;example-simple-client&quot;</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;indicator-messages&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">appindicator</span><span class="pyg-o">.</span><span class="pyg-n">CATEGORY_APPLICATION_STATUS</span><span class="pyg-p">)</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">ind</span><span class="pyg-o">.</span><span class="pyg-n">set_status</span> <span class="pyg-p">(</span><span class="pyg-n">appindicator</span><span class="pyg-o">.</span><span class="pyg-n">STATUS_ACTIVE</span><span class="pyg-p">)</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">ind</span><span class="pyg-o">.</span><span class="pyg-n">set_attention_icon</span> <span class="pyg-p">(</span><span class="pyg-s">&quot;indicator-messages-new&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">ind</span><span class="pyg-o">.</span><span class="pyg-n">set_icon</span><span class="pyg-p">(</span><span class="pyg-s">&quot;distributor-logo&quot;</span><span class="pyg-p">)</span>

        <span class="pyg-c"># create a menu</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Menu</span><span class="pyg-p">()</span>

        <span class="pyg-c"># create items for the menu - labels, checkboxes, radio buttons and images are supported:</span>
        
        <span class="pyg-n">item</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">MenuItem</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Regular Menu Item&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">item</span><span class="pyg-o">.</span><span class="pyg-n">show</span><span class="pyg-p">()</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-o">.</span><span class="pyg-n">append</span><span class="pyg-p">(</span><span class="pyg-n">item</span><span class="pyg-p">)</span>

        <span class="pyg-n">check</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">CheckMenuItem</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Check Menu Item&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">check</span><span class="pyg-o">.</span><span class="pyg-n">show</span><span class="pyg-p">()</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-o">.</span><span class="pyg-n">append</span><span class="pyg-p">(</span><span class="pyg-n">check</span><span class="pyg-p">)</span>

        <span class="pyg-n">radio</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">RadioMenuItem</span><span class="pyg-p">(</span><span class="pyg-bp">None</span><span class="pyg-p">,</span> <span class="pyg-s">&quot;Radio Menu Item&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">radio</span><span class="pyg-o">.</span><span class="pyg-n">show</span><span class="pyg-p">()</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-o">.</span><span class="pyg-n">append</span><span class="pyg-p">(</span><span class="pyg-n">radio</span><span class="pyg-p">)</span>

        <span class="pyg-n">image</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">ImageMenuItem</span><span class="pyg-p">(</span><span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">STOCK_QUIT</span><span class="pyg-p">)</span>
        <span class="pyg-n">image</span><span class="pyg-o">.</span><span class="pyg-n">connect</span><span class="pyg-p">(</span><span class="pyg-s">&quot;activate&quot;</span><span class="pyg-p">,</span> <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">quit</span><span class="pyg-p">)</span>
        <span class="pyg-n">image</span><span class="pyg-o">.</span><span class="pyg-n">show</span><span class="pyg-p">()</span>
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-o">.</span><span class="pyg-n">append</span><span class="pyg-p">(</span><span class="pyg-n">image</span><span class="pyg-p">)</span>
                    
        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-o">.</span><span class="pyg-n">show</span><span class="pyg-p">()</span>

        <span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">ind</span><span class="pyg-o">.</span><span class="pyg-n">set_menu</span><span class="pyg-p">(</span><span class="pyg-bp">self</span><span class="pyg-o">.</span><span class="pyg-n">menu</span><span class="pyg-p">)</span>

    <span class="pyg-k">def</span> <span class="pyg-nf">quit</span><span class="pyg-p">(</span><span class="pyg-bp">self</span><span class="pyg-p">,</span> <span class="pyg-n">widget</span><span class="pyg-p">,</span> <span class="pyg-n">data</span><span class="pyg-o">=</span><span class="pyg-bp">None</span><span class="pyg-p">):</span>
        <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main_quit</span><span class="pyg-p">()</span>


<span class="pyg-k">def</span> <span class="pyg-nf">main</span><span class="pyg-p">():</span>
    <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main</span><span class="pyg-p">()</span>
    <span class="pyg-k">return</span> <span class="pyg-mi">0</span>

<span class="pyg-k">if</span> <span class="pyg-n">__name__</span> <span class="pyg-o">==</span> <span class="pyg-s">&quot;__main__&quot;</span><span class="pyg-p">:</span>
    <span class="pyg-n">indicator</span> <span class="pyg-o">=</span> <span class="pyg-n">AppIndicatorExample</span><span class="pyg-p">()</span>
    <span class="pyg-n">main</span><span class="pyg-p">()</span>
</pre>
</td>
</tr>
</table>
</div>
</div>
<p id="footer" class="fl">
Loggerhead is a web-based interface for <a href="http://bazaar-vcs.org/">Bazaar</a> branches
<br />
Version: 1.18.2<span>, Revision: 16985</span>
</p>
</div>
</body>
</html>