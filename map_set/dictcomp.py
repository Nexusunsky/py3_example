DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
# 字典推导 dict comp
if __name__ == '__main__':
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)

    upper_map = {code: country.upper() for country, code in country_code.items()}
    print(upper_map)
