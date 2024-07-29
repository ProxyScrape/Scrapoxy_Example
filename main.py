import requests

def html_parser_(html_content):
    lines = html_content.strip().split('\n')

    # Initialize an empty dictionary
    response_dict = {}

    # Iterate over the lines and parse key-value pairs
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            response_dict[key.strip()] = value.strip()

    for k in response_dict.keys():
        print(k, ":", response_dict[k])


ca = "YOUR_PATH_TO_CA"
proxy = "http://USERNAME:PASSWORD@localhost:8888"

if __name__ == '__main__':

    r = requests.get(
        "https://ssl-judge2.api.proxyscrape.com/",
        proxies={"http": proxy, "https": proxy},
        verify=ca
    )

    # parse data from html
    html_parser_(r.text)
