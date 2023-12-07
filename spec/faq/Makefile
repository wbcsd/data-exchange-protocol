OUTDIR := ../upload/faq

all: index.html

clean:
	rm -rf node_modules index.html

publish: index.html
	mkdir -p $(OUTDIR)
	cp $< $(OUTDIR)

index.html: index.bs
	bikeshed spec $< $@
