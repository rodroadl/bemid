# Related work
- [Search for Maine schools](https://neo.maine.gov/DOE/neo/Supersearch/ContactSearch/SearchForMaineSchools)
  - finicky
- [facilities map](https://gmri.org/projects/facilities-resource-map/)
  - research institute
  - support map/filter/sort
- [jobsplan dashboard](https://maine.gov/jobsplan/dashboard)
  - jobs plan investement dashboard
  - the one I, James, was talking about
  - map/filter/sort
- [BIOME](https://biomaine.org/member-directory/)
  - not a dashboard
  - Trade organization for biosciences in the state -- membership driven
  - Good for identifying a cohort of companies for plotting
- [EMSTAR](https://www.lifesciencesmaine.com/about)
  - Midcoast group -- beginning to organize things
  - Information underneath the names is more relevant for filtering, etc.
* [Aileen's site](https://teel.sites.northeastern.edu/life-sciences-in-maine/) in early stages
* Would like a GUI for intellectual capital rather than just brick and mortar (which is what's there now)
* Dataviz ideas
  * [Force-directed graph](https://observablehq.com/@d3/force-directed-graph?collection=@d3/d3-drag)
  * [Obama budget](https://archive.nytimes.com/www.nytimes.com/interactive/2012/02/13/us/politics/2013-budget-proposal-graphic.html)
  * [Divisibility network](https://observablehq.com/@mbostock/divisibility-network)
  
# Bioscience in Maine
The Bioscience Dashboard found at https://cs7290.github.io/bioscience/ presents three interactive visualizations: a Study Roadmap, an Academic Collapsible Tree, and a Business Network diagram.  Each of these visualizations have been built using Observable notebooks.  While not all data sets used come from real sources, the visualizations can be updated within Observable so long as the format of the data is consistent with the current structure.  Links to our notebooks as well as data sources for each visualization are provided below.

## Study Roadmap
### Observable Notebooks
Each of the following notebooks are linked and utilize eachother.  The data source is loaded within the ***Data for BioScience*** notebook and imported to the other notebooks.  To update the data, attach new data within the ***Data for BioScience*** notebook, update the cell under the "Data" header, and ensure the import cells within the ***Cirriculum Path*** and ***Bioscience Map*** notebooks are updated with the new source.  

[Bio Science - Curriculum Path - v5](https://observablehq.com/@cs7290/bio-science-curriculum-path-v5)

∟[Bioscience Map of Maine - v2](https://observablehq.com/@cs7290/bioscience-map-of-maine-v2)

∟[Data for BioScience](https://observablehq.com/@cs7290/data-for-bioscience)

### Data Source:
[bioscience_input_0.11](https://docs.google.com/spreadsheets/d/1dIol4lwkCH--nbRmlacVVbiOhaW_OoCG-bKq1HX0cCQ/edit?usp=sharing)

Above data is dummy data to make the prototype, as long as data follows such format, it is replaceble.

Below is schema for the dummy data:

![schema](https://github.com/cs7290/bioscience/blob/main/imgs/image.png)

## Academic Collapsible Tree
### Observable Notebook
To update the data, create a new google sheet following the format of the current sheet attached below.  In the Bioscience: Collapsible Tree notebook, update the link used within the getTsvUrl cell under the "Appendix 1: Data Import" header.  

[Bioscience: Collapsible Tree](https://observablehq.com/@aaronfihn/bioscience-collapsible-tree-1-0-0)

### Data Source:
[Google Sheet 2](https://docs.google.com/spreadsheets/d/1X8SNuN75ASXs34Opg2vUDFGSSsaviK9oXn0tYE-ppKo/edit?usp=sharing)


## Business Network 
### Observable Notebook
The map on the left is connected to the force-directed graph on the right 2-way. 
Clicking on the map data points can update the graph.
And clicking on the graph data points will highlight the points directly connected as well as filter the map data points (only if the point clicked is the sector dot in blue).  

[Bioscience Company Map and Graph](https://observablehq.com/d/a87ed5abd750078a)

 

### Data Source
[Google Sheet - Companies Sheet](https://docs.google.com/spreadsheets/d/1dIol4lwkCH--nbRmlacVVbiOhaW_OoCG-bKq1HX0cCQ)

