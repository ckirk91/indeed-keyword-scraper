import requests
from bs4 import BeautifulSoup

class IndeedScraper:
    def __init__(self, keywords, location):
        self.keywords = keywords
        self.location = location
        self.job_listings = []

    def scrape_job_listings(self):
        for keyword in self.keywords:
            url = f"https://www.indeed.com/jobs?q={keyword}&l={self.location}"

            response = requests.get(url)
            html = response.content

            soup = BeautifulSoup(html, "html.parser")

            job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")

            for job_listing in job_listings:
                self.job_listings.append(job_listing)

    def sort_job_listings_by_location(self):
        self.job_listings.sort(key=lambda job_listing: job_listing.find("span", class_="location").text)

    def sort_job_listings_by_keyword(self):
        self.job_listings.sort(key=lambda job_listing: job_listing.find("a", class_="jobtitle").text)

    import requests
from bs4 import BeautifulSoup

class IndeedScraper:
    def __init__(self, keywords, location):
        self.keywords = keywords
        self.location = location
        self.job_listings = []

    def scrape_job_listings(self):
        for keyword in self.keywords:
            url = f"https://www.indeed.com/jobs?q={keyword}&l={self.location}"

            response = requests.get(url)
            html = response.content

            soup = BeautifulSoup(html, "html.parser")

            # Extract the job listings for the specified keyword and location.
            job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard", href=True)

            # Add the job listings to the `job_listings` attribute.
            for job_listing in job_listings:
                self.job_listings.append(job_listing)

    def sort_job_listings_by_location(self):
        # Create a new sorted list of job listings, sorted by location.
        sorted_job_listings = sorted(self.job_listings, key=lambda job_listing: job_listing.find("span", class_="location").text)

        # Update the `job_listings` attribute with the sorted list.
        self.job_listings = sorted_job_listings

    def sort_job_listings_by_keyword(self):
        # Create a new sorted list of job listings, sorted by keyword.
        sorted_job_listings = sorted(self.job_listings, key=lambda job_listing: job_listing.find("a", class_="jobtitle").text)

        # Update the `job_listings` attribute with the sorted list.
        self.job_listings = sorted_job_listings

    def save_job_listings_to_csv(self, location_dataset_filename, keyword_dataset_filename):
        # Open the CSV files in append mode.
        with open(location_dataset_filename, "a", encoding="utf-8") as f_location, open(keyword_dataset_filename, "a", encoding="utf-8") as f_keyword:
            # Write the header row to the CSV files.
            f_location.write("Job Title,Location,Company\n")
            f_keyword.write("Job Title,Keyword,Company\n")

            # Iterate over the job listings and write them to the CSV files.
            for job_listing in self.job_listings:
                job_title = job_listing.find("a", class_="jobtitle").text
                location = job_listing.find("span", class_="location").text
                company = job_listing.find("span", class_="company").text

                f_location.write(f"{job_title},{location},{company}\n")
                f_keyword.write(f"{job_title},{self.keywords[job_listing.index(job_listing)]},{company}\n")

if __name__ == "__main__":
    # Initialize the scraper with the desired keywords and location.
    scraper = IndeedScraper(["CISSP"], ["Washington, DC"])

    # Scrape the job listings.
    scraper.scrape_job_listings()

    # Sort the job listings by location and keyword.
    scraper.sort_job_listings_by_location()
    scraper.sort_job_listings_by_keyword()

    # Save the job listings to CSV files.
    scraper.save_job_listings_to_csv("location_dataset.csv", "keyword_dataset.csv")

