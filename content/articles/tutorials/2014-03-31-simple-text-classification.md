Title: Simple text classification in Python
Date: 2014-03-31 20:33
Category: tutorials
Tags: pelican, ipython, notebook, scikit-learn, text analysis
Slug: simple-text-classification
Author: Rebecca Weiss
Summary: Demonstrating text classification in Python.

In this post, I'm (selfishly) testing the integration between pelican and `IPython` notebooks.

I've been meaning to do this for awhile, since I have quite a few `R` and `Python` tutorials on a variety of subjects written up as `IPython` notebooks, my distribution platform of choice.

I was having trouble getting the `pelican-bootstrap3` theme to play nicely with the `liquid-tags` pelican plugin.  I have to give a hat-tip to [Kyle Cranmer][cranmer] who posted his [solution][cranmerhack] (involves chopping up the `_nb_header.html` and creating a `_nb_header_minimal.html`, which is referred to in your `pelicanconf.py` as `EXTRA_HEADER` instead).  

It's crazy to see someone else with a similar workflow!  I only discovered his work since I was having *the worst time ever* trying to get pelican to play nicely with notebooks.

His hack does the job, and now the notebooks are more nicely styled than without the additional css, but it makes me feel a little leery since it has the feel of something that will break with an update.  That's what you get when you use open-source projects.

So here is one of the notebooks from a workshop I gave at [Mozfest][mozfest] in 2013, the entirety of which is available [here][mozfest2013].  I *probably* ought to rewrite this as a proper blog post, since there's a lot of room for improvement.

* * *

{% notebook Python_classification.ipynb %}

[mozfest]: http://www.mozillafestival.org
[mozfest2013]: http://rjweiss.github.io/mozfest2013/
[cranmer]: http://theoryandpractice.org/
[cranmerhack]: http://theoryandpractice.org/2014/03/Testing-Pelican-Migration/