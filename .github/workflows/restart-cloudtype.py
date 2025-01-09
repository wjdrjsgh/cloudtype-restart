from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import time

# 환경 변수에서 GitHub 로그인 정보 가져오기
GIT_USERNAME = os.getenv("GIT_USERNAME")
GIT_PASSWORD = os.getenv("GIT_PASSWORD")

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# WebDriver 설정
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Selenium 스크립트 실행 시작")
    
    # GitHub 로그인
    driver.get("https://github.com/login")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    ).send_keys(GIT_USERNAME)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    ).send_keys(GIT_PASSWORD)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "commit"))
    ).click()
    print("GitHub 로그인 완료")

    # Cloudtype 로그인
    driver.get("https://app.cloudtype.io/auth/signin?redirect=/")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'GitHub로 로그인')]"))
    ).click()
    print("Cloudtype 로그인 완료")

    # Cloudtype 앱 정지 및 시작
    driver.get("https://app.cloudtype.io/@hoding1023/youtubecloud:main/youtubesummarizer")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='정지']"))
    ).click()
    print("앱 정지 완료")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='시작']"))
    ).click()
    print("앱 시작 완료")

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()
    print("Selenium 스크립트 실행 종료")
