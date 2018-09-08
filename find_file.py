<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of os/find_file.py at revision 100</title>
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
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/os">os</a>/find_file.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/os/find_file.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=find_file.py-20100329045713-gq4lls4e2jsqyr9h-1">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/find_file.py-20100329045713-gq4lls4e2jsqyr9h-1/find_file.py">download file</a>
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
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-c">#!/usr/bin/env python</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># [SNIPPET_NAME: Find a file]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: os]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: Recursively search directories for a file]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: Andy Breiner &lt;breinera@gmail.com&gt;]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>
<span class="pyg-c"># [SNIPPET_DOCS: http://docs.python.org/library/os.html, http://diveintopython.org/file_handling/os_module.html]</span>

<span class="pyg-kn">import</span> <span class="pyg-nn">os</span>

<span class="pyg-k">def</span> <span class="pyg-nf">look_in_directory</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">):</span>
    <span class="pyg-sd">&quot;&quot;&quot;Loop through the current directory for the file, if the current item</span>
<span class="pyg-sd">       is a directory, it recusively looks through that folder&quot;&quot;&quot;</span>

    <span class="pyg-c"># Loop over all the items in the directory</span>
    <span class="pyg-k">for</span> <span class="pyg-n">f</span> <span class="pyg-ow">in</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">listdir</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">):</span>
        <span class="pyg-c"># Uncomment the line below to see how the files/folders are searched</span>
        <span class="pyg-c"># print &quot;Looking in &quot; + directory</span>

        <span class="pyg-c"># If the item is a file check to see if it is what we are looking</span>
        <span class="pyg-c"># for, if it is, print that we found it and return true</span>
        <span class="pyg-k">if</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">isfile</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)):</span>
            <span class="pyg-k">if</span> <span class="pyg-n">f</span> <span class="pyg-o">==</span> <span class="pyg-n">file_to_find</span><span class="pyg-p">:</span>
                <span class="pyg-k">print</span> <span class="pyg-s">&quot;Found file: &quot;</span> <span class="pyg-o">+</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)</span>
                <span class="pyg-k">return</span> <span class="pyg-bp">True</span>

        <span class="pyg-c"># If the item is a directory, we recursivley look through that</span>
        <span class="pyg-c"># directory if it is found, we again return true</span>
        <span class="pyg-k">if</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">isdir</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)):</span>
            <span class="pyg-k">if</span> <span class="pyg-n">look_in_directory</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)):</span>
                <span class="pyg-k">return</span> <span class="pyg-bp">True</span>

<span class="pyg-c"># we will look for the file recursively</span>
<span class="pyg-n">file_to_find</span> <span class="pyg-o">=</span> <span class="pyg-s">&quot;jono.png&quot;</span>
<span class="pyg-c"># Start looking in the home directory (~)</span>
<span class="pyg-c"># If it is not found, ie it did not return True, tell the user it was &quot;Not</span>
<span class="pyg-c"># Found&quot;</span>
<span class="pyg-k">if</span> <span class="pyg-n">look_in_directory</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">expanduser</span><span class="pyg-p">(</span><span class="pyg-s">&quot;~&quot;</span><span class="pyg-p">))</span> <span class="pyg-o">!=</span> <span class="pyg-bp">True</span><span class="pyg-p">:</span>
    <span class="pyg-k">print</span> <span class="pyg-s">&quot;Not Found&quot;</span>
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