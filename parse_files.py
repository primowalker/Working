<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of os/parse_files.py at revision 100</title>
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
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/os">os</a>/parse_files.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/os/parse_files.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=parse_files.py-20100329194226-hqqk0al277z9c2bk-1">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/parse_files.py-20100329194226-hqqk0al277z9c2bk-1/parse_files.py">download file</a>
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
<a id="L74" href="#L74">74</a>
<a id="L75" href="#L75">75</a>
<a id="L76" href="#L76">76</a>
<a id="L77" href="#L77">77</a>
<a id="L78" href="#L78">78</a>
<a id="L79" href="#L79">79</a>
<a id="L80" href="#L80">80</a>
<a id="L81" href="#L81">81</a>
<a id="L82" href="#L82">82</a>
<a id="L83" href="#L83">83</a>
<a id="L84" href="#L84">84</a>
<a id="L85" href="#L85">85</a>
<a id="L86" href="#L86">86</a>
<a id="L87" href="#L87">87</a>
<a id="L88" href="#L88">88</a>
<a id="L89" href="#L89">89</a>
<a id="L90" href="#L90">90</a>
<a id="L91" href="#L91">91</a>
<a id="L92" href="#L92">92</a>
<a id="L93" href="#L93">93</a>
<a id="L94" href="#L94">94</a>
<a id="L95" href="#L95">95</a>
<a id="L96" href="#L96">96</a>
<a id="L97" href="#L97">97</a>
<a id="L98" href="#L98">98</a>
<a id="L99" href="#L99">99</a>
<a id="L100" href="#L100">100</a>
<a id="L101" href="#L101">101</a>
<a id="L102" href="#L102">102</a>
<a id="L103" href="#L103">103</a>
<a id="L104" href="#L104">104</a>
<a id="L105" href="#L105">105</a>
<a id="L106" href="#L106">106</a>
<a id="L107" href="#L107">107</a>
<a id="L108" href="#L108">108</a>
</pre>
</td>
<td class="viewCont">
<pre><span class="pyg-c">#!/usr/bin/env python</span>
<span class="pyg-c">#</span>
<span class="pyg-c"># [SNIPPET_NAME: Parse a File]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: os, Regular Expression]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: Recursively go through all the python files and see who has submitted the most (assuming they put their name on them)]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: Andy Breiner &lt;breinera@gmail.com&gt;]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>
<span class="pyg-c"># [SNIPPET_DOCS: http://docs.python.org/library/os.html, # http://docs.python.org/library/re.html]</span>

<span class="pyg-kn">import</span> <span class="pyg-nn">os</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">re</span>

<span class="pyg-c"># A dictionary to store information about who contributed what</span>
<span class="pyg-c"># it is assumed that the file has the format</span>
<span class="pyg-c"># SNIPPET_AUTHOR: USER_NAME &lt;USER_EMAIL&gt;], if this is not the case then</span>
<span class="pyg-c"># this program doesn&#39;t count that file</span>
<span class="pyg-n">name_list</span> <span class="pyg-o">=</span> <span class="pyg-p">{}</span>
<span class="pyg-n">count_list</span> <span class="pyg-o">=</span> <span class="pyg-p">{}</span>


<span class="pyg-k">def</span> <span class="pyg-nf">find_python_files</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">):</span>
    <span class="pyg-sd">&quot;&quot;&quot;Loop through the current directory and look for a python file, if</span>
<span class="pyg-sd">       one is found look for the author and create a list showing who has</span>
<span class="pyg-sd">       contributed the most snippets&quot;&quot;&quot;</span>

    <span class="pyg-c"># Loop over all the items in the directory</span>
    <span class="pyg-k">for</span> <span class="pyg-n">f</span> <span class="pyg-ow">in</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">listdir</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">):</span>
        <span class="pyg-c"># If the item is a file, check to see if it ends with .py and if</span>
        <span class="pyg-c"># so, parse it and find the Author</span>
        <span class="pyg-k">if</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">isfile</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)):</span>
            <span class="pyg-c"># this will get the last three characters of the filename</span>
            <span class="pyg-k">if</span> <span class="pyg-n">f</span><span class="pyg-p">[</span><span class="pyg-o">-</span><span class="pyg-mi">3</span><span class="pyg-p">:]</span> <span class="pyg-o">==</span> <span class="pyg-s">&quot;.py&quot;</span><span class="pyg-p">:</span>

                <span class="pyg-c"># this will open the file</span>
                <span class="pyg-n">file_handler</span> <span class="pyg-o">=</span> <span class="pyg-nb">open</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">),</span> <span class="pyg-s">&quot;r&quot;</span><span class="pyg-p">)</span>

                <span class="pyg-c"># this will read all of the file content</span>
                <span class="pyg-n">content</span> <span class="pyg-o">=</span> <span class="pyg-n">file_handler</span><span class="pyg-o">.</span><span class="pyg-n">read</span><span class="pyg-p">()</span>

                <span class="pyg-c"># this will close the file</span>
                <span class="pyg-n">file_handler</span><span class="pyg-o">.</span><span class="pyg-n">close</span><span class="pyg-p">()</span>

                <span class="pyg-c"># we are looking for a string that has &quot;SNIPPET_AUTHOR:&quot;</span>
                <span class="pyg-c"># and then any character after it (.) one or more times (+)</span>
                <span class="pyg-c"># the newline will end this search</span>
                <span class="pyg-n">found</span> <span class="pyg-o">=</span> <span class="pyg-n">re</span><span class="pyg-o">.</span><span class="pyg-n">search</span><span class="pyg-p">(</span><span class="pyg-s">&#39;SNIPPET_AUTHOR:.+&#39;</span><span class="pyg-p">,</span> <span class="pyg-n">content</span><span class="pyg-p">)</span>
                <span class="pyg-k">try</span><span class="pyg-p">:</span>
                    <span class="pyg-c"># found.group(0) contains the first and should be only</span>
                    <span class="pyg-c"># occurance of this regular expression</span>
                    <span class="pyg-n">line</span> <span class="pyg-o">=</span> <span class="pyg-n">found</span><span class="pyg-o">.</span><span class="pyg-n">group</span><span class="pyg-p">(</span><span class="pyg-mi">0</span><span class="pyg-p">)</span>
                    <span class="pyg-c"># we do a regular search on the line looking for</span>
                    <span class="pyg-c"># the email which should be surrounded by &lt; &gt;</span>
                    <span class="pyg-n">email_search</span> <span class="pyg-o">=</span> <span class="pyg-n">re</span><span class="pyg-o">.</span><span class="pyg-n">search</span><span class="pyg-p">(</span><span class="pyg-s">&#39;&lt;.+&gt;&#39;</span><span class="pyg-p">,</span> <span class="pyg-n">line</span><span class="pyg-p">)</span>

                    <span class="pyg-c"># email_search.group(0) has the email, the [1:-1]</span>
                    <span class="pyg-c"># tells python to ignore the first character (&lt;)</span>
                    <span class="pyg-c"># and the last character (&gt;)</span>
                    <span class="pyg-n">email</span> <span class="pyg-o">=</span> <span class="pyg-n">email_search</span><span class="pyg-o">.</span><span class="pyg-n">group</span><span class="pyg-p">(</span><span class="pyg-mi">0</span><span class="pyg-p">)[</span><span class="pyg-mi">1</span><span class="pyg-p">:</span><span class="pyg-o">-</span><span class="pyg-mi">1</span><span class="pyg-p">]</span>

                    <span class="pyg-c"># we look between the : and &lt; which should be the</span>
                    <span class="pyg-c"># name</span>
                    <span class="pyg-n">name_search</span> <span class="pyg-o">=</span> <span class="pyg-n">re</span><span class="pyg-o">.</span><span class="pyg-n">search</span><span class="pyg-p">(</span><span class="pyg-s">&#39;:.*&lt;&#39;</span><span class="pyg-p">,</span> <span class="pyg-n">line</span><span class="pyg-p">)</span>

                    <span class="pyg-c"># name_search.group(0) has the name, the [1:-1]</span>
                    <span class="pyg-c"># tells python to ignore the first character (:)</span>
                    <span class="pyg-c"># and the last character (&lt;), finally strip()</span>
                    <span class="pyg-c"># removes any extra spaces at the begin or end</span>
                    <span class="pyg-n">name</span> <span class="pyg-o">=</span> <span class="pyg-n">name_search</span><span class="pyg-o">.</span><span class="pyg-n">group</span><span class="pyg-p">(</span><span class="pyg-mi">0</span><span class="pyg-p">)[</span><span class="pyg-mi">1</span><span class="pyg-p">:</span><span class="pyg-o">-</span><span class="pyg-mi">1</span><span class="pyg-p">]</span><span class="pyg-o">.</span><span class="pyg-n">strip</span><span class="pyg-p">()</span>

                    <span class="pyg-c"># see if this author has already been encountered</span>
                    <span class="pyg-c"># before</span>
                    <span class="pyg-k">try</span><span class="pyg-p">:</span>
                        <span class="pyg-n">count_list</span><span class="pyg-p">[</span><span class="pyg-n">email</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-n">count_list</span><span class="pyg-p">[</span><span class="pyg-n">email</span><span class="pyg-p">]</span> <span class="pyg-o">+</span> <span class="pyg-mi">1</span>
                    <span class="pyg-k">except</span><span class="pyg-p">:</span>
                        <span class="pyg-c"># they have not been seen before so add them</span>
                        <span class="pyg-n">count_list</span><span class="pyg-p">[</span><span class="pyg-n">email</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-mi">1</span>
                        <span class="pyg-n">name_list</span><span class="pyg-p">[</span><span class="pyg-n">email</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-n">name</span>
                <span class="pyg-k">except</span><span class="pyg-p">:</span>
                    <span class="pyg-c"># something was wrong with finding a regular</span>
                    <span class="pyg-c"># expression</span>
                    <span class="pyg-k">pass</span>

        <span class="pyg-c"># If the item is a directory, we recursivley look through that</span>
        <span class="pyg-c"># directory</span>
        <span class="pyg-k">if</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">isdir</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">)):</span>
            <span class="pyg-n">find_python_files</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">directory</span><span class="pyg-p">,</span> <span class="pyg-n">f</span><span class="pyg-p">))</span>

<span class="pyg-c"># go up one level and start searching for python files</span>
<span class="pyg-n">location</span> <span class="pyg-o">=</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">join</span><span class="pyg-p">(</span><span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">getcwd</span><span class="pyg-p">(),</span> <span class="pyg-s">&quot;../&quot;</span><span class="pyg-p">)</span>

<span class="pyg-c"># Recurse through that location and parse all the python files to see who</span>
<span class="pyg-c"># has contributed the most</span>
<span class="pyg-n">find_python_files</span><span class="pyg-p">(</span><span class="pyg-n">location</span><span class="pyg-p">)</span>

<span class="pyg-c"># sort the collection</span>
<span class="pyg-n">count_list</span> <span class="pyg-o">=</span> <span class="pyg-nb">sorted</span><span class="pyg-p">(</span><span class="pyg-n">count_list</span><span class="pyg-o">.</span><span class="pyg-n">items</span><span class="pyg-p">(),</span> <span class="pyg-n">key</span><span class="pyg-o">=</span><span class="pyg-k">lambda</span><span class="pyg-p">(</span><span class="pyg-n">key</span><span class="pyg-p">,</span> <span class="pyg-n">value</span><span class="pyg-p">):</span> <span class="pyg-p">(</span><span class="pyg-n">value</span><span class="pyg-p">,</span> <span class="pyg-n">key</span><span class="pyg-p">))</span>

<span class="pyg-c"># print the count_list in reverse order while looking inside name_list for</span>
<span class="pyg-c"># the given name</span>
<span class="pyg-n">count_list</span><span class="pyg-o">.</span><span class="pyg-n">reverse</span><span class="pyg-p">()</span>
<span class="pyg-k">for</span> <span class="pyg-n">index</span> <span class="pyg-ow">in</span> <span class="pyg-nb">range</span><span class="pyg-p">(</span><span class="pyg-mi">0</span><span class="pyg-p">,</span> <span class="pyg-nb">len</span><span class="pyg-p">(</span><span class="pyg-n">count_list</span><span class="pyg-p">)):</span>
    <span class="pyg-c"># get the first entry which is similar to (email, count)</span>
    <span class="pyg-c"># then get the first item in that entry</span>
    <span class="pyg-n">email</span> <span class="pyg-o">=</span> <span class="pyg-n">count_list</span><span class="pyg-p">[</span><span class="pyg-n">index</span><span class="pyg-p">][</span><span class="pyg-mi">0</span><span class="pyg-p">]</span>

    <span class="pyg-c"># use the email to lookup the name and then print the name along with</span>
    <span class="pyg-c"># the second item in the entry which should be the python snippet count</span>
    <span class="pyg-k">print</span> <span class="pyg-n">name_list</span><span class="pyg-p">[</span><span class="pyg-n">email</span><span class="pyg-p">]</span> <span class="pyg-o">+</span> <span class="pyg-s">&quot; &quot;</span> <span class="pyg-o">+</span> <span class="pyg-nb">str</span><span class="pyg-p">(</span><span class="pyg-n">count_list</span><span class="pyg-p">[</span><span class="pyg-n">index</span><span class="pyg-p">][</span><span class="pyg-mi">1</span><span class="pyg-p">])</span>
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