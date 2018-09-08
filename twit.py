<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of twitter/twit.py at revision 100</title>
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
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/twitter">twitter</a>/twit.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/twitter/twit.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=twit.py-20100402221018-9fjbn77lj706q8s7-2">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/twit.py-20100402221018-9fjbn77lj706q8s7-2/twit.py">download file</a>
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
<a id="L60" href="#L60">60</a>
<a id="L61" href="#L61">61</a>
<a id="L62" href="#L62">62</a>
<a id="L63" href="#L63">63</a>
<a id="L64" href="#L64">64</a>
<a id="L65" href="#L65">65</a>
<a id="L66" href="#L66">66</a>
<a id="L67" href="#L67">67</a>
<a id="L68" href="#L68">68</a>
<a id="L69" href="#L69">69</a>
<a id="L70" href="#L70">70</a>
<a id="L71" href="#L71">71</a>
<a id="L72" href="#L72">72</a>
<a id="L73" href="#L73">73</a>
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-c"># [SNIPPET_NAME: Login and Tweet]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: twitter, PyGTK]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: Log in to your Twitter account and update your status. Uses http://code.google.com/p/python-twitter/]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: Joel Auterson joel.auterson@googlemail.com]</span>
<span class="pyg-c"># [SNIPPET_DOCS: http://static.unto.net/python-twitter/0.6/doc/twitter.html]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>

<span class="pyg-kn">import</span> <span class="pyg-nn">twitter</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">pygtk</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">gtk</span>

<span class="pyg-k">class</span> <span class="pyg-nc">GTK_Main</span><span class="pyg-p">():</span>

    <span class="pyg-k">def</span> <span class="pyg-nf">__init__</span><span class="pyg-p">(</span><span class="pyg-bp">self</span><span class="pyg-p">):</span>

        <span class="pyg-k">def</span> <span class="pyg-nf">loginClicked</span><span class="pyg-p">(</span><span class="pyg-n">loginButton</span><span class="pyg-p">):</span>

            <span class="pyg-n">user</span> <span class="pyg-o">=</span> <span class="pyg-n">loginUserT</span><span class="pyg-o">.</span><span class="pyg-n">get_text</span><span class="pyg-p">()</span>
            <span class="pyg-n">passwd</span> <span class="pyg-o">=</span> <span class="pyg-n">loginPassT</span><span class="pyg-o">.</span><span class="pyg-n">get_text</span><span class="pyg-p">()</span>
            <span class="pyg-k">global</span> <span class="pyg-n">api</span>
            <span class="pyg-n">api</span> <span class="pyg-o">=</span> <span class="pyg-n">twitter</span><span class="pyg-o">.</span><span class="pyg-n">Api</span><span class="pyg-p">(</span><span class="pyg-n">username</span><span class="pyg-o">=</span><span class="pyg-n">user</span><span class="pyg-p">,</span> <span class="pyg-n">password</span><span class="pyg-o">=</span><span class="pyg-n">passwd</span><span class="pyg-p">)</span>
            <span class="pyg-n">login</span><span class="pyg-o">.</span><span class="pyg-n">hide</span><span class="pyg-p">()</span>
            <span class="pyg-n">window</span><span class="pyg-o">.</span><span class="pyg-n">show_all</span><span class="pyg-p">()</span>

        <span class="pyg-k">def</span> <span class="pyg-nf">twitClicked</span><span class="pyg-p">(</span><span class="pyg-n">twitButton</span><span class="pyg-p">):</span>

            <span class="pyg-n">newtweet</span> <span class="pyg-o">=</span> <span class="pyg-n">twitE</span><span class="pyg-o">.</span><span class="pyg-n">get_text</span><span class="pyg-p">()</span>
            <span class="pyg-n">api</span><span class="pyg-o">.</span><span class="pyg-n">PostUpdate</span><span class="pyg-p">(</span><span class="pyg-n">newtweet</span><span class="pyg-p">)</span>
            <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main_quit</span><span class="pyg-p">()</span>

        <span class="pyg-c">#Create things - Login</span>

        <span class="pyg-n">login</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Window</span><span class="pyg-p">()</span>
        <span class="pyg-n">login</span><span class="pyg-o">.</span><span class="pyg-n">connect</span><span class="pyg-p">(</span><span class="pyg-s">&quot;destroy&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main_quit</span><span class="pyg-p">)</span>
        <span class="pyg-n">login</span><span class="pyg-o">.</span><span class="pyg-n">set_title</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Login&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginVbox</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">VBox</span><span class="pyg-p">(</span><span class="pyg-n">homogeneous</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginLabel</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Label</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Please log in to Twitter!&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox1</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">HBox</span><span class="pyg-p">(</span><span class="pyg-n">homogeneous</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">,</span> <span class="pyg-n">spacing</span><span class="pyg-o">=</span><span class="pyg-mi">3</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox2</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">HBox</span><span class="pyg-p">(</span><span class="pyg-n">homogeneous</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">,</span> <span class="pyg-n">spacing</span><span class="pyg-o">=</span><span class="pyg-mi">3</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginUserL</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Label</span><span class="pyg-p">(</span><span class="pyg-s">&quot;User:&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginPassL</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Label</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Pass:&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginUserT</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Entry</span><span class="pyg-p">()</span>
        <span class="pyg-n">loginPassT</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Entry</span><span class="pyg-p">()</span>
        <span class="pyg-n">loginButton</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Button</span><span class="pyg-p">(</span><span class="pyg-n">label</span><span class="pyg-o">=</span><span class="pyg-s">&quot;Log In&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginButton</span><span class="pyg-o">.</span><span class="pyg-n">connect</span><span class="pyg-p">(</span><span class="pyg-s">&quot;clicked&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">loginClicked</span><span class="pyg-p">)</span>

        <span class="pyg-n">login</span><span class="pyg-o">.</span><span class="pyg-n">add</span><span class="pyg-p">(</span><span class="pyg-n">loginVbox</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginVbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginLabel</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginVbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginHbox1</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginVbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginHbox2</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginVbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginButton</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox1</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginUserL</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox1</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginUserT</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox2</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginPassL</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">loginHbox2</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">loginPassT</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>

        <span class="pyg-c">#Create tweeting window</span>

        <span class="pyg-n">window</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Window</span><span class="pyg-p">()</span>
        <span class="pyg-n">window</span><span class="pyg-o">.</span><span class="pyg-n">connect</span><span class="pyg-p">(</span><span class="pyg-s">&quot;destroy&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main_quit</span><span class="pyg-p">)</span>
        <span class="pyg-n">window</span><span class="pyg-o">.</span><span class="pyg-n">set_title</span><span class="pyg-p">(</span><span class="pyg-s">&quot;Twitter&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">twitvbox</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">VBox</span><span class="pyg-p">(</span><span class="pyg-n">homogeneous</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">twitE</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Entry</span><span class="pyg-p">()</span>
        <span class="pyg-n">twitButton</span> <span class="pyg-o">=</span> <span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">Button</span><span class="pyg-p">(</span><span class="pyg-n">label</span><span class="pyg-o">=</span><span class="pyg-s">&quot;Tweet!&quot;</span><span class="pyg-p">)</span>
        <span class="pyg-n">window</span><span class="pyg-o">.</span><span class="pyg-n">add</span><span class="pyg-p">(</span><span class="pyg-n">twitvbox</span><span class="pyg-p">)</span>
        <span class="pyg-n">twitvbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">twitE</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">False</span><span class="pyg-p">)</span>
        <span class="pyg-n">twitvbox</span><span class="pyg-o">.</span><span class="pyg-n">pack_start</span><span class="pyg-p">(</span><span class="pyg-n">twitButton</span><span class="pyg-p">,</span> <span class="pyg-n">expand</span><span class="pyg-o">=</span><span class="pyg-bp">True</span><span class="pyg-p">)</span>
        <span class="pyg-n">twitButton</span><span class="pyg-o">.</span><span class="pyg-n">connect</span><span class="pyg-p">(</span><span class="pyg-s">&quot;clicked&quot;</span><span class="pyg-p">,</span> <span class="pyg-n">twitClicked</span><span class="pyg-p">)</span>

        <span class="pyg-n">login</span><span class="pyg-o">.</span><span class="pyg-n">show_all</span><span class="pyg-p">()</span>

<span class="pyg-n">GTK_Main</span><span class="pyg-p">()</span>
<span class="pyg-n">gtk</span><span class="pyg-o">.</span><span class="pyg-n">main</span><span class="pyg-p">()</span>
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