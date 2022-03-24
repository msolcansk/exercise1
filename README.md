# Exercise 1

## 1.1 Ansible playbook

Ansible playbook that will:
- Install the Docker service
- Enable container logging to Docker host’s syslog file


### Prerequesities:
- ansible is installed
- ansible-galaxy requirements are installed:
```
ansible-galaxy install -r requirements.yml
```

### How to run:
```
ansible-playbook -i "localhost," -c local site.yml
```
</br>

## 1.2 Weather reporting program

- Gets the current weather from https://openweathermap.org/api
- It can be parametrized via env vars OWM_API_KEY, OWM_CITY

### Prerequesities:
- api key from https://openweathermap.org (Create a free account to get one).
- python
- python-pip : (See requirements.txt)
```
pip install -r requirements.txt
```


### How to run:
```
 export OWM_API_KEY='<your_open_weather_api_key>'
 export OWM_CITY='Bratislava'
python app/getweather.py
```
</br>

## 1.3 Dockerized getweather

</br>

### Build:
In project root:
```
docker build --tag msolcansk/getweather:latest .
```

### Run:
```
docker run -e OWM_API_KEY="<you_open_weather_api_key>" -e OWM_CITY="Bratislava" msolcansk/getweather:latest
```