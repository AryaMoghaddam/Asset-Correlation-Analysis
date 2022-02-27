# Stock-Correlation-Analysis

<div id="top"></div>

<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://user-images.githubusercontent.com/63557848/155867059-dfc4407f-6cb9-4fba-97c2-d1736b7feba8.png)


A dive into understanding the correlation between different stock tickers and crypto currencies.

Here's why:
* By understanding asset correlation I can better adjust my portfolio for future investements.
* Learn about Negative Correlation and it's meaning!
* Find the hidden insights of different company stocks and their values :smile:



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [seaborn](https://seaborn.pydata.org/)
* [pandas](https://pandas.pydata.org/)
* [matplotlib](https://matplotlib.org/)
* [datetime](https://docs.python.org/3/library/datetime.html)



<!-- GETTING STARTED -->
## Getting Started

There are a couple of prerequisites that had to be installed for this project, outlined below.

### Prerequisites

1- We have to install packages
  ```sh
  pip install matplotlib seaborn pandas 
  ```
- You may run into troubles with your pip version if it's not the last updated version.
- To update pip run the command below:
  ```sh
  pip install pip --upgrade
  ```
2- Yahoo Finance API recently went through some changes with the pandas-datareader
- You might have to install data-reader through Conda CMD if you're using Jupyter through Anaconda like me
- In addition you might have to install the package in a cell on the notebook itself through:
  ```sh
  !pip install pandas-datareader
  ```
### Yahoo Finance API
To use the Yahoo Finance API directly you can use the following command
   ```sh
   get_data_yahoo
   ```
Then you can implement the data you want to read from the API by feeding the Ticker and the sart and finishing time.

<!-- USAGE EXAMPLES -->
## Usage

To get the price changes and ploting a visualization I used the following cell:
   ```sh
   for ticker in tickers:
    plt.plot(combined[ticker], label=ticker)
    
plt.legend(loc="upper right")
plt.show
   ```
   ![image](https://user-images.githubusercontent.com/63557848/155867635-a9cd66a5-c678-4577-a598-92bb212f5659.png)

   You can than change to scaling to logarithmic to get a better visualization of the ticker changes

After getting the price differences I set an empty list in addition to a list of stocks or Crypto currencies I wanted to find the correlation in.
You can use something like the code cell below:

   ```sh
for chip in chips:
    data_chip = pdr.get_data_yahoo(chip, start, now)
    if len(colnames_chip) == 0:
        #Take the closest adjusted price and copy it
        combined_chip = data_chip[['Adj Close']].copy()
    else:
        combined_chip = combined_chip.join(data_chip['Adj Close'])
    #Append to the colnames to know which stock we already added
    colnames_chip.append(chip)
    combined_chip.columns = colnames_chip
   ```
Next you can input the data in a combined list and visualize a seaborn heatmap, the result should look like below:
![image](https://user-images.githubusercontent.com/63557848/155867707-7831baf5-f0e5-4ba3-8ec7-935391428c83.png)


<!-- CONTACT -->
## Contact

Arya Moghadddam - arya.javadi80@gmail.com

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

