# Nearest bars

Script analyze info about bars from [data.mos.ru](https://data.mos.ru/) and prints out biggest, smallest and nearest ones

#### Run script:
```
python bars.py <filename> <longitude> <latitude>
```
where  `<filename>` - json filename, `<longitude>` and ` <latitude>` current geo coordinates

#### Output:
Three lines with biggest, smallest and nearest bars, describing their names, amount of seats and distance to each of them

#### Run script example:
```
python bars.py bars.json 37.635709999610896, 55.805575000158512
```
#### Output example:
```
Biggest bar named Sport bar «Red Machine», has 450 seats and located in 11.609 km
Smallest bar named BAR. Juices, has 0 seats and located in 17.908 km
Closest bar named Bar «Jonnie Green Pub», has 50 seats and located in 0.000 km

```

#### Run unit tests:
```
python test_bar.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)