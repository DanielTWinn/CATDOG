# CATDOG
A basic machine learning model that attempts to detect whether a 150px by 150px image is of a cat or a dog.

[ <i>Any detection <b>below 70%</b> should be taken as uncertain</i> ]

<br>

<b>Using <i>run.py</i>:</b>
```
python run.py path/to/image
```
[ <i>Make sure you edit the 7th line of the Python script to select which model you are using</i> ]

<br>

<b>Model Accuracy Tests:</b>

<br>

1. <i>CATDOG 315.2k</i>

<b>Cat Images Test Results:</b>

Total: 20, Passed: 7, Unsure: 0, Failed: 13

<b>Dog Images Test Results:</b>

Total: 20, Passed: 14, Unsure: 1, Failed: 5

Overall Pass Rate: 21/40 (<b>52.50%</b>)

<br>

2. <i>CATDOG 389.2k</i>

<b>Cat Images Test Results:</b>

Total: 20, Passed: 0, Unsure: 7, Failed: 13

<b>Dog Images Test Results:</b>

Total: 20, Passed: 15, Unsure: 5, Failed: 0

Overall Pass Rate: 15/40 (<b>37.50%</b>)

<br>

3. <i>CATDOG 1.2m</i>

<b>Cat Images Test Results:</b>

Total: 20, Passed: 7, Unsure: 0, Failed: 13

<b>Dog Images Test Results:</b>

Total: 20, Passed: 15, Unsure: 0, Failed: 5

Overall Pass Rate: 22/40 (<b>55.00%</b>)

<br>

4. <i>CATDOG 2.1m</i>

<b>Cat Images Test Results:</b>

Total: 20, Passed: 7, Unsure: 1, Failed: 12

<b>Dog Images Test Results:</b>

Total: 20, Passed: 15, Unsure: 1, Failed: 4

Overall Pass Rate: 22/40 (<b>55.00%</b>)
