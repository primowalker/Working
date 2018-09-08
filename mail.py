<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="Loggerhead/1.18.2 Python/2.7.3 Bazaar/2.6.0 Paste/1.7.5.1 PasteDeploy/1.3.4 SimpleTAL/4.3 Pygments/1.6 simplejson/3.1.3" name="generator" />
<title>~akkzilla/python-snippets/maintrunk : contents of email/mail.py at revision 100</title>
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
/<a href="/~akkzilla/python-snippets/maintrunk/files/100/email">email</a>/mail.py
</span> (revision 100)</span>
</div>

<div>

<ul id="submenuTabs">
<li id="first">
<a href="/~akkzilla/python-snippets/maintrunk/files/100">browse files</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/annotate/head:/email/mail.py">view with revision information</a>
</li>

<li>
<a href="/~akkzilla/python-snippets/maintrunk/revision/100">view revision</a>
</li>
<li>
<a href="/~akkzilla/python-snippets/maintrunk/changes?filter_file_id=mail.py-20100424183351-1kexeo0i6c9q8f94-2">view changes to this file</a>
</li>
<li id="last">
<a href="/~akkzilla/python-snippets/maintrunk/download/head:/mail.py-20100424183351-1kexeo0i6c9q8f94-2/mail.py">download file</a>
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
<pre><span class="pyg-c"># [SNIPPET_NAME: Sending Email]</span>
<span class="pyg-c"># [SNIPPET_CATEGORIES: smtplib, email]</span>
<span class="pyg-c"># [SNIPPET_DESCRIPTION: Sending mail from gmail account with many attachements and to_many_mails_ids]</span>
<span class="pyg-c"># [SNIPPET_AUTHOR: kutuma]</span>
<span class="pyg-c"># [SNIPPET_LICENSE: GPL]</span>
<span class="pyg-c"># [SNIPPET_UPLOADED_BY: Arulalan.T &lt;tarulalan@gmail.com&gt;]</span>

<span class="pyg-c"># you need to set the gmail user name and its password at the line of 22 and 23 st (in gedit, line number) of this snippet.</span>

<span class="pyg-c"># you need to set the to_mail_ids in a string array , subject, body , attachements_absolute_path in a string array from the line of 26 of this snippet.</span>


<span class="pyg-c">#!/usr/bin/python</span>
<span class="pyg-c"># ref : http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">smtplib</span>
<span class="pyg-kn">from</span> <span class="pyg-nn">email.MIMEMultipart</span> <span class="pyg-kn">import</span> <span class="pyg-n">MIMEMultipart</span>
<span class="pyg-kn">from</span> <span class="pyg-nn">email.MIMEBase</span> <span class="pyg-kn">import</span> <span class="pyg-n">MIMEBase</span>
<span class="pyg-kn">from</span> <span class="pyg-nn">email.MIMEText</span> <span class="pyg-kn">import</span> <span class="pyg-n">MIMEText</span>
<span class="pyg-kn">from</span> <span class="pyg-nn">email</span> <span class="pyg-kn">import</span> <span class="pyg-n">Encoders</span>
<span class="pyg-kn">import</span> <span class="pyg-nn">os</span>

<span class="pyg-n">gmail_user</span> <span class="pyg-o">=</span> <span class="pyg-s">&quot;username@gmail.com&quot;</span>
<span class="pyg-n">gmail_pwd</span> <span class="pyg-o">=</span> <span class="pyg-s">&quot;gmail_password&quot;</span>


<span class="pyg-n">body</span><span class="pyg-o">=</span><span class="pyg-s">&quot; I am Body &quot;</span>
<span class="pyg-n">subject</span><span class="pyg-o">=</span><span class="pyg-s">&quot;I   am     Subject &quot;</span>

<span class="pyg-n">to_mail_ids</span><span class="pyg-o">=</span><span class="pyg-p">[</span><span class="pyg-s">&quot;friend1_mail_id&quot;</span><span class="pyg-p">,</span><span class="pyg-s">&quot;friend2_mail_id&quot;</span><span class="pyg-p">]</span>
<span class="pyg-n">attachements_path</span><span class="pyg-o">=</span><span class="pyg-p">[</span><span class="pyg-s">&quot;absolute_attachement1_with_extension&quot;</span><span class="pyg-p">,</span><span class="pyg-s">&quot;absolute_attachement2_with_extension&quot;</span><span class="pyg-p">]</span><span class="pyg-c"># for eg : /home/arul/z/nnk.txt, /home/arul/python/sam.py</span>



<span class="pyg-k">def</span> <span class="pyg-nf">mail</span><span class="pyg-p">(</span><span class="pyg-n">to</span><span class="pyg-p">,</span> <span class="pyg-n">subject</span><span class="pyg-p">,</span> <span class="pyg-n">text</span><span class="pyg-p">,</span> <span class="pyg-n">attach</span><span class="pyg-o">=</span><span class="pyg-p">[]):</span>
   <span class="pyg-n">msg</span> <span class="pyg-o">=</span> <span class="pyg-n">MIMEMultipart</span><span class="pyg-p">()</span>

   <span class="pyg-n">msg</span><span class="pyg-p">[</span><span class="pyg-s">&#39;From&#39;</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-n">gmail_user</span>
   <span class="pyg-n">msg</span><span class="pyg-p">[</span><span class="pyg-s">&#39;To&#39;</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-n">to</span>
   <span class="pyg-n">msg</span><span class="pyg-p">[</span><span class="pyg-s">&#39;Subject&#39;</span><span class="pyg-p">]</span> <span class="pyg-o">=</span> <span class="pyg-n">subject</span>

   <span class="pyg-n">msg</span><span class="pyg-o">.</span><span class="pyg-n">attach</span><span class="pyg-p">(</span><span class="pyg-n">MIMEText</span><span class="pyg-p">(</span><span class="pyg-n">text</span><span class="pyg-p">))</span>

   <span class="pyg-k">try</span><span class="pyg-p">:</span>

		<span class="pyg-k">for</span> <span class="pyg-n">i</span> <span class="pyg-ow">in</span> <span class="pyg-nb">range</span><span class="pyg-p">(</span><span class="pyg-nb">len</span><span class="pyg-p">(</span><span class="pyg-n">attach</span><span class="pyg-p">)):</span>
				<span class="pyg-n">part</span> <span class="pyg-o">=</span> <span class="pyg-n">MIMEBase</span><span class="pyg-p">(</span><span class="pyg-s">&#39;application&#39;</span><span class="pyg-p">,</span> <span class="pyg-s">&#39;octet-stream&#39;</span><span class="pyg-p">)</span>
				<span class="pyg-n">part</span><span class="pyg-o">.</span><span class="pyg-n">set_payload</span><span class="pyg-p">(</span><span class="pyg-nb">open</span><span class="pyg-p">(</span><span class="pyg-n">attach</span><span class="pyg-p">[</span><span class="pyg-n">i</span><span class="pyg-p">],</span> <span class="pyg-s">&#39;rb&#39;</span><span class="pyg-p">)</span><span class="pyg-o">.</span><span class="pyg-n">read</span><span class="pyg-p">())</span>
				<span class="pyg-n">Encoders</span><span class="pyg-o">.</span><span class="pyg-n">encode_base64</span><span class="pyg-p">(</span><span class="pyg-n">part</span><span class="pyg-p">)</span>
				<span class="pyg-n">part</span><span class="pyg-o">.</span><span class="pyg-n">add_header</span><span class="pyg-p">(</span><span class="pyg-s">&#39;Content-Disposition&#39;</span><span class="pyg-p">,</span><span class="pyg-s">&#39;attachment; filename=&quot;</span><span class="pyg-si">%s</span><span class="pyg-s">&quot;&#39;</span> <span class="pyg-o">%</span> <span class="pyg-n">os</span><span class="pyg-o">.</span><span class="pyg-n">path</span><span class="pyg-o">.</span><span class="pyg-n">basename</span><span class="pyg-p">(</span><span class="pyg-nb">str</span><span class="pyg-p">(</span><span class="pyg-n">attach</span><span class="pyg-p">[</span><span class="pyg-n">i</span><span class="pyg-p">])))</span>
				<span class="pyg-n">msg</span><span class="pyg-o">.</span><span class="pyg-n">attach</span><span class="pyg-p">(</span><span class="pyg-n">part</span><span class="pyg-p">)</span>
   <span class="pyg-k">except</span><span class="pyg-p">:</span>
		<span class="pyg-k">print</span> <span class="pyg-s">&quot; The attachments doesnt exist in the path </span><span class="pyg-si">%s</span><span class="pyg-s"> and </span><span class="pyg-si">%s</span><span class="pyg-s">&quot;</span> <span class="pyg-o">%</span> <span class="pyg-p">(</span><span class="pyg-n">attach</span><span class="pyg-p">[</span><span class="pyg-mi">0</span><span class="pyg-p">],</span><span class="pyg-n">attach</span><span class="pyg-p">[</span><span class="pyg-mi">1</span><span class="pyg-p">])</span>
			

   <span class="pyg-n">mailServer</span> <span class="pyg-o">=</span> <span class="pyg-n">smtplib</span><span class="pyg-o">.</span><span class="pyg-n">SMTP</span><span class="pyg-p">(</span><span class="pyg-s">&quot;smtp.gmail.com&quot;</span><span class="pyg-p">,</span> <span class="pyg-mi">587</span><span class="pyg-p">)</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">ehlo</span><span class="pyg-p">()</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">starttls</span><span class="pyg-p">()</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">ehlo</span><span class="pyg-p">()</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">login</span><span class="pyg-p">(</span><span class="pyg-n">gmail_user</span><span class="pyg-p">,</span> <span class="pyg-n">gmail_pwd</span><span class="pyg-p">)</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">sendmail</span><span class="pyg-p">(</span><span class="pyg-n">gmail_user</span><span class="pyg-p">,</span> <span class="pyg-n">to</span><span class="pyg-p">,</span> <span class="pyg-n">msg</span><span class="pyg-o">.</span><span class="pyg-n">as_string</span><span class="pyg-p">())</span>
   <span class="pyg-c"># Should be mailServer.quit(), but that crashes...</span>
   <span class="pyg-n">mailServer</span><span class="pyg-o">.</span><span class="pyg-n">close</span><span class="pyg-p">()</span>



<span class="pyg-k">for</span> <span class="pyg-n">to_mail_id</span> <span class="pyg-ow">in</span> <span class="pyg-p">(</span><span class="pyg-n">to_mail_ids</span><span class="pyg-p">):</span>
   <span class="pyg-n">mail</span><span class="pyg-p">(</span><span class="pyg-n">to_mail_id</span><span class="pyg-p">,</span>
   <span class="pyg-n">subject</span><span class="pyg-p">,</span>
   <span class="pyg-n">body</span><span class="pyg-p">,</span>
   <span class="pyg-n">attachements_path</span><span class="pyg-p">)</span>
   <span class="pyg-k">print</span> <span class="pyg-s">&quot;mail sent to :&quot;</span><span class="pyg-o">+</span><span class="pyg-n">to_mail_id</span>

<span class="pyg-k">print</span> <span class="pyg-s">&quot;</span><span class="pyg-se">\n</span><span class="pyg-s">mail sent successfully to all</span><span class="pyg-se">\n</span><span class="pyg-s">&quot;</span>
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