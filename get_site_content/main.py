import requests
import re


def _save_file(file, to_write):
	with open("{}".format(file), "w") as f:
		f.write(to_write)


def is_online(url):
	"""
	Raise exception if website is not found
	"""
	if not requests.get(url).status_code == requests.codes.ok:
		raise Exception("Failed to find website")


def get_html(url):
	"""
	Returns html code of url
	"""
	is_online(url)
	html=requests.get(url).text
	sequences=[r'<[ ]*script.*?\/[ ]*script[ ]*>',
				r'<[ ]*style.*?\/[ ]*style[ ]*>',
				r'<[ ]*meta.*?>',
				r'<[ ]*!--.*?--[ ]*>'
				]

	for sequence in sequences:
		html = re.sub(sequence, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
	html = re.sub(r'(?<=\n)\s+\n','',html)
	return html


def get_txt(url):
	"""
	Returns all text found on page
	"""
	txt=re.sub(r'<[^<]+?>', '', get_html(url))
	txt=re.sub(r'(?<=\n)\s+\n','',txt)
	return txt


def save_html(url, file_dir):
	"""
	Saves html code of url to file_dir
	"""
	_save_file("{}.html".format(file_dir), get_html(url))


def save_txt(url, file_dir):
	"""
	Saves all text found to file_dir
	"""
	_save_file("{}.txt".format(file_dir), get_txt(url))


def main():
	save_txt("https://www.python.org/", "site")


if __name__=="__main__":
	main()