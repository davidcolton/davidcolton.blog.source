Author: David Colton
Date: 2020-03-04 19:45
Category: blogging
Tags: pelican, python, blogging
Title: Building My Blog With Pelican And Python 
Slug: building_my_blog

# Building My Blog With Pelican And Python

It's all [Erik O'Shaughnessy's](@JnyJny) fault. A little while ago he shared his tutorial [Run your blog on GitHub Pages with Python](https://opensource.com/article/19/5/run-your-blog-github-pages-python) on the [PyBites](@PyBites) Slack Channel. Creating my own blog is something that I had played around with before but never with much success. But hey I said, this looks easy, let's give it a go.

## Instant Results

Within minutes I had a blog running in Pelican. However, having been burned before, I immediately realised that I needed more targeted hand holding. I needed something that would accelerate my grasp of Pelican but at the same time offer a more long term sustainable architecture. Last thing I wanted, assuming that I keep this site active, is a single folder with 2000 random files with no structure. Enter [Matthew Devaney](https://matthewdevaney.com/)

## A More Advanced Recipe

Thanks to our friends at the worlds biggest search engine I'd quickly found a lot of what looked like really good tutorials that went beyond the basics that Erik's tutorial gave me. The two most promising I found were:

1. [Build A Blog With Pelican And Python](https://matthewdevaney.com/posts/2019/03/04/build-a-blog-with-pelican-and-python-pt-1-installation-theme/)
1. [How Do I Pelican?](https://pages.charlesreid1.com/how-do-i-pelican/)

But literally, there are so many other [great tutorials](https://www.google.com/search?q=pelican+tutorial+python&rlz=1C5CHFA_enGB861IE861&oq=pelican+tutorial) out there you should look yourself and find one that suits your learning style and your specific requirements.

I decided to go with Mathew's tutorial, the first in the list, mostly because it was broken down into multiple easily consumable articles, each focused on a single specific task. Also it suggested an initial project structure that I was happy I could maintain in the short to medium term. Happy days.

## A Quick Tour of the Highlights

Mathew's tutorial is broken down into six parts. I only followed four of them for reasons I'll come back to later.

### Installation And Theme

This is your basic _get things going_ steps including installing Pelican and Markdown, setting up an initial folder structure for your content and your output and configuring Pelican to understand this structure. Mathew also covered additional topics like installing a theme, internationalisation, plugins, setting up your social contact information and, importantly for me, how to setup a style for `code-blocks`. Job done. New initial Pelican setup complete.

### Content

In his next article, Mathew then spent some time introducing the reader to Marrdown. I've been using Markdown for years so I had no need for this. However, knowing that no two Markdown renderers work that same I used Mathew's sample Markdown to verify how Pelican / Python handled what I considered standard. To this end my first actual post to my blog was actual a summary of the main Markdown syntax. You can find my [First Post]({filename}/articles/20200223_markdown_examples.md) of this Markdown here.

There were other key points in this article which can't be over-looked. The Pelican `meta-data` is introduced. This is what tells Pelican about the articles and pages on your blog. Speaking of pages and articles these are both discussed and their differences explained. Finally the structure of your project is refactored to make it more sustainable, my favourite part, before details how to specify the generated structure of your static blog is explained. All in all, this second part of this article was essential for me and part of the reason I went with Mathew's tutorial.

### Deploying A Static Website To Github Pages

Now that I have the folder structure setup I'm ready to publish using Github, what initially attracted me most in Erik's post. This article goes through the steps to setup separate GitHub repositories one each for the source of the blog and one for the static generated content. Once this is done correctly it's a simple matter of follow the instructions Mathew gives and viola, you have a static HTML blog hosted on `github.io`.

One gotcha. Initially, after running the commands described a second time, I found that the Github files in the output folder structure had been deleted as as part of the process to regenerate the static HTML content. Quick search and the solution was found. The following line needs to be added to your `publishconf.py`:

    :::python
    DELETE_OUTPUT_DIRECTORY = False

The downside of this is that you may now have to manually clean up renamed files etc. More investigation is required but for now this got me over this hurdle.

### Disqus Comments With Pelican

The final task, for now, was to include the ability to add comments to the blog posts. Mathew to the rescue again. To quote directly from Mathew's article:

> You can implement comments on your website but the trick is to use a service that will host it for you. [Disqus](https://disqus.com/) is a popular solution to this problem.

Once again the instructions and steps to follow were really clear and simple to follow. Withing minutes I had added comments to my blog. One small thing I noticed was that one of the screen shots was slightly out of date. You now have to scroll down the page a little to get the free advertisement. Job done.

### Custom Domain and Google Analytics

For now, I haven't implemented a custom domain or add Google Analytics to my blog site. The Custom Domain option uses Google Domains which is not yet available in Ireland. One to come back to later. I didn't add Google Analytics because at the moment I have no need for this. If I suddenly started getting a ton loads of comments or even any traffic at all ;-) this is something I'll add again in the future.

## Summary

Not perfect but overall I'm happy with the results. There are some things that I know I'll need to add in the future and some things I'll need to revisit. 

1. I want to add support for Maths Symbols similar to the way Latex works
1. I want add an About Me Page and the Things to Do Page
1. I want to try to make regular posts, at least 1 a fortnight
1. I'm hearing great things about using `make` with Pelican. I need to investigate.

If you like this blog post or have any suggestions please leave a comment below.


