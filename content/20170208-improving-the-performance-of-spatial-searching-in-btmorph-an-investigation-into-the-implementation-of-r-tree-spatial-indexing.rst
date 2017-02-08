Improving the performance of spatial searching in BTMORPH: An investigation into the implementation of R-tree spatial indexing
##############################################################################################################################
:date: 2017-02-08 15:56:46
:author: Sam Sutton
:category: Seminars
:tags: BTMORPH, R-tree
:slug: improving-the-performance-of-spatial-searching-in-btmorph-an-investigation-into-the-implementation-of-r-tree-spatial-indexing
:summary: Sam Sutton's journal club session on improving BTMORPH's spatial querying capabilities.

In order to improve BTMORPH’s spatial querying capabilities, an implementation of Guttman’s (1984) R-tree and an investigation to determine the best parameters for performance was conducted. This presentation will discuss: 

- the precursory improvements to work flow
- the implementation of forest structures that were a necessary to the addition of spatial indexing into BTMORPH
- the effects on the R-tree of the parameter M
- the method of node splitting during R-tree construction
- the BTMORPH forest handling strategy

All of which were used to produce a 400% reduction in average search time on a 130,000 node search.


**Date:** 10/02/2017 |br|
**Time:** 16:00 |br|
**Location**: LB252

.. |br| raw:: html

    <br />
