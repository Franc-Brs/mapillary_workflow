The script is a workaround at the moment and it is only a draft but it works, even though it can be optimized.

![test](https://user-images.githubusercontent.com/79576081/153572037-791d14e3-a394-4743-b1cd-a4107374c173.gif)

and 

![test1](https://user-images.githubusercontent.com/79576081/153572827-0ca1c0ca-3181-470c-8012-ebbe05f38b37.gif)

The layer with the points where the photos are located should be loaded with QGIS, with the name "images" (if you change the name you should also change the code, at the moment it works in this way so pay attention to the names of the layers).
To download the points from mapillay I strongly advise to use the same tools I used, something like this script https://github.com/Franc-Brs/mapillary_workflow/tree/main/download_data

In QGIS the attribute table should have the id of the photo in order to retrive the data with the mapillary API and with mapillary.js.

![image](https://user-images.githubusercontent.com/79576081/153563128-4fe5c55a-ebb8-4014-a134-7dbc880b7ba9.png)

In the lizmap plugin the images layer should have the popup (auto) enabled (and I think that to optimize the wms request the number of elements in the popup should be 1 as it is shown in the next screen), since I don't want to see this layer in the legend and I don't want it to be toggled at the beginning I don't check these options:

![image](https://user-images.githubusercontent.com/79576081/153940757-8de2e00b-873a-4c32-9a07-bc9c6e4f8a60.png)

In the QGIS `project properties`at the `QGIS Server` menu you should check the Publish options under the WFS Capabilities tab:

![image](https://user-images.githubusercontent.com/79576081/153940218-40d86fce-ab49-42a4-a77e-742d826feadb.png)

