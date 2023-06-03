import random
import time

def generate_user_agent():
    platforms = ['Linux', 'Windows', 'iPhone', 'Ubuntu', 'Tesla Phone']
    android_versions = [f'Android {i}' for i in range(4, 14)]
    chrome_versions = [f'Chrome/{i}.0.{random.randint(1000, 9999)}.0' for i in range(1, 100)]

    platform = random.choice(platforms)
    if platform == 'Linux':
        user_agent = f'Mozilla/5.0 ({platform}; {random.choice(android_versions)}; {random.choice(platforms)} {random.randint(100, 999)}) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(chrome_versions)} Mobile Safari/537.36'
    elif platform == 'Windows':
        user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(chrome_versions)} Safari/537.36'
    elif platform == 'iPhone':
        user_agent = f'Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(1, 14)}_{random.randint(0, 4)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) {random.choice(chrome_versions)} Mobile/15E148'
    elif platform == 'Ubuntu':
        user_agent = f'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/{random.randint(1,80)}.0 {random.choice(chrome_versions)}'
    elif platform == 'Tesla Phone':
        user_agent = f'Mozilla/5.0 (Linux; Android 9.0.0; TESLA PHONE Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Mobile Safari/537.36'

    return user_agent

duration = int(input("Generate Ampe Berapa Detik: "))

end_time = time.time() + duration
while time.time() < end_time:
    user_agent = generate_user_agent()
    with open('ua.txt', 'a') as file:
        file.write(user_agent + '\n')
    print(user_agent)
    time.sleep(0)

print("Udah Kelar, Moga Mledak Ya.")
