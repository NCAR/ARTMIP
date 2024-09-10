|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |


<table>
  <tr>
    <td>Row with</td>
    <td>2 cols</td>
  </tr>
  <tr>
    <td colspan="2">Row with only one col</td>
  </tr>
</table>


<!DOCTYPE html>
<html>
<body>

<!---
This table seems confusing! But DO NOT fret!
We need "geometry requirements" to have 4 colomns and "regions" to have 6 colomns, so we just split everything into 12 colomns to make it all lineup right!
--->
<table style="width:100%">
  <tr><!---Header row--->
    <td></td>
    <th colspan="100%">Parameter Type</th>
  </tr>
  <tr><!---Empty row so things are spaced right!---></tr>
  <tr><!---Header row--->
    <th rowspan="100%">Parameters Choices</th>
    <th rowspan="2">Computation Type</th>
    <th rowspan="2">Geometry Requirements</th>
    <th rowspan="2">Threshold Requirements</th>
    <th rowspan="2">Temporal Requirements</th>
    <th rowspan="2">Regions (Examples)</th>
  </tr>
  <tr><!---Empty row so things are spaced right!---></tr>
  <tr><!---Row 1/12--->
    <td rowspan="6">**Condition**<p><br>If conditions are met, then AR exists for each grid point.</p>
      <p><br>This counts time slices at a specific grid point.</p></td>
    <td rowspan="3">Length</td>
    <td rowspan="4">Absolute<p><br>Value is explicitly defined.</p></td>
    <td rowspan="6">Time slice<p><br>Consecutive time slices can be counted to compute AR duration, but it is not required to identify an AR.</p></td>
    <td rowspan="2">Global</td>
  </tr>
  <tr><!---Row 2/12. Empty row so things are spaced right!---></tr>
  <tr><!---Row 3/12--->
    <td rowspan="2">North Pacific Landfalling</td>
  </tr>
  <tr><!---Row 4/12--->
    <td rowspan="3">Width</td>
  </tr>
  <tr><!---Row 5/12--->
    <td rowspan="4">Relative<p><br>Value is computed based on anomaly or statistic.</p></td>
    <td rowspan="2">North Atlantic Landfalling</td>
  </tr>
  <tr><!---Row 6/12. Empty row so things are spaced right!---></tr>
  <tr><!---Row 7/12--->
    <td rowspan="6">Tracking<p><br>Lagrangian approach: If conditions are met, AR object is defined and followed across time and space.</p></td>
    <td rowspan="3">Shape</td>
    <td rowspan="6">Time stitching<p><br>Coherent AR object is followed through time as a part of the algorithm.</p></td>
    <td rowspan="2">Southeast U.S.</td>
  </tr>
  <tr><!---Row 8/12. Empty row so things are spaced right!---></tr>
  <tr><!---Row 9/12--->
    <td rowspan="4">No Thresholds (object only)</td>
    <td rowspan="2">South America</td>
  </tr>
  <tr><!---Row 10/12--->
    <td rowspan="3">Axis or Orientation</td>
  </tr>
  <tr><!---Row 11/12--->
    <td rowspan="2">Polar</td>
  </tr>
  <tr><!---Row 12/12. Empty row so things are spaced right!---></tr>
</table>
</body>
</html>
