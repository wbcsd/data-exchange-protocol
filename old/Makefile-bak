OUTDIR := ../upload
MMDC := ./node_modules/.bin/mmdc

all: index.html

clean:
	rm -rf node_modules index.html

publish: index.html
	mkdir -p $(OUTDIR)
	cp $< $(OUTDIR)

index.html: index.bs $(DIAGRAMS)
	bikeshed --allow-nonlocal-files spec $< $@ 

serve:
	bikeshed serve index.bs

.PHONY: publish clean serve
