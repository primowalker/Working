<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of tarfile/createtar1.py at revision 100</title>
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
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/tarfile">tarfile</a>/createtar1.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/tarfile/createtar1.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=createtar1.py-20100329001919-xdy2jmy92rifwgoz-2">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/createtar1.py-20100329001919-xdy2jmy92rifwgoz-2/createtar1.py">download file</a>
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
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-c">#!/usr/bin/env python</span>
<span class="pyg-c"># [SNIPPET_NAME: Create a tar file from path]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: tarfile]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: Create a tar file from a path, including compression]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: Tim Voet &lt;tim.voet@gmail.com&gt;]</span>
<span class="pyg-c"># [SNIPPET_DOCS: http://docs.python.org/library/tarfile.html#module-tarfile]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>

<span class="pyg-kn">import</span> <span class="pyg-nn">tarfile</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">os</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">sys</span>

<span class="pyg-n">user</span> <span class="pyg-o">=</span>  <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">getenv</span><span class="pyg-p">(</span><span class="pyg-s">&#39;USERNAME&#39;</span><span class="pyg-p">)</span>

<span class="pyg-n">filename</span> <span class="pyg-o">=</span> <span class="pyg-s">&#39;/home/</span><span class="pyg-si">%s</span><span class="pyg-s">/tmp.tgz&#39;</span> <span class="pyg-o">%</span> <span class="pyg-n">user</span>
<span class="pyg-k">print</span> <span class="pyg-s">&#39;The tar file was created here: </span><span class="pyg-si">%s</span><span class="pyg-s">&#39;</span> <span class="pyg-o">%</span> <span class="pyg-n">filename</span>
<span class="pyg-n">mode</span> <span class="pyg-o">=</span> <span class="pyg-s">&#39;w:gz&#39;</span>

<span class="pyg-nb">file</span> <span class="pyg-o">=</span> <span class="pyg-n">tarfile</span><span class="pyg-o">.</span><span class="pyg-n">open</span><span class="pyg-p">(</span> <span class="pyg-n">filename</span><span class="pyg-p">,</span> <span class="pyg-n">mode</span> <span class="pyg-p">)</span>

<span class="pyg-nb">file</span><span class="pyg-o">.</span><span class="pyg-n">add</span><span class="pyg-p">(</span> <span class="pyg-s">&#39;/var/log/auth.log&#39;</span> <span class="pyg-p">)</span>
<span class="pyg-nb">file</span><span class="pyg-o">.</span><span class="pyg-n">add</span><span class="pyg-p">(</span> <span class="pyg-s">&#39;/var/log/messages&#39;</span> <span class="pyg-p">)</span>

<span class="pyg-nb">file</span><span class="pyg-o">.</span><span class="pyg-n">close</span><span class="pyg-p">()</span>
<span class="pyg-k">print</span> <span class="pyg-s">&#39;done&#39;</span>
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