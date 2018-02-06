build:
	jekyll build

serve:
	jekyll serve

install-deps:
	bundle install

clean:
	rm -rf _site
	rm -rf .sass-cache
