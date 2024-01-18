import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def get_movie_rating_filmaffinity():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-site-isolation-trials')
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    movie_ratings = []

    try:
        url = "https://www.filmaffinity.com/us/main.html"
        search_class = "css-xlut8b"
        search_id = "top-search-input-2"
        rating_class = "avgrat-box"

        while True:
            driver.get(url)
            time.sleep(1)

            try:
                find_input = driver.find_element(By.CLASS_NAME, search_class)
                find_input.click()
                time.sleep(0.5)
            except NoSuchElementException:
                pass

            search = driver.find_element(By.ID, search_id)
            movie_title = input("Enter movie title: ")
            
            search.send_keys(movie_title)
            search.send_keys(Keys.RETURN)
            time.sleep(2)

            try:
                score_element = driver.find_element(By.CLASS_NAME, rating_class)
                score_text = score_element.text

                score_match = re.search(r'(\d+\.\d+|\d+)', score_text)
                if score_match:
                    score = float(score_match.group())
                    movie_ratings.append(f"Movie {movie_title} rating is {score}")
                    print(f"Rating for '{movie_title}': {score}")
                else:
                    movie_ratings.append(f"Rating not found for '{movie_title}'.")
                    print(f"Rating not found for '{movie_title}'.")

            except NoSuchElementException:
                movie_ratings.append(f"Rating not found for '{movie_title}'.")
                print(f"Rating not found for '{movie_title}'.")

            another_movie = input("Do you want to enter another movie? (yes/no): ")
            if another_movie.lower() != 'yes':
                break
            else:
                continue

    except Exception as e:
        print(f"An error has occurred: {e}")

    finally:
        driver.quit()

    return movie_ratings

results = get_movie_rating_filmaffinity()
print(results)
