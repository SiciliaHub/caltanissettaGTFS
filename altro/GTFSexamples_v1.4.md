**About**

This document shows examples of [*General Transit Feed Specification
(GTFS)*](https://developers.google.com/transit/gtfs/reference) data to
illustrate how the Specification can be used to describe various
configurations of transit service. Various schedule and fare
configurations are presented. In many cases, there can be multiple ways
of presenting the same transit service, and these examples aim to
illustrate some of those approach options. Feel free to add comments to
this document with questions or suggestions. Request edit permissions if
you would like to add examples or make enhancements to the document.

A Chinese-translated version of version 1.2 of this document is
available from the World Bank’s [*link repository for international GTFS
training
materials*](https://github.com/WorldBank-Transport/GTFS-Training-Materials/wiki/Link-repository-for-international-GTFS-training-materials).

***Document versions***

-   **1.41** (7-July-2016) Add World Bank’s link repository for international GTFS training materials

-   **1.4** (10-January-2016) Change background link from Appropedia to TransitWiki; added example 11 with linked dataset

-   **1.3** (30-October-2014): Add “Background / Overview of the Specification” section to the document

-   **1.2** (1-Dec-2013): Add example 4, which shows multiple records in frequencies.txt associated with one trip\_id.

**Table of contents**

### Background / Overview of the Specification

-   TransitWiki provides a approachable and complete [*background on GTFS*](http://www.transitwiki.org/TransitWiki/index.php?title=General_Transit_Feed_Specification).

-   GTFS datasets consist of multiple spreadsheet-like files, in a comma-separated values (CSV) format. Understanding these examples, and GTFS, requires understanding the basic definition of a CSV file (see Wikipedia, [*“Comma-separated values”*](http://en.wikipedia.org/wiki/Comma-separated_values#Example))

-   The CSV files in a GTFS dataset are “relational”. This means that multiple files contain related information, stored as tables of rows (records) and columns (fields), and allowing a link to be established between separate files that have a matching field ([*relational database definition*](http://dictionary.reference.com/browse/relational+database)).

-   While not required to understand these examples, we recommend at least skimming the [*“General Transit Feed Specification” definition document*](https://developers.google.com/transit/gtfs/reference).

![](./myMediaFolder/media/image2.png){width="5.708333333333333in"
height="4.916666666666667in"}

(Data model of the GTFS file format, created by Martin Davis, as per
blog post
[*http://lin-ear-th-inking.blogspot.com.au/2011/09/data-model-diagrams-for-gtfs.html*](http://lin-ear-th-inking.blogspot.com.au/2011/09/data-model-diagrams-for-gtfs.html).)

###

###

### Example 1: relationships between files to define schedules.

Schedules defined using stop\_times.txt without frequencies.txt. Only
winter weekday service is defined.

Two round-trips occur between downtown and the airport every weekday,
also stopping at the railway station.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                           

|**service\_id**|**start\_date**|**end\_date**|**monday**|**tuesday**|**wednesday**|**thursday**|**friday**|**saturday**|**sunday**|
|---|---|
|winter\_weekday|20130921|20140619|1|1|1|1|1|0|0|

 **routes.txt**

|**route\_id**|**route\_short\_name**|**route\_long\_name**|**route\_type**|
|---|---|
|route\_1|1|Downtown/Airport|3|

  **trips.txt**                                                         

|**trip\_id**|**route\_id**|**service\_id**|**direction\_id**|**trip\_headsign**|
|---|---|
|trip\_1|route\_1|winter\_weekday|0|Airport|
|trip\_2|route\_1|winter\_weekday|1|Downtown|
|trip\_3|route\_1|winter\_weekday|0|Airport|
|trip\_4|route\_1|winter\_weekday|1|Downtown\|

  **stops.txt**                                      

|**stop\_id**|**stop\_name**|**stop\_lat**|**stop\_lon**|
|---|---|---|---|
|stop\_1|Main and 1st St.|28.8|115.9|
|stop\_2|Railway Station|28.9|116|
|stop\_3|Airport|29|116.1|

  **stop\_times.txt**                                                           

|**trip\_id**|**stop\_sequence**|**stop\_id**|**arrival\_time**|**departure\_time**|
|---|---|---|---|---|
|trip\_1|1|stop\_1|9:00:00|9:00:00|
|trip\_1|2|stop\_2|9:10:00|9:10:00|
|trip\_1|3|stop\_3|9:30:00|9:30:00|
|trip\_2|1|stop\_3|9:30:00|9:30:00|
|trip\_2|2|stop\_2|9:50:00|9:50:00|
|trip\_2|3|stop\_1|10:00:00|10:00:00|
|trip\_3|1|stop\_1|10:00:00|10:00:00|
|trip\_3|2|stop\_2|10:10:00|10:10:00|
|trip\_3|3|stop\_3|10:30:00|10:30:00|
|trip\_4|1|stop\_3|10:30:00|10:30:00|
|trip\_4|2|stop\_2|10:50:00|10:50:00|
|trip\_4|3|stop\_1|11:00:00|11:00:00|

 -- -- -- --




  -- -- -- --

### Example 2: using calendar.txt to define seasonal schedules.

Schedules defined using stop\_times.txt only (no frequencies.txt). Only
winter weekday, and summer service (Tuesdays and Thursdays only) is
defined. Two-round trips per day occur in the winter. There is one
round-trip in the summer, with shorter travel time. Data is color-coded
according to seasonal schedules (service\_id).

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                                      
  ----------------------------- ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**               **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday               20160921          20170619        1            1             1               1              1            0              0
  summer\_tuesdays\_thursdays   20170620          20170920        0            1             0               1              0            0              0

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Downtown/Airport        3

  **trips.txt**                                                                     
  --------------- --------------- ----------------------------- ------------------- --------------------
  **trip\_id**    **route\_id**   **service\_id**               **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday               0                   Airport
  trip\_2         route\_1        winter\_weekday               1                   Downtown
  trip\_3         route\_1        winter\_weekday               0                   Airport
  trip\_4         route\_1        winter\_weekday               1                   Downtown
  trip\_5         route\_1        summer\_tuesdays\_thursdays   0                   Airport
  trip\_6         route\_1        summer\_tuesdays\_thursdays   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        9:00:00             9:00:00
  trip\_1               2                    stop\_2        9:10:00             9:10:00
  trip\_1               3                    stop\_3        9:30:00             9:30:00
  trip\_2               1                    stop\_3        9:30:00             9:30:00
  trip\_2               2                    stop\_2        9:50:00             9:50:00
  trip\_2               3                    stop\_1        10:00:00            10:00:00
  trip\_3               1                    stop\_1        10:00:00            10:00:00
  trip\_3               2                    stop\_2        10:10:00            10:10:00
  trip\_3               3                    stop\_3        10:30:00            10:30:00
  trip\_4               1                    stop\_3        10:30:00            10:30:00
  trip\_4               2                    stop\_2        10:50:00            10:50:00
  trip\_4               3                    stop\_1        11:00:00            11:00:00
  trip\_5               1                    stop\_1        9:00:00             9:00:00
  trip\_5               2                    stop\_2        9:08:00             9:08:00
  trip\_5               3                    stop\_3        9:20:00             9:20:00
  trip\_6               1                    stop\_3        9:20:00             9:20:00
  trip\_6               2                    stop\_2        9:32:00             9:32:00
  trip\_6               3                    stop\_1        9:40:00             9:40:00

### Example 3: using frequencies.txt with stop\_times.txt

Route 1 runs every 1 hour from 9:00 to 11:00 on winter weekdays. With
frequencies.txt, service periods defined in frequencies.txt override
specific departure\_time and arrival\_time values. Travel intervals are
provided by stop\_times.txt. The service defined here is the same as
what is defined in Example 2. Both options are correct GTFS and will be
readable by GTFS applications.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                                      
  ----------------------------- ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**               **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday               20130921          20140619        1            1             1               1              1            0              0
  summer\_tuesdays\_thursdays   20130620          20130920        0            1             0               1              0            0              0

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Downtown/Airport        3

  **trips.txt**                                                                     
  --------------- --------------- ----------------------------- ------------------- --------------------
  **trip\_id**    **route\_id**   **service\_id**               **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday               0                   Airport
  trip\_2         route\_1        winter\_weekday               1                   Downtown
  trip\_3         route\_1        summer\_tuesdays\_thursdays   0                   Airport
  trip\_4         route\_1        summer\_tuesdays\_thursdays   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        0:00:00             0:00:00
  trip\_1               2                    stop\_2        0:10:00             0:10:00
  trip\_1               3                    stop\_3        0:30:00             0:30:00
  trip\_2               1                    stop\_3        0:00:00             0:00:00
  trip\_2               2                    stop\_2        0:20:00             0:20:00
  trip\_2               3                    stop\_1        0:30:00             0:30:00
  trip\_3               1                    stop\_1        9:00:00             9:00:00
  trip\_3               2                    stop\_2        9:08:00             9:08:00
  trip\_3               3                    stop\_3        9:20:00             9:20:00
  trip\_4               1                    stop\_3        9:20:00             9:20:00
  trip\_4               2                    stop\_2        9:32:00             9:32:00
  trip\_4               3                    stop\_1        9:40:00             9:40:00

  **frequencies.txt**                                         
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**   **end\_time**
  trip\_1               3600                9:00:00           10:00:00
  trip\_2               3600                9:30:00           10:30:00

### Example 4: another look at frequencies.txt; headways intervals vary throughout the day.

Route 1 operates service in both directions with 5 minute average
headways from 7:00 to 12:00. From 12:00 to 22:00, Route 1 operates with
10 minute average headways.

Colors match trips\_ids.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                           
  ------------------ ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**    **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday    20130921          20140619        1            1             1               1              1            0              0

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Downtown/Airport        3

  **trips.txt**                                                         
  --------------- --------------- ----------------- ------------------- --------------------
  **trip\_id**    **route\_id**   **service\_id**   **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday   0                   Airport
  trip\_2         route\_1        winter\_weekday   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        0:00:00             0:00:00
  trip\_1               2                    stop\_2        0:10:00             0:10:00
  trip\_1               3                    stop\_3        0:30:00             0:30:00
  trip\_2               1                    stop\_3        0:00:00             0:00:00
  trip\_2               2                    stop\_2        0:10:00             0:10:00
  trip\_2               3                    stop\_1        0:30:00             0:30:00

  **frequencies.txt**                                         
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**   **end\_time**
  trip\_1               300                 7:00:00           12:00:00
  trip\_1               600                 12:00:00          22:00:00
  trip\_2               300                 7:00:00           12:00:00
  trip\_2               600                 12:00:00          22:00:00

###

### Example 5: another look at frequencies.txt; headways intervals and travel times vary throughout the day.

Route 1 operates service in both directions with 5 minute average
headways from 7:00 to 12:00. From 12:00 to 22:00, Route 1 operates with
10 minute average headways, but service is faster (less travel time).

Colors match trips\_ids.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                           
  ------------------ ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**    **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday    20130921          20140619        1            1             1               1              1            0              0

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Downtown/Airport        3

**trips.txt**

  **trip\_id**   **route\_id**   **service\_id**   **direction\_id**   **trip\_headsign**
  -------------- --------------- ----------------- ------------------- --------------------
  trip\_1        route\_1        winter\_weekday   0                   Airport
  trip\_2        route\_1        winter\_weekday   1                   Downtown
  trip\_3        route\_1        winter\_weekday   0                   Airport
  trip\_4        route\_1        winter\_weekday   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        0:00:00             0:00:00
  trip\_1               2                    stop\_2        0:10:00             0:10:00
  trip\_1               3                    stop\_3        0:30:00             0:30:00
  trip\_2               1                    stop\_3        0:00:00             0:00:00
  trip\_2               2                    stop\_2        0:10:00             0:10:00
  trip\_2               3                    stop\_1        0:30:00             0:30:00
  trip\_3               1                    stop\_1        0:00:00             0:00:00
  trip\_3               2                    stop\_2        0:08:00             0:08:00
  trip\_3               3                    stop\_3        0:20:00             0:20:00
  trip\_4               1                    stop\_3        0:00:00             0:00:00
  trip\_4               2                    stop\_2        0:12:00             0:12:00
  trip\_4               3                    stop\_1        0:20:00             0:20:00

  **frequencies.txt**                                         
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**   **end\_time**
  trip\_1               300                 7:00:00           12:00:00
  trip\_2               300                 7:00:00           12:00:00
  trip\_3               600                 12:00:00          22:00:00
  trip\_4               600                 12:00:00          22:00:00

### Example 6: Trip variations: express and short trips

In addition to trips that serve the full route, Route 1 service includes
express trips to the airport that skip the railway station, and
shortened trips that end at the railway station. A different
trip\_headsign value indicates the difference in trip patterns.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                           
  ------------------ ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**    **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday    20130921          20140619        1            1             1               1              1            0              0

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Downtown/Airport        3

  **trips.txt**                                                         
  --------------- --------------- ----------------- ------------------- --------------------
  **trip\_id**    **route\_id**   **service\_id**   **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday   0                   Airport
  trip\_2         route\_1        winter\_weekday   1                   Downtown
  trip\_3         route\_1        winter\_weekday   0                   Airport (Express)
  trip\_4         route\_1        winter\_weekday   1                   Downtown (Express)
  trip\_5         route\_1        winter\_weekday   0                   Railway Station
  trip\_6         route\_1        winter\_weekday   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        0:00:00             0:00:00
  trip\_1               2                    stop\_2        0:10:00             0:10:00
  trip\_1               3                    stop\_3        0:30:00             0:30:00
  trip\_2               1                    stop\_3        0:00:00             0:00:00
  trip\_2               2                    stop\_2        0:10:00             0:10:00
  trip\_2               3                    stop\_1        0:30:00             0:30:00
  trip\_3               1                    stop\_1        9:00:00             9:00:00
  trip\_3               2                    stop\_3        9:22:00             9:22:00
  trip\_4               1                    stop\_3        9:22:00             9:22:00
  trip\_4               2                    stop\_1        9:42:00             9:42:00
  trip\_5               1                    stop\_1        10:00:00            10:00:00
  trip\_5               2                    stop\_2        10:10:00            10:10:00
  trip\_6               1                    stop\_2        10:10:00            10:10:00
  trip\_6               2                    stop\_1        10:20:00            10:20:00

  **frequencies.txt**                                         
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**   **end\_time**
  trip\_1               3600                9:00:00           10:30:00
  trip\_2               3600                9:30:00           11:00:00

### Example 7: Different but similar travel patterns are defined as separate routes

The schedule defined here is the same as is defined in example 5.
However, in this case, variations are presented to customers as
different routes (1, 1A, and 1B). Colors match to route\_id.

*Required file not shown: agency.txt*

  **calendar.txt**                                                                                                                           
  ------------------ ----------------- --------------- ------------ ------------- --------------- -------------- ------------ -------------- ------------
  **service\_id**    **start\_date**   **end\_date**   **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**
  winter\_weekday    20130921          20140619        1            1             1               1              1            0              0

  **routes.txt**                                                       
  ---------------- ------------------------ -------------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**      **route\_type**
  route\_1         1                        Downtown/Airport           3
  route\_1a        1A                       Airport Express            3
  route\_1b        1B                       Downtown/Railway Station   3

  **trips.txt**                                                         
  --------------- --------------- ----------------- ------------------- --------------------
  **trip\_id**    **route\_id**   **service\_id**   **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday   0                   Airport
  trip\_2         route\_1        winter\_weekday   1                   Downtown
  trip\_3         route\_1a       winter\_weekday   0                   Airport
  trip\_4         route\_1a       winter\_weekday   1                   Downtown
  trip\_5         route\_1b       winter\_weekday   0                   Railway Station
  trip\_6         route\_1b       winter\_weekday   1                   Downtown

  **stops.txt**                                      
  --------------- ------------------ --------------- ---------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**
  stop\_1         Main and 1st St.   28.8            115.9
  stop\_2         Railway Station    28.9            116
  stop\_3         Airport            29              116.1

  **stop\_times.txt**                                                           
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**   **departure\_time**
  trip\_1               1                    stop\_1        0:00:00             0:00:00
  trip\_1               2                    stop\_2        0:10:00             0:10:00
  trip\_1               3                    stop\_3        0:30:00             0:30:00
  trip\_2               1                    stop\_3        0:00:00             0:00:00
  trip\_2               2                    stop\_2        0:10:00             0:10:00
  trip\_2               3                    stop\_1        0:30:00             0:30:00
  trip\_3               1                    stop\_1        9:00:00             9:00:00
  trip\_3               2                    stop\_3        9:22:00             9:22:00
  trip\_4               1                    stop\_3        9:22:00             9:22:00
  trip\_4               2                    stop\_1        9:42:00             9:42:00
  trip\_5               1                    stop\_1        10:00:00            10:00:00
  trip\_5               2                    stop\_2        10:10:00            10:10:00
  trip\_6               1                    stop\_2        10:10:00            10:10:00
  trip\_6               2                    stop\_1        10:20:00            10:20:00

  **frequencies.txt**                                         
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**   **end\_time**
  trip\_1               3600                9:00:00           10:30:00
  trip\_2               3600                9:30:00           11:00:00


### Example 8: Fares, a combination of free and discounted transfers

One ride is 2 RMB, but customers may purchase a transfer for an
additional 1 RMB. This fare structure is applied across the system.

  **fare\_attributes.txt**                                                                          
  -------------------------- ----------- -------------------- --------------------- --------------- ------------------------
  **fare\_id**               **price**   **currency\_type**   **payment\_method**   **transfers**   **transfer\_duration**
  one\_ride                  2           CNY                  1                     0               
  transfer\_fare             3           CNY                  1                     1               

### Example 9: Fares are defined by zones

Travel within the central district (zone\_a) is less expensive than
travel between zones.

Coloring according to fare\_id.

  **stops.txt**                                                      
  --------------- ------------------ --------------- --------------- --------------
  **stop\_id**    **stop\_name**     **stop\_lat**   **stop\_lon**   **zone\_id**
  stop\_1         Main and 1st St.   28.8            115.9           zone\_a
  stop\_2         Railway Station    28.9            116             zone\_a
  stop\_3         Airport            29              116.1           zone\_b

  **fare\_attributes.txt**                                                                          
  -------------------------- ----------- -------------------- --------------------- --------------- ------------------------
  **fare\_id**               **price**   **currency\_type**   **payment\_method**   **transfers**   **transfer\_duration**
  one\_zone                  2           CNY                  1                                     
  two\_zones                 3           CNY                  1                                     

  **fare\_rules.txt**                    
  --------------------- ---------------- ---------------------
  **fare\_id**          **origin\_id**   **destination\_id**
  one\_zone             zone\_a          zone\_a
  two\_zones            zone\_a          zone\_b
  two\_zones            zone\_b          zone\_a

###

###

### Example 10: Fare structure includes free transfers, but only for specific routes

Routes 1 and 2 cost 1 RMB to ride. Transfers are available between those
routes for 0.5 RMB of extra cost (transfers are valid for 1 hour).Routes
3 and 4 cost 5 RMB to ride. Discounted transfers are not available
between those routes. However, free transfers are available to Routes 1
and 2. Notice that route\_3\_fare and route\_4\_fare are applied for
route\_1 and route\_2 in fare\_rules.txt. Still, when the rider only
uses Route 1 or 2, the less expensive fare will be returned: when
software reads the GTFS and determines the fare, it will always select
the least expensive fare if multiple rules match.

*Coloring according to fare\_id.*

  **fare\_attributes.txt**                                                                          
  -------------------------- ----------- -------------------- --------------------- --------------- ------------------------
  **fare\_id**               **price**   **currency\_type**   **payment\_method**   **transfers**   **transfer\_duration**
  cheap\_fare                1           CNY                  1                                     
  cheap\_fare\_transfer      1.5         CNY                  1                                     3600
  route\_3\_fare             5           CNY                  1                                     3600
  route\_4\_fare             5           CNY                  1                                     3600

  **fare\_rules.txt**     
  ----------------------- ---------------
  **fare\_id**            **route\_id**
  cheap\_fare             route\_1
  cheap\_fare             route\_2
  cheap\_fare\_transfer   route\_1
  cheap\_fare\_transfer   route\_2
  route\_3\_fare          route\_3
  route\_3\_fare          route\_1
  route\_3\_fare          route\_2
  route\_4\_fare          route\_4
  route\_4\_fare          route\_1
  route\_4\_fare          route\_2

### Example 11: A full example, with trips, frequencies, and fares

-   Mon-Fri service in winter, 2 trips in each direction per day

-   Mon-Sun service in the summer

    -   10 min headway before noon

    -   15 min headway in afternoon

-   Zone-based fares

    -   \$3 fare to/from Stagecoach Hotel & Casino

    -   \$2 fare for other trips

This dataset can be downloaded from
[*http://data.trilliumtransit.com/gtfs/deathvalley-demo-ca-us/*](http://data.trilliumtransit.com/gtfs/deathvalley-demo-ca-us/)

  **agency.txt**                                                                                                     
  ---------------- ------------------------ ----------------------------- ---------------------- ------------------- ----------------------------------------------- ------------------
  **agency\_id**   **agency\_name**         **agency\_url**               **agency\_timezone**   **agency\_phone**   **agency\_fare\_url**
  249              Demo Transit Authority   http://gtfsdemo-transit.org   America/Los\_Angeles   503-567-8422        http://gtfsdemo-transit.org/fares-and-tickets

  **stops.txt**                                               
  --------------- --------------------------- --------------- --------------- --------------
  **stop\_id**    **stop\_name**              **stop\_lat**   **stop\_lon**
  stop\_1         E Main St and S Irving St   36.905697       -116.76218
  stop\_2         North Ave at D Ave N        36.914893       -116.76821
  stop\_3         Stagecoach Hotel & Casino   36.915682       -116.751677

  **calendar.txt**                                                                                                                        
  ------------------ ------------ ------------- --------------- -------------- ------------ -------------- ------------ ----------------- ---------------
  **service\_id**    **monday**   **tuesday**   **wednesday**   **thursday**   **friday**   **saturday**   **sunday**   **start\_date**   **end\_date**
  winter\_weekday    1            1             1               1              1            0              0            20151101          20160430
  summer\_daily      1            1             1               1              1            1              1            20160501          20161031

  **routes.txt**                                                    
  ---------------- ------------------------ ----------------------- -----------------
  **route\_id**    **route\_short\_name**   **route\_long\_name**   **route\_type**
  route\_1         1                        Beatty Local            3

  **trips.txt**                                                         
  --------------- --------------- ----------------- ------------------- -------------------------------------
  **trip\_id**    **route\_id**   **service\_id**   **direction\_id**   **trip\_headsign**
  trip\_1         route\_1        winter\_weekday   0                   Stagecoach Hotel & Casino
  trip\_2         route\_1        winter\_weekday   1                   E Main St and S Irving St (Express)
  trip\_3         route\_1        winter\_weekday   0                   Stagecoach Hotel & Casino (Express)
  trip\_4         route\_1        winter\_weekday   1                   E Main St and S Irving St
  trip\_5         route\_1        summer\_daily     0                   Stagecoach Hotel & Casino
  trip\_6         route\_1        summer\_daily     1                   E Main St and S Irving St
  trip\_7         route\_1        summer\_daily     0                   Stagecoach Hotel & Casino
  trip\_8         route\_1        summer\_daily     1                   E Main St and S Irving St

  **stop\_times.txt**                                       
  --------------------- -------------------- -------------- ------------------- ---------------------
  **trip\_id**          **stop\_sequence**   **stop\_id**   **arrival\_time**
  trip\_1               1                    stop\_1        10:00:00
  trip\_1               2                    stop\_2        10:10:00
  trip\_1               3                    stop\_3        10:30:00
  trip\_2               1                    stop\_3        10:30:00
  trip\_2               3                    stop\_1        11:00:00
  trip\_3               1                    stop\_1        15:00:00
  trip\_3               3                    stop\_3        15:30:00
  trip\_4               1                    stop\_3        15:30:00
  trip\_4               2                    stop\_2        15:50:00
  trip\_4               3                    stop\_1        16:00:00
  trip\_5               1                    stop\_1        7:00:00
  trip\_5               2                    stop\_2        7:10:00
  trip\_5               3                    stop\_3        7:30:00
  trip\_6               1                    stop\_3        7:30:00
  trip\_6               2                    stop\_2        7:50:00
  trip\_6                                    stop\_3        8:00:00
  trip\_7               1                    stop\_1        12:00:00
  trip\_7               2                    stop\_2        12:08:00
  trip\_7               3                    stop\_3        12:25:00
  trip\_8               1                    stop\_3        12:25:00
  trip\_8               2                    stop\_2        12:37:00
  trip\_8               3                    stop\_1        12:50:00

  **frequencies.txt**                       
  --------------------- ------------------- ----------------- ---------------
  **trip\_id**          **headway\_secs**   **start\_time**
  trip\_5               600                 7:00:00
  trip\_6               600                 7:30:00
  trip\_7               900                 12:00:00
  trip\_8               900                 12:25:00

  **fare\_attributes.txt**                                    
  -------------------------- ----------- -------------------- --------------------- --------------- ------------------------
  **fare\_id**               **price**   **currency\_type**   **payment\_method**
  one\_zone                  2           USD                  1
  two\_zones                 3           USD                  1

  **fare\_rules.txt**   
  --------------------- ---------------- ---------------------
  **fare\_id**          **origin\_id**
  one\_zone             zone\_a
  two\_zones            zone\_a
  two\_zones            zone\_b

###

###

### Document contributors

**Aaron Antrim**

[*Trillium Solutions, Inc.*](http://www.trilliumtransit.com/)

Portland, Oregon USA

[*aaron@trilliumtransit.com*](mailto:aaron@trilliumtransit.com)

Twitter: [*@trilliumtransit*](https://twitter.com/trilliumtransit/)

\(503) 567-8422

**Holly Krambeck**

The World Bank

Washington, DC USA

Phone: +1 (202) 473-2282

Email: hkrambeck@worldbank.org

Blog:
[*http://blogs.worldbank.org/transport/blogs/holly-krambeck*](http://blogs.worldbank.org/transport/blogs/holly-krambeck)

**Linghong Zou**

Columbia University, GSAPP, Master of Science in Urban Planning
Candidate 2014

[*linghongzou0116@gmail.com*](mailto:linghongzou0116@gmail.com)

**Dr. Li Qu**

The World Bank

Washington, DC USA

lqu@worldbank.org

**Chris Perry**

[*Trillium Solutions, Inc.*](http://www.trilliumtransit.com/)

Portland, Oregon USA

**Kalon Thomas**

Trillium Solutions, Inc.

Portland, Oregon USA
