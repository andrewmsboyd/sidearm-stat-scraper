# sidearm-stat-scraper

`sidearm-stat-scraper` is a simple Python script intended for use in scraping sports statistical data from websites implemented by [Sidearm Sports](https://www.sidearmsports.com/). Many American universities use Sidearm's product for their athletic websites.

The project was originally created to scrape baseball statistics from Tarleton State University's athletics site in order to perform analysis on current players.

**At this time, it is not known how universal the application of this script can be, since it is still in early stages of development and has only been tested on Tarleton's site.**

## Usage

At runtime, the script will ask the user to specify a URL from which to scrape the data. It should be mentioned that (at least at the time of this writing, it is unlikely this will work properly with out any modifcations to the script). Some knowledge of Python web scraping is highly recommended.

### Running the script

Clone this repo, change into the cloned directory, and run the script:

```bash
python3 sidescrape.py
```

## License

This project is licensed under [GLWTPL](https://github.com/me-shaon/GLWTPL/blob/master/LICENSE). (More information available at [Github repo me-shaon/GLWTPL](https://github.com/me-shaon/GLWTPL))