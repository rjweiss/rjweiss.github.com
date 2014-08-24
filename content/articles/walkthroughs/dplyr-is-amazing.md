Title: `dplyr` is amazing
Slug: dplyr-is-amazing
Category: Walkthroughs
<!-- Status: draft -->
Date: 2014-05-10 15:30


Everyone's jumping on the big data train.  For `R` users, "Big Data" usually refers to dimensionality: lots of rows, lots of columns.  The sad reality of base `R` is that it wasn't really designed for data of that scale.  Luckily, there are lots of people working on making `R` more capable of handling larger data sets.

I've been meaning to test out `dply` against `plyr` for some time now.  Here's a short walkthrough of my early explorations.

## The data
I've been working a lot with broadcast media data.  One of my projects involves exploring the daily and weekly distribution of time spent on various topics and issues covered by news media.  

So let's say I have been estimating the proportion of 

Here's an example of what this data looks like:

```r
head(data_meta)
```

```
##                                 X_id channel                          show
## 2 ObjectID(53514f1518d183146e0297df)    WBAL                 11_News_at_11
## 3 ObjectID(53514f1518d183146e0297e0)     KGO ABC_News_Good_Morning_America
## 4 ObjectID(53514f1518d183146e0297e1)   CSPAN                C-SPAN_Weekend
## 5 ObjectID(53514f1518d183146e0297e2)    CNNW                  CNN_Newsroom
## 6 ObjectID(53514f1518d183146e0297e3)    WETA                  Charlie_Rose
## 7 ObjectID(53514f1518d183146e0297e4)    WUSA              9News_Now_at_5am
##         date               travel              weather
## 2 2012-12-18                    0  0.24538968568110764
## 3 2013-07-20   0.1278605873919483 0.022781254955870685
## 4 2009-10-04 0.016729502805801842  0.01535445055974056
## 5 2013-05-01 0.050835327865678688                    0
## 6 2009-09-08                    0                    0
## 7 2012-05-30                    0  0.73114682970368883
##              courtcase              spanish        entertainment
## 2                    0                    0                    0
## 3  0.11708132091946018                    0 0.084127564947818062
## 4 0.014249124150100946 0.012178693872352059 0.028658802987892217
## 5                    0                    0                    0
## 6                    0                    0                    0
## 7                    0 0.024926795827934899                    0
##                anchors       international commercial (pharmaceuticals)
## 2                    0                   0                            0
## 3 0.053211951186896055                   0                            0
## 4 0.011049798871040071 0.51276068588080359         0.013694404795273802
## 5  0.28482916006481529                   0         0.090046909604937622
## 6                    0 0.14220227621188578                            0
## 7                    0                   0                            0
##                 sports                 food             disaster congress
## 2 0.051181164774435128                    0                    0        0
## 3 0.010236471895859771  0.42907115788935529 0.023480680939842322        0
## 4  0.01643453479315584 0.025048814439873255 0.016534022586565122        0
## 5                    0                    0                    0        0
## 6                    0                    0                    0        0
## 7                    0 0.023709207139960893                    0        0
##          international             election       international
## 2                    0                    0                   0
## 3                    0                    0                   0
## 4 0.020215145925370593 0.020380596933545568 0.01981606477389786
## 5                    0                    0                   0
## 6                    0                    0 0.64879509574938443
## 7                    0                    0                   0
##               congress              holiday               sports
## 2                    0  0.15938748235923789  0.12928395775625715
## 3                    0                    0 0.036021633565328566
## 4 0.021363046781977948 0.019380246931825981 0.023768516036536447
## 5                    0                    0                    0
## 6                    0                    0                    0
## 7 0.011866120100390988                    0 0.075958347079646174
##   commercial (healthcare)               noise                 guns
## 2                       0                   0  0.30624569555502507
## 3                       0                   0                    0
## 4    0.010302204760063252                   0 0.015419699258861708
## 5                       0                   0                    0
## 6                       0 0.20433971873521387                    0
## 7                       0                   0                    0
##              terrorism         gay marriage commericial (pharmaceuticals)
## 2                    0                    0                             0
## 3                    0                    0                             0
## 4 0.016154696635270641 0.014975569350437378           0.01272488145340281
## 5  0.50158505789980889                    0          0.033029030438272634
## 6                    0                    0                             0
## 7                    0 0.015530416954335324                             0
##              obamacare            campaigns             business
## 2                    0                    0                    0
## 3                    0                    0                    0
## 4 0.014950090339991593 0.013738158393050247 0.020096873662985959
## 5                    0                    0                    0
## 6                    0                    0                    0
## 7                    0 0.030038991037657305  0.03613208959912452
##                  local             congress              scandal
## 2 0.072404016072238328 0.032011391184895738                    0
## 3 0.035592987943989775                    0 0.053572183274267625
## 4 0.011747443301002086 0.021154305473626393 0.024581689768446522
## 5                    0                    0 0.038273122763922508
## 6                    0                    0                    0
## 7                    0                    0 0.037360094596050157
```


If I want to compute daily or weekly averages of the topic probability per show and per topic, I have to create a number of groupings according to those dimensions.  This is a classic split-apply-combine problem.  

To do weekly averages, this also requires a bit of date handling.  Luckily, `lubridate` makes this pretty easy (and I've [written about `lubridate` before]()).  What's the time period that I'm evaluating?

```r
start = min(data_meta$date)
end = max(data_meta$date)
start
```

```
## [1] "2009-06-04 UTC"
```

```r
end
```

```
## [1] "2014-03-25 UTC"
```


How many days am I working with?

```r
end - start
```

```
## Time difference of 1755 days
```


How many weeks?

```r
round((end - start)/eweeks(1))
```

```
## [1] 251
```


Say I want to see a weekly average, but I want this to be over the full multi-year period.  I'm going to create a new dimension that consists of a week index over this time period, and then I'm going to transform this data from wide to long format.

```r
data_meta$week = round((data_meta$date - min(data_meta$date))/eweeks(1))
data_meta$date = NULL  # I'm going to melt this data and I don't want date in the way.
melted_data = melt(data_meta, id.vars = c("X_id", "channel", "show", "week"))
```

```
## Warning: attributes are not identical across measure variables; they will
## be dropped
```

```r
dim(melted_data)
```

```
## [1] 10109525        6
```


## Creating a weekly average

Again, this is a split-apply-combine problem.  I want to split this data into each topic, each channel, and each week.  For each of these subsets, I want to compute the average topic probability for each show's text that I've got.  

`plyr` was the canonical tool to turn to for split-apply-combine problems in `R`, and computing summary data within that analytical context is pretty textbook:

```r
melted_data_total = ddply(melted_data, .(variable, channel, week), summarise, 
    value = mean(as.numeric(value), na.rm = T))
```


And this results in a weekly average of coverage per topic, such as the following:

```r
dim(melted_data_total)
```

```
## [1] 180225      4
```

```r
head(melted_data_total)
```

```
##   variable channel week   value
## 1   travel ALJAZAM  220 0.01298
## 2   travel ALJAZAM  221 0.02217
## 3   travel ALJAZAM  222 0.01152
## 4   travel ALJAZAM  223 0.01883
## 5   travel ALJAZAM  224 0.02175
## 6   travel ALJAZAM  225 0.02471
```


The problem is that this takes quite a bit of time to execute:

```r
ddply_time = system.time(ddply(melted_data, .(variable, channel, week), summarise, 
    value = mean(as.numeric(value), na.rm = T)))
print(ddply_time)
```

```
##    user  system elapsed 
##   435.2   255.0   690.2
```


This is a relatively small set of data compared to the real world. 400k observations is pretty reasonable and the scale of really Big Data, I can easily imagine wanting to explore millions of observations.

`plyr` is wonderful, but one of the problems with this package (and with base `R` in general) is that it wasn't originally designed to scale to data of this size.  Nothing prevents you from running this `ddply` command, but what if you goofed in your selection of group-by variables?  For example, maybe I chose channel, but actually I meant show?  

It's completely reasonable to expect to have to iterate several times on a query to get the right subset and representation of your data.  And if a function takes minutes to hours to execute, it will slow down your workflow dramatically.

[Enter `dplyr`](http://blog.rstudio.org/2014/01/17/introducing-dplyr/).  I don't really want to go into the implementation details (and besides, you can always just [review the source code](https://github.com/hadley/dplyr) if you really are curious).  There are really only a few things you need to know:

1. If you are working with tabular data (or can think of your data as a `data.frame`), `dplyr` is for you
2. If you are frustrated with how slow it is to do split-apply-combine problems on your data with `ddply`, `dplyr` is for you
3. If you are working with data that is stored in a tabular format-supporting database (e.g. SQL), `dplyr` is for you.

There are other tools out there for big `data.frames`, such as `data.table`, but I specifically wanted to do a head-to-head comparison of `dplyr` and `ddply`.  I like living in Wickham world.  One of my criticisms of `R` is that the community supports too many philosophies regarding how `R` packages should work, how syntax should be structured, and what kind of objects a package should create.  For me, `R` is about `data.frames`, and the Hadley world just feels like it's been more carefully considered.

## Get to the point.  How much faster is `dplyr`?

Working with `dplyr` is pretty easy.  There's an operator `%.%` that allows for function chaining, which means that performing a split-apply-combine can be considered much in the same structure as `ddply`:

```r
melted_data_dplyr = melted_data %.% group_by(variable, channel, week) %.% summarise(value = mean(as.numeric(value), 
    na.rm = T))

class(melted_data_dplyr)
```

```
## [1] "data.frame"
```


You can treat the resulting object like a `data.frame` and call functions like `head` on it:

```r
head(melted_data_dplyr)
```

```
##     value
## 1 0.03143
```


We get the same results as with `ddply`.  So how much faster was the `dplyr` approach?

```r
dplyr_time = system.time(melted_data %.% group_by(variable, channel, week) %.% 
    summarise(value = mean(as.numeric(value), na.rm = T)))
print(dplyr_time)
```

```
##    user  system elapsed 
##   3.673   0.227   3.901
```


That's a pretty substantial increase in efficiency: from minutes to seconds.

```r
ddply_time/dplyr_time
```

```
##    user  system elapsed 
##   118.5  1123.4   176.9
```


That's about a 14-fold increase in efficiency.  Does this performance hold as data size increases?  Instead of a weekly average, let's try computing a daily average.  Going from 52 weeks to 365 days a year is about a 7-fold increase in data size, do we see a 7-fold increase in the execution time?

```r
data_meta = cbind(meta, data)
melted_data = melt(data_meta, id.vars = c("X_id", "channel", "show", "date"))
```

```
## Warning: attributes are not identical across measure variables; they will
## be dropped
```

```r

dplyr_time_daily = system.time(melted_data %.% group_by(variable, channel, date) %.% 
    summarise(value = mean(as.numeric(value), na.rm = T)))

melted_data_dplyr = melted_data %.% group_by(variable, channel, date) %.% summarise(value = mean(as.numeric(value), 
    na.rm = T))

dplyr_time_daily/dplyr_time
```

```
##    user  system elapsed 
##   2.303   1.692   2.268
```


Looks like we see about a 4x increase in execution time going from weeks to days.  What's the dimensionality of these `data.frame`s and how long did it take to perform this `summarise`?

```r
dim(melted_data)
```

```
## [1] 10109525        6
```

```r
tbl_df(melted_data_dplyr)
```

```
## Source: local data frame [1 x 1]
## 
##     value
## 1 0.03143
```

```r
dplyr_time_daily
```

```
##    user  system elapsed 
##   8.460   0.384   8.848
```


About 22 seconds to work with over a million observations.  How long would this have taken with `ddply`?

```r
ddply_time_daily = system.time(ddply(melted_data, .(variable, channel, date), 
    summarise, value = mean(as.numeric(value), na.rm = T)))
ddply_time_daily
```

```
##    user  system elapsed 
##    2913    1608    4521
```


That's quite a bit longer in actual time; what is the rate of improvement?

```r
ddply_time_daily/dplyr_time_daily
```

```
##    user  system elapsed 
##   344.3  4187.5   511.0
```


Now we see about a 23-fold improvement using `dplyr` over `ddply`.  But because the data was in the scale of millions of rows, this means I had to wait about 8.5 minutes for the `ddply` transform to complete, whereas the `dplyr` version only took 20 seconds.  That means if I borked my initial transformation, I could probably try a few more versions of the same split-apply-combine approach in the amount of time it took to see a single result from `ddply`.

Additionally, it looks like the execution time of `ddply` more closely scales with the increase in observations.


```r
# ddply_time_daily/ddply_time
```


## In summary...

`dplyr` is amazing.  This will dramatically increase my productivity with `R`.  I don't think I'll ever use `ddply` again.  I also prefer the expressiveness of the `%.%` operator (though I am honestly starting to grow a little concerned with all the operator overloading in the Wickham world of `R`).

### Version information

```r
sessionInfo()
```

```
## R version 3.1.0 (2014-04-10)
## Platform: x86_64-apple-darwin10.8.0 (64-bit)
## 
## locale:
## [1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8
## 
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base     
## 
## other attached packages:
## [1] reshape2_1.4    lubridate_1.3.3 ggplot2_0.9.3.1 plyr_1.8.1     
## [5] dplyr_0.1.3     knitr_1.5      
## 
## loaded via a namespace (and not attached):
##  [1] assertthat_0.1   colorspace_1.2-4 digest_0.6.4     evaluate_0.5.5  
##  [5] formatR_0.10     grid_3.1.0       gtable_0.1.2     MASS_7.3-31     
##  [9] memoise_0.2.1    munsell_0.4.2    proto_0.3-10     Rcpp_0.11.1     
## [13] scales_0.2.4     stringr_0.6.2    tools_3.1.0
```


