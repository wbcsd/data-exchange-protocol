# Build all documents and diagrams from spec/ into the build/ 
# output folder. Please read RELEASE.md for more details on 
# publishing the documents.
#
# Assumes python3 is installed
# Assumes npm is installed
#
# Examples of usage:
# make all
#	make a clean build
# make build
#   build the documents and diagrams
# make clean
#   clean the build directory
# make install
# 	Will install bikeshed and mermaid-cli globally

# spec/**.mmd -> build/**.svg
DIAGRAMS := $(wildcard spec/v2/diagrams/*.mmd)
DIAGRAMS := $(DIAGRAMS:spec/%.mmd=build/%.svg)
SOURCES := $(wildcard **.bs)

# Build rule for bikeshed documents
build/%.html: spec/%.bs
	@echo Check release status and version
	$(eval status := $(shell sed -n 's/^Text Macro: STATUS //p' $<))
	$(eval version := $(shell sed -n 's/^Text Macro: VERSION //p' $<))
	$(eval date := $(shell sed -n 's/^Text Macro: DATE //p' $<))

	@echo Build the document
	mkdir -p $(dir $@)
	bikeshed --allow-nonlocal-files spec $< $@

	@echo Set the status in the document

	@if [ "$(status)" = "Release" ]; then \
		echo "Release: add version to title"; \
		mv -f $@ $@.tmp; \
		sed 's/<title>\(.*\)<\/title>/<title>\1 (Version $(version))<\/title>/g' $@.tmp > $@; \
		mv -f $@ $@.tmp; \
		sed 's/\(<h1 .*id="title">.*\)\(<\/h1>\)/\1 (Version $(version))\2/g' $@.tmp > $@; \
	elif [ "$(status)" = "Draft" ] || [ "$(status)" = "Consultation" ]; then \
		echo "No release: add version-date to title"; \
		mv -f $@ $@.tmp; \
		sed 's/<title>\(.*\)<\/title>/<title>\1 (Version $(version)-$(date))<\/title>/g' $@.tmp > $@; \
		mv -f $@ $@.tmp; \
		sed 's/\(<h1 .*id="title">.*\)\(<\/h1>\)/\1 (Version $(version)-$(date))\2/g' $@.tmp > $@; \
	else \
		echo "No status can be found"; \
	fi
	mv -f $@ $@.tmp; \
	sed 's/\(<h2 .*id="profile-and-date">\).*\(<\/h2>\)/\1$(status)\2/g' $@.tmp > $@; \
	rm -f $@.tmp;


# Build rule for mermaid diagrams
build/%.svg: spec/%.mmd
	mkdir -p $(dir $@)
	mmdc -i $< -o $@ --theme default

all: clean build

install:
	@echo Install Bikeshed
	pip3 install bikeshed && bikeshed update
	@echo Install Mermaid
	npm list -g @mermaid-js/mermaid-cli || npm install -g @mermaid-js/mermaid-cli

clean:
	rm -rf build

build: \
	build/index.html \
	build/v2/index.html \
	build/faq/index.html \
	$(DIAGRAMS)

release: clean build
	$(eval release_year := 2024)
	$(eval version := v2)
	@echo "Release $(version) of the PACT Technical Specifications"
	@echo "Please read RELEASE.md for more details on publishing the documents."	

	$(eval status := $(shell sed -n 's/^Text Macro: STATUS //p' spec/$(version)/index.bs))
	$(eval release_date := $(shell sed -n 's/^Text Macro: DATE //p' spec/$(version)/index.bs))
	@if [ "$(status)" = "Release" ]; then \
		echo "Creating release at ../tr/$(release_year)/data-exchange-protocol-${release_date}"; \
		rm -rf ../tr/data-exchange-protocol; \
		cp -r build/$(version)/ ../tr/data-exchange-protocol; \
		cp -r build/$(version)/ ../tr/$(release_year)/data-exchange-protocol-${release_date}; \
		echo "Please create a branch in ../tr, commit the changes and push them to the repository."; \
		pushd ../tr ; \
		git fetch origin main ; \
		git checkout -f -B release-${release_date} origin/main ; \
		git add . ;\
		popd ; \
	else \
		echo "STATUS is not Release, adapt index.bs. See RELEASE.md for more information."; \
	fi
