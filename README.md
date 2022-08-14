# Charisoft/GiveConnect

## Curbing Malnutrition one place at a time
Is a web application tool to visualize and provide donations to places
affected by [Severe Acute
Malnutrition](https://apps.who.int/nutrition/topics/severe_malnutrition/en/index.html)
   in Ethiopia.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The places affected by Severe Acute Malnutrition are displayed on the
map, in addition to place name, the relevant government organization
active in that area and  Non-governmental organization (NGO). In
addition, the number of people affected by Severe Acute Malnutrition in
that area is displayed. To donate click on the Donation link and it
would take you to the NGO that is active in that specific area. Children
 are especially at a particular risk of Malnutrition, according to WHO
Severe Acute Malnutrition is directly or indirectly responsible for [35%
 of deaths among children under
five](https://apps.who.int/nutrition/topics/severe_malnutrition/en/index.html).
 In light of this depressing statistic we encourage you to donate.

## Technologies
Project is created with:
* Python version: 3.10.5
* Package Installer for Python(pip): v22.2.2
* pandas library version: 1.3.4
* folium library version: 0.12.1.post1
* numpy library version: 1.23.1
* openpyxl library version: 3.0.10

For a full list of libraries that were used in development see [librarieslist.txt](linktolist)

## Setup
### Installing dependencies
After install python, download and install pip using cURL:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
To install all the libraries listed using pip run the following commands in succession:
```
pip install pandas
pip install folium
pip install numpy
pip install openpyxl
```
After installing the dependencies clone this repo using the running the following command in the terminal.
 ```bash
  git clone https://github.com/tsionshamsu/NextHack.git
  ```
Then change directory to NextHack and then run [maphack.py](https://github.com/tsionshamsu/NextHack/blob/main/maphack.py):
```bash
  cd ./NextHack
  ./maphack.py
  ```
Finally, you can open the [ethmap.html](https://github.com/tsionshamsu/NextHack/blob/main/ethmap.htm) with a browser of your choice from your local repository. All the affected areas will be rendered. Places with the number of Severe Acute Malnutrition less than 200 are shown with a dark green marker, those between 200 and 400 are shown in orange and those who exceed 400 are shown in red. In addition to all the functionalities described in the [General info](#general-info). Go ahead and donate to the place(s) of your choosing.




## Authors

- [@benealshamsu](https://github.com/benLBrook)
- [@tsionshamsu](https://www.github.com/tsionshamsu)
- [@rediatshamsu](https://www.github.com/rediatbrook)


## License

[MIT](https://github.com/tsionshamsu/NextHack/blob/main/LICENSE)


## Acknowledgements

 - [DEVPOST](https://devpost.com/)

 - [NextStep Hacks 2022](https://nextstep2022.devpost.com/?ref_feature=challenge&ref_medium=your-open-hackathons&ref_content=Submissions+open)
