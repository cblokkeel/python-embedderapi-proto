# Data Readiness Levels: Turning Data from Palid to Vivid

Created: October 25, 2022 10:18 AM
Tags: DIGITAL, Data
URL: https://inverseprobability.com/2017/01/12/data-readiness-levels
Durée: 274

Application of models to data is fraught. You are faced with collaborators who sometimes have a very basic understanding of the complications of collating, processing and curating data. Challenges include: poor data collection practices, missing values, inconvenient storage mechanisms, intellectual property, security and privacy. All these aspects obstruct the sharing and interconnection of data.

All these problems arise before modeling even starts. Both questions and data are badly characterised. This is particularly true in the era of Big Data, where one gains the impression that the depth of data-discussion in many decision making forums is of the form “We have a Big Data problem, do you have a Big Data solution?”, “Yes, I have a Big Data solution.” Of course in practice it also turns out to be a solution that requires Big Money to pay for because in practice no one bothered to scope the nature of the problem, the data, or the solution.

![Data%20Readiness%20Levels%20Turning%20Data%20from%20Palid%20to%20V%200d1afed904c048b38a7fe9ec95a33486/Gandalf-TJ-drawing.jpg](Data%20Readiness%20Levels%20Turning%20Data%20from%20Palid%20to%20V%200d1afed904c048b38a7fe9ec95a33486/Gandalf-TJ-drawing.jpg)

Sortitouticus!

Data scientists and statisticians are often treated like magicians who wave a model across a disparate and carelessly collated set of data and with a cry of ‘sortitouticus’ a magical conclusion is drawn. In practice the sea of data we are faced with is normally undrinkable. The challenge of data desalination is very resource hungry and many projects fail to achieve their potential as a result.

For any data analyst, when embarking on a project, a particular challenge is assessing the quality of the available data. This difficulty can be compounded when project partners do not themselves have a deep understanding of the process of data analysis. If partners are not data-savy they may not understand just how much good practice needs to be placed in the curation of data to ensure that conclusions are robust and representative.

In one such meeting, while scoping a project with potential collaborators in the domain of health monitoring, it occurred to me that in most proposal documents, very scant attention is paid to these obstacles (other than ensuring a data-wizard is named on the project).

One difficulty is that the concept of “data”, for many people, is somehow abstract and disembodied. This seems to mean that it is challenging for us to reason about. Psychologists refer to the idea of *vivid* information as information that is weighted more heavily in reasoning than non-vivid or *pallid information*. In this sense data seems to be rendered *vivid* to be properly accounted for in planning.

A parallel thought occurred to me is that the idea of “technology” is also similarly disembodied, it is pallid information. Perhaps to deal with this challenge, in large scale projects, when deploying technology, we are nowadays guided to consider its *readiness stage*. The readiness of the technology is embodied in a set of numbers which describe its characteristics: is it lab tested only? Is it ready for commercialization? Is it merely conceptual? No doubt there are pros and cos of such readiness levels, but one of the pros is that the embodiment of the technological readiness pipeline ensures that some thought is given to that process. Technology is rendered more vivd even when it is still disembodied.

So it occurred to me that it would be very useful to have a scale to embody *data readiness*. This idea would allow analysts to encourage better consideration of the data collection/production and consolidation, with a set of simple questions, “And what will the data readiness level be at that point?”. Or “How will that have progressed the data readiness?”. Or to make statements, “we’ll be unable to deliver on that integration unless the data readiness level is at least B3.”.

It turns out, that like all (potential) good ideas, I’m not the first there. However, this [discussion document from the nanotechnology community in 2013](http://www.nano.gov/node/1015) is not general enough to give me what we need (it seems very domain specific, it has an obsession with units which would often be inappropriate).

So I’d like to start a discussion in the statistics and data science communities by proposing some rough levels of data readiness.

My first proposal is that data readiness should be split into three *bands*. Each band being represented by a letter, A, B and C. These bands reflect stages of data readiness which would each likely have some sub-levels, so the best data would be A1 and the worst data might be C4. But I don’t want to get fine grained too early (I think that’s the error of the nanotechnologists above. So allow me to propose the bands as follows.

## Band C

![Data%20Readiness%20Levels%20Turning%20Data%20from%20Palid%20to%20V%200d1afed904c048b38a7fe9ec95a33486/stature-935643_1920.jpg](Data%20Readiness%20Levels%20Turning%20Data%20from%20Palid%20to%20V%200d1afed904c048b38a7fe9ec95a33486/stature-935643_1920.jpg)

Band C is about the accessibility of a data set. The lowest level of Band C (let’s label it as C4) would represent a belief that the data may exist, but its existence isn’t even verified. Signs that data is C4 might include statements like “The sales department should have a record of that.” Or “The data should be available because we stipulated it in the software requirements.” We might think of it as hearsay data. Data that you’ve heard about so you say it’s there. Problems with hearsay data might include

- whether it really is being recorded
- the format in which it’s being recorded (e.g. handwritten log book, stored in PDF format or old machine formats)
- privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
- limitations on access due to topology (e.g. it’s distributed across a number of devices)

Data which arrives at C1 would have all these considerations fulfilled. When data arrives at C1 it’s ready tobe loaded into analysis software. It is machine readable and ethical procedures for data handling have been addressed. Bringing data to C1 is often a significant effort itself involving many lines of bespoke software and human understanding of systems and ethics.

## Band B

Band B is about the faithfulness and representation of the data. Now that it’s loaded into the software, is what is recorded matching what is purported to be recorded? How are missing values handled, what is there encoding? What is the noise characterization (for sensors) or for manual data are there data entry errors? This stage contains considerable aspects of exploratory data analysis. Visualizations of the data should be carried out to help render the data vivid and to ensure decision makers, who may not be data aware, can become involved in the analysis process and are given an understanding of any limitations of the data set.

As part of Band B the characteristics of the collection process should also be verified, was data collection randomized, is it biased in any particular way?

Other things to watch for at this stage include:

1. 
    
    If the data has been agglomerated at some point (for example, for privacy) how were missing values dealt with before agglomeration? If they weren’t dealt with then that entire section of the data may be invalidated
    
2. 
    
    If the data has been through a spreadsheet software, can you confirm that no common spreadsheet analysis errors were made? For example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?
    

By the end of Band B, when data is B1, a broad idea of data limitations in the data should be present in the experts mind. Data at C4 was hearsay data, someone heard the data existed and they said what they thought it might be good for. At B1 the analyst knows how faithful the data is to that description.

## Band A

Band A is about data in context. It is at Band A that we consider the appropriateness of a given data set to answer a particular question or to be subject to a particular analysis. This context could be “Can this data be used to predict a user preference?” or “Can we use this data to prove the efficacy of a drug?” or “Does this data verify the functioning of our rocket engine?”. Data in A1 condition is ready to be deployed in the context given. Use of the appropriate methodology in combination with the data will give us the answer we are looking for. In the case of a classical statistical study the experimental design is normally set up with the expectation of the idea that at the end of data collection data will *already* be in A1 condition. However, in the modern data science era, establishing this condition may involve

- active collection of new data.
- annotation of data by human experts
- revisiting the collection (and running through the appropriate stages again)

Data in context may also require further ethical approvals or considerations.

## The Analysis Pipeline

A common mistake in data analysis is to not acknowledge the different processes above. This mistake occurs often because an understanding of the data collection process is often missing. The analyst also needs to be intimately familiar with the collection process so that any biases in data collection can be understood. This understanding develops in B and C with corrective actions being taken in Band A as part of analyzing the data in context.

Of course, some data sets consist of different sub-sets of data. Each of these sub-sets may require it’s own pipeline of analysis. Just as a lot of modern technology relies on integrating older technology. A particular difference is that many data sets would revert to B1 status when the context of their usage was changed, even if they had been refined to A1 many times in the past.

## Potential Results

The idea of these levels is to increase the accountability of the process and allow the nature of the data to be better embodied. With data readiness levels in place you can now imagine conversations that would include statements like the following:

> 
> 
> 
> Be careful, that department claims to have made 10,000 data sets available, but we estimate that only 25% of those data sets are available at C1 readiness.
> 

> 
> 
> 
> The cost of bringing the data to C1 would be prohibitive for this study alone, but the company-wide data audit is targeting this data to be C1 by Q3 2017 which means we can go ahead and recruit the statisticians we need.
> 

> 
> 
> 
> The project failed because we over recruited statistical expertise and then deployed them on bringing the daa set to C1 readiness, a job that would have been better done by building up our software engineering resource.
> 

> 
> 
> 
> What’s the data readiness level? My team will be ineffectual until it’s B1 and at the moment I see no provision in the plan for resource to bring it there.
> 

> 
> 
> 
> We estimate that it’s a $100,000 dollar cost to bring that data to B1, but we can amortize that cost across four further studies that also need this data.
> 

> 
> 
> 
> I gave them the data readiness levels to go through and they realized they hadn’t yet got the necessary ethics approval for sharing the zip codes. We’ll revisit when they’ve got through that and can asure us they can share a C1 set.
> 

> 
> 
> 
> While their knowledge of the latest methodologies wasn’t as good as I’d hoped, the candidate had a lot of experience of bringing data from C1 to B1, and that’s a skill set that we’re in dire need of.
> 

> 
> 
> 
> The project came in under budget because they found a team with experience of getting a closely related data set to A1. Many of the associated challenges were the same and they could even reuse some of that team’s statistical models.
> 

I didn’t get into data analysis to do project management, but I can’t escape the impression that many of our failings in large data projects are associated with a failure to provision resource for the challenges involved in preparing our data. These costs are often underestimated and those who do the work in Band C and Band B are very often undervalued. This is the work at the pithead of data mining. Some consensus about such levels would help organisations (and their managers, accountants) quantify some of the value associated with data and allocate resource correctly to developing data sets that are robust and representative. Well conducted data analyses can save lives, so by the same token badly conducted analysis don’t just waste resources but they miss life saving opportunities.

## Debate

These are just ideas, and for DRLs to work there needs to be consensus. Would love to see a debate around these thoughts and whether they’d be effective in practice.

## Also on **inverseprobability.com**