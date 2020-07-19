docker build -t apiautomation:1.0 .
docker run -v "$(pwd)":/home/apitest/ apiautomation:1.0 hrun /home/apitest/www.bing.com.json