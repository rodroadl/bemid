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
And clicking on the graph data points will highlight the points directly connected as well as filter the map data points (only if the point clicked is the sector dot in blue).  To update the data, edit the 'Company' tab of google sheet provided below.

[Bioscience Company Map and Graph](https://observablehq.com/d/a87ed5abd750078a)

 

### Data Source
[Google Sheet - Companies Sheet](https://docs.google.com/spreadsheets/d/1dIol4lwkCH--nbRmlacVVbiOhaW_OoCG-bKq1HX0cCQ)

