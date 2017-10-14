# Nearest bars

Script analyze info about bars from [data.mos.ru](https://data.mos.ru/) and prints out biggest, smallest and nearest ones

#### Run script:
```
python bars.py <filename> <longitude> <latitude>
```
where  `<filename>` - json filename, `<longitude>` and ` <latitude>` current geo coordinates

#### Output:
Three lines with biggest, smallest and nearest bars, describing their names and amount of seats

#### Run script example:
```
python bars.py bars.json 37.635709999610896, 55.805575000158512
```
#### Output example:
```
Biggest bar named Спорт бар «Красная машина», has 450 seats
Smallest bar named БАР. СОКИ, has 0 seats
Nearest bar named Staropramen, has 50 seats

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)