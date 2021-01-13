## Sentiment Analysis on Soccer Players
- Implemented a data-collection pipeline leveraging **Python**, **MongoDB** and **NLP libraries such as TextBlob and NLTK** to find out the popularity of soccer across countries and sentiment analysis of reactions of Twitterati during soccer matches.
- Live Twitter data was collected using **Tweepy** based on hashtags, stored to the dataset using MongoDB and fed to the pipeline for analysis and visualized with the help of matplotlib and seaborn modules.
- Significant **preprocessing** of collected data was done before analysis such as removal of white spaces, emoji, links, hashtags, mentions and also converting the data to lowercase for ease.
- One **challenge** faced was the shortage of live racist tweets attacking players during tournaments. This was handled by broadening the goal of analysis to not only look at racist tweets but also to determine the polarity of all live tweets during league matches and popularity of soccer across the world.

The source code is at Data_Science_Project.ipynb.
